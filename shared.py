# shared.py — Enterprise Redis-backed shared state
# All in-memory dicts and asyncio.Lock instances are removed.
# Redis is the single source of truth for persistent state.
# Traffic accounting uses atomic Lua scripts to prevent data loss on restart.

import asyncio
import collections
import json
import time
import logging
import threading
from datetime import datetime, timezone, timedelta
from typing import Any

import redis.asyncio as aioredis
import redis as sync_redis

logger = logging.getLogger("White-Panel")

# ── Timezone ──────────────────────────────────────────────────────────────────
IRAN_TZ = timezone(timedelta(hours=3, minutes=30))


def now_ir() -> datetime:
    return datetime.now(IRAN_TZ)


# ── Redis Configuration ──────────────────────────────────────────────────────
REDIS_URL = "redis://localhost:6379/0"

# Async client — used by FastAPI request handlers
redis_client: aioredis.Redis | None = None

# Sync client — used for the Lua script (EVALSHA needs a sync call from the
# relay thread context, but we use the async client's register_script instead)
_redis_lua_sha: str | None = None


async def init_redis() -> bool:
    """Initialize the async Redis connection pool. Returns True on success."""
    global redis_client
    try:
        redis_client = aioredis.from_url(
            REDIS_URL,
            decode_responses=True,
            max_connections=50,
            retry_on_timeout=True,
            socket_connect_timeout=5,
            socket_timeout=5,
        )
        await redis_client.ping()
        # Register the atomic traffic-accounting Lua script
        await _register_traffic_lua()
        logger.info("Redis connected successfully")
        return True
    except Exception as e:
        logger.error(f"Redis connection failed: {e} — falling back to SQLite")
        redis_client = None
        return False


async def close_redis():
    global redis_client
    if redis_client:
        await redis_client.aclose()
        redis_client = None


# ── Atomic Traffic-Accounting Lua Script ─────────────────────────────────────
# Executes entirely inside Redis — zero Python-side locks, zero data loss.
# Keys:  link:{uuid}:meta  (hash),  stats:global  (hash)
# Args:  uuid, nbytes, now_ts, hour_key
TRAFFIC_LUA = """
local link_key = 'link:' .. ARGV[1] .. ':meta'
local active = redis.call('HGET', link_key, 'active')
if active == false or active == '0' or active == 'false' then
    return 0
end
local exp = redis.call('HGET', link_key, 'expires_at')
if exp ~= false and exp ~= '' and exp ~= 'None' then
    if tonumber(ARGV[3]) > 0 and tonumber(ARGV[3]) > tonumber(exp) then
        return 0
    end
end
local limit = tonumber(redis.call('HGET', link_key, 'limit_bytes') or '0')
local used  = tonumber(redis.call('HGET', link_key, 'used_bytes') or '0')
if limit > 0 and used >= limit then
    return 0
end
local new_used = used + tonumber(ARGV[2])
redis.call('HINCRBY', link_key, 'used_bytes', tonumber(ARGV[2]))
redis.call('HINCRBY', 'stats:global', 'total_bytes', tonumber(ARGV[2]))
redis.call('HINCRBY', 'stats:global', 'total_requests', 1)
redis.call('HINCRBY', 'hourly:' .. ARGV[4], 'bytes', tonumber(ARGV[2]))
redis.call('HINCRBY', 'hourly:' .. ARGV[4], 'requests', 1)
local user_id = redis.call('HGET', link_key, 'user_id')
if user_id ~= false and user_id ~= '' then
    local user_key = 'user:' .. user_id .. ':meta'
    redis.call('HINCRBY', user_key, 'traffic_used_bytes', tonumber(ARGV[2]))
end
return 1
"""
_traffic_script = None


async def _register_traffic_lua():
    """Register the Lua script once and cache its SHA."""
    global _traffic_script, _redis_lua_sha
    if redis_client is None:
        return
    try:
        _traffic_script = redis_client.register_script(TRAFFIC_LUA)
        _redis_lua_sha = await _traffic_script
        logger.info("Traffic Lua script registered")
    except Exception as e:
        logger.error(f"Failed to register traffic Lua script: {e}")


async def atomic_check_and_use(uuid: str, nbytes: int) -> bool:
    """Atomically check link validity and increment traffic counters.

    Returns True if the link is allowed and bytes were counted,
    False if the link is disabled/expired/quota-exceeded/unknown.
    Uses a single Redis EVAL — no Python-side locks, no race conditions.
    """
    if redis_client is None or _traffic_script is None:
        return False
    try:
        hour_key = now_ir().strftime("%H:00")
        now_ts = str(int(time.time()))
        result = await _traffic_script(keys=[], args=[uuid, str(nbytes), now_ts, hour_key])
        return result == 1
    except Exception as e:
        logger.warning(f"atomic_check_and_use failed: {e}")
        return False


# ── Redis Key Helpers ────────────────────────────────────────────────────────
# Persistent state lives under these key patterns:
#   state:{name}  — JSON blob for dict/list state (LINKS, USERS, INBOUNDS, etc.)
#   link:{uuid}:meta  — hash for per-link traffic (used_bytes, active, etc.)
#   user:{uid}:meta   — hash for per-user traffic (traffic_used_bytes)
#   stats:global       — hash for global counters (total_bytes, total_requests)
#   hourly:{HH:00}    — hash for hourly traffic buckets
#   announcements      — hash for global announcements
#   sessions:{token}   — string with TTL for auth sessions
#   ip_map:{uid}       — set of currently-connected IPs

STATE_PREFIX = "state:"


async def redis_get_state(name: str, default=None):
    """Fetch a JSON-serialized state blob from Redis."""
    if redis_client is None:
        return default
    try:
        raw = await redis_client.get(f"{STATE_PREFIX}{name}")
        if raw is None:
            return default
        return json.loads(raw)
    except Exception as e:
        logger.warning(f"redis_get_state({name}) failed: {e}")
        return default


async def redis_set_state(name: str, value):
    """Store a JSON-serialized state blob to Redis."""
    if redis_client is None:
        return
    try:
        await redis_client.set(f"{STATE_PREFIX}{name}", json.dumps(value, ensure_ascii=False))
    except Exception as e:
        logger.warning(f"redis_set_state({name}) failed: {e}")


async def redis_delete_state(name: str):
    if redis_client is None:
        return
    try:
        await redis_client.delete(f"{STATE_PREFIX}{name}")
    except Exception as e:
        logger.warning(f"redis_delete_state({name}) failed: {e}")


# ── Link hash helpers ────────────────────────────────────────────────────────
async def redis_get_link(uuid: str) -> dict | None:
    """Fetch a single link hash from Redis."""
    if redis_client is None:
        return None
    try:
        data = await redis_client.hgetall(f"link:{uuid}:meta")
        if not data:
            return None
        # Convert numeric fields
        for k in ("used_bytes", "limit_bytes"):
            if k in data:
                try:
                    data[k] = int(data[k])
                except (ValueError, TypeError):
                    data[k] = 0
        if "active" in data:
            data["active"] = data["active"] in ("1", "true", "True", True)
        return data
    except Exception as e:
        logger.warning(f"redis_get_link({uuid}) failed: {e}")
        return None


async def redis_set_link(uuid: str, link: dict):
    """Store a link hash to Redis."""
    if redis_client is None:
        return
    try:
        # Convert all values to strings for Redis hash storage
        flat = {}
        for k, v in link.items():
            if isinstance(v, bool):
                flat[k] = "1" if v else "0"
            elif v is None:
                flat[k] = ""
            else:
                flat[k] = str(v)
        await redis_client.hset(f"link:{uuid}:meta", mapping=flat)
    except Exception as e:
        logger.warning(f"redis_set_link({uuid}) failed: {e}")


async def redis_delete_link(uuid: str):
    if redis_client is None:
        return
    try:
        await redis_client.delete(f"link:{uuid}:meta")
    except Exception as e:
        logger.warning(f"redis_delete_link({uuid}) failed: {e}")


# ── User hash helpers ────────────────────────────────────────────────────────
async def redis_get_user(uid: str) -> dict | None:
    if redis_client is None:
        return None
    try:
        data = await redis_client.hgetall(f"user:{uid}:meta")
        if not data:
            return None
        for k in ("traffic_used_bytes", "traffic_limit_bytes", "concurrent_connections"):
            if k in data:
                try:
                    data[k] = int(data[k])
                except (ValueError, TypeError):
                    data[k] = 0
        return data
    except Exception as e:
        logger.warning(f"redis_get_user({uid}) failed: {e}")
        return None


async def redis_set_user(uid: str, user: dict):
    if redis_client is None:
        return
    try:
        flat = {}
        for k, v in user.items():
            if isinstance(v, bool):
                flat[k] = "1" if v else "0"
            elif v is None:
                flat[k] = ""
            else:
                flat[k] = str(v)
        await redis_client.hset(f"user:{uid}:meta", mapping=flat)
    except Exception as e:
        logger.warning(f"redis_set_user({uid}) failed: {e}")


# ── Global stats helpers ─────────────────────────────────────────────────────
async def redis_incr_stats(field: str, amount: int = 1):
    if redis_client is None:
        return
    await redis_client.hincrby("stats:global", field, amount)


async def redis_get_stats() -> dict:
    if redis_client is None:
        return {"total_bytes": 0, "total_requests": 0, "total_errors": 0}
    try:
        data = await redis_client.hgetall("stats:global")
        return {
            "total_bytes": int(data.get("total_bytes", 0)),
            "total_requests": int(data.get("total_requests", 0)),
            "total_errors": int(data.get("total_errors", 0)),
        }
    except Exception:
        return {"total_bytes": 0, "total_requests": 0, "total_errors": 0}


# ── Hourly traffic helpers ───────────────────────────────────────────────────
async def redis_get_hourly_traffic() -> dict:
    """Return {hour_key: bytes} for the last 24 hours."""
    if redis_client is None:
        return {}
    try:
        result = {}
        now = now_ir()
        for i in range(24):
            h = (now - timedelta(hours=i)).strftime("%H:00")
            data = await redis_client.hgetall(f"hourly:{h}")
            if data:
                result[h] = int(data.get("bytes", 0))
        return result
    except Exception:
        return {}


# ── IP map helpers ───────────────────────────────────────────────────────────
async def redis_ip_add(uid: str, ip: str) -> bool:
    """Add an IP to a user's connected-IP set. Returns False if limit reached."""
    if redis_client is None:
        return True  # no Redis = no enforcement
    key = f"ip_map:{uid}"
    try:
        await redis_client.sadd(key, ip)
        await redis_client.expire(key, 3600)  # auto-expire after 1h idle
        return True
    except Exception:
        return True


async def redis_ip_remove(uid: str, ip: str):
    if redis_client is None:
        return
    try:
        await redis_client.srem(f"ip_map:{uid}", ip)
    except Exception:
        pass


async def redis_ip_count(uid: str) -> int:
    if redis_client is None:
        return 0
    try:
        return await redis_client.scard(f"ip_map:{uid}")
    except Exception:
        return 0


# ── Session helpers (Redis-backed with in-memory fallback) ──────────────────
SESSION_TTL = 60 * 60 * 24 * 7  # 7 days
_INMEMORY_SESSIONS: dict[str, float] = {}


async def redis_create_session(token: str, ttl: int = SESSION_TTL):
    if redis_client is not None:
        try:
            await redis_client.set(f"sessions:{token}", "1", ex=ttl)
            return
        except Exception:
            pass
    _INMEMORY_SESSIONS[token] = time.time() + ttl


async def redis_is_valid_session(token: str) -> bool:
    if not token:
        return False
    if redis_client is not None:
        try:
            return await redis_client.exists(f"sessions:{token}") == 1
        except Exception:
            pass
    exp = _INMEMORY_SESSIONS.get(token)
    if exp is None:
        return False
    if time.time() > exp:
        _INMEMORY_SESSIONS.pop(token, None)
        return False
    return True


async def redis_destroy_session(token: str):
    if redis_client is not None:
        try:
            await redis_client.delete(f"sessions:{token}")
        except Exception:
            pass
    _INMEMORY_SESSIONS.pop(token, None)


# ── Announcements ────────────────────────────────────────────────────────────
async def redis_get_announcement() -> str:
    if redis_client is None:
        return ""
    try:
        return await redis_client.hget("announcements", "message") or ""
    except Exception:
        return ""


async def redis_set_announcement(message: str):
    if redis_client is None:
        return
    try:
        await redis_client.hset("announcements", "message", message)
        await redis_client.hset("announcements", "updated_at", datetime.now().isoformat())
    except Exception:
        pass


# ── Ephemeral state (in-memory only — short-lived, no persistence needed) ────
# These are WebSocket/XHTTP connection trackers that only exist while the
# connection is alive. No need for Redis — they're process-local by nature.
connections: dict = {}
sub_clients: dict = {}

# ── Ephemeral counters (rebuilt from Redis on startup) ───────────────────────
stats = {
    "total_bytes": 0,
    "total_requests": 0,
    "total_errors": 0,
    "start_time": time.time(),
}
error_logs = collections.deque(maxlen=50)
hourly_traffic = collections.defaultdict(int)

# ── Relay constants ──────────────────────────────────────────────────────────
RELAY_BUF = 256 * 1024
RELAY_BUF_LOCAL = 256 * 1024
TIMEOUT = 30
