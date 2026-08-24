# bot.py — White Panel Enterprise Admin Bot (Telegram, aiogram v3, pure asyncio)
#
# Connects to the FastAPI backend over its internal HTTP API (cookie-session),
# so it works embedded in-process, on localhost, or against a remote panel URL.
#
# Env vars:
#   BOT_TOKEN            (required) Telegram bot token from @BotFather
#   ADMIN_TELEGRAM_IDS   (required) comma-separated numeric Telegram IDs of admins
#   PANEL_URL            (default http://127.0.0.1:8080) panel base URL
#   PANEL_PASSWORD       (default "admin") panel admin password (POST /api/login)
#   DATA_DIR             (default ./data) subscribers persistence dir
#
# Run standalone:  python bot.py
# Embedded mode:   main.py auto-starts it when BOT_TOKEN is set.

import asyncio
import html
import json
import logging
import os
import time
from pathlib import Path

import httpx

from aiogram import Bot, Dispatcher, F, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("White-Bot")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()
ADMIN_IDS = {
    int(x) for x in os.environ.get("ADMIN_TELEGRAM_IDS", "").replace(" ", "").split(",")
    if x.strip().lstrip("-").isdigit()
}
PANEL_URL = os.environ.get("PANEL_URL", "http://127.0.0.1:8080").rstrip("/")
PANEL_PASSWORD = os.environ.get("PANEL_PASSWORD") or os.environ.get("ADMIN_PASSWORD", "admin")
DATA_DIR = Path(os.environ.get("DATA_DIR") or (Path(__file__).parent / "data"))
SUBSCRIBERS_FILE = DATA_DIR / "bot_subscribers.json"

PAGE_SIZE = 6
BC_CONCURRENCY = 20          # parallel sends during broadcast fan-out
API_TIMEOUT = httpx.Timeout(30.0, connect=10.0)

router = Router()


class PanelError(Exception):
    pass


# ── Panel HTTP client (auto re-login on session expiry) ──────────────────────
class PanelClient:
    def __init__(self, base_url: str, password: str):
        self._client = httpx.AsyncClient(
            base_url=base_url, timeout=API_TIMEOUT, follow_redirects=True
        )
        self._password = password
        self._lock = asyncio.Lock()
        self._logged_in = False

    async def close(self):
        await self._client.aclose()

    async def _ensure_session(self):
        if self._logged_in:
            return
        async with self._lock:
            if self._logged_in:
                return
            resp = await self._client.post("/api/login", json={"password": self._password})
            if resp.status_code != 200:
                raise PanelError(f"panel login failed ({resp.status_code})")
            self._logged_in = True

    async def request(self, method: str, path: str, ok_codes=(200,), retry_auth: bool = True, **kw):
        await self._ensure_session()
        resp = await self._client.request(method, path, **kw)
        if resp.status_code == 401 and retry_auth:
            # Panel session expired (TTL 7d) — transparently re-login once.
            self._logged_in = False
            return await self.request(method, path, ok_codes, retry_auth=False, **kw)
        if resp.status_code not in ok_codes:
            detail = ""
            try:
                detail = resp.json().get("detail", "")
            except Exception:
                detail = resp.text[:200]
            raise PanelError(f"{method} {path} → {resp.status_code} {detail}")
        try:
            return resp.json()
        except Exception:
            return resp.text

    async def get(self, path, **kw):
        return await self.request("GET", path, **kw)

    async def post(self, path, json_body=None, **kw):
        kw.setdefault("json", json_body)
        return await self.request("POST", path, **kw)


api = PanelClient(PANEL_URL, PANEL_PASSWORD)


# ── Subscribers persistence (lock-guarded, atomic writes) ────────────────────
_subs_lock = asyncio.Lock()


def _read_subs_sync() -> list:
    if not SUBSCRIBERS_FILE.exists():
        return []
    try:
        return json.loads(SUBSCRIBERS_FILE.read_text(encoding="utf-8")).get("chat_ids", [])
    except Exception:
        return []


def _write_subs_sync(ids: list):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    tmp = SUBSCRIBERS_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps({"chat_ids": ids}), encoding="utf-8")
    tmp.replace(SUBSCRIBERS_FILE)


async def load_subscribers() -> list:
    async with _subs_lock:
        raw = await asyncio.to_thread(_read_subs_sync)
    out = []
    for x in raw:
        s = str(x).strip()
        if s.lstrip("-").isdigit():
            out.append(int(s))
    return out


async def mutate_subscribers(chat_id: int, add: bool) -> bool:
    async with _subs_lock:
        subs = await asyncio.to_thread(_read_subs_sync)
        present = chat_id in subs
        if add and present:
            return False
        if not add and not present:
            return False
        if add:
            subs.append(chat_id)
        else:
            subs.remove(chat_id)
        await asyncio.to_thread(_write_subs_sync, subs)
    return True


def esc(s) -> str:
    return html.escape(str(s if s is not None else ""))


def fmt_bytes(b) -> str:
    b = int(b or 0)
    if b < 1024:
        return f"{b} B"
    for unit in ("KB", "MB", "GB", "TB"):
        b /= 1024
        if b < 1024:
            return f"{b:.2f} {unit}"
    return f"{b:.2f} PB"


def fmt_uptime(secs) -> str:
    secs = int(secs or 0)
    d, secs = divmod(secs, 86400)
    h, secs = divmod(secs, 3600)
    m, _ = divmod(secs, 60)
    return f"{d}d {h}h {m}m"


def is_admin(user) -> bool:
    return bool(user and user.id in ADMIN_IDS)


# ── Keyboards ─────────────────────────────────────────────────────────────────
def main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📊 Server Status", callback_data="status"),
            InlineKeyboardButton(text="🌐 Edge Nodes", callback_data="edges"),
        ],
        [
            InlineKeyboardButton(text="👥 Users", callback_data="users:p0"),
            InlineKeyboardButton(text="➕ Create Config", callback_data="create"),
        ],
        [InlineKeyboardButton(text="📢 Broadcast", callback_data="bc:start")],
    ])


def back_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Main Menu", callback_data="menu")],
    ])


def users_kb(users: list, page: int, total_pages: int) -> InlineKeyboardMarkup:
    rows = [[
        InlineKeyboardButton(
            text=("🟢 " if u.get("status") == "active" else "🔴 ")
                 + str(u.get("username") or u.get("user_id")),
            callback_data=f"user:{u['user_id']}",
        )
    ] for u in users]
    nav = []
    if page > 0:
        nav.append(InlineKeyboardButton(text="◀️", callback_data=f"users:p{page - 1}"))
    nav.append(InlineKeyboardButton(
        text=f"{page + 1}/{max(total_pages, 1)}", callback_data="noop"))
    if page < total_pages - 1:
        nav.append(InlineKeyboardButton(text="▶️", callback_data=f"users:p{page + 1}"))
    if nav:
        rows.append(nav)
    rows.append([InlineKeyboardButton(text="➕ New Config", callback_data="create")])
    rows.append([InlineKeyboardButton(text="🔙 Main Menu", callback_data="menu")])
    return InlineKeyboardMarkup(inline_keyboard=rows)


def user_actions_kb(u: dict) -> InlineKeyboardMarkup:
    uid = u["user_id"]
    active = u.get("status") == "active"
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🧾 Config", callback_data=f"uact:{uid}:cfg"),
            InlineKeyboardButton(text="🔄 Reset Traffic", callback_data=f"uact:{uid}:reset"),
        ],
        [
            InlineKeyboardButton(
                text="⛔ Disable" if active else "✅ Enable",
                callback_data=f"uact:{uid}:toggle",
            ),
            InlineKeyboardButton(text="🗑 Delete", callback_data=f"uact:{uid}:del"),
        ],
        [
            InlineKeyboardButton(text="◀️ Users", callback_data="users:p0"),
            InlineKeyboardButton(text="🔙 Main Menu", callback_data="menu"),
        ],
    ])


def delete_confirm_kb(uid: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ YES, delete", callback_data=f"uact:{uid}:del2"),
            InlineKeyboardButton(text="❌ Cancel", callback_data=f"user:{uid}"),
        ],
    ])


PROTOCOLS = ("vless", "vmess", "trojan", "shadowsocks", "reality",
             "hysteria2", "tuic", "xtls-vision")


def proto_kb() -> InlineKeyboardMarkup:
    rows, row = [], []
    for p in PROTOCOLS:
        row.append(InlineKeyboardButton(text=p.upper(), callback_data=f"proto:{p}"))
        if len(row) == 3:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    rows.append([InlineKeyboardButton(text="❌ Cancel", callback_data="create:cancel")])
    return InlineKeyboardMarkup(inline_keyboard=rows)


def broadcast_confirm_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🚀 Send now", callback_data="bc:confirm"),
            InlineKeyboardButton(text="❌ Cancel", callback_data="bc:cancel"),
        ],
    ])


async def safe_edit(cb: CallbackQuery, text: str, kb: InlineKeyboardMarkup | None = None):
    """Edit message text; ignore 'not modified' floods gracefully."""
    try:
        await cb.message.edit_text(text, reply_markup=kb)
    except TelegramBadRequest as e:
        if "not modified" not in str(e):
            raise


# ── FSM states ────────────────────────────────────────────────────────────────
class CreateWizard(StatesGroup):
    username = State()
    traffic_gb = State()
    expire_days = State()
    protocol = State()


class BroadcastState(StatesGroup):
    waiting_message = State()


# ── Admin gate ────────────────────────────────────────────────────────────────
@router.message(CommandStart())
async def cmd_start(m: Message):
    if not is_admin(m.from_user):
        await m.answer("⛔ این پنل ربات مدیریت است. دسترسی ندارید.\n"
                       "اگر کاربر هستید دستور /subscribe را بفرستید.")
        return
    await m.answer(
        f"🛡 <b>White Panel — Enterprise Admin</b>\n"
        f"Backend: <code>{esc(PANEL_URL)}</code>\n"
        f"Admin: <a href='tg://user?id={m.from_user.id}'>{esc(m.from_user.full_name)}</a>\n\n"
        "یک بخش را انتخاب کنید:",
        reply_markup=main_menu(),
    )


@router.message(Command("menu"))
async def cmd_menu(m: Message):
    if not is_admin(m.from_user):
        return
    await m.answer("🎛 منوی اصلی:", reply_markup=main_menu())


@router.callback_query(F.data == "noop")
async def cb_noop(cb: CallbackQuery):
    await cb.answer()


@router.callback_query(F.data == "menu")
async def cb_menu(cb: CallbackQuery, state: FSMContext):
    await state.clear()
    await safe_edit(cb, "🎛 منوی اصلی:", main_menu())
    await cb.answer()


# ── a) Live Server Status ────────────────────────────────────────────────────
async def _render_status() -> str:
    resources, stats, conns = await asyncio.gather(
        api.get("/api/server/resources"),
        api.get("/stats"),
        api.get("/api/connections"),
        return_exceptions=True,
    )
    lines = ["📊 <b>Live Server Status</b>", ""]
    if isinstance(resources, dict) and "error" not in resources:
        bar = lambda pct: "▓" * int(pct // 10) + "░" * (10 - int(pct // 10))
        lines += [
            f"🖥 CPU: <b>{resources.get('cpu_percent', 0)}%</b>  <code>{bar(resources.get('cpu_percent', 0))}</code>",
            f"💾 RAM: <b>{resources.get('ram_percent', 0)}%</b>"
            f" ({resources.get('ram_used_gb', 0)}/{resources.get('ram_total_gb', 0)} GB)",
            f"🗄 Disk: {resources.get('disk_percent', 0)}% ({resources.get('disk_total_gb', 0)} GB)",
            f"⬆️ Sent: {resources.get('net_sent_mb', 0)} MB · ⬇️ Recv: {resources.get('net_recv_mb', 0)} MB",
            f"⏱ Uptime: {fmt_uptime(resources.get('uptime_seconds'))}",
            "",
        ]
    elif isinstance(resources, Exception):
        lines.append(f"⚠️ Resources unavailable: {esc(resources)}")
    if isinstance(stats, dict):
        lines += [
            f"👥 Users: <b>{stats.get('total_users', '?')}</b>"
            f" · Active: <b>{stats.get('active_users', '?')}</b>",
            f"🔗 Configs: {stats.get('total_configs', '?')}",
            f"📈 Total traffic: <b>{fmt_bytes(stats.get('total_traffic_mb', 0) * 1024 * 1024)}</b>",
            f"⚡ Errors: {stats.get('total_errors', 0)}"
            f" · Requests: {stats.get('total_requests', '?')}",
            f"🩺 Server status: <b>{esc(stats.get('server_status', '?'))}</b>",
        ]
    if isinstance(conns, dict):
        lines += [
            "",
            f"🔌 Connections: <b>{conns.get('raw_count', 0)}</b> raw / "
            f"<b>{conns.get('count', 0)}</b> unique IPs",
        ]
        top = (conns.get("connections") or [])[:5]
        for c in top:
            lines.append(f"   • <code>{esc(c.get('ip'))}</code> — {c.get('sessions')} sess, {c.get('bytes_fmt')}")
    return "\n".join(lines)


@router.callback_query(F.data == "status")
async def cb_status(cb: CallbackQuery):
    try:
        text = await _render_status()
    except PanelError as e:
        await cb.answer(f"Panel error: {e}", show_alert=True)
        return
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Refresh", callback_data="status")],
        [InlineKeyboardButton(text="🔙 Main Menu", callback_data="menu")],
    ])
    await safe_edit(cb, text, kb)
    await cb.answer()


@router.callback_query(F.data == "edges")
async def cb_edges(cb: CallbackQuery):
    try:
        data = await api.get("/api/edge/nodes")
    except PanelError as e:
        await cb.answer(f"Panel error: {e}", show_alert=True)
        return
    nodes = data.get("nodes") or []
    lines = [f"🌐 <b>Edge Nodes</b> (revision {data.get('revision', '-')})", ""]
    if not nodes:
        lines.append("هیچ گرهی ثبت نشده است.")
    for n in nodes:
        icon = "🟢" if n.get("online") else "🔴"
        lines.append(
            f"{icon} <b>{esc(n.get('name'))}</b> (<code>{n.get('node_id')}</code>)\n"
            f"     CPU {n.get('cpu_percent', 0)}% · RAM {n.get('ram_percent', 0)}% · "
            f"Conns {n.get('connections', 0)} · Reports {n.get('reports_count', 0)}"
        )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Refresh", callback_data="edges")],
        [InlineKeyboardButton(text="🔙 Main Menu", callback_data="menu")],
    ])
    await safe_edit(cb, "\n".join(lines), kb)
    await cb.answer()


# ── b) User Management ───────────────────────────────────────────────────────
async def _users_page(page: int):
    data = await api.get("/api/users")
    users = sorted(data.get("users") or [], key=lambda u: u.get("created_at") or "", reverse=True)
    total_pages = max(1, -(-len(users) // PAGE_SIZE))
    page = max(0, min(page, total_pages - 1))
    chunk = users[page * PAGE_SIZE:(page + 1) * PAGE_SIZE]
    active = sum(1 for u in users if u.get("status") == "active")
    used = sum(int(u.get("traffic_used_bytes") or 0) for u in users)
    header = (f"👥 <b>Users</b> — {len(users)} total ({active} active)\n"
              f"Consumed: <b>{fmt_bytes(used)}</b>\n")
    return header, chunk, page, total_pages


@router.callback_query(F.data.startswith("users:p"))
async def cb_users(cb: CallbackQuery):
    page = int(cb.data.rsplit("p", 1)[-1] or 0)
    try:
        header, chunk, page, total_pages = await _users_page(page)
    except PanelError as e:
        await cb.answer(f"Panel error: {e}", show_alert=True)
        return
    body = header + ("برای مدیریت روی یک کاربر بزنید:" if chunk else "هیچ کاربری وجود ندارد.")
    await safe_edit(cb, body, users_kb(chunk, page, total_pages))
    await cb.answer()


async def _render_user(u: dict) -> str:
    limit = u.get("traffic_limit_bytes") or 0
    used = u.get("traffic_used_bytes") or 0
    pct = min(100.0, used / limit * 100) if limit else 0.0
    exp = str(u.get("expire_at") or "∞").replace("T", " ")[:16]
    proto = esc((u.get("protocol") or "").upper())
    inb = esc(u.get("inbound_name") or "-")
    conns = u.get("connections", 0)
    return (
        f"👤 <b>{esc(u.get('username'))}</b>  ({'🟢 Active' if u.get('status') == 'active' else '🔴 ' + esc(u.get('status'))})\n"
        f"├ Protocol: <b>{proto}</b> · Inbound: {inb}\n"
        f"├ Traffic: <b>{fmt_bytes(used)}</b> / {fmt_bytes(limit) if limit else '∞'}"
        f" ({pct:.1f}%)\n"
        f"{'│' + '▓' * int(pct // 10) + '░' * (10 - int(pct // 10)) + '│'}\n"
        f"├ Expires: {exp} · Conns now: {conns}\n"
        f"└ UUID: <code>{esc(u.get('config_uuid'))}</code>"
    )


@router.callback_query(F.data.regexp(r"^user:[^:]+$"))
async def cb_user_detail(cb: CallbackQuery):
    uid = cb.data.split(":", 1)[1]
    try:
        data = await api.get(f"/api/users")
        u = next((x for x in data.get("users") or [] if x["user_id"] == uid), None)
    except PanelError as e:
        await cb.answer(f"Panel error: {e}", show_alert=True)
        return
    if not u:
        await cb.answer("کاربر پیدا نشد", show_alert=True)
        return
    await safe_edit(cb, await _render_user(u), user_actions_kb(u))
    await cb.answer()


@router.callback_query(F.data.startswith("uact:"))
async def cb_user_action(cb: CallbackQuery):
    _, uid, action = cb.data.split(":", 2)

    async def refresh_detail():
        data = await api.get("/api/users")
        u = next((x for x in data.get("users") or [] if x["user_id"] == uid), None)
        if u:
            await safe_edit(cb, await _render_user(u), user_actions_kb(u))

    try:
        if action == "reset":
            await api.request("PATCH", f"/api/users/{uid}/reset")
            await cb.answer("🔄 Traffic reset ✓")
            await refresh_detail()
        elif action == "toggle":
            r = await api.request("PATCH", f"/api/users/{uid}/toggle")
            new_status = r.get("status")
            await cb.answer("✅ Enabled" if new_status == "active" else "⛔ Disabled")
            await refresh_detail()
        elif action == "del":
            await safe_edit(cb, "⚠️ <b>حذف قطعی کاربر؟</b> این عمل قابل بازگشت نیست.",
                            delete_confirm_kb(uid))
            await cb.answer()
        elif action == "del2":
            await api.request("DELETE", f"/api/users/{uid}")
            await cb.answer("🗑 Deleted")
            header, chunk, page, total_pages = await _users_page(0)
            await safe_edit(cb, header + "کاربر حذف شد.", users_kb(chunk, page, total_pages))
        elif action == "cfg":
            cfg = await api.get(f"/api/users/{uid}/config")
            text = cfg if isinstance(cfg, str) else json.dumps(cfg)[:3500]
            await cb.message.answer(
                "🧾 <b>Config:</b>\n<code>" + esc(text[:3500]) + "</code>")
            await cb.answer()
        else:
            await cb.answer()
    except PanelError as e:
        await cb.answer(f"Error: {e}", show_alert=True)


# ── Create-config wizard ─────────────────────────────────────────────────────
_pending_creates: dict = {}


@router.callback_query(F.data == "create")
async def cb_create(cb: CallbackQuery, state: FSMContext):
    await state.set_state(CreateWizard.username)
    await safe_edit(cb, "➕ <b>ساخت کانفیگ جدید</b>\n\nنام کاربری را بفرستید:")
    await cb.answer()


@router.callback_query(F.data == "create:cancel")
async def cb_create_cancel(cb: CallbackQuery, state: FSMContext):
    await state.clear()
    _pending_creates.pop(cb.from_user.id, None)
    await safe_edit(cb, "❌ لغو شد.", back_menu())
    await cb.answer()


@router.callback_query(F.data.startswith("proto:"))
async def cb_pick_protocol(cb: CallbackQuery, state: FSMContext):
    proto = cb.data.split(":", 1)[1]
    draft = _pending_creates.setdefault(cb.from_user.id, {})
    draft["protocol"] = proto
    await state.set_state(CreateWizard.protocol)
    d = draft
    confirm_text = (
        f"📋 <b>تایید نهایی</b>\n"
        f"├ Username: <b>{esc(d.get('username'))}</b>\n"
        f"├ Traffic: <b>{d.get('traffic_gb')} GB</b>\n"
        f"├ Expiry: <b>{d.get('expire_days')} روز</b>\n"
        f"└ Protocol: <b>{esc(proto).upper()}</b>\n\n"
        "برای ساخت تایید کنید:"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Create", callback_data="create:do"),
            InlineKeyboardButton(text="❌ Cancel", callback_data="create:cancel"),
        ],
    ])
    await safe_edit(cb, confirm_text, kb)
    await cb.answer()


@router.callback_query(F.data == "create:do")
async def cb_create_do(cb: CallbackQuery, state: FSMContext):
    d = _pending_creates.pop(cb.from_user.id, None)
    if not d:
        await cb.answer("اطلاعات ناقص — دوباره شروع کنید", show_alert=True)
        return
    await cb.answer("در حال ساخت…")
    try:
        r = await api.post("/api/users", {
            "username": d.get("username"),
            "traffic_limit_gb": float(d.get("traffic_gb") or 0),
            "expire_days": int(d.get("expire_days") or 0),
            "protocol": d.get("protocol", "vless"),
        })
    except PanelError as e:
        await safe_edit(cb, f"❌ ساخت ناموفق:\n{esc(e)}", back_menu())
        return
    await state.clear()
    cfg = r.get("config") or ""
    sub_url = r.get("subscription_url") or ""
    body = (
        f"✅ <b>کانفیگ ساخته شد</b> — <b>{esc(r.get('username'))}</b>\n"
        f"Protocol: <b>{esc(r.get('protocol', '')).upper()}</b>\n\n"
        + (f"<code>{esc(cfg[:1200])}</code>\n\n" if cfg else "")
        + (f"🔗 Sub: {esc(sub_url)}" if sub_url else "")
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👥 Back to Users", callback_data="users:p0")],
        [InlineKeyboardButton(text="🔙 Main Menu", callback_data="menu")],
    ])
    await safe_edit(cb, body, kb)


@router.message(CreateWizard.username)
async def wiz_username(m: Message, state: FSMContext):
    if not is_admin(m.from_user):
        return
    name = (m.text or "").strip()
    if not name or len(name) > 40 or " " in name:
        await m.answer("نام نامعتبر (بدون فاصله، حداکثر ۴۰ کاراکتر). دوباره بفرستید:")
        return
    _pending_creates.setdefault(m.from_user.id, {})["username"] = name
    await state.set_state(CreateWizard.traffic_gb)
    await m.answer("حجم ترافیک به گیگابایت (۰ = نامحدود):")


@router.message(CreateWizard.traffic_gb)
async def wiz_traffic(m: Message, state: FSMContext):
    if not is_admin(m.from_user):
        return
    try:
        gb = float((m.text or "0").strip().replace(",", "."))
        assert gb >= 0
    except Exception:
        await m.answer("عدد معتبر بفرستید (مثلاً 50 یا 0):")
        return
    _pending_creates.setdefault(m.from_user.id, {})["traffic_gb"] = gb
    await state.set_state(CreateWizard.expire_days)
    await m.answer("مدت اعتبار به روز (۰ = بدون انقضا):")


@router.message(CreateWizard.expire_days)
async def wiz_expire(m: Message, state: FSMContext):
    if not is_admin(m.from_user):
        return
    try:
        days = int((m.text or "0").strip())
        assert days >= 0
    except Exception:
        await m.answer("عدد صحیح و >= 0 بفرستید:")
        return
    _pending_creates.setdefault(m.from_user.id, {})["expire_days"] = days
    await state.set_state(CreateWizard.protocol)
    await m.answer("پروتکل را انتخاب کنید:", reply_markup=proto_kb())


# ── c) Broadcasting ──────────────────────────────────────────────────────────
_broadcast_cache: dict = {}   # admin_id -> {"chat_id":…, "message_id":…}


@router.callback_query(F.data == "bc:start")
async def bc_start(cb: CallbackQuery, state: FSMContext):
    subs = await load_subscribers()
    await state.set_state(BroadcastState.waiting_message)
    await safe_edit(
        cb,
        f"📢 <b>Broadcast</b>\n"
        f"مخاطبان: <b>{len(subs)}</b> مشترک + {len(ADMIN_IDS)} ادمین\n\n"
        "پیام را بفرستید (متن/عکس/ویدیو — هر نوعی). برای لغو /cancel:",
    )
    await cb.answer()


@router.message(Command("cancel"))
async def cmd_cancel(m: Message, state: FSMContext):
    await state.clear()
    _pending_creates.pop(m.from_user.id, None)
    await m.answer("❌ لغو شد.", reply_markup=None)


@router.message(BroadcastState.waiting_message)
async def bc_capture(m: Message, state: FSMContext):
    if not is_admin(m.from_user):
        return
    _broadcast_cache[m.from_user.id] = {"chat_id": m.chat.id, "message_id": m.message_id}
    await state.set_state(None)
    preview_note = "پیام بالا همین پیام شماست."
    await m.answer(
        f"👁 {preview_note}\nارسال به همه مخاطبان؟",
        reply_markup=broadcast_confirm_kb(),
    )


@router.callback_query(F.data == "bc:cancel")
async def bc_cancel(cb: CallbackQuery, state: FSMContext):
    _broadcast_cache.pop(cb.from_user.id, None)
    await state.clear()
    await safe_edit(cb, "❌ Broadcast لغو شد.", back_menu())
    await cb.answer()


@router.callback_query(F.data == "bc:confirm")
async def bc_confirm(cb: CallbackQuery, state: FSMContext):
    src = _broadcast_cache.pop(cb.from_user.id, None)
    await state.clear()
    if not src:
        await cb.answer("پیامی در صف نیست — دوباره شروع کنید", show_alert=True)
        return
    targets = list(await load_subscribers())
    targets += [i for i in ADMIN_IDS if i not in targets]
    # de-duplicate while preserving order
    seen, uniq = set(), []
    for t in targets:
        if t not in seen:
            seen.add(t)
            uniq.append(t)
    await cb.answer(f"در حال ارسال به {len(uniq)} مخاطب…")
    sent, failed = 0, 0

    sem = asyncio.Semaphore(BC_CONCURRENCY)

    async def deliver(chat_id: int) -> bool:
        nonlocal sent, failed
        async with sem:
            try:
                await cb.bot.copy_message(
                    chat_id=chat_id,
                    from_chat_id=src["chat_id"],
                    message_id=src["message_id"],
                )
                sent += 1
                return True
            except TelegramForbiddenError:
                failed += 1
                await mutate_subscribers(chat_id, add=False)  # prune blocked chats
                return False
            except Exception:
                failed += 1
                return False

    t0 = time.perf_counter()
    await asyncio.gather(*(deliver(c) for c in uniq))
    dt = time.perf_counter() - t0
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Main Menu", callback_data="menu")],
    ])
    await safe_edit(
        cb,
        f"📣 <b>Broadcast finished</b> in {dt:.1f}s\n"
        f"✅ Delivered: <b>{sent}</b>\n"
        f"⚠️ Failed/pruned: <b>{failed}</b>",
        kb,
    )


# ── Subscriber commands (for end-users of the bot) ───────────────────────────
@router.message(Command("subscribe"))
async def cmd_subscribe(m: Message):
    added = await mutate_subscribers(m.chat.id, add=True)
    await m.answer("✅ ثبت شد — اعلان‌ها و اطلاعیه‌ها را دریافت خواهید کرد."
                   if added else "قبلاً ثبت شده‌اید.")


@router.message(Command("unsubscribe"))
async def cmd_unsubscribe(m: Message):
    removed = await mutate_subscribers(m.chat.id, add=False)
    await m.answer("👋 لغو اشتراک شد." if removed else "در لیست نبودید.")


@router.message(Command("subscribers"))
async def cmd_subscribers(m: Message):
    if not is_admin(m.from_user):
        return
    subs = await load_subscribers()
    await m.answer(f"👥 مشترکین: {len(subs)}\n" + "\n".join(f"• <code>{s}</code>" for s in subs[:50]))


# ── Lifecycle ────────────────────────────────────────────────────────────────
async def run_bot_task():
    """Entry point usable both standalone and embedded inside the panel loop.

    Embedded mode (from main.py startup): handle_signals=False so uvicorn
    keeps ownership of signal handling.
    """
    global BOT_TOKEN
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN env var is required")
    if not ADMIN_IDS:
        logger.warning("ADMIN_TELEGRAM_IDS is empty — no one can use admin features")
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    logger.info("Telegram admin bot polling started (panel=%s)", PANEL_URL)
    try:
        await dp.start_polling(bot, handle_signals=False, allowed_updates=["message", "callback_query"])
    finally:
        await bot.session.close()
        await api.close()


if __name__ == "__main__":
    asyncio.run(run_bot_task())
