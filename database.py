# database.py — Async SQLite persistence layer for White Panel (Enterprise)
#
# Design goals:
#   * Strictly non-blocking: every query runs through aiosqlite on the loop.
#   * Zero "database is locked": WAL journal + busy_timeout + SINGLE WRITER
#     connection funneled through an asyncio.Lock; N pooled reader connections
#     serve concurrent reads (WAL lets readers run while the writer commits).
#   * Data integrity: FK constraints ON, CHECK constraints, transactions around
#     multi-statement operations, atomic traffic deltas via executemany.
#   * Typed facade: entities go in/out as plain dicts matching the shapes the
#     panel's hot cache (main.py USERS/LINKS/...) already uses, with fixed
#     relational columns for queryable fields + a `data` JSON column for the
#     long tail (proxy_ips, custom_ip_inbounds, protocol blobs, ...).
#
# Concurrency model
# -----------------
#   writes : 1 connection, serialized by an asyncio.Lock (SQLite permits a
#            single writer anyway — funneling removes SQLITE_BUSY entirely).
#   reads  : pool of `reader_count` connections handed out via asyncio.Queue.
#   Durability: WAL + synchronous=NORMAL — the recommended production pairing.

from __future__ import annotations

import asyncio
import json
import logging
import sqlite3
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, Iterable, Mapping, Optional, Sequence

import aiosqlite

logger = logging.getLogger("White-DB")

SCHEMA_VERSION = 1

_DDL = """
CREATE TABLE IF NOT EXISTS meta (
    key         TEXT PRIMARY KEY,
    value       TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    user_id                 TEXT PRIMARY KEY,
    username                TEXT NOT NULL,
    password_hash           TEXT NOT NULL DEFAULT '',
    protocol                TEXT NOT NULL DEFAULT 'vless',
    config_uuid             TEXT UNIQUE,
    subscription_uuid       TEXT UNIQUE,
    traffic_limit_bytes     INTEGER NOT NULL DEFAULT 0
                            CHECK (traffic_limit_bytes >= 0),
    traffic_used_bytes      INTEGER NOT NULL DEFAULT 0
                            CHECK (traffic_used_bytes >= 0),
    expire_at               TEXT,
    concurrent_connections  INTEGER NOT NULL DEFAULT 3,
    status                  TEXT NOT NULL DEFAULT 'active'
                            CHECK (status IN ('active','disabled','expired')),
    server                  TEXT NOT NULL DEFAULT '',
    created_at              TEXT,
    path                    TEXT NOT NULL DEFAULT '',
    transport_type          TEXT NOT NULL DEFAULT 'ws',
    inbound_id              TEXT,
    telegram_secret         TEXT NOT NULL DEFAULT '',
    data                    TEXT NOT NULL DEFAULT '{}'
);
CREATE INDEX IF NOT EXISTS idx_users_username    ON users (username);
CREATE INDEX IF NOT EXISTS idx_users_config_uuid ON users (config_uuid);
CREATE INDEX IF NOT EXISTS idx_users_status      ON users (status);

CREATE TABLE IF NOT EXISTS user_inbounds (
    user_id     TEXT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    inbound_id  TEXT NOT NULL,
    PRIMARY KEY (user_id, inbound_id)
);
CREATE INDEX IF NOT EXISTS idx_ui_inbound ON user_inbounds (inbound_id);

CREATE TABLE IF NOT EXISTS links (
    uuid_key        TEXT PRIMARY KEY,
    label           TEXT NOT NULL DEFAULT '',
    limit_bytes     INTEGER NOT NULL DEFAULT 0,
    used_bytes      INTEGER NOT NULL DEFAULT 0,
    created_at      TEXT,
    active          INTEGER NOT NULL DEFAULT 1,
    expires_at      TEXT,
    note            TEXT NOT NULL DEFAULT '',
    is_default      INTEGER NOT NULL DEFAULT 0,
    sub_id          TEXT,
    protocol        TEXT NOT NULL DEFAULT 'vless',
    path            TEXT NOT NULL DEFAULT '',
    user_id         TEXT REFERENCES users(user_id) ON DELETE SET NULL,
    data            TEXT NOT NULL DEFAULT '{}'
);
CREATE INDEX IF NOT EXISTS idx_links_path   ON links (path);
CREATE INDEX IF NOT EXISTS idx_links_sub    ON links (sub_id);
CREATE INDEX IF NOT EXISTS idx_links_user   ON links (user_id);

CREATE TABLE IF NOT EXISTS subs (
    sub_id      TEXT PRIMARY KEY,
    label       TEXT NOT NULL DEFAULT '',
    note        TEXT NOT NULL DEFAULT '',
    active      INTEGER NOT NULL DEFAULT 1,
    created_at  TEXT,
    expires_at  TEXT,
    data        TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS inbounds (
    inbound_id       TEXT PRIMARY KEY,
    name             TEXT NOT NULL,
    protocol         TEXT NOT NULL DEFAULT 'vless',
    port             INTEGER,
    network          TEXT NOT NULL DEFAULT 'ws',
    security         TEXT NOT NULL DEFAULT 'tls',
    domain           TEXT NOT NULL DEFAULT '',
    external_domain  TEXT NOT NULL DEFAULT '',
    sni              TEXT NOT NULL DEFAULT '',
    external_port    TEXT NOT NULL DEFAULT '',
    fingerprint      TEXT NOT NULL DEFAULT 'chrome',
    created_at       TEXT,
    data             TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS groups (
    group_id     TEXT PRIMARY KEY,
    name         TEXT NOT NULL,
    description  TEXT NOT NULL DEFAULT '',
    created_at   TEXT,
    data         TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS group_users (
    group_id   TEXT NOT NULL REFERENCES groups(group_id) ON DELETE CASCADE,
    user_id    TEXT NOT NULL REFERENCES users(user_id)  ON DELETE CASCADE,
    PRIMARY KEY (group_id, user_id)
);

CREATE TABLE IF NOT EXISTS settings (
    key    TEXT PRIMARY KEY,
    value  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ip_pool (
    idx           INTEGER PRIMARY KEY AUTOINCREMENT,
    ip            TEXT NOT NULL UNIQUE,
    status        TEXT NOT NULL DEFAULT 'unknown',
    latency_ms    REAL,
    location      TEXT NOT NULL DEFAULT '',
    assigned_user TEXT,
    last_check    TEXT,
    data          TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS ip_blacklist (
    ip        TEXT PRIMARY KEY,
    added_at  TEXT
);

CREATE TABLE IF NOT EXISTS edge_nodes (
    node_id                TEXT PRIMARY KEY,
    name                   TEXT NOT NULL,
    token_hash             TEXT NOT NULL,
    token_hint             TEXT NOT NULL DEFAULT '',
    status                 TEXT NOT NULL DEFAULT 'pending',
    last_seen              TEXT NOT NULL DEFAULT '',
    ip                     TEXT NOT NULL DEFAULT '',
    version                TEXT NOT NULL DEFAULT '',
    connections            INTEGER NOT NULL DEFAULT 0,
    cpu_percent            REAL    NOT NULL DEFAULT 0,
    ram_percent            REAL    NOT NULL DEFAULT 0,
    traffic_reported_bytes INTEGER NOT NULL DEFAULT 0,
    reports_count          INTEGER NOT NULL DEFAULT 0,
    created_at             TEXT,
    data                   TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS worker_state (
    id    INTEGER PRIMARY KEY CHECK (id = 1),
    data  TEXT NOT NULL DEFAULT '{}'
);
"""

_USER_COLS = (
    "username", "password_hash", "protocol", "config_uuid", "subscription_uuid",
    "traffic_limit_bytes", "traffic_used_bytes", "expire_at",
    "concurrent_connections", "status", "server", "created_at", "path",
    "transport_type", "inbound_id", "telegram_secret",
)  # user_id handled separately as PK
_LINK_COLS = (
    "label", "limit_bytes", "used_bytes", "created_at", "active", "expires_at",
    "note", "is_default", "sub_id", "protocol", "path", "user_id",
)


class DatabaseError(RuntimeError):
    """Generic database failure."""


class IntegrityViolation(DatabaseError):
    """UNIQUE/CHECK/FK constraint failure (duplicate username, etc.)."""


def _json(obj: Any) -> str:
    return json.dumps(obj if obj is not None else {}, ensure_ascii=False,
                      separators=(",", ":"))


def _unjson(raw: Any, default: Any = None) -> Any:
    if raw is None or raw == "":
        return default
    try:
        return json.loads(raw)
    except (TypeError, ValueError):
        return default


def _int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


# NOT NULL column fallbacks — legacy JSON snapshots predate the schema and may
# omit fields entirely; inserting NULL would violate constraints and abort a
# migration. Sparse dicts are padded with the schema's own defaults instead.
_USER_DEFAULTS = {
    "username": "", "password_hash": "", "protocol": "vless",
    "concurrent_connections": 3, "status": "active", "server": "",
    "path": "", "transport_type": "ws", "telegram_secret": "",
}
_LINK_DEFAULTS = {
    "label": "", "limit_bytes": 0, "used_bytes": 0, "active": 1,
    "note": "", "is_default": 0, "protocol": "vless", "path": "",
}
_EDGE_DEFAULTS = {
    "name": "", "token_hash": "", "token_hint": "", "status": "pending",
    "last_seen": "", "ip": "", "version": "", "connections": 0,
    "cpu_percent": 0, "ram_percent": 0, "traffic_reported_bytes": 0,
    "reports_count": 0,
}
_INBOUND_DEFAULTS = {
    "name": "", "protocol": "vless", "network": "ws", "security": "tls",
    "domain": "", "external_domain": "", "sni": "", "fingerprint": "chrome",
}


def _pad_nones(col: dict, defaults: Mapping[str, Any]) -> dict:
    """Replace None values for NOT NULL columns with schema defaults."""
    for k, dv in defaults.items():
        if col.get(k) is None:
            col[k] = dv
    return col


class Database:
    """Async SQLite facade: pooled readers + one serialized writer."""

    def __init__(self, path: str | Path, reader_count: int = 4):
        self.path = Path(path)
        self.reader_count = max(1, int(reader_count))
        self._writer: Optional[aiosqlite.Connection] = None
        self._wlock = asyncio.Lock()
        self._readers: asyncio.Queue = asyncio.Queue()
        self._opened = False
        self._init_lock = asyncio.Lock()

    # ── lifecycle ────────────────────────────────────────────────────────────
    async def _connect(self) -> aiosqlite.Connection:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        conn = await aiosqlite.connect(str(self.path), timeout=30.0)
        conn.row_factory = aiosqlite.Row
        # WAL lets pooled readers run concurrently with the single writer.
        await conn.execute("PRAGMA journal_mode=WAL")
        await conn.execute("PRAGMA synchronous=NORMAL")
        await conn.execute("PRAGMA busy_timeout=10000")
        await conn.execute("PRAGMA foreign_keys=ON")
        await conn.execute("PRAGMA temp_store=MEMORY")
        await conn.execute("PRAGMA cache_size=-16000")  # ~16 MB page cache
        return conn

    async def initialize(self) -> None:
        """Open the pool, apply PRAGMAs, create/upgrade the schema."""
        async with self._init_lock:
            if self._opened:
                return
            self._writer = await self._connect()
            for _ in range(self.reader_count):
                self._readers.put_nowait(await self._connect())
            async with self.write_txn() as cur:
                await cur.executescript(_DDL)
                await cur.execute(
                    "INSERT INTO meta(key,value) VALUES('schema_version',?) "
                    "ON CONFLICT(key) DO NOTHING",
                    (str(SCHEMA_VERSION),),
                )
            await self._writer.execute(f"PRAGMA user_version={SCHEMA_VERSION}")
            await self._writer.commit()
            self._opened = True
            logger.info("SQLite ready at %s (WAL, readers=%d)",
                        self.path, self.reader_count)

    async def close(self) -> None:
        if not self._opened:
            return
        conns: list = [self._writer]
        while not self._readers.empty():
            conns.append(self._readers.get_nowait())
        for c in conns:
            if c is None:
                continue
            try:
                await c.commit()
            except Exception:
                pass
            try:
                await c.close()
            except Exception:
                pass
        self._writer = None
        self._readers = asyncio.Queue()
        self._opened = False

    # ── low-level access ─────────────────────────────────────────────────────
    @asynccontextmanager
    async def _reader(self):
        if not self._opened or self._writer is None:
            raise DatabaseError("database not initialized")
        conn = await self._readers.get()
        try:
            yield conn
        finally:
            self._readers.put_nowait(conn)

    @asynccontextmanager
    async def write_txn(self):
        """Serialized write transaction: BEGIN IMMEDIATE … COMMIT/ROLLBACK."""
        if self._writer is None:
            raise DatabaseError("database not initialized")
        async with self._wlock:
            cur = await self._writer.cursor()
            try:
                await cur.execute("BEGIN IMMEDIATE")
            except Exception as e:  # pragma: no cover
                raise DatabaseError(f"BEGIN failed: {e}") from e
            try:
                yield cur
                await self._writer.commit()
            except sqlite3.IntegrityError as e:
                await self._writer.rollback()
                raise IntegrityViolation(str(e)) from e
            except BaseException:
                await self._writer.rollback()
                raise
            finally:
                await cur.close()

    async def fetch_one(self, sql: str, params: Sequence = ()) -> Optional[dict]:
        async with self._reader() as conn:
            cur = await conn.execute(sql, params)
            row = await cur.fetchone()
            await cur.close()
            return dict(row) if row else None

    async def fetch_all(self, sql: str, params: Sequence = ()) -> list:
        async with self._reader() as conn:
            cur = await conn.execute(sql, params)
            rows = await cur.fetchall()
            await cur.close()
            return [dict(r) for r in rows]

    # ════════════════════════════════════════════════════════════════════
    # USERS — typed CRUD
    # ════════════════════════════════════════════════════════════════════
    @staticmethod
    def _split_user(u: Mapping[str, Any]) -> tuple[dict, dict]:
        col = {c: u.get(c) for c in _USER_COLS}
        col["traffic_limit_bytes"] = max(0, _int(col["traffic_limit_bytes"]))
        col["traffic_used_bytes"] = max(0, _int(col["traffic_used_bytes"]))
        col["concurrent_connections"] = _int(col.get("concurrent_connections"), 3)
        if col.get("status") not in ("active", "disabled", "expired"):
            col["status"] = "active"
        _pad_nones(col, _USER_DEFAULTS)
        known = set(_USER_COLS) | {"inbound_ids"}
        extra = {k: v for k, v in u.items() if k not in known}
        return col, extra

    @staticmethod
    def _row_to_user(row: Mapping[str, Any]) -> dict:
        u: dict = {"user_id": row["user_id"]}
        u.update({c: row[c] for c in _USER_COLS})
        u.update(_unjson(row.get("data"), {}) or {})
        return u

    async def upsert_user(self, user_id: str, user: Mapping[str, Any]) -> None:
        """Insert or fully update one user + its inbound memberships."""
        col, extra = self._split_user(user)
        cols = ["user_id"] + list(_USER_COLS) + ["data"]
        updates = ", ".join(f"{c}=excluded.{c}" for c in cols if c != "user_id")
        iids = [str(i) for i in (
            user.get("inbound_ids")
            or ([user["inbound_id"]] if user.get("inbound_id") else [])
        )]
        async with self.write_txn() as cur:
            await cur.execute(
                f"INSERT INTO users ({', '.join(cols)}) "
                f"VALUES ({', '.join(['?'] * len(cols))}) "
                f"ON CONFLICT(user_id) DO UPDATE SET {updates}",
                [user_id] + [col[c] for c in _USER_COLS] + [_json(extra)],
            )
            await cur.execute("DELETE FROM user_inbounds WHERE user_id=?",
                              (user_id,))
            if iids:
                await cur.executemany(
                    "INSERT OR IGNORE INTO user_inbounds(user_id,inbound_id) "
                    "VALUES(?,?)",
                    [(user_id, i) for i in iids],
                )

    async def get_user(self, user_id: str) -> Optional[dict]:
        row = await self.fetch_one("SELECT * FROM users WHERE user_id=?", (user_id,))
        if not row:
            return None
        u = self._row_to_user(row)
        pairs = await self.fetch_all(
            "SELECT inbound_id FROM user_inbounds WHERE user_id=?", (user_id,))
        u["inbound_ids"] = [p["inbound_id"] for p in pairs]
        return u

    async def get_user_by_uuid(self, config_uuid: str) -> Optional[dict]:
        row = await self.fetch_one(
            "SELECT user_id FROM users WHERE config_uuid=?", (config_uuid,))
        return await self.get_user(row["user_id"]) if row else None

    async def list_users(self) -> dict:
        """All users keyed by user_id (cache-rehydration shape)."""
        rows = await self.fetch_all("SELECT * FROM users")
        pairs = await self.fetch_all(
            "SELECT user_id, inbound_id FROM user_inbounds")
        by_uid: dict = {}
        for p in pairs:
            by_uid.setdefault(p["user_id"], []).append(p["inbound_id"])
        out: dict = {}
        for r in rows:
            uid = r["user_id"]
            u = self._row_to_user(r)
            iids = by_uid.get(uid, [])
            if u.get("inbound_id"):
                iids = [u["inbound_id"]] + [i for i in iids if i != u["inbound_id"]]
            elif u.get("config_uuid") and u["config_uuid"] not in iids:
                pass
            u["inbound_ids"] = iids
            out[uid] = u
        return out

    async def delete_user(self, user_id: str) -> bool:
        async with self.write_txn() as cur:
            await cur.execute("DELETE FROM links WHERE uuid_key="
                              "(SELECT config_uuid FROM users WHERE user_id=?)",
                              (user_id,))
            await cur.execute("DELETE FROM users WHERE user_id=?", (user_id,))
            return cur.rowcount > 0

    async def update_user_status(self, user_id: str, status: str) -> bool:
        async with self.write_txn() as cur:
            await cur.execute("UPDATE users SET status=? WHERE user_id=?",
                              (status, user_id))
            return cur.rowcount > 0

    async def reset_user_traffic(self, user_id: str) -> bool:
        async with self.write_txn() as cur:
            await cur.execute(
                "UPDATE users SET traffic_used_bytes=0 WHERE user_id=?", (user_id,))
            return cur.rowcount > 0

    async def bump_user_traffic(self, user_id: str, nbytes: int) -> None:
        """Atomic increment (relay / MTProto proxy accounting)."""
        async with self.write_txn() as cur:
            await cur.execute(
                "UPDATE users SET traffic_used_bytes = traffic_used_bytes + ? "
                "WHERE user_id=?",
                (max(0, _int(nbytes)), user_id),
            )

    async def apply_traffic_deltas(
            self, deltas: Sequence[tuple[str, int]]) -> int:
        """Bulk quota update from edge reports — ONE txn, executemany.

        Items are (user_id_resolved, nbytes). Returns number of rows bound.
        """
        if not deltas:
            return 0
        payload = [(max(0, _int(n)), uid) for uid, n in deltas]
        async with self.write_txn() as cur:
            await cur.executemany(
                "UPDATE users SET traffic_used_bytes = traffic_used_bytes + ? "
                "WHERE user_id=?",
                payload,
            )
            return len(payload)

    # ════════════════════════════════════════════════════════════════════
    # LINKS
    # ════════════════════════════════════════════════════════════════════
    async def upsert_link(self, link: Mapping[str, Any], uuid_key: str) -> None:
        col = {c: link.get(c) for c in _LINK_COLS}
        col["limit_bytes"] = max(0, _int(col["limit_bytes"]))
        col["used_bytes"] = max(0, _int(col["used_bytes"]))
        col["active"] = 1 if link.get("active", True) else 0
        col["is_default"] = 1 if link.get("is_default") else 0
        _pad_nones(col, _LINK_DEFAULTS)
        extra = {k: v for k, v in link.items() if k not in set(_LINK_COLS)}
        cols = ["uuid_key"] + list(_LINK_COLS) + ["data"]
        updates = ", ".join(f"{c}=excluded.{c}" for c in cols if c != "uuid_key")
        async with self.write_txn() as cur:
            await cur.execute(
                f"INSERT INTO links ({', '.join(cols)}) "
                f"VALUES ({', '.join(['?'] * len(cols))}) "
                f"ON CONFLICT(uuid_key) DO UPDATE SET {updates}",
                [uuid_key] + [col[c] for c in _LINK_COLS] + [_json(extra)],
            )

    @staticmethod
    def _row_to_link(row: Mapping[str, Any]) -> dict:
        link: dict = {c: row[c] for c in _LINK_COLS}
        link["active"] = bool(link["active"])
        link["is_default"] = bool(link["is_default"])
        link.update(_unjson(row.get("data"), {}) or {})
        return link

    async def list_links(self) -> dict:
        rows = await self.fetch_all("SELECT * FROM links")
        return {r["uuid_key"]: self._row_to_link(r) for r in rows}

    async def delete_link(self, uuid_key: str) -> bool:
        async with self.write_txn() as cur:
            await cur.execute("DELETE FROM links WHERE uuid_key=?", (uuid_key,))
            return cur.rowcount > 0

    # ════════════════════════════════════════════════════════════════════
    # INBOUNDS
    # ════════════════════════════════════════════════════════════════════
    _INBOUND_COLS = ("name", "protocol", "port", "network", "security", "domain",
                     "external_domain", "sni", "external_port", "fingerprint",
                     "created_at")

    async def upsert_inbound(self, inbound_id: str,
                             ib: Mapping[str, Any]) -> None:
        col = {c: ib.get(c) for c in self._INBOUND_COLS}
        col["port"] = _int(col.get("port")) or None
        col["external_port"] = "" if col.get("external_port") is None \
            else str(col.get("external_port"))
        _pad_nones(col, _INBOUND_DEFAULTS)
        extra = {k: v for k, v in ib.items()
                 if k not in set(self._INBOUND_COLS)}
        cols = ["inbound_id"] + list(self._INBOUND_COLS) + ["data"]
        updates = ", ".join(f"{c}=excluded.{c}" for c in cols if c != "inbound_id")
        async with self.write_txn() as cur:
            await cur.execute(
                f"INSERT INTO inbounds ({', '.join(cols)}) "
                f"VALUES ({', '.join(['?'] * len(cols))}) "
                f"ON CONFLICT(inbound_id) DO UPDATE SET {updates}",
                [inbound_id] + [col[c] for c in self._INBOUND_COLS] + [_json(extra)],
            )

    async def list_inbounds(self) -> dict:
        rows = await self.fetch_all("SELECT * FROM inbounds")
        out: dict = {}
        for r in rows:
            ib: dict = {c: r[c] for c in self._INBOUND_COLS}
            ib.update(_unjson(r.get("data"), {}) or {})
            out[r["inbound_id"]] = ib
        return out

    async def delete_inbound(self, inbound_id: str) -> bool:
        async with self.write_txn() as cur:
            await cur.execute("DELETE FROM inbounds WHERE inbound_id=?",
                              (inbound_id,))
            return cur.rowcount > 0

    # ════════════════════════════════════════════════════════════════════
    # GROUPS / SUBS
    # ════════════════════════════════════════════════════════════════════
    async def upsert_group(self, group_id: str, g: Mapping[str, Any]) -> None:
        members = [str(m) for m in (g.get("user_ids") or [])]
        extra = {k: v for k, v in g.items()
                 if k not in ("name", "description", "created_at", "user_ids")}
        async with self.write_txn() as cur:
            await cur.execute(
                "INSERT INTO groups (group_id,name,description,created_at,data) "
                "VALUES(?,?,?,?,?) ON CONFLICT(group_id) DO UPDATE SET "
                "name=excluded.name, description=excluded.description, "
                "data=excluded.data",
                (group_id, str(g.get("name", "")), str(g.get("description", "")),
                 g.get("created_at"), _json(extra)),
            )
            await cur.execute("DELETE FROM group_users WHERE group_id=?",
                              (group_id,))
            if members:
                await cur.executemany(
                    "INSERT OR IGNORE INTO group_users(group_id,user_id) "
                    "VALUES(?,?)",
                    [(group_id, m) for m in members],
                )

    async def list_groups(self) -> dict:
        rows = await self.fetch_all("SELECT * FROM groups")
        pairs = await self.fetch_all(
            "SELECT group_id,user_id FROM group_users")
        by_g: dict = {}
        for p in pairs:
            by_g.setdefault(p["group_id"], []).append(p["user_id"])
        out: dict = {}
        for r in rows:
            g: dict = {"name": r["name"], "description": r["description"],
                       "created_at": r["created_at"]}
            g.update(_unjson(r.get("data"), {}) or {})
            g["user_ids"] = by_g.get(r["group_id"], [])
            out[r["group_id"]] = g
        return out

    async def delete_group(self, group_id: str) -> bool:
        async with self.write_txn() as cur:
            await cur.execute("DELETE FROM groups WHERE group_id=?", (group_id,))
            return cur.rowcount > 0

    async def upsert_sub(self, sub_id: str, s: Mapping[str, Any]) -> None:
        known = {"sub_id", "label", "note", "active", "created_at", "expires_at"}
        extra = {k: v for k, v in s.items() if k not in known}
        async with self.write_txn() as cur:
            await cur.execute(
                "INSERT INTO subs (sub_id,label,note,active,created_at,"
                "expires_at,data) VALUES(?,?,?,?,?,?,?) ON CONFLICT(sub_id) "
                "DO UPDATE SET label=excluded.label, note=excluded.note, "
                "active=excluded.active, expires_at=excluded.expires_at, "
                "data=excluded.data",
                (sub_id, str(s.get("label", "")), str(s.get("note", "")),
                 1 if s.get("active", True) else 0, s.get("created_at"),
                 s.get("expires_at"), _json(extra)),
            )

    async def list_subs(self) -> dict:
        rows = await self.fetch_all("SELECT * FROM subs")
        out: dict = {}
        for r in rows:
            s: dict = {"label": r["label"], "note": r["note"],
                       "active": bool(r["active"]),
                       "created_at": r["created_at"],
                       "expires_at": r["expires_at"]}
            s.update(_unjson(r.get("data"), {}) or {})
            out[r["sub_id"]] = s
        return out

    async def delete_sub(self, sub_id: str) -> bool:
        async with self.write_txn() as cur:
            await cur.execute("DELETE FROM subs WHERE sub_id=?", (sub_id,))
            return cur.rowcount > 0

    # ════════════════════════════════════════════════════════════════════
    # SETTINGS / AUTH / WORKER (JSON documents)
    # ════════════════════════════════════════════════════════════════════
    async def put_setting(self, key: str, value: Any) -> None:
        async with self.write_txn() as cur:
            await cur.execute(
                "INSERT INTO settings(key,value) VALUES(?,?) "
                "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
                (key, _json(value)),
            )

    async def get_setting(self, key: str, default: Any = None) -> Any:
        row = await self.fetch_one("SELECT value FROM settings WHERE key=?",
                                   (key,))
        return _unjson(row["value"]) if row else default

    async def save_app_settings(self, settings: Mapping[str, Any],
                                password_hash: str, saved_secret: str) -> None:
        async with self.write_txn() as cur:
            await cur.executemany(
                "INSERT INTO settings(key,value) VALUES(?,?) "
                "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
                [("app", _json(settings)),
                 ("auth_password_hash", str(password_hash)),
                 ("saved_secret", str(saved_secret))],
            )

    async def load_app_settings(
            self) -> tuple[Optional[dict], Optional[str], Optional[str]]:
        rows = await self.fetch_all("SELECT key,value FROM settings")
        m = {r["key"]: r["value"] for r in rows}

        def flexible(raw: Optional[str]) -> Any:
            """Settings blobs are JSON; auth hash/secret may be bare strings."""
            if raw is None:
                return None
            val = _unjson(raw)
            return raw if val is None else val

        return (flexible(m.get("app")),
                flexible(m.get("auth_password_hash")),
                flexible(m.get("saved_secret")))

    async def save_worker(self, worker: Mapping[str, Any]) -> None:
        async with self.write_txn() as cur:
            await cur.execute(
                "INSERT INTO worker_state(id,data) VALUES(1,?) "
                "ON CONFLICT(id) DO UPDATE SET data=excluded.data",
                (_json(worker),),
            )

    async def load_worker(self) -> Optional[dict]:
        row = await self.fetch_one("SELECT data FROM worker_state WHERE id=1")
        return _unjson(row["data"]) if row else None

    # ════════════════════════════════════════════════════════════════════
    # IP POOL / BLACKLIST
    # ════════════════════════════════════════════════════════════════════
    async def set_ip_pool(self, entries: Iterable[Mapping[str, Any]]) -> None:
        rows, seen = [], set()
        for e in entries:
            ip = str(e.get("ip") or "").strip()
            if not ip or ip in seen:
                continue  # legacy files may carry duplicates — keep first
            seen.add(ip)
            extra = {k: v for k, v in e.items()
                     if k not in ("ip", "status", "latency_ms", "location",
                                  "assigned_user", "last_check")}
            latency = e.get("latency_ms")
            rows.append((ip, str(e.get("status") or "unknown"),
                         float(latency) if latency is not None else None,
                         str(e.get("location") or ""), e.get("assigned_user"),
                         e.get("last_check"), _json(extra)))
        async with self.write_txn() as cur:
            await cur.execute("DELETE FROM ip_pool")
            if rows:
                await cur.executemany(
                    "INSERT INTO ip_pool(ip,status,latency_ms,location,"
                    "assigned_user,last_check,data) VALUES(?,?,?,?,?,?,?)",
                    rows)

    async def list_ip_pool(self) -> list:
        rows = await self.fetch_all("SELECT * FROM ip_pool ORDER BY idx")
        out = []
        for r in rows:
            e: dict = {"ip": r["ip"], "status": r["status"],
                       "latency_ms": r["latency_ms"], "location": r["location"],
                       "assigned_user": r["assigned_user"],
                       "last_check": r["last_check"]}
            e.update(_unjson(r.get("data"), {}) or {})
            out.append(e)
        return out

    async def set_blacklist(self, ips: Iterable[str]) -> None:
        uniq = sorted({str(i).strip() for i in ips if str(i).strip()})
        async with self.write_txn() as cur:
            await cur.execute("DELETE FROM ip_blacklist")
            if uniq:
                await cur.executemany(
                    "INSERT OR IGNORE INTO ip_blacklist(ip,added_at) VALUES(?,NULL)",
                    [(i,) for i in uniq])

    async def list_blacklist(self) -> list:
        rows = await self.fetch_all("SELECT ip FROM ip_blacklist")
        return [r["ip"] for r in rows]

    # ════════════════════════════════════════════════════════════════════
    # EDGE NODES
    # ════════════════════════════════════════════════════════════════════
    _EDGE_FIXED = ("name", "token_hash", "token_hint", "status", "last_seen",
                   "ip", "version", "connections", "cpu_percent", "ram_percent",
                   "traffic_reported_bytes", "reports_count", "created_at")

    async def upsert_edge(self, node_id: str, edge: Mapping[str, Any]) -> None:
        col = {c: edge.get(c) for c in self._EDGE_FIXED}
        _pad_nones(col, _EDGE_DEFAULTS)
        col["connections"] = _int(col["connections"])
        col["traffic_reported_bytes"] = _int(col["traffic_reported_bytes"])
        col["reports_count"] = _int(col["reports_count"])
        col["cpu_percent"] = float(col["cpu_percent"] or 0)
        col["ram_percent"] = float(col["ram_percent"] or 0)
        extra = {k: v for k, v in edge.items()
                 if k not in set(self._EDGE_FIXED)}
        cols = ["node_id"] + list(self._EDGE_FIXED) + ["data"]
        updates = ", ".join(f"{c}=excluded.{c}" for c in cols if c != "node_id")
        async with self.write_txn() as cur:
            await cur.execute(
                f"INSERT INTO edge_nodes ({', '.join(cols)}) "
                f"VALUES ({', '.join(['?'] * len(cols))}) "
                f"ON CONFLICT(node_id) DO UPDATE SET {updates}",
                [node_id] + [col[c] for c in self._EDGE_FIXED] + [_json(extra)],
            )

    async def list_edges(self) -> dict:
        rows = await self.fetch_all("SELECT * FROM edge_nodes")
        out: dict = {}
        for r in rows:
            e: dict = {c: r[c] for c in self._EDGE_FIXED}
            e.update(_unjson(r.get("data"), {}) or {})
            out[r["node_id"]] = e
        return out

    async def delete_edge(self, node_id: str) -> bool:
        async with self.write_txn() as cur:
            await cur.execute("DELETE FROM edge_nodes WHERE node_id=?",
                              (node_id,))
            return cur.rowcount > 0

    async def persist_edges_health(
            self, edges: Mapping[str, Mapping[str, Any]]) -> int:
        """Bulk health flush from the report path (executemany, 1 txn)."""
        if not edges:
            return 0
        payload = [
            (str(e.get("status") or ""), str(e.get("last_seen") or ""),
             str(e.get("ip") or ""), str(e.get("version") or ""),
             _int(e.get("connections")), float(e.get("cpu_percent") or 0),
             float(e.get("ram_percent") or 0),
             _int(e.get("traffic_reported_bytes")), _int(e.get("reports_count")),
             nid)
            for nid, e in edges.items()
        ]
        async with self.write_txn() as cur:
            await cur.executemany(
                "UPDATE edge_nodes SET status=?, last_seen=?, ip=?, version=?, "
                "connections=?, cpu_percent=?, ram_percent=?, "
                "traffic_reported_bytes=?, reports_count=? WHERE node_id=?",
                payload,
            )
            return len(payload)

    # ════════════════════════════════════════════════════════════════════
    # FULL-SNAPSHOT SYNC (coalesced durability shim behind save_state())
    # ════════════════════════════════════════════════════════════════════
    async def sync_snapshot(self, *, users: Mapping[str, dict],
                            links: Mapping[str, dict], subs: Mapping[str, dict],
                            settings: Mapping[str, Any],
                            groups: Mapping[str, dict],
                            inbounds: Mapping[str, dict],
                            ip_pool: Sequence[dict],
                            ip_blacklist: Iterable[str],
                            edges: Mapping[str, dict],
                            worker: Mapping[str, Any],
                            password_hash: str = "",
                            saved_secret: str = "") -> None:
        """Persist the whole working set in ONE transaction; rows that were
        deleted from the cache are removed from the DB too (legacy paths that
        mutate-then-save keep working without targeted CRUD)."""
        ucols = ["user_id"] + list(_USER_COLS) + ["data"]
        u_ph = ", ".join(["?"] * len(ucols))
        u_upd = ", ".join(f"{c}=excluded.{c}" for c in ucols)

        user_rows: list[list] = []
        ui_rows: list[tuple] = []
        live_uids: list[str] = []
        for uid, u in users.items():
            col, extra = self._split_user(u)
            user_rows.append([uid] + [col[c] for c in _USER_COLS] + [_json(extra)])
            live_uids.append(uid)
            iids = [str(i) for i in (
                u.get("inbound_ids")
                or ([u["inbound_id"]] if u.get("inbound_id") else []))]
            for i in iids:
                ui_rows.append((uid, i))

        lcols = ["uuid_key"] + list(_LINK_COLS) + ["data"]
        l_ph = ", ".join(["?"] * len(lcols))
        l_upd = ", ".join(f"{c}=excluded.{c}" for c in lcols)
        link_rows: list[list] = []
        for k, lnk in links.items():
            col = {c: lnk.get(c) for c in _LINK_COLS}
            col["active"] = 1 if lnk.get("active", True) else 0
            col["is_default"] = 1 if lnk.get("is_default") else 0
            col["limit_bytes"] = max(0, _int(col["limit_bytes"]))
            col["used_bytes"] = max(0, _int(col["used_bytes"]))
            _pad_nones(col, _LINK_DEFAULTS)
            extra = {kk: vv for kk, vv in lnk.items()
                     if kk not in set(_LINK_COLS)}
            link_rows.append([k] + [col[c] for c in _LINK_COLS] + [_json(extra)])

        async with self.write_txn() as cur:
            await cur.executemany(
                f"INSERT INTO users ({', '.join(ucols)}) VALUES ({u_ph}) "
                f"ON CONFLICT(user_id) DO UPDATE SET {u_upd}",
                user_rows)
            await cur.execute("DELETE FROM user_inbounds")
            if ui_rows:
                await cur.executemany(
                    "INSERT OR IGNORE INTO user_inbounds(user_id,inbound_id) "
                    "VALUES(?,?)", ui_rows)
            await cur.executemany(
                f"INSERT INTO links ({', '.join(lcols)}) VALUES ({l_ph}) "
                f"ON CONFLICT(uuid_key) DO UPDATE SET {l_upd}",
                link_rows)
            if live_uids:  # removals: present in DB but gone from cache
                q = ",".join("?" * len(live_uids))
                await cur.execute(
                    f"DELETE FROM users WHERE user_id NOT IN ({q})", live_uids)
            live_lks = [r[0] for r in link_rows]
            if live_lks:
                q = ",".join("?" * len(live_lks))
                await cur.execute(
                    f"DELETE FROM links WHERE uuid_key NOT IN ({q})", live_lks)
            await cur.execute("DELETE FROM subs")
            for sid, s in subs.items():
                known = {"sub_id", "label", "note", "active", "created_at",
                         "expires_at"}
                extra = {k: v for k, v in s.items() if k not in known}
                await cur.execute(
                    "INSERT INTO subs(sub_id,label,note,active,created_at,"
                    "expires_at,data) VALUES(?,?,?,?,?,?,?)",
                    (sid, str(s.get("label", "")), str(s.get("note", "")),
                     1 if s.get("active", True) else 0, s.get("created_at"),
                     s.get("expires_at"), _json(extra)))
            await cur.execute("DELETE FROM groups")
            for gid, g in groups.items():
                extra = {k: v for k, v in g.items()
                         if k not in ("name", "description", "created_at",
                                      "user_ids")}
                await cur.execute(
                    "INSERT INTO groups(group_id,name,description,created_at,"
                    "data) VALUES(?,?,?,?,?)",
                    (gid, str(g.get("name", "")), str(g.get("description", "")),
                     g.get("created_at"), _json(extra)))
                for m in (g.get("user_ids") or []):
                    await cur.execute(
                        "INSERT OR IGNORE INTO group_users(group_id,user_id) "
                        "VALUES(?,?)", (gid, str(m)))
            await cur.execute("DELETE FROM inbounds")
            for iid, ib in inbounds.items():
                col = {c: ib.get(c) for c in self._INBOUND_COLS}
                col["port"] = _int(col.get("port")) or None
                col["external_port"] = "" if col.get("external_port") is None \
                    else str(col.get("external_port"))
                _pad_nones(col, _INBOUND_DEFAULTS)
                extra = {k: v for k, v in ib.items()
                         if k not in set(self._INBOUND_COLS)}
                await cur.execute(
                    f"INSERT INTO inbounds(inbound_id,"
                    f"{', '.join(self._INBOUND_COLS)},data) "
                    f"VALUES({', '.join(['?'] * (len(self._INBOUND_COLS) + 2))})",
                    [iid] + [col[c] for c in self._INBOUND_COLS] + [_json(extra)])
            await cur.executemany(
                "INSERT INTO settings(key,value) VALUES(?,?) "
                "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
                [("app", _json(settings)),
                 ("auth_password_hash", str(password_hash)),
                 ("saved_secret", str(saved_secret))])
            await cur.execute(
                "INSERT INTO worker_state(id,data) VALUES(1,?) "
                "ON CONFLICT(id) DO UPDATE SET data=excluded.data",
                (_json(worker),))
            await cur.execute("DELETE FROM ip_pool")
            seen: set = set()
            ip_rows: list[tuple] = []
            for e in ip_pool:
                ip = str(e.get("ip") or "").strip()
                if not ip or ip in seen:
                    continue
                seen.add(ip)
                extra = {k: v for k, v in e.items()
                         if k not in ("ip", "status", "latency_ms", "location",
                                      "assigned_user", "last_check")}
                latency = e.get("latency_ms")
                ip_rows.append((ip, str(e.get("status") or "unknown"),
                                float(latency) if latency is not None else None,
                                str(e.get("location") or ""),
                                e.get("assigned_user"), e.get("last_check"),
                                _json(extra)))
            if ip_rows:
                await cur.executemany(
                    "INSERT INTO ip_pool(ip,status,latency_ms,location,"
                    "assigned_user,last_check,data) VALUES(?,?,?,?,?,?,?)",
                    ip_rows)
            await cur.execute("DELETE FROM ip_blacklist")
            bl = sorted({str(i).strip() for i in ip_blacklist if str(i).strip()})
            if bl:
                await cur.executemany(
                    "INSERT OR IGNORE INTO ip_blacklist(ip,added_at) "
                    "VALUES(?,NULL)", [(i,) for i in bl])
            await cur.execute("DELETE FROM edge_nodes")
            for nid, e in edges.items():
                col = {c: e.get(c) for c in self._EDGE_FIXED}
                _pad_nones(col, _EDGE_DEFAULTS)
                extra = {k: v for k, v in e.items()
                         if k not in set(self._EDGE_FIXED)}
                await cur.execute(
                    f"INSERT INTO edge_nodes(node_id,{', '.join(self._EDGE_FIXED)},"
                    f"data) VALUES({', '.join(['?'] * (len(self._EDGE_FIXED) + 2))})",
                    [nid] + [col[c] for c in self._EDGE_FIXED] + [_json(extra)])

    # ── maintenance / diagnostics ────────────────────────────────────────────
    async def checkpoint(self) -> None:
        """Fold the WAL back into the main db (idle-time maintenance)."""
        if self._writer is None:
            return
        async with self._wlock:
            await self._writer.execute("PRAGMA wal_checkpoint(TRUNCATE)")

    async def integrity_check(self) -> list:
        rows = await self.fetch_all("PRAGMA integrity_check")
        return [r.get("integrity_check") for r in rows]

    async def foreign_key_check(self) -> list:
        return await self.fetch_all("PRAGMA foreign_key_check")

    async def counts(self) -> dict:
        out: dict = {}
        for t in ("users", "links", "subs", "inbounds", "groups", "edge_nodes",
                  "ip_pool"):
            row = await self.fetch_one(f"SELECT COUNT(*) AS n FROM {t}")
            out[t] = row["n"] if row else 0
        return out
