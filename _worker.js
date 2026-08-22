// White Panel — VLESS Worker (ESM Module)
// ══════════════════════════════════════════════════════════════════════════════
// Deployed by the panel to Cloudflare Workers. Serves VLESS/WS/TLS configs with
// country-based routing and manages users (UUID → traffic/expiry) in KV.
//
// Route handling:
//   /{uuid}          → direct VLESS WS tunnel (user's assigned proxy_ip)
//   /route/{code}    → multi-location: looks up country proxy from KV, authenticates
//                       user from the VLESS header UUID
//
// Injected at deploy time:
//   __PANEL_TOKEN__   → random control token (JSON string)
//   __PANEL_DOMAIN__  → panel public domain (JSON string)
// ══════════════════════════════════════════════════════════════════════════════

const PANEL_TOKEN = __PANEL_TOKEN__;
const PANEL_DOMAIN = __PANEL_DOMAIN__;
const BUF = 64 * 1024;

// ── Utility ─────────────────────────────────────────────────────────────────
function json(data, status) {
  return new Response(JSON.stringify(data), {
    status: status || 200,
    headers: { 'content-type': 'application/json', 'access-control-allow-origin': '*' },
  });
}
function authorized(request) {
  return (request.headers.get('Authorization') || '') === 'Bearer ' + PANEL_TOKEN;
}
function uuidRe() { return /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i; }

// ── KV Helpers ──────────────────────────────────────────────────────────────
// User record: {uuid, remark, limit_bytes, expire, used_bytes, proxy_ip, concurrent_connections}
async function getUser(env, uuid) {
  uuid = (uuid || '').toLowerCase();
  if (!uuidRe().test(uuid)) return null;
  try {
    const raw = await env.WHITE_KV.get('user:' + uuid);
    if (!raw) return null;
    const u = JSON.parse(raw);
    if (u.expire && Date.now() / 1000 > u.expire) return null;
    if (u.limit_bytes > 0 && (u.used_bytes || 0) >= u.limit_bytes) return null;
    return u;
  } catch (e) { return null; }
}
async function setUser(env, uuid, u) {
  await env.WHITE_KV.put('user:' + uuid, JSON.stringify(u));
}

// ── Batched Traffic Accounting ───────────────────────────────────────────────
// Flushed to KV only every ~1 MiB to stay within KV write limits.
async function addUsage(env, uuid, n, holder) {
  holder.p = (holder.p || 0) + n;
  if (holder.p < 1048576) return true;
  const p = holder.p; holder.p = 0;
  const u = await getUser(env, uuid);
  if (!u) return false;
  u.used_bytes = (u.used_bytes || 0) + p;
  await setUser(env, uuid, u);
  return !(u.limit_bytes > 0 && u.used_bytes >= u.limit_bytes);
}
async function flushUsage(env, uuid, holder) {
  if (!holder.p || !uuid) return;
  const p = holder.p; holder.p = 0;
  const u = await getUser(env, uuid);
  if (!u) return;
  u.used_bytes = (u.used_bytes || 0) + p;
  await setUser(env, uuid, u);
}

// ── Per-User Concurrent-IP Limit ────────────────────────────────────────────
const IP_TTL = 900;
const IP_HEARTBEAT_MS = 300000;

async function getIpList(env, uuid) {
  try {
    const raw = await env.WHITE_KV.get('ips:' + uuid);
    return raw ? JSON.parse(raw) : null;
  } catch (e) { return null; }
}
async function setIpList(env, uuid, rec) {
  try { await env.WHITE_KV.put('ips:' + uuid, JSON.stringify(rec)); } catch (e) {}
}
async function touchIp(env, uuid, ip, maxIp) {
  if (!ip || ip === 'unknown' || ip === '127.0.0.1') return true;
  if (!maxIp || maxIp < 1) return true;
  const now = Date.now() / 1000;
  const rec = (await getIpList(env, uuid)) || { ips: [] };
  const live = rec.ips.filter(x => x && x.exp > now);
  const existing = live.find(x => x.ip === ip);
  if (existing) {
    existing.exp = now + IP_TTL;
  } else if (live.length >= maxIp) {
    return false;
  } else {
    live.push({ ip, exp: now + IP_TTL });
  }
  await setIpList(env, uuid, { ips: live });
  return true;
}
async function removeIp(env, uuid, ip) {
  if (!ip || ip === 'unknown' || !uuid) return;
  const rec = await getIpList(env, uuid);
  if (!rec) return;
  const now = Date.now() / 1000;
  rec.ips = rec.ips.filter(x => x && x.ip !== ip && x.exp > now);
  await setIpList(env, uuid, rec);
}

// ── Client IP ───────────────────────────────────────────────────────────────
function clientIp(request) {
  const cf = request.headers.get('CF-Connecting-IP');
  if (cf) return cf.trim();
  const fwd = request.headers.get('x-forwarded-for');
  if (fwd) return fwd.split(',')[0].trim();
  return 'unknown';
}

// ── VLESS Protocol Parsing ──────────────────────────────────────────────────
function formatUuid(b) {
  if (!b || b.length !== 16) return '';
  const hex = [];
  for (let i = 0; i < 16; i++) hex.push((b[i] < 16 ? '0' : '') + b[i].toString(16));
  return hex.slice(0,4).join('') + '-' + hex.slice(4,6).join('') + '-' +
         hex.slice(6,8).join('') + '-' + hex.slice(8,10).join('') + '-' + hex.slice(10).join('');
}

function parseVlessHeader(data) {
  if (data.length < 24) return null;
  let pos = 1;
  const userId = formatUuid(data.subarray(pos, pos + 16)); pos += 16;
  const addonLen = data[pos]; pos += 1 + addonLen;
  pos += 1; // command (1 = TCP)
  const port = (data[pos] << 8) | data[pos + 1]; pos += 2;
  const atype = data[pos]; pos += 1;
  let address;
  if (atype === 1) { address = data.slice(pos, pos + 4).join('.'); pos += 4; }
  else if (atype === 2) { const dlen = data[pos]; pos += 1; address = new TextDecoder().decode(data.subarray(pos, pos + dlen)); pos += dlen; }
  else if (atype === 3) { const b = data.subarray(pos, pos + 16); pos += 16; const hex=[]; for(let i=0;i<16;i+=2) hex.push(((b[i]<<8)|b[i+1]).toString(16)); address=hex.join(':'); }
  else return null;
  return { userId, address, port, payload: data.subarray(pos) };
}

// ── Country Proxy Lookup ────────────────────────────────────────────────────
async function getCountryProxy(env, code) {
  try {
    const raw = await env.WHITE_KV.get('proxies') || '[]';
    const list = JSON.parse(raw);
    const loc = list.find(x => String(x.code || '').toLowerCase() === code);
    if (!loc) return '';
    return String(loc.proxy || ((loc.proxies || [])[0]) || '');
  } catch (e) { return ''; }
}

// ── Outbound Connection ─────────────────────────────────────────────────────
// Uses Cloudflare's connect() Socket API to establish outbound TCP.
// When proxyIP is provided, connects to the proxy IP on port 443 with TLS.
// The VLESS client sends TLS ClientHello through the WS tunnel, so the
// proxy (Cloudflare edge) accepts it via SNI-based routing.
//
// Connection priority:
//   1. connect() with TLS to proxyIP:443 (best — uses edge routing)
//   2. connect() raw TCP to proxyIP:443 (fallback — VLESS client handles TLS)
//   3. connect() raw TCP to target host:port (last resort — direct connection)
function getConnector(fetcher) {
  if (typeof connect === 'function') return connect;
  if (fetcher && typeof fetcher.connect === 'function') return fetcher.connect.bind(fetcher);
  return null;
}

async function connectToProxy(proxyIP) {
  const connector = getConnector();
  if (!connector || !proxyIP) return null;

  const [host, portStr] = proxyIP.split(':');
  const port = parseInt(portStr) || 443;

  // Try TLS connection through the proxy (Cloudflare edge handles TLS termination)
  try {
    const sock = await connector({ hostname: host, port, tls: true, serverName: host });
    if (sock && sock.readable && sock.writable) {
      return { socket: sock, reader: sock.readable.getReader(), writer: sock.writable.getWriter() };
    }
  } catch (e) { /* TLS not supported on this proxy, try raw TCP */ }

  // Fallback: raw TCP to proxy (VLESS client sends TLS ClientHello through tunnel)
  try {
    const sock = await connector({ hostname: host, port });
    if (sock && sock.readable && sock.writable) {
      return { socket: sock, reader: sock.readable.getReader(), writer: sock.writable.getWriter() };
    }
  } catch (e) { /* proxy connect failed */ }

  return null;
}

async function connectDirect(host, port) {
  const connector = getConnector();
  if (!connector) return null;
  try {
    const sock = await connector({ hostname: host, port });
    if (sock && sock.readable && sock.writable) {
      return { socket: sock, reader: sock.readable.getReader(), writer: sock.writable.getWriter() };
    }
  } catch (e) {}
  return null;
}

// ── VLESS WebSocket Tunnel ──────────────────────────────────────────────────
async function handleVlessWs(request, env, country, preUser) {
  const pair = new WebSocketPair();
  const [client, server] = Object.values(pair);
  server.accept();
  server.binaryType = 'arraybuffer';
  const connIp = clientIp(request);
  const usage = { p: 0 };

  server.addEventListener('message', async (ev) => {
    const data = new Uint8Array(ev.data);
    if (!server.__h) {
      // First message: parse VLESS header to get target address + user UUID
      const h = parseVlessHeader(data);
      if (!h) { try { server.close(4002, 'bad header'); } catch(e){} return; }
      server.__h = h;

      // Resolve user: preUser for /{uuid} paths, or from VLESS header for /route/{code}
      let user = preUser;
      if (!user && h.userId) {
        user = await getUser(env, h.userId.toLowerCase());
      }
      if (!user) { try { server.close(4030, 'unauthorized'); } catch(e){} return; }
      server.__user = user;

      // Enforce per-user concurrent-IP limit
      if (!await touchIp(env, user.uuid, connIp, user.concurrent_connections)) {
        try { server.close(4031, 'ip limit reached'); } catch(e){}
        return;
      }

      // Heartbeat: renew IP entry every 5 min while connection stays open
      if (!server.__hb) {
        server.__hb = setInterval(async () => {
          await touchIp(env, user.uuid, connIp, user.concurrent_connections);
        }, IP_HEARTBEAT_MS);
      }

      // Resolve proxy: country route → country's proxy; otherwise user's proxy_ip
      let proxy = '';
      if (country) proxy = await getCountryProxy(env, country);
      if (!proxy) proxy = user.proxy_ip;

      // Establish outbound connection
      let conn = null;
      if (proxy) {
        conn = await connectToProxy(proxy);
      }
      if (!conn) {
        // Direct connection to target (no proxy)
        conn = await connectDirect(h.address, h.port);
      }
      if (!conn) {
        try { server.close(4001, 'connect failed'); } catch(e){}
        return;
      }

      server.__conn = conn;
      server.__wsToTcp = async (chunk) => {
        try { await conn.writer.write(chunk); } catch(e){ try{server.close(4003);}catch(_){} }
      };

      // Send any leftover payload from the first message
      if (h.payload.length) {
        try { await conn.writer.write(h.payload); } catch(e){}
        addUsage(env, user.uuid, h.payload.length, usage);
      }

      // Start reading from TCP → WebSocket
      pumpTcpToWs(conn, server);
      return;
    }

    // Subsequent messages: forward raw data to TCP
    if (server.__wsToTcp) {
      server.__wsToTcp(data);
      addUsage(env, server.__user.uuid, data.length, usage);
    }
  });

  server.addEventListener('close', async () => {
    if (server.__hb) clearInterval(server.__hb);
    try { server.__conn && server.__conn.socket.close(); } catch(e){}
    await flushUsage(env, server.__user && server.__user.uuid, usage);
    await removeIp(env, server.__user && server.__user.uuid, connIp);
  });
  server.addEventListener('error', async () => {
    if (server.__hb) clearInterval(server.__hb);
    try { server.__conn && server.__conn.socket.close(); } catch(e){}
    await flushUsage(env, server.__user && server.__user.uuid, usage);
    await removeIp(env, server.__user && server.__user.uuid, connIp);
  });

  return new Response(null, { status: 101, webSocket: client });
}

// ── TCP → WebSocket Pump ────────────────────────────────────────────────────
async function pumpTcpToWs(conn, server) {
  try {
    while (true) {
      const { done, value } = await conn.reader.read();
      if (done) break;
      if (value && value.length) {
        // VLESS over WS: frame = [0x00 0x00] + data
        const frame = new Uint8Array(value.length + 2);
        frame[0] = 0; frame[1] = 0; frame.set(value, 2);
        try { server.send(frame); } catch(e){ break; }
      }
    }
  } catch (e) { /* silent close */ }
  try { server.close(1000); } catch(e){}
}

// ══════════════════════════════════════════════════════════════════════════════
// Main Handler
// ══════════════════════════════════════════════════════════════════════════════
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    // ── Health / Debug ──
    if (path === '/health' || path === '/') {
      return new Response('White VLESS Worker online', { headers: { 'content-type': 'text/plain' } });
    }
    if (path === '/debug-socket') {
      const info = { global_connect: typeof connect === 'function' };
      if (info.global_connect) {
        try {
          const sock = await connect({ hostname: 'www.google.com', port: 443, tls: true, serverName: 'www.google.com' });
          info.tls_works = true;
          await sock.close();
        } catch (e) { info.tls_error = e.message; }
      }
      return json(info);
    }

    // ── Admin API (Bearer PANEL_TOKEN) ──
    if (path.startsWith('/api/')) {
      if (!authorized(request)) return json({ error: 'Forbidden' }, 403);

      // GET /api/users — list all users
      if (path === '/api/users' && request.method === 'GET') {
        const out = [];
        const list = await env.WHITE_KV.list({ prefix: 'user:' });
        for (const k of list.keys) {
          const raw = await env.WHITE_KV.get(k.name);
          if (raw) out.push(JSON.parse(raw));
        }
        return json({ ok: true, users: out });
      }

      // POST /api/users — create/update a user
      if (path === '/api/users' && request.method === 'POST') {
        const body = await request.json();
        const uuid = String(body.uuid || '').toLowerCase();
        if (!uuidRe().test(uuid)) return json({ error: 'bad uuid' }, 400);
        const u = {
          uuid,
          remark: String(body.remark || 'user'),
          limit_bytes: Number(body.limit_bytes) || 0,
          expire: Number(body.expire) || 0,
          used_bytes: Number(body.used_bytes) || 0,
          proxy_ip: String(body.proxy_ip || ''),
          concurrent_connections: Number(body.concurrent_connections) || 0,
          created: Date.now(),
        };
        await setUser(env, uuid, u);
        return json({ ok: true, user: u });
      }

      // GET/DELETE /api/user/{uuid}
      if (path.startsWith('/api/user/')) {
        const uuid = path.split('/').pop().toLowerCase();
        if (request.method === 'DELETE') {
          await env.WHITE_KV.delete('user:' + uuid);
          return json({ ok: true });
        }
        const u = await getUser(env, uuid);
        if (!u) return json({ error: 'not found' }, 404);
        return json({ ok: true, user: u });
      }

      // GET /api/locations — list country proxy locations
      if (path === '/api/locations' && request.method === 'GET') {
        const raw = await env.WHITE_KV.get('proxies') || '[]';
        try { return json({ ok: true, locations: JSON.parse(raw) }); } catch(e){ return json({ ok: true, locations: [] }); }
      }

      // POST /api/proxies — update proxy map
      if (path === '/api/proxies' && request.method === 'POST') {
        const body = await request.json();
        await env.WHITE_KV.put('proxies', JSON.stringify(body.locations || []));
        return json({ ok: true });
      }

      return json({ error: 'Not Found' }, 404);
    }

    // ── VLESS WS Tunnel ──
    // Supported paths:
    //   /{uuid}          → direct tunnel (user's proxy_ip from KV)
    //   /route/{code}    → country-based routing (proxy from KV 'proxies' map)
    const seg = path.split('/').filter(Boolean);
    const first = (seg[0] || '').toLowerCase();

    // Route: /route/{code} — multi-location with country proxy lookup
    if (first === 'route' && seg[1]) {
      if (request.headers.get('Upgrade') !== 'websocket') {
        return json({ error: 'websocket upgrade required' }, 400);
      }
      return handleVlessWs(request, env, seg[1].toLowerCase(), null);
    }

    // Direct: /{uuid} — user authenticated by UUID in path
    if (uuidRe().test(first)) {
      const u = await getUser(env, first);
      if (!u) return json({ error: 'unauthorized' }, 403);
      if (request.headers.get('Upgrade') === 'websocket') {
        return handleVlessWs(request, env, '', u);
      }
      return json({ error: 'websocket upgrade required' }, 400);
    }

    return json({ error: 'Not Found' }, 404);
  },
};
