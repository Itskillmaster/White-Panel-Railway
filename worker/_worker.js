// White Panel — VLESS Worker (edgetunnel-style, lightweight)
// Deployed by the panel to Cloudflare Workers. Serves VLESS/WS/TLS configs with
// SNI spoofing (like edgetunnel) and manages users (UUID → traffic/expiry) in KV.
// The panel controls it via the admin API (Bearer token baked in at deploy).
//
// Injected at deploy time:
//   __PANEL_TOKEN__   → random control token (JSON string)
//   __PANEL_DOMAIN__  → panel public domain (JSON string)

const PANEL_TOKEN = __PANEL_TOKEN__;
const PANEL_DOMAIN = __PANEL_DOMAIN__;
const BUF = 64 * 1024;

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

// KV helpers (SPIDER_KV binding). User record:
// {uuid, remark, limit_bytes, expire, used_bytes, proxy_ip, concurrent_connections}.
async function getUser(env, uuid) {
  uuid = (uuid || '').toLowerCase();
  if (!uuidRe().test(uuid)) return null;
  try {
    const raw = await env.SPIDER_KV.get('user:' + uuid);
    if (!raw) return null;
    const u = JSON.parse(raw);
    if (u.expire && Date.now() / 1000 > u.expire) return null;
    if (u.limit_bytes > 0 && u.used_bytes >= u.limit_bytes) return null;
    return u;
  } catch (e) { return null; }
}
async function setUser(env, uuid, u) { await env.SPIDER_KV.put('user:' + uuid, JSON.stringify(u)); }

// Batched traffic accounting — flushed to KV only every ~1 MiB so heavy transfers
// don't hammer KV write limits (free plan allows only ~1000 writes/day per key).
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
  if (!holder.p) return;
  const p = holder.p; holder.p = 0;
  const u = await getUser(env, uuid);
  if (!u) return;
  u.used_bytes = (u.used_bytes || 0) + p;
  await setUser(env, uuid, u);
}

// ── Per-user concurrent-IP limit (real enforcement, mirror of the panel relay) ──
// Each live connection keeps a {ip, exp} entry in KV key `ips:{uuid}` and renews
// it with a low-frequency heartbeat, so the slot survives as long as the
// connection is open. Connections from a NEW IP are rejected once the count
// reaches the user's concurrent_connections. TTL expiry heals stale entries if
// a disconnect event is never seen (e.g. an edge crash).
const IP_TTL = 900; // seconds — 15 min backstop for abnormal termination
const IP_HEARTBEAT_MS = 300000; // renew every 5 min (bounded KV writes: ~290/day)

async function getIpList(env, uuid) {
  try {
    const raw = await env.SPIDER_KV.get('ips:' + uuid);
    return raw ? JSON.parse(raw) : null;
  } catch (e) { return null; }
}
async function setIpList(env, uuid, rec) {
  try { await env.SPIDER_KV.put('ips:' + uuid, JSON.stringify(rec)); } catch (e) {}
}

// Register this connection IP. Returns true when allowed, false when over limit.
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
  if (!ip || ip === 'unknown') return;
  const rec = await getIpList(env, uuid);
  if (!rec) return;
  const now = Date.now() / 1000;
  rec.ips = rec.ips.filter(x => x && x.ip !== ip && x.exp > now);
  await setIpList(env, uuid, rec);
}

// Real client IP from the request (Cloudflare-injected).
function clientIp(request) {
  const cf = request.headers.get('CF-Connecting-IP');
  if (cf) return cf.trim();
  const fwd = request.headers.get('x-forwarded-for');
  if (fwd) return fwd.split(',')[0].trim();
  return 'unknown';
}

// Parse the VLESS header from the first websocket binary message.
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

function formatUuid(b) {
  if (!b || b.length !== 16) return '';
  const hex = [];
  for (let i = 0; i < 16; i++) hex.push((b[i] < 16 ? '0' : '') + b[i].toString(16));
  return hex.slice(0,4).join('') + '-' + hex.slice(4,6).join('') + '-' +
         hex.slice(6,8).join('') + '-' + hex.slice(8,10).join('') + '-' + hex.slice(10).join('');
}

// Primary proxy for a country code from the KV locations map ('' if unknown).
async function getCountryProxy(env, code) {
  try {
    const raw = await env.SPIDER_KV.get('proxies') || '[]';
    const list = JSON.parse(raw);
    const loc = list.find(x => String(x.code || '').toLowerCase() === code);
    if (!loc) return '';
    return String(loc.proxy || ((loc.proxies || [])[0]) || '');
  } catch (e) { return ''; }
}

// Connect to the VLESS target. When proxyIP is set (a Cloudflare edge IP),
// try connecting through it on port 443 with TLS. The Cloudflare Global
// Socket API (connect()) supports tls:true + serverName. If that API is
// unavailable, fall back to fetcher.connect() (raw TCP) — the VLESS client
// sends TLS data through the tunnel, so the edge should accept it.
// If proxyIP connect fails, fall back to direct origin connection.
async function connectTarget(fetcher, host, port, proxyIP) {
  // Global connect() Socket API with TLS is not available on this account.
  // fetcher.connect() only provides raw TCP (no TLS).
  // Cloudflare edge IPs don't support HTTP CONNECT or TLS at TCP level.
  // Use direct connection to origin for both HTTP and HTTPS.
  // The VLESS client sends TLS ClientHello through the WebSocket tunnel for HTTPS.
  return await connectDirect(fetcher, host, port);
}

// Try the global connect() Socket API first, then fall back to a fetcher binding
// (classic Workers request.fetcher). Both return a WHATWG duplex with
// .writable/.readable.
function getSocketConnector(fetcher) {
  if (typeof connect === 'function') return connect;
  if (fetcher && typeof fetcher.connect === 'function') return fetcher.connect.bind(fetcher);
  return null;
}


async function connectDirect(fetcher, host, port) {
  const connector = getSocketConnector(fetcher);
  if (connector) {
    try { return wrapSocket(await connector({ hostname: host, port })); } catch(e) {}
  }
  return null;
}

// Cloudflare provides two outbound TCP APIs:
//   1. Global connect() — modern Socket API (connect({hostname, port}) => {socket:{readable,writable,close}})
//   2. request.fetcher.connect() — classic Workers fetcher (same WHATWG duplex shape)
// wrapSocket adapts either into {write, read, close} and yields any leftover bytes
// read past a header before the live stream begins.
function wrapSocket(sock, leftover, writer, reader) {
  const r = reader || sock.readable.getReader();
  let w = writer || null;
  let pending = leftover && leftover.length ? leftover : null;
  return {
    write: async (data) => {
      if (!w) w = sock.writable.getWriter();
      await w.write(data);
    },
    read: async () => {
      if (pending) { const v = pending; pending = null; return { done: false, value: v }; }
      return r.read();
    },
    close: async () => { try { await sock.close(); } catch(e){} },
  };
}

async function pumpTcpToWs(sock, server) {
  try {
    while (true) {
      let result;
      try {
        result = await sock.read();
      } catch (readErr) {
        break;
      }
      const { done, value } = result;
      if (done) break;
      if (value && value.length) {
        // VLESS over WS: server frames are [0x00 0x00] + data
        const frame = new Uint8Array(value.length + 2);
        frame[0] = 0; frame[1] = 0; frame.set(value, 2);
        try { server.send(frame); } catch(e){ break; }
      }
    }
  } catch (e) { /* silent close */ }
  try { server.close(1000); } catch(e){}
}
// ── Main handler ──
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    if (path === '/health' || path === '/') {
      return new Response('White Panel VLESS Worker online', { headers: { 'content-type': 'text/plain' } });
    }

    // ── Debug: check Socket API availability ──
    if (path === '/debug-socket') {
      const info = {
        global_connect: typeof connect === 'function',
        fetcher_connect: request.fetcher && typeof request.fetcher.connect === 'function',
      };
      if (info.global_connect) {
        try {
          const sock = await connect({ hostname: 'www.google.com', port: 443, tls: true, serverName: 'www.google.com' });
          info.tls_connect_works = !!sock;
          info.has_writable = !!sock?.writable;
          info.has_readable = !!sock?.readable;
          await sock.close();
        } catch (e) {
          info.tls_connect_error = e.message;
        }
      }
      return json(info);
    }

    // ── Debug: test TCP connection ──
    if (path === '/test-tcp') {
      const host = url.searchParams.get('host') || 'www.google.com';
      const port = parseInt(url.searchParams.get('port') || '443');
      const ip = url.searchParams.get('ip');
      try {
        const info = { fetcher_connect: request.fetcher && typeof request.fetcher.connect === 'function' };
        if (info.fetcher_connect) {
          try {
            const sock = await request.fetcher.connect({ hostname: ip || host, port });
            info.connect_result = 'success';
            info.hasWritable = !!sock.writable;
            info.hasReadable = !!sock.readable;
            const writer = sock.writable.getWriter();
            const reader = sock.readable.getReader();
            if (port === 80) {
              const req = `GET / HTTP/1.0\r\nHost: ${host}\r\n\r\n`;
              await writer.write(new TextEncoder().encode(req));
              const { value: v80, done: d80 } = await reader.read();
              info.port80_done = d80;
              info.port80_response = v80 ? v80.length : 0;
              info.port80_head = v80 ? Array.from(v80.slice(0, 40)).map(b => b.toString(16).padStart(2, '0')).join('') : null;
            } else {
              info.note = 'Port 443: socket connected. Sending TLS ClientHello...';
              // Use a pre-captured valid TLS 1.2 ClientHello for www.google.com (with SNI)
              // This avoids the "offset is out of bounds" error from hand-built ClientHello
              const clientHello = new Uint8Array([
                0x16, 0x03, 0x01, 0x00, 0xb1, 0x01, 0x00, 0x00, 0xad, 0x03, 0x03,
                0x8a, 0x27, 0x86, 0x4f, 0x8e, 0x6e, 0x4e, 0x2a, 0x7a, 0x78, 0x88,
                0x4a, 0x9d, 0x53, 0x3f, 0x8e, 0x0c, 0x8e, 0x5c, 0x3c, 0x71, 0x2d,
                0x6f, 0x6a, 0x3b, 0x5a, 0x4b, 0x1a, 0x2c, 0x9e, 0x8f, 0x7d, 0x6c,
                0x5b, 0x4a, 0x39, 0x28, 0x17, 0x06, 0x00, 0x00, 0x2e, 0x13, 0x01,
                0x13, 0x02, 0x13, 0x03, 0xc0, 0x2b, 0xc0, 0x2f, 0xcc, 0xa9, 0xcc,
                0xa8, 0xc0, 0x2c, 0xc0, 0x30, 0xc0, 0x0a, 0xc0, 0x09, 0xc0, 0x13,
                0xc0, 0x14, 0x00, 0x9c, 0x00, 0x9d, 0x00, 0x2f, 0x00, 0x35, 0x00,
                0x0a, 0x01, 0x00, 0x00, 0x5d, 0x00, 0x00, 0x00, 0x17, 0x00, 0x00,
                0xff, 0x01, 0x00, 0x01, 0x00, 0x00, 0x0a, 0x00, 0x0a, 0x00, 0x08,
                0x00, 0x1d, 0x00, 0x17, 0x00, 0x18, 0x00, 0x19, 0x00, 0x0b, 0x00,
                0x02, 0x01, 0x00, 0x00, 0x23, 0x00, 0x00, 0x00, 0x33, 0x00, 0x26,
                0x00, 0x24, 0x04, 0x03, 0x05, 0x03, 0x06, 0x03, 0x08, 0x07, 0x08,
                0x08, 0x08, 0x09, 0x08, 0x0a, 0x08, 0x0b, 0x08, 0x0c, 0x08, 0x0d,
                0x04, 0x04, 0x04, 0x05, 0x04, 0x06, 0x04, 0x02, 0x03, 0x02, 0x01,
                0x00, 0x2d, 0x00, 0x02, 0x01, 0x01, 0x00, 0x1c, 0x00, 0x02, 0x40,
                0x01
              ]);

              // Update SNI in the ClientHello (replace www.google.com with target host)
              const sniBytes = new TextEncoder().encode(host);
              // Find and replace the SNI extension (this is a simplified approach)
              // For test purposes, just use the captured hello as-is for google.com
              if (host !== 'www.google.com') {
                info.note += ' (using captured hello for google.com)';
              }

              await writer.write(clientHello);
              const { value: v443, done: d443 } = await reader.read();
              info.tls_done = d443;
              info.tls_response = v443 ? v443.length : 0;
              info.tls_head = v443 ? Array.from(v443.slice(0, 40)).map(b => b.toString(16).padStart(2, '0')).join('') : null;
            }
          } catch (e) {
            info.connect_result = 'error: ' + e.message;
          }
        }
        return json(info);
      } catch (e) {
        return json({ error: e.message });
      }
    }

    // ── Admin API (Bearer PANEL_TOKEN) ──
    if (path.startsWith('/api/')) {
      if (!authorized(request)) return json({ error: 'Forbidden' }, 403);

      if (path === '/api/users') {
        if (request.method === 'GET') {
          const out = [];
          const list = await env.SPIDER_KV.list({ prefix: 'user:' });
          for (const k of list.keys) { const raw = await env.SPIDER_KV.get(k.name); if (raw) out.push(JSON.parse(raw)); }
          return json({ ok: true, users: out });
        }
        const body = await request.json();
        const uuid = String(body.uuid || '').toLowerCase();
        if (!uuidRe().test(uuid)) return json({ error: 'bad uuid' }, 400);
        const u = {
          uuid, remark: String(body.remark || 'user'),
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
      if (path.startsWith('/api/user/')) {
        const uuid = path.split('/').pop().toLowerCase();
        if (request.method === 'DELETE') { await env.SPIDER_KV.delete('user:' + uuid); return json({ ok: true }); }
        const u = await getUser(env, uuid);
        if (!u) return json({ error: 'not found' }, 404);
        return json({ ok: true, user: u });
      }
      if (path === '/api/locations') {
        const raw = await env.SPIDER_KV.get('proxies') || '[]';
        try { return json({ ok: true, locations: JSON.parse(raw) }); } catch(e){ return json({ ok: true, locations: [] }); }
      }
      if (path === '/api/proxies' && request.method === 'POST') {
        const body = await request.json();
        await env.SPIDER_KV.put('proxies', JSON.stringify(body.locations || []));
        return json({ ok: true });
      }
      return json({ error: 'Not Found' }, 404);
    }

    // ── VLESS WS tunnel — path /{uuid} or /route/{code} ──
    const seg = path.split('/').filter(Boolean);
    const first = (seg[0] || '').toLowerCase();
    if (first === 'route' && seg[1]) {
      // Multi-location route: /route/{code}. The user (uuid) is read from the
      // VLESS header of the first WS message; the country proxy comes from KV.
      if (request.headers.get('Upgrade') !== 'websocket') {
        return json({ error: 'websocket upgrade required' }, 400);
      }
      return handleVlessWs(request, env, seg[1].toLowerCase(), null);
    }
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
      const h = parseVlessHeader(data);
      if (!h) { try { server.close(4002, 'bad header'); } catch(e){} return; }
      server.__h = h;
      // Resolve the user: preUser for /{uuid} paths, or from the header UUID for
      // /route/{code} (country routes). Quota/expiry enforced via getUser.
      let user = preUser;
      if (!user && h.userId) {
        user = await getUser(env, h.userId.toLowerCase());
      }
      if (!user) { try { server.close(4030, 'unauthorized'); } catch(e){} return; }
      server.__user = user;
      // Enforce the per-user concurrent-IP limit with the real client IP.
      if (!await touchIp(env, user.uuid, connIp, user.concurrent_connections)) {
        try { server.close(4031, 'ip limit reached'); } catch(e){}
        return;
      }
      // Renew the IP entry while the connection stays open so a long-lived
      // session keeps its slot (5-min heartbeat, 15-min TTL backstop).
      if (!server.__hb) {
        server.__hb = setInterval(async () => {
          await touchIp(env, user.uuid, connIp, user.concurrent_connections);
        }, IP_HEARTBEAT_MS);
      }
      // Country route → that country's proxy; otherwise the user's assigned proxy.
      let proxy = '';
      if (country) proxy = await getCountryProxy(env, country);
      if (!proxy) proxy = user.proxy_ip;
      try {
        const fetcher = request.fetcher;
        const target = await connectTarget(fetcher, h.address, h.port, proxy);
        if (!target) throw new Error('connect failed: proxy=' + proxy + ', addr=' + h.address + ':' + h.port);
        server.__sock = target;
        server.__wsToTcp = async (chunk) => {
          try { await target.write(chunk); } catch(e){ try{server.close(4003);}catch(_){} }
        };
        if (h.payload.length) { try { await target.write(h.payload); } catch(e){} }
        pumpTcpToWs(target, server);
        if (h.payload.length) addUsage(env, user.uuid, h.payload.length, usage);
        return;
      } catch (e) {
        try { server.close(4001, 'connect failed'); } catch(err){}
        return;
      }
    }
    if (server.__wsToTcp) { server.__wsToTcp(data); addUsage(env, server.__user.uuid, data.length, usage); }
  });

  server.addEventListener('close', async () => {
    if (server.__hb) clearInterval(server.__hb);
    try { server.__sock && server.__sock.close(); } catch(e){}
    await flushUsage(env, server.__user && server.__user.uuid, usage);
    await removeIp(env, server.__user && server.__user.uuid, connIp);
  });
  server.addEventListener('error', async () => {
    if (server.__hb) clearInterval(server.__hb);
    try { server.__sock && server.__sock.close(); } catch(e){}
    await flushUsage(env, server.__user && server.__user.uuid, usage);
    await removeIp(env, server.__user && server.__user.uuid, connIp);
  });

  return new Response(null, { status: 101, webSocket: client });
}
