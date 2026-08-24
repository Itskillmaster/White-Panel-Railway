# migrate_json_to_sqlite.py — One-shot legacy migration for White Panel.
#
# Reads data/white_state.json and inserts every record into the SQLite schema
# defined by database.py using the SAME row-mapping code the panel uses at
# runtime (zero drift between migration and application logic).
#
# Safety properties:
#   * Single transaction  — all-or-nothing insert.
#   * Idempotent          — safe to re-run (upsert semantics).
#   * Verified            — per-table count reconciliation + PRAGMA
#                           integrity_check + foreign_key_check before success.
#   * Non-destructive     — the JSON file is left untouched unless --cutover
#                           is passed, which renames it to .migrated-<ts>.
#
# Usage:
#   python migrate_json_to_sqlite.py                       # dry-run + migrate, keep json
#   python migrate_json_to_sqlite.py --json /path/state.json --db /path/panel.db
#   python migrate_json_to_sqlite.py --cutover             # retire the json after success

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import sys
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from database import Database, SCHEMA_VERSION  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("White-Migrate")

DEFAULT_JSON = Path(__file__).parent / "data" / "white_state.json"
DEFAULT_DB = Path(__file__).parent / "data" / "white_panel.db"


def load_legacy_state(json_path: Path) -> dict:
    """Read + structurally validate the legacy snapshot."""
    if not json_path.is_file():
        raise FileNotFoundError(f"legacy state not found: {json_path}")
    # utf-8-sig transparently strips a BOM (common on Windows-written files)
    raw = json_path.read_text(encoding="utf-8-sig")
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("legacy state root must be a JSON object")
    # Coerce guaranteed-collection keys so downstream code never sees None.
    for key in ("links", "users", "subs", "groups", "inbounds", "edges"):
        if not isinstance(data.get(key), dict):
            data[key] = {}
    for key in ("ip_pool", "ip_blacklist"):
        if not isinstance(data.get(key), list):
            data[key] = []
    if not isinstance(data.get("worker"), dict):
        data["worker"] = {}
    if not isinstance(data.get("settings"), dict):
        data["settings"] = {}
    _heal_duplicate_uuids(data)
    return data


def _heal_duplicate_uuids(state: dict) -> int:
    """Legacy files may carry duplicate config_uuid / subscription_uuid values
    (crash-corrupted writes). The schema declares them UNIQUE; regenerate fresh
    UUIDs for later duplicates instead of aborting the whole migration."""
    import uuid as _uuid

    def heal(field: str, regen: bool = True) -> int:
        seen: dict = {}
        fixed = 0
        for uid, u in state.get("users", {}).items():
            val = u.get(field)
            if not val:
                continue
            if val in seen:
                new_val = str(_uuid.uuid4()) if regen else f"{uid}-{field}"
                logger.warning("duplicate %s '%s' on user %s → regenerated (%s)",
                               field, val, uid, new_val)
                u[field] = new_val
                # keep stored paths consistent with the new uuid
                old_path = str(u.get("path") or "")
                if old_path and val in old_path:
                    u["path"] = old_path.replace(val, new_val)
                fixed += 1
            else:
                seen[val] = uid
        return fixed

    total = heal("config_uuid") + heal("subscription_uuid")
    if total:
        logger.warning("healed %d duplicate UUID(s) in legacy state", total)
    return total


async def migrate_json_to_sqlite(
    db: Database,
    state: dict,
    *,
    password_hash: str | None = None,
    saved_secret: str | None = None,
) -> dict:
    """Insert a validated legacy snapshot into the DB (one transaction).

    Returns a report dict with source/target counts for verification.
    """
    await db.initialize()

    settings = state.get("settings") or {}
    auth_hash = password_hash or ""
    secret = saved_secret or ""

    t0 = time.perf_counter()
    # sync_snapshot() writes every entity family inside ONE BEGIN IMMEDIATE
    # transaction and deletes stale rows → idempotent re-runs converge cleanly.
    await db.sync_snapshot(
        users=state.get("users") or {},
        links=state.get("links") or {},
        subs=state.get("subs") or {},
        groups=state.get("groups") or {},
        inbounds=state.get("inbounds") or {},
        edges=state.get("edges") or {},
        ip_pool=state.get("ip_pool") or [],
        ip_blacklist=state.get("ip_blacklist") or [],
        worker=state.get("worker") or {},
        settings=settings,
        password_hash=auth_hash,
        saved_secret=secret,
    )
    elapsed = time.perf_counter() - t0

    src_counts = {
        "users": len(state.get("users") or {}),
        "links": len(state.get("links") or {}),
        "subs": len(state.get("subs") or {}),
        "inbounds": len(state.get("inbounds") or {}),
        "groups": len(state.get("groups") or {}),
        "edge_nodes": len(state.get("edges") or {}),
        "ip_pool": len(state.get("ip_pool") or []),
    }
    dst_counts = await db.counts()

    report = {
        "schema_version": SCHEMA_VERSION,
        "elapsed_seconds": round(elapsed, 3),
        "source": src_counts,
        "database": dst_counts,
        "integrity": await db.integrity_check(),
        "foreign_key_violations": await db.foreign_key_check(),
    }

    problems = []
    for table, expected in src_counts.items():
        got = dst_counts.get(table, 0)
        # ip_pool dedupes duplicates by design — allow fewer rows than source.
        if got != expected:
            if table == "ip_pool" and got <= expected:
                continue
            problems.append(f"{table}: source={expected} db={got}")
    if report["integrity"] != ["ok"]:
        problems.append(f"integrity_check: {report['integrity']}")
    if report["foreign_key_violations"]:
        problems.append(f"fk violations: {report['foreign_key_violations'][:5]}")
    report["ok"] = not problems
    report["problems"] = problems
    return report


async def main() -> int:
    ap = argparse.ArgumentParser(description="Migrate White Panel JSON state → SQLite")
    ap.add_argument("--json", type=Path, default=DEFAULT_JSON,
                    help=f"legacy white_state.json path (default: {DEFAULT_JSON})")
    ap.add_argument("--db", type=Path, default=DEFAULT_DB,
                    help=f"target sqlite database (default: {DEFAULT_DB})")
    ap.add_argument("--readers", type=int, default=4,
                    help="reader connection pool size (default 4)")
    ap.add_argument("--cutover", action="store_true",
                    help="after verified migration rename the json to .migrated-<ts>")
    args = ap.parse_args()

    logger.info("Loading legacy state: %s", args.json)
    state = load_legacy_state(args.json)
    logger.info(
        "Loaded: users=%d links=%d subs=%d inbounds=%d groups=%d edges=%d ips=%d",
        len(state["users"]), len(state["links"]), len(state["subs"]),
        len(state["inbounds"]), len(state["groups"]), len(state["edges"]),
        len(state["ip_pool"]),
    )

    db = Database(args.db, reader_count=args.readers)
    try:
        report = await migrate_json_to_sqlite(
            db, state,
            password_hash=state.get("password_hash"),
            saved_secret=state.get("saved_secret"),
        )
    finally:
        await db.close()

    print(json.dumps(report, indent=2, ensure_ascii=False))
    if not report["ok"]:
        logger.error("VERIFICATION FAILED — JSON left untouched, DB rolled back "
                     "or partial; inspect 'problems' above.")
        return 1

    if args.cutover:
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        target = args.json.with_name(f"{args.json.name}.migrated-{stamp}")
        args.json.rename(target)
        logger.info("Cutover complete — legacy file retired to %s", target)
    else:
        logger.info("Migration verified. JSON kept in place (pass --cutover to retire).")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(asyncio.run(main()))
    except FileNotFoundError as e:
        logger.error("%s", e)
        sys.exit(2)
