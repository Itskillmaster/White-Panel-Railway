# core_singbox.py — Sing-box Core for Hysteria2 & Shadowsocks-2022
# Enterprise Edition: auto-download, config generation, process lifecycle

import os
import json
import asyncio
import httpx
import shutil
import platform
import logging
from pathlib import Path

logger = logging.getLogger("White-Panel")

SINGBOX_DIR = Path(os.path.dirname(os.path.abspath(__file__))) / "singbox"
SINGBOX_BIN = SINGBOX_DIR / "sing-box"
SINGBOX_CONFIG = SINGBOX_DIR / "config.json"

# Auto-detect architecture for download URL
_ARCH_MAP = {
    "amd64": "amd64",
    "x86_64": "amd64",
    "arm64": "arm64",
    "aarch64": "arm64",
}
_SINGBOX_ARCH = _ARCH_MAP.get(platform.machine().lower(), "amd64")
SINGBOX_VERSION = "1.9.3"
SINGBOX_URL = (
    f"https://github.com/SagerNet/sing-box/releases/download/"
    f"v{SINGBOX_VERSION}/sing-box-{SINGBOX_VERSION}-linux-{_SINGBOX_ARCH}.tar.gz"
)

_singbox_proc: asyncio.subprocess.Process | None = None
_singbox_lock = asyncio.Lock()


async def ensure_singbox() -> bool:
    """Download and install Sing-box binary if not present or too small."""
    if SINGBOX_BIN.exists() and SINGBOX_BIN.stat().st_size > 100000:
        return True

    logger.info("Downloading Sing-box core for Hysteria2/SS-2022...")
    try:
        SINGBOX_DIR.mkdir(parents=True, exist_ok=True)
        tar_path = SINGBOX_DIR / "singbox.tar.gz"

        async with httpx.AsyncClient(timeout=120, follow_redirects=True) as c:
            r = await c.get(SINGBOX_URL)
            if r.status_code != 200:
                logger.error(f"Sing-box download failed: HTTP {r.status_code}")
                return False
            tar_path.write_bytes(r.content)

        import tarfile
        with tarfile.open(tar_path, "r:gz") as tar:
            tar.extractall(path=SINGBOX_DIR)

        extracted_dirs = list(SINGBOX_DIR.glob(f"sing-box-{SINGBOX_VERSION}-linux-{_SINGBOX_ARCH}*"))
        if not extracted_dirs:
            logger.error("Sing-box extraction failed: no binary found in archive")
            return False

        extracted_dir = extracted_dirs[0]
        shutil.move(str(extracted_dir / "sing-box"), str(SINGBOX_BIN))

        os.chmod(SINGBOX_BIN, 0o755)
        tar_path.unlink(missing_ok=True)
        shutil.rmtree(extracted_dir, ignore_errors=True)

        logger.info(f"Sing-box {SINGBOX_VERSION} installed successfully ({_SINGBOX_ARCH}).")
        return True
    except Exception as e:
        logger.error(f"Failed to install Sing-box: {e}")
        return False


def generate_singbox_config(inbounds_data: dict, users_data: dict) -> dict:
    """Generate Sing-box config.json based on panel inbounds and users.

    Supports:
      - Hysteria2 (UDP/QUIC with TLS)
      - Shadowsocks-2022 (AEAD: 2022-blake3-aes-128-gcm / 256-gcm)
    """
    config = {
        "log": {
            "level": "warn",
            "timestamp": True,
        },
        "inbounds": [],
        "outbounds": [
            {
                "type": "direct",
                "tag": "direct",
            }
        ],
    }

    for iid, ib in inbounds_data.items():
        proto = (ib.get("protocol") or "").lower()

        if proto == "hysteria2":
            users = []
            for uid, u in users_data.items():
                inbound_ids = list(u.get("inbound_ids") or [])
                if u.get("inbound_id") and u["inbound_id"] not in inbound_ids:
                    inbound_ids.append(u["inbound_id"])

                if iid in inbound_ids and u.get("status") == "active":
                    # Hysteria2 password is the user's config UUID
                    password = u.get("config_uuid") or uid
                    users.append({
                        "name": u.get("username", uid),
                        "password": password,
                    })

            if users:
                port = int(ib.get("port", 443))
                up_mbps = int(ib.get("up_mbps", 100))
                down_mbps = int(ib.get("down_mbps", 100))

                # TLS config — use custom certs if provided, otherwise self-signed
                tls_config = {
                    "enabled": True,
                    "alpn": ["h3"],
                }
                cert_path = ib.get("cert_path", "")
                key_path = ib.get("key_path", "")
                if cert_path and key_path:
                    tls_config["certificate_path"] = cert_path
                    tls_config["key_path"] = key_path
                else:
                    # Self-signed for Hysteria2 (clients must skip cert verify)
                    tls_config["certificate_path"] = "/etc/xray/cert.pem"
                    tls_config["key_path"] = "/etc/xray/key.pem"

                inbound = {
                    "type": "hysteria2",
                    "tag": f"inbound-{iid}",
                    "listen": "::",
                    "listen_port": port,
                    "users": users,
                    "up_mbps": up_mbps,
                    "down_mbps": down_mbps,
                    "tls": tls_config,
                }
                # Optional: obfs password for obfs-plugin
                obfs_password = ib.get("obfs_password", "")
                if obfs_password:
                    inbound["obfs"] = {
                        "type": "password",
                        "password": obfs_password,
                    }
                config["inbounds"].append(inbound)

        elif proto == "shadowsocks-2022":
            users = []
            for uid, u in users_data.items():
                inbound_ids = list(u.get("inbound_ids") or [])
                if u.get("inbound_id") and u["inbound_id"] not in inbound_ids:
                    inbound_ids.append(u["inbound_id"])

                if iid in inbound_ids and u.get("status") == "active":
                    # Shadowsocks 2022 user password: base64(username:config_uuid)
                    import base64
                    ss_user = u.get("username", uid)
                    ss_uuid = u.get("config_uuid") or uid
                    user_password = base64.b64encode(
                        f"{ss_user}:{ss_uuid}".encode()
                    ).decode().rstrip("=")
                    users.append({
                        "name": ss_user,
                        "password": user_password,
                    })

            if users:
                # Global shared password (server secret)
                method = ib.get("ss_method", "2022-blake3-aes-128-gcm")
                global_password = ib.get("ss_password", "")

                config["inbounds"].append({
                    "type": "shadowsocks",
                    "tag": f"inbound-{iid}",
                    "listen": "::",
                    "listen_port": int(ib.get("port", 8388)),
                    "method": method,
                    "password": global_password,
                    "users": users,
                })

    return config


async def apply_singbox(inbounds_data: dict, users_data: dict):
    """Apply new config and restart Sing-box process.

    If no Hysteria2/SS-2022 inbounds exist, stops the process.
    If Sing-box binary is missing, downloads it first.
    """
    global _singbox_proc

    config = generate_singbox_config(inbounds_data, users_data)

    # No sing-box inbounds → stop the process
    if not config["inbounds"]:
        if _singbox_proc and _singbox_proc.returncode is None:
            try:
                _singbox_proc.terminate()
                await asyncio.wait_for(_singbox_proc.wait(), timeout=5)
            except Exception:
                try:
                    _singbox_proc.kill()
                except Exception:
                    pass
            _singbox_proc = None
            logger.info("Sing-box stopped (no Hysteria2/SS-2022 inbounds)")
        return

    if not await ensure_singbox():
        return

    async with _singbox_lock:
        # Stop previous process
        if _singbox_proc and _singbox_proc.returncode is None:
            _singbox_proc.terminate()
            try:
                await asyncio.wait_for(_singbox_proc.wait(), timeout=5)
            except Exception:
                try:
                    _singbox_proc.kill()
                except Exception:
                    pass

        # Write config
        try:
            SINGBOX_CONFIG.write_text(
                json.dumps(config, indent=2, ensure_ascii=False)
            )
        except Exception as e:
            logger.error(f"Failed to write Sing-box config: {e}")
            return

        # Start new process
        try:
            _singbox_proc = await asyncio.create_subprocess_exec(
                str(SINGBOX_BIN), "run", "-c", str(SINGBOX_CONFIG),
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.PIPE,
            )
            logger.info(
                f"Sing-box started (pid={_singbox_proc.pid}) "
                f"with {len(config['inbounds'])} inbound(s) "
                f"({', '.join(ib['type'] for ib in config['inbounds'])})"
            )
            # Log stderr in background for debugging
            asyncio.create_task(_log_singbox_stderr(_singbox_proc))
        except Exception as e:
            logger.error(f"Failed to start Sing-box: {e}")


async def _log_singbox_stderr(proc: asyncio.subprocess.Process):
    """Read and log Sing-box stderr for debugging (non-blocking)."""
    try:
        while True:
            line = await proc.stderr.readline()
            if not line:
                break
            text = line.decode("utf-8", errors="ignore").strip()
            if text:
                logger.debug(f"[sing-box] {text}")
    except Exception:
        pass


def get_singbox_status() -> dict:
    """Return current Sing-box process status."""
    if _singbox_proc is None:
        return {"running": False, "pid": None}
    return {
        "running": _singbox_proc.returncode is None,
        "pid": _singbox_proc.pid,
        "returncode": _singbox_proc.returncode,
    }
