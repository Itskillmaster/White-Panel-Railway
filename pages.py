# pages.py â€” White Panel Enterprise Theme
# Exports: LOGIN_HTML, DASHBOARD_HTML, get_public_page_html()

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ÙˆØ±ÙˆØ¯ Â· White Panel</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Estedad:wght@300;400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
:root{
  --wp-blue:#6366f1;--wp-purple:#8b5cf6;--wp-red:#ef4444;
  --text-primary:#0F172A;--text-secondary:#475569;
  --bg:#F8FAFC;--surface:#FFFFFF;--border:#E2E8F0;
  --radius-sm:12px;--radius:18px;--radius-lg:24px;--radius-xl:28px;
}
[data-theme="dark"]{
  --text-primary:#F1F5F9;--text-secondary:#94A3B8;
  --bg:#030712;--surface:rgba(15,23,42,.85);--border:rgba(148,163,184,.08);
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%;overflow:hidden}
body{font-family:'Estedad',sans-serif;background:var(--bg);display:flex;align-items:center;justify-content:center;padding:20px;transition:background .5s ease}

/* === Animated Mesh Gradient Background === */
.bg-layer{position:fixed;inset:0;z-index:0;overflow:hidden;background:linear-gradient(135deg,#eef2ff 0%,#f5f3ff 50%,#fef2f2 100%)}
[data-theme="dark"] .bg-layer{background:#030712}
.morph-blob{position:absolute;border-radius:40% 60% 70% 30%/40% 50% 60% 50%;filter:blur(90px);animation:morphDrift 14s ease-in-out infinite alternate,blobFloat 10s ease-in-out infinite}
.morph-blob.b1{width:600px;height:600px;background:rgba(99,102,241,.22);top:-250px;left:-150px;animation-duration:14s,12s}
[data-theme="dark"] .morph-blob.b1{background:rgba(99,102,241,.12)}
.morph-blob.b2{width:500px;height:500px;background:rgba(139,92,246,.18);bottom:-200px;right:-180px;animation-delay:-4s,0s;animation-duration:16s,11s}
[data-theme="dark"] .morph-blob.b2{background:rgba(139,92,246,.1)}
.morph-blob.b3{width:420px;height:420px;background:rgba(239,68,68,.1);top:30%;left:50%;animation-delay:-8s,-3s;animation-duration:18s,13s}
[data-theme="dark"] .morph-blob.b3{background:rgba(239,68,68,.06)}
.morph-blob.b4{width:350px;height:350px;background:rgba(167,139,250,.15);top:60%;left:10%;animation-delay:-2s,-6s;animation-duration:15s,14s}
[data-theme="dark"] .morph-blob.b4{background:rgba(167,139,250,.08)}
@keyframes morphDrift{
  0%{border-radius:40% 60% 70% 30%/40% 50% 60% 50%}
  25%{border-radius:60% 40% 30% 70%/50% 60% 40% 50%}
  50%{border-radius:30% 60% 50% 40%/60% 40% 70% 30%}
  75%{border-radius:50% 40% 60% 50%/30% 70% 40% 60%}
  100%{border-radius:40% 60% 70% 30%/40% 50% 60% 50%}
}
@keyframes blobFloat{0%,100%{transform:translateY(0) scale(1)}50%{transform:translateY(-40px) scale(1.06)}}

/* === Grid overlay === */
.grid-bg{position:fixed;inset:0;z-index:0;opacity:.4;background-image:linear-gradient(rgba(99,102,241,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(99,102,241,.035) 1px,transparent 1px);background-size:48px 48px}

/* === Floating Particles (dots) === */
.particles{position:fixed;inset:0;z-index:1;pointer-events:none}
.particle{position:absolute;border-radius:50%;opacity:0;animation:particleFloat linear infinite}
.particle:nth-child(1){width:4px;height:4px;background:var(--wp-blue);top:18%;left:12%;animation-duration:16s}
.particle:nth-child(2){width:3px;height:3px;background:var(--wp-purple);top:58%;left:22%;animation-duration:20s;animation-delay:-6s}
.particle:nth-child(3){width:5px;height:5px;background:var(--wp-red);top:28%;left:68%;animation-duration:18s;animation-delay:-9s}
.particle:nth-child(4){width:3px;height:3px;background:var(--wp-blue);top:72%;left:52%;animation-duration:22s;animation-delay:-3s}
.particle:nth-child(5){width:4px;height:4px;background:var(--wp-purple);top:8%;left:42%;animation-duration:17s;animation-delay:-12s}
.particle:nth-child(6){width:3px;height:3px;background:var(--wp-red);top:82%;left:78%;animation-duration:24s;animation-delay:-8s}
.particle:nth-child(7){width:4px;height:4px;background:var(--wp-blue);top:42%;left:32%;animation-duration:19s;animation-delay:-5s}
.particle:nth-child(8){width:3px;height:3px;background:var(--wp-purple);top:52%;left:62%;animation-duration:21s;animation-delay:-10s}
.particle:nth-child(9){width:2px;height:2px;background:var(--wp-red);top:35%;left:85%;animation-duration:15s;animation-delay:-2s}
.particle:nth-child(10){width:3px;height:3px;background:var(--wp-blue);top:65%;left:8%;animation-duration:23s;animation-delay:-7s}
@keyframes particleFloat{
  0%{transform:translate(0,0) scale(1);opacity:0}
  10%{opacity:.6}
  50%{opacity:.4}
  90%{opacity:.5}
  100%{transform:translate(50px,-70px) scale(.3);opacity:0}
}

/* === Login Wrap & Card === */
.login-wrap{position:relative;z-index:10;width:100%;max-width:440px;animation:cardEntrance .8s cubic-bezier(.22,1,.36,1) both}
@keyframes cardEntrance{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}

.login-card{
  background:rgba(255,255,255,.65);
  backdrop-filter:blur(32px) saturate(200%);
  -webkit-backdrop-filter:blur(32px) saturate(200%);
  border-radius:var(--radius-xl);
  padding:44px 36px 38px;
  position:relative;
  overflow:hidden;
  transition:all .35s ease;
}
/* Animated gradient border */
.login-card::before{
  content:'';position:absolute;inset:0;border-radius:var(--radius-xl);
  padding:1.5px;
  background:linear-gradient(135deg,var(--wp-blue),var(--wp-purple),var(--wp-red),var(--wp-purple),var(--wp-blue));
  background-size:300% 300%;
  animation:borderShift 5s ease infinite;
  -webkit-mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);
  mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);
  -webkit-mask-composite:xor;mask-composite:exclude;
  pointer-events:none;
}
@keyframes borderShift{
  0%{background-position:0% 50%}
  50%{background-position:100% 50%}
  100%{background-position:0% 50%}
}
.login-card::after{
  content:'';position:absolute;top:-60%;left:-20%;width:200%;height:200%;
  background:radial-gradient(ellipse at 30% 20%,rgba(99,102,241,.06),transparent 55%),
             radial-gradient(ellipse at 70% 80%,rgba(139,92,246,.05),transparent 55%);
  pointer-events:none;animation:cardGlow 6s ease-in-out infinite alternate;
}
@keyframes cardGlow{
  0%{opacity:.6;transform:translateX(-3%)}
  100%{opacity:1;transform:translateX(3%)}
}
[data-theme="dark"] .login-card{background:rgba(15,23,42,.7);box-shadow:0 20px 60px rgba(0,0,0,.4)}
[data-theme="dark"] .login-card::before{background:linear-gradient(135deg,rgba(99,102,241,.4),rgba(139,92,246,.3),rgba(239,68,68,.25),rgba(139,92,246,.3),rgba(99,102,241,.4));background-size:300% 300%;animation:borderShift 5s ease infinite}

/* === Logo === */
.logo-wrap{display:flex;align-items:center;justify-content:center;margin-bottom:24px;position:relative;z-index:2}
.wp-logo{width:76px;height:76px;animation:logoGlow 3s ease-in-out infinite alternate}
@keyframes logoGlow{
  0%{filter:drop-shadow(0 4px 16px rgba(99,102,241,.25)) drop-shadow(0 0 20px rgba(99,102,241,.1))}
  100%{filter:drop-shadow(0 4px 20px rgba(139,92,246,.4)) drop-shadow(0 0 35px rgba(139,92,246,.2))}
}

/* === Title & Sub === */
.login-title{text-align:center;font-size:26px;font-weight:800;margin-bottom:6px;letter-spacing:-.02em;position:relative;z-index:2}
.login-title .gradient-text{
  background:linear-gradient(135deg,var(--wp-blue),var(--wp-purple),var(--wp-red));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}
.login-sub{text-align:center;font-size:13px;color:var(--text-secondary);margin-bottom:26px;position:relative;z-index:2;line-height:1.7}

/* === Error === */
.error-msg{display:none;align-items:center;gap:8px;background:rgba(239,68,68,.07);border:1px solid rgba(239,68,68,.18);border-radius:var(--radius-sm);padding:11px 14px;margin-bottom:18px;color:var(--wp-red);font-size:12px;position:relative;z-index:2}
.error-msg.show{display:flex}
.error-msg i{font-size:16px;flex-shrink:0}

/* === Hint === */
.login-hint{display:flex;align-items:center;justify-content:space-between;gap:10px;background:rgba(99,102,241,.05);border:1px solid rgba(99,102,241,.12);border-radius:var(--radius-sm);padding:11px 16px;margin-bottom:20px;position:relative;z-index:2}
[data-theme="dark"] .login-hint{background:rgba(99,102,241,.06);border-color:rgba(99,102,241,.1)}
.hint-label{font-size:11px;color:var(--text-secondary);font-weight:500}
.hint-value{font-family:'Inter',monospace;font-size:14px;font-weight:700;color:var(--wp-blue);background:rgba(99,102,241,.1);border:1px solid rgba(99,102,241,.2);padding:4px 14px;border-radius:10px;cursor:pointer;transition:all .25s ease;letter-spacing:.06em}
.hint-value:hover{background:rgba(99,102,241,.18);transform:translateY(-1px);box-shadow:0 4px 12px rgba(99,102,241,.15)}

/* === Password Field === */
.field-group{position:relative;z-index:2;margin-bottom:20px}
.field-label{font-size:11px;font-weight:700;color:var(--text-secondary);margin-bottom:8px;text-transform:uppercase;letter-spacing:.06em;display:flex;align-items:center;gap:6px}
.field-label i{font-size:13px;color:var(--wp-purple)}
.input-wrap{position:relative}
.input-wrap input{
  width:100%;padding:14px 48px 14px 48px;border-radius:var(--radius);
  border:1.5px solid var(--border);
  background:rgba(255,255,255,.5);backdrop-filter:blur(10px);
  color:var(--text-primary);font-family:'Estedad',sans-serif;font-size:14px;
  outline:none;transition:all .3s ease;
}
[data-theme="dark"] .input-wrap input{background:rgba(15,23,42,.55)}
.input-wrap input:focus{
  border-color:var(--wp-blue);
  background:rgba(255,255,255,.8);
  box-shadow:0 0 0 4px rgba(99,102,241,.1),0 0 20px rgba(99,102,241,.08);
}
[data-theme="dark"] .input-wrap input:focus{
  background:rgba(15,23,42,.75);
  box-shadow:0 0 0 4px rgba(99,102,241,.12),0 0 24px rgba(99,102,241,.06);
}
.input-wrap input:hover:not(:focus){border-color:rgba(99,102,241,.3)}
.input-icon{position:absolute;right:16px;top:50%;transform:translateY(-50%);color:var(--text-secondary);font-size:18px;pointer-events:none;transition:color .3s}
input:focus ~ .input-icon{color:var(--wp-blue)}
.eye-toggle{position:absolute;left:10px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--text-secondary);cursor:pointer;font-size:17px;padding:6px;display:flex;align-items:center;transition:all .25s;border-radius:8px}
.eye-toggle:hover{color:var(--wp-purple);background:rgba(139,92,246,.08)}

/* === Submit Button === */
.login-btn{
  width:100%;height:60px;border:none;border-radius:var(--radius);cursor:pointer;
  position:relative;z-index:2;font-family:'Estedad',sans-serif;font-size:15px;font-weight:700;
  color:#fff;overflow:hidden;transition:all .35s ease;
  display:flex;align-items:center;justify-content:center;gap:8px;
  background:linear-gradient(135deg,var(--wp-blue),var(--wp-purple),var(--wp-red));
  background-size:200% 200%;
  animation:btnGradient 4s ease infinite;
}
@keyframes btnGradient{
  0%{background-position:0% 50%}
  50%{background-position:100% 50%}
  100%{background-position:0% 50%}
}
.login-btn:hover{
  transform:translateY(-2px);
  box-shadow:0 10px 35px rgba(99,102,241,.35),0 4px 14px rgba(139,92,246,.2);
  background-size:300% 300%;
}
.login-btn:active{transform:translateY(0) scale(.98)}
.login-btn:disabled{opacity:.5;cursor:not-allowed;transform:none}
.login-btn span{position:relative;z-index:1;display:flex;align-items:center;gap:8px}

/* === Loading Spinner === */
.spinner{width:18px;height:18px;border:2.5px solid rgba(255,255,255,.3);border-top-color:#fff;border-radius:50%;animation:spin .65s linear infinite;display:none}
.btn-loading .spinner{display:inline-block}
.btn-loading .btn-text{display:none}
@keyframes spin{to{transform:rotate(360deg)}}

/* === Footer === */
.login-footer{text-align:center;margin-top:24px;position:relative;z-index:2;font-size:11px;color:var(--text-secondary);display:flex;align-items:center;justify-content:center;gap:8px}
.login-footer .dot{width:5px;height:5px;border-radius:50%;background:var(--wp-purple);display:inline-block}
.login-footer .dot:first-child{background:var(--wp-blue)}
.login-footer .dot:last-child{background:var(--wp-red)}

/* === Responsive === */
@media(max-width:480px){
  .login-card{padding:32px 24px 30px}
  .login-title{font-size:22px}
  .wp-logo{width:64px;height:64px}
}
</style>
</head>
<body data-theme="light">
<div class="bg-layer">
  <div class="morph-blob b1"></div>
  <div class="morph-blob b2"></div>
  <div class="morph-blob b3"></div>
  <div class="morph-blob b4"></div>
</div>
<div class="grid-bg"></div>
<div class="particles">
  <div class="particle"></div><div class="particle"></div><div class="particle"></div>
  <div class="particle"></div><div class="particle"></div><div class="particle"></div>
  <div class="particle"></div><div class="particle"></div><div class="particle"></div>
  <div class="particle"></div>
</div>
<div class="login-wrap">
  <div class="login-card">
    <div class="logo-wrap">
      <svg class="wp-logo" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="wp-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#6366f1"/>
      <stop offset="50%" style="stop-color:#8b5cf6"/>
      <stop offset="100%" style="stop-color:#a78bfa"/>
    </linearGradient>
    <filter id="wp-glow"><feGaussianBlur stdDeviation="3" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <path d="M50 5 L90 22 L90 55 C90 78 72 93 50 98 C28 93 10 78 10 55 L10 22 Z" fill="url(#wp-grad)" filter="url(#wp-glow)" opacity="0.95"/>
  <path d="M50 18 L75 30 L75 54 C75 70 63 80 50 85 C37 80 25 70 25 54 L25 30 Z" fill="rgba(255,255,255,0.12)"/>
  <rect x="43" y="38" width="14" height="22" rx="2" fill="rgba(255,255,255,0.9)"/>
  <circle cx="50" cy="33" r="5" fill="rgba(255,255,255,0.9)"/>
</svg>
    </div>
    <div class="login-title">
      <span class="gradient-text">WHITE PANEL</span>
    </div>
    <div class="login-sub">Ø¨Ù‡ Ù¾Ù†Ù„ Ù…Ø¯ÛŒØ±ÛŒØª Ø®ÙˆØ´ Ø¢Ù…Ø¯ÛŒØ¯<br>Ø¨Ø±Ø§ÛŒ Ø§Ø¯Ø§Ù…Ù‡ Ø±Ù…Ø² Ø¹Ø¨ÙˆØ± Ø±Ø§ ÙˆØ§Ø±Ø¯ Ú©Ù†ÛŒØ¯</div>
    <div class="error-msg" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <div class="login-hint">
      <span class="hint-label"><i class="ti ti-key"></i> Ø±Ù…Ø² Ù¾ÛŒØ´â€ŒÙØ±Ø¶</span>
      <span class="hint-value" onclick="document.getElementById('pw').value='123456';document.getElementById('pw').focus()">123456</span>
    </div>
    <form id="form">
      <div class="field-group">
        <div class="field-label"><i class="ti ti-lock"></i> Ø±Ù…Ø² Ø¹Ø¨ÙˆØ±</div>
        <div class="input-wrap">
          <input type="password" id="pw" placeholder="â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢" autofocus required>
          <i class="ti ti-lock input-icon"></i>
          <button type="button" class="eye-toggle" id="eye-btn" title="Ù†Ù…Ø§ÛŒØ´ Ø±Ù…Ø²">
            <i class="ti ti-eye"></i>
          </button>
        </div>
      </div>
      <button type="submit" class="login-btn" id="btn">
        <span class="spinner"></span>
        <span class="btn-text"><i class="ti ti-login-2"></i> ÙˆØ±ÙˆØ¯ Ø¨Ù‡ Ø¯Ø§Ø´Ø¨ÙˆØ±Ø¯</span>
      </button>
    </form>
    <div class="login-footer">
      <span class="dot"></span>
      White Panel
      <span class="dot"></span>
    </div>
  </div>
</div>
<script>
(function(){
  var d=document.documentElement;
  var saved=localStorage.getItem('wp-theme')||'light';
  d.setAttribute('data-theme',saved);
  var pw=document.getElementById('pw'),eye=document.getElementById('eye-btn'),eyeIcon=eye.querySelector('i');
  eye.onclick=function(){
    var show=pw.type==='password';
    pw.type=show?'text':'password';
    eyeIcon.className='ti '+(show?'ti-eye-off':'ti-eye');
  };
  document.getElementById('form').addEventListener('submit',async function(e){
    e.preventDefault();
    var btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');
    err.classList.remove('show');btn.disabled=true;btn.classList.add('btn-loading');
    try{
      var r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:pw.value})});
      if(!r.ok){var d=await r.json().catch(function(){return{}});throw new Error(d.detail||'Ø®Ø·Ø§ Ø¯Ø± ÙˆØ±ÙˆØ¯');}
      location.href='/dashboard';
    }catch(ex){
      et.textContent=ex.message;err.classList.add('show');
      btn.disabled=false;btn.classList.remove('btn-loading');
    }
  });
})();
</script>
</body></html>"""



DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>White Panel Â· Ø¯Ø§Ø´Ø¨ÙˆØ±Ø¯</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Estedad:wght@300;400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
/* â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
   WHITE PANEL ENTERPRISE â€” HYPER-GLASSMORPHISM DESIGN SYSTEM
   â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• */

/* â”€â”€ CSS VARIABLES â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
:root{
  --neon-cyan:#06b6d4;--neon-purple:#a855f7;--neon-emerald:#10b981;
  --neon-blue:#6366f1;--neon-pink:#ec4899;--neon-amber:#f59e0b;
  --wp-blue:#6366f1;--wp-purple:#8b5cf6;--wp-red:#ef4444;
  --success:#10b981;--warning:#f59e0b;--danger:#ef4444;
  --text-primary:#f0f0f0;--text-secondary:#64748b;
  --bg:#000000;--surface:rgba(255,255,255,.03);--surface-glass:rgba(255,255,255,.04);
  --surface-hover:rgba(255,255,255,.06);--border:rgba(255,255,255,.06);
  --border-solid:rgba(255,255,255,.08);
  --gradient:linear-gradient(135deg,#06b6d4,#a855f7,#10b981);
  --gradient-purple:linear-gradient(135deg,#a855f7,#6366f1);
  --gradient-blue:linear-gradient(135deg,#6366f1,#06b6d4);
  --gradient-accent:linear-gradient(90deg,#06b6d4,#a855f7,#10b981);
  --radius-sm:10px;--radius:14px;--radius-lg:18px;--radius-xl:22px;
  --shadow-sm:0 1px 2px rgba(0,0,0,.4);--shadow-md:0 4px 16px rgba(0,0,0,.5);
  --shadow-lg:0 12px 40px rgba(0,0,0,.6);--shadow-hover:0 8px 30px rgba(6,182,212,.08);
  --sidebar-w:240px;--topbar-h:64px;--transition:.3s cubic-bezier(.4,0,.2,1);
}

[data-theme="light"]{
  --text-primary:#0f172a;--text-secondary:#64748b;
  --bg:#f8fafc;--surface:rgba(255,255,255,.7);--surface-glass:rgba(255,255,255,.65);
  --surface-hover:rgba(255,255,255,.9);--border:rgba(0,0,0,.06);--border-solid:rgba(0,0,0,.08);
  --shadow-sm:0 1px 3px rgba(0,0,0,.04);--shadow-md:0 4px 16px rgba(0,0,0,.06);
  --shadow-lg:0 12px 40px rgba(0,0,0,.08);--shadow-hover:0 8px 30px rgba(99,102,241,.08);
}

/* â”€â”€ RESET â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{font-family:'Estedad','Inter',sans-serif;background:var(--bg);color:var(--text-primary);min-height:100vh;display:flex;font-size:14px;transition:background var(--transition),color var(--transition);overflow-x:hidden}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:rgba(6,182,212,.15);border-radius:10px}
::-webkit-scrollbar-thumb:hover{background:rgba(6,182,212,.3)}
*{scrollbar-width:thin;scrollbar-color:rgba(6,182,212,.15) transparent}
a{color:inherit;text-decoration:none}

/* â”€â”€ WEBGL CANVAS BACKGROUND â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
#bg-canvas{position:fixed;inset:0;z-index:0;pointer-events:none;opacity:.6}
[data-theme="light"] #bg-canvas{opacity:.3}

/* â”€â”€ FLOATING DOCK SIDEBAR â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
.sidebar{
  width:var(--sidebar-w);min-height:100vh;
  background:rgba(6,182,212,.02);
  backdrop-filter:blur(40px) saturate(200%);-webkit-backdrop-filter:blur(40px) saturate(200%);
  border-left:1px solid var(--border);
  display:flex;flex-direction:column;flex-shrink:0;
  position:fixed;right:0;top:0;bottom:0;z-index:200;
  transition:transform var(--transition),background var(--transition);
}
[data-theme="light"] .sidebar{background:rgba(255,255,255,.5)}
.sidebar-logo{display:flex;align-items:center;gap:10px;padding:18px 16px 14px;border-bottom:1px solid var(--border);flex-shrink:0}
.sidebar-logo svg{width:32px;height:32px;filter:drop-shadow(0 0 12px rgba(6,182,212,.4));flex-shrink:0}
.sidebar-logo-text{font-size:14px;font-weight:800;color:var(--text-primary);letter-spacing:-.02em}
.sidebar-logo-sub{font-size:8.5px;color:var(--text-secondary);margin-top:1px;letter-spacing:.04em}
.sidebar-nav{flex:1;overflow-y:auto;padding:6px 0}
.nav-section{padding:14px 16px 5px;font-size:8px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--text-secondary);opacity:.5}
.nav-item{
  display:flex;align-items:center;gap:9px;padding:9px 13px;
  color:var(--text-secondary);font-size:12px;font-weight:500;
  cursor:pointer;border-right:2px solid transparent;
  transition:all .25s cubic-bezier(.4,0,.2,1);
  margin:1px 6px;border-radius:0 var(--radius-sm) var(--radius-sm) 0;
  position:relative;
}
.nav-item i{font-size:16px;width:20px;text-align:center;flex-shrink:0;transition:all .25s}
.nav-item:hover{background:rgba(6,182,212,.05);color:var(--text-primary)}
.nav-item.active{
  background:linear-gradient(135deg,rgba(6,182,212,.08),rgba(168,85,247,.06));
  color:var(--neon-cyan);border-right-color:var(--neon-cyan);font-weight:700;
  box-shadow:inset 0 0 20px rgba(6,182,212,.04),0 0 20px rgba(6,182,212,.06);
}
.nav-item.active i{color:var(--neon-cyan);filter:drop-shadow(0 0 8px rgba(6,182,212,.5))}
.nav-badge{margin-right:auto;background:rgba(6,182,212,.1);color:var(--neon-cyan);font-size:8.5px;padding:2px 7px;border-radius:20px;font-weight:700}
.sidebar-footer{padding:10px 14px;border-top:1px solid var(--border);flex-shrink:0}
.sidebar-user{display:flex;align-items:center;gap:9px;margin-bottom:8px}
.sidebar-avatar{width:34px;height:34px;border-radius:var(--radius-sm);background:linear-gradient(135deg,#06b6d4,#a855f7);display:flex;align-items:center;justify-content:center;color:#fff;font-size:14px;flex-shrink:0;box-shadow:0 0 16px rgba(6,182,212,.3)}
.sidebar-user-name{font-size:11.5px;font-weight:700;color:var(--text-primary)}
.sidebar-user-role{font-size:8.5px;color:var(--text-secondary)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:6px;width:100%;padding:8px;border:none;border-radius:var(--radius-sm);background:rgba(6,182,212,.05);color:var(--text-secondary);font-family:inherit;font-size:11px;font-weight:600;cursor:pointer;transition:all .25s;border:1px solid var(--border)}
.theme-btn:hover{background:rgba(6,182,212,.1);color:var(--text-primary);border-color:rgba(6,182,212,.15)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:6px;width:100%;padding:8px;border:none;border-radius:var(--radius-sm);background:rgba(239,68,68,.05);color:var(--wp-red);font-family:inherit;font-size:11px;font-weight:600;cursor:pointer;transition:all .25s;margin-top:5px;border:1px solid rgba(239,68,68,.08)}
.logout-btn:hover{background:rgba(239,68,68,.1);border-color:rgba(239,68,68,.15)}

/* â”€â”€ MOBILE â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
.mobile-top{display:none;position:fixed;top:0;right:0;left:0;height:52px;background:rgba(0,0,0,.8);backdrop-filter:blur(30px) saturate(200%);border-bottom:1px solid var(--border);z-index:150;align-items:center;justify-content:space-between;padding:0 14px}
[data-theme="light"] .mobile-top{background:rgba(255,255,255,.7)}
.mobile-brand{display:flex;align-items:center;gap:8px}
.mobile-brand svg{width:26px;height:26px;filter:drop-shadow(0 0 8px rgba(6,182,212,.4))}
.mobile-brand span{font-size:12px;font-weight:700;color:var(--text-primary)}
.mobile-actions{display:flex;gap:5px}
.mob-btn{background:rgba(6,182,212,.05);border:1px solid var(--border);color:var(--text-secondary);width:32px;height:32px;border-radius:8px;font-size:15px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .2s}
.mob-btn:hover{background:rgba(6,182,212,.1);color:var(--neon-cyan)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:190;backdrop-filter:blur(8px)}
.overlay.show{display:block}

/* â”€â”€ MAIN CONTENT â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
.main{margin-right:var(--sidebar-w);flex:1;padding:22px 26px 40px;min-width:0;transition:margin var(--transition);position:relative;z-index:1}
.page{display:none;animation:pageIn .4s cubic-bezier(.4,0,.2,1)}
.page.active{display:block}
@keyframes pageIn{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}

/* â”€â”€ TOPBAR â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:10px}
.topbar-title{font-size:20px;font-weight:800;color:var(--text-primary);display:flex;align-items:center;gap:8px;letter-spacing:-.03em}
.topbar-title i{background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-size:22px}
.topbar-sub{font-size:10px;color:var(--text-secondary);margin-top:2px}
.topbar-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.welcome-text{font-size:11.5px;color:var(--text-secondary);display:flex;align-items:center;gap:4px;font-weight:500}
.bell-btn{width:36px;height:36px;border-radius:var(--radius-sm);background:var(--surface);border:1px solid var(--border);color:var(--text-secondary);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:16px;transition:all .25s;position:relative}
.bell-btn:hover{background:rgba(6,182,212,.08);color:var(--neon-cyan);border-color:rgba(6,182,212,.15);box-shadow:0 0 16px rgba(6,182,212,.08)}
.bell-btn::after{content:'';position:absolute;top:7px;left:7px;width:6px;height:6px;border-radius:50%;background:var(--neon-pink);border:2px solid var(--bg);box-shadow:0 0 6px var(--neon-pink)}

/* â”€â”€ BUTTONS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
.btn{font-family:'Estedad','Inter',sans-serif;font-size:11.5px;font-weight:600;border-radius:var(--radius);padding:8px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .25s cubic-bezier(.4,0,.2,1);white-space:nowrap}
.btn i{font-size:12px}
.btn-primary{background:linear-gradient(135deg,#06b6d4,#a855f7);color:#fff;box-shadow:0 4px 20px rgba(6,182,212,.25);position:relative;overflow:hidden}
.btn-primary::before{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.12),transparent);transition:left .5s}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(6,182,212,.35)}
.btn-primary:hover::before{left:100%}
.btn-primary:active{transform:translateY(0)}
.btn-ghost{background:rgba(6,182,212,.05);color:var(--neon-cyan);border:1px solid rgba(6,182,212,.1)}
.btn-ghost:hover{background:rgba(6,182,212,.1);border-color:rgba(6,182,212,.2);box-shadow:0 0 12px rgba(6,182,212,.06)}
.btn-danger{background:rgba(239,68,68,.05);color:var(--wp-red);border:1px solid rgba(239,68,68,.1)}
.btn-danger:hover{background:rgba(239,68,68,.1);border-color:rgba(239,68,68,.2);box-shadow:0 0 12px rgba(239,68,68,.06)}
.btn-sm{padding:5px 9px;font-size:10px;border-radius:8px}
.btn-icon{width:30px;height:30px;padding:0;justify-content:center;border-radius:8px}
.btn-purple{background:rgba(168,85,247,.06);color:var(--neon-purple);border:1px solid rgba(168,85,247,.1)}
.btn-purple:hover{background:rgba(168,85,247,.12);border-color:rgba(168,85,247,.2)}
.btn-success{background:rgba(16,185,129,.06);color:var(--neon-emerald);border:1px solid rgba(16,185,129,.1)}
.btn-success:hover{background:rgba(16,185,129,.12);border-color:rgba(16,185,129,.2)}

/* â”€â”€ BADGES â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
.badge{font-size:9px;padding:3px 9px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:4px;white-space:nowrap}
.badge-blue{background:rgba(6,182,212,.1);color:var(--neon-cyan)}
.badge-green{background:rgba(16,185,129,.1);color:var(--neon-emerald)}
.badge-red{background:rgba(239,68,68,.1);color:var(--wp-red)}
.badge-purple{background:rgba(168,85,247,.1);color:var(--neon-purple)}
.badge-amber{background:rgba(245,158,11,.1);color:var(--warning)}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dot-green{background:var(--neon-emerald);box-shadow:0 0 6px var(--neon-emerald)}
.dot-red{background:var(--wp-red);box-shadow:0 0 6px var(--wp-red)}
.dot-blue{background:var(--neon-cyan);box-shadow:0 0 6px var(--neon-cyan)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.85)}}

/* â”€â”€ STAT CARDS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
.stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px}
.stat-card{
  background:var(--surface-glass);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);
  border:1px solid var(--border);border-radius:var(--radius-lg);
  padding:18px 16px 14px;transition:all .35s cubic-bezier(.4,0,.2,1);
  position:relative;overflow:hidden;cursor:default;
  animation:staggerIn .5s cubic-bezier(.4,0,.2,1) both;
}
.stat-card:nth-child(1){animation-delay:.05s}
.stat-card:nth-child(2){animation-delay:.1s}
.stat-card:nth-child(3){animation-delay:.15s}
.stat-card:nth-child(4){animation-delay:.2s}
@keyframes staggerIn{from{opacity:0;transform:translateY(16px) scale(.97)}to{opacity:1;transform:none}}
.stat-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--gradient-accent);opacity:0;transition:opacity .3s}
.stat-card:hover::before{opacity:1}
.stat-card:hover{transform:translateY(-3px);border-color:rgba(6,182,212,.15);box-shadow:0 12px 40px rgba(6,182,212,.06)}
.stat-card::after{content:'';position:absolute;top:0;right:0;width:2px;height:0;background:var(--gradient-accent);border-radius:0 0 0 4px;transition:height .35s}
.stat-card:hover::after{height:50px}
.stat-icon{width:38px;height:38px;border-radius:var(--radius-sm);display:flex;align-items:center;justify-content:center;font-size:17px;margin-bottom:10px;transition:all .3s}
.stat-card:hover .stat-icon{filter:drop-shadow(0 0 12px currentColor);transform:scale(1.08)}
.stat-icon.blue{background:rgba(6,182,212,.08);color:var(--neon-cyan)}
.stat-icon.purple{background:rgba(168,85,247,.08);color:var(--neon-purple)}
.stat-icon.green{background:rgba(16,185,129,.08);color:var(--neon-emerald)}
.stat-icon.red{background:rgba(239,68,68,.08);color:var(--wp-red)}
.stat-label{font-size:9.5px;font-weight:700;color:var(--text-secondary);text-transform:uppercase;letter-spacing:.08em;margin-bottom:4px}
.stat-value{font-size:26px;font-weight:800;color:var(--text-primary);line-height:1;letter-spacing:-.03em;font-family:'Inter',sans-serif}
.stat-sub{font-size:9.5px;color:var(--text-secondary);margin-top:6px;display:flex;align-items:center;gap:4px}
.stat-sub.up{color:var(--neon-emerald)}

/* â”€â”€ QUICK ACTIONS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
.quick-actions{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:20px}
.qa-btn{
  display:flex;align-items:center;gap:9px;padding:12px 14px;
  border-radius:var(--radius);border:1px solid var(--border);
  background:var(--surface-glass);backdrop-filter:blur(16px);
  color:var(--text-primary);font-family:inherit;font-size:11.5px;font-weight:600;
  cursor:pointer;transition:all .3s cubic-bezier(.4,0,.2,1);
  animation:staggerIn .5s cubic-bezier(.4,0,.2,1) both;
}
.qa-btn:nth-child(1){animation-delay:.25s}.qa-btn:nth-child(2){animation-delay:.3s}
.qa-btn:nth-child(3){animation-delay:.35s}.qa-btn:nth-child(4){animation-delay:.4s}
.qa-btn:hover{background:linear-gradient(135deg,rgba(6,182,212,.12),rgba(168,85,247,.08));border-color:rgba(6,182,212,.2);box-shadow:0 8px 24px rgba(6,182,212,.1);transform:translateY(-2px)}
.qa-btn i{font-size:16px;transition:transform .3s;color:var(--neon-cyan)}
.qa-btn:hover i{transform:scale(1.1)}

/* â”€â”€ SERVER PANEL â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
.server-panel{
  background:var(--surface-glass);backdrop-filter:blur(24px);border:1px solid var(--border);
  border-radius:var(--radius-lg);padding:20px 22px 18px;margin-bottom:20px;
  box-shadow:var(--shadow-sm);position:relative;overflow:hidden;
  animation:staggerIn .5s cubic-bezier(.4,0,.2,1) .45s both;
}
.server-panel::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--gradient-accent)}
.server-title{font-size:13px;font-weight:800;color:var(--text-primary);margin-bottom:14px;display:flex;align-items:center;gap:7px}
.server-title i{font-size:16px;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.server-bars{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.srv-bar-item{display:flex;flex-direction:column;gap:6px}
.srv-bar-label{display:flex;justify-content:space-between;font-size:10px;font-weight:600}
.srv-bar-name{color:var(--text-secondary)}
.srv-bar-pct{color:var(--text-primary);font-family:'Inter',sans-serif}
.srv-bar-track{height:6px;border-radius:3px;background:rgba(255,255,255,.04);overflow:hidden}
[data-theme="light"] .srv-bar-track{background:rgba(0,0,0,.04)}
.srv-bar-fill{height:100%;border-radius:3px;transition:width .8s cubic-bezier(.4,0,.2,1);position:relative}
.srv-bar-fill::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.3),transparent);width:50%;animation:shimmer 2.5s linear infinite}
.srv-bar-fill.blue{background:linear-gradient(90deg,#06b6d4,#22d3ee)}
.srv-bar-fill.purple{background:linear-gradient(90deg,#a855f7,#c084fc)}
.srv-bar-fill.amber{background:linear-gradient(90deg,#f59e0b,#fbbf24)}
.srv-bar-fill.green{background:linear-gradient(90deg,#10b981,#34d399)}
@keyframes shimmer{0%{transform:translateX(-100%)}100%{transform:translateX(200%)}}

/* â”€â”€ TABLE â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
.table-wrap{
  background:var(--surface-glass);backdrop-filter:blur(24px);border:1px solid var(--border);
  border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-sm);position:relative;
  animation:staggerIn .5s cubic-bezier(.4,0,.2,1) .5s both;
}
.table-wrap::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--gradient-accent)}
.table-wrap table{width:100%;border-collapse:collapse}
.table-wrap th{background:rgba(6,182,212,.03);font-size:9px;font-weight:800;color:var(--text-secondary);text-transform:uppercase;letter-spacing:.08em;padding:11px 12px;text-align:right;border-bottom:1px solid var(--border);position:sticky;top:0;z-index:1}
.table-wrap td{padding:10px 12px;font-size:11.5px;color:var(--text-primary);border-bottom:1px solid var(--border);transition:all .2s}
.table-wrap tbody tr{animation:staggerIn .3s cubic-bezier(.4,0,.2,1) both}
.table-wrap tbody tr:nth-child(1){animation-delay:.55s}.table-wrap tbody tr:nth-child(2){animation-delay:.6s}
.table-wrap tbody tr:nth-child(3){animation-delay:.65s}.table-wrap tbody tr:nth-child(4){animation-delay:.7s}
.table-wrap tbody tr:nth-child(5){animation-delay:.75s}
.table-wrap tbody tr:nth-child(even){background:rgba(6,182,212,.015)}
.table-wrap tbody tr:hover{background:rgba(6,182,212,.03)}
.table-wrap tr:last-child td{border-bottom:none}
.proto-badge{font-size:8.5px;padding:2.5px 7px;border-radius:5px;font-weight:700}
.pb-vless{background:rgba(6,182,212,.1);color:var(--neon-cyan)}
.pb-vmess{background:rgba(168,85,247,.1);color:var(--neon-purple)}
.pb-trojan{background:rgba(239,68,68,.1);color:var(--wp-red)}
.pb-ss{background:rgba(16,185,129,.1);color:var(--neon-emerald)}
.pb-wg{background:rgba(245,158,11,.1);color:var(--warning)}
.usage-bar-wrap{width:100%;min-width:90px}
.usage-bar{height:5px;border-radius:3px;background:rgba(255,255,255,.04);overflow:hidden;margin-bottom:3px}
[data-theme="light"] .usage-bar{background:rgba(0,0,0,.04)}
.usage-fill{height:100%;border-radius:3px;background:linear-gradient(90deg,#06b6d4,#a855f7);transition:width .5s ease}
.usage-text{font-size:9px;color:var(--text-secondary);display:flex;justify-content:space-between;font-family:'Inter',sans-serif}
.status-dot{display:flex;align-items:center;gap:5px;font-weight:600;font-size:10.5px}
.status-dot.active{color:var(--neon-emerald)}
.status-dot.expired{color:var(--wp-red)}
.exp-chip{font-size:8.5px;padding:2px 7px;border-radius:5px;font-weight:700}
.exp-ok{background:rgba(16,185,129,.08);color:var(--neon-emerald)}
.exp-warn{background:rgba(245,158,11,.08);color:var(--warning)}
.exp-bad{background:rgba(239,68,68,.08);color:var(--wp-red)}
.action-btns{display:flex;gap:3px}

/* â”€â”€ MODALS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
.modal-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.7);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(10px);padding:20px}
.modal-overlay.open{display:flex}
.modal-card{
  background:rgba(10,15,30,.9);backdrop-filter:blur(40px) saturate(200%);-webkit-backdrop-filter:blur(40px) saturate(200%);
  border:1px solid rgba(255,255,255,.06);border-radius:var(--radius-xl);
  padding:0;max-width:520px;width:100%;max-height:90vh;overflow-y:auto;
  box-shadow:0 24px 80px rgba(0,0,0,.5),0 0 40px rgba(6,182,212,.05);
  animation:modalIn .35s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden;
}
[data-theme="light"] .modal-card{background:rgba(255,255,255,.85);border:1px solid rgba(0,0,0,.06)}
.modal-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--gradient-accent)}
@keyframes modalIn{from{opacity:0;transform:scale(.94) translateY(12px)}to{opacity:1;transform:scale(1) translateY(0)}}
.modal-head{padding:20px 24px 16px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;position:relative}
.modal-head::before{content:'';position:absolute;top:0;right:0;width:120px;height:120px;background:radial-gradient(circle,rgba(6,182,212,.04),transparent 70%);pointer-events:none}
.modal-title{font-size:15px;font-weight:800;color:var(--text-primary);display:flex;align-items:center;gap:7px;position:relative;z-index:1}
.modal-title i{font-size:17px;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.modal-close{width:30px;height:30px;border-radius:8px;background:rgba(255,255,255,.04);border:1px solid var(--border);color:var(--text-secondary);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:14px;transition:all .25s}
.modal-close:hover{background:rgba(239,68,68,.1);color:var(--wp-red);border-color:rgba(239,68,68,.15)}
.modal-body{padding:18px 24px}
.modal-footer{padding:14px 24px 18px;border-top:1px solid var(--border);display:flex;gap:8px;justify-content:flex-end}
.form-field{margin-bottom:12px}
.form-field label{display:flex;align-items:center;gap:4px;font-size:9px;font-weight:800;color:var(--text-secondary);text-transform:uppercase;letter-spacing:.05em;margin-bottom:5px}
.form-field label i{font-size:12px;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.form-input{width:100%;padding:9px 12px;border-radius:var(--radius);border:1px solid var(--border);background:rgba(255,255,255,.03);backdrop-filter:blur(8px);color:var(--text-primary);font-family:inherit;font-size:12px;outline:none;transition:all .25s}
[data-theme="light"] .form-input{background:rgba(0,0,0,.02)}
.form-input:focus{border-color:var(--neon-cyan);box-shadow:0 0 0 3px rgba(6,182,212,.08),0 0 16px rgba(6,182,212,.04)}
.form-input::placeholder{color:var(--text-secondary);opacity:.4}
.form-row{display:flex;gap:8px;flex-wrap:wrap}
.form-row .form-field{flex:1;min-width:110px}
.form-select{width:100%;padding:9px 12px;border-radius:var(--radius);border:1px solid var(--border);background:rgba(255,255,255,.03);backdrop-filter:blur(8px);color:var(--text-primary);font-family:inherit;font-size:12px;outline:none;cursor:pointer;transition:all .25s}
[data-theme="light"] .form-select{background:rgba(0,0,0,.02)}
.form-select:focus{border-color:var(--neon-cyan);box-shadow:0 0 0 3px rgba(6,182,212,.08)}
.form-textarea{width:100%;padding:9px 12px;border-radius:var(--radius);border:1px solid var(--border);background:rgba(255,255,255,.03);backdrop-filter:blur(8px);color:var(--text-primary);font-family:inherit;font-size:12px;outline:none;resize:vertical;min-height:60px;transition:all .25s}
.form-textarea:focus{border-color:var(--neon-cyan);box-shadow:0 0 0 3px rgba(6,182,212,.08)}
[data-theme="light"] .form-textarea{background:rgba(0,0,0,.02)}
.toggle-wrap{display:flex;align-items:center;gap:8px}
.toggle-switch{width:40px;height:22px;border-radius:11px;background:rgba(100,116,139,.2);position:relative;cursor:pointer;transition:all .3s;border:none;flex-shrink:0}
.toggle-switch::after{content:'';position:absolute;width:16px;height:16px;border-radius:50%;background:#fff;right:3px;top:3px;transition:all .3s;box-shadow:0 1px 3px rgba(0,0,0,.2)}
.toggle-switch.on{background:var(--neon-emerald);box-shadow:0 0 12px rgba(16,185,129,.2)}
.toggle-switch.on::after{right:21px}
.toggle-label{font-size:11px;color:var(--text-secondary);font-weight:600}

/* â”€â”€ CONFIG CARDS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
.cfg-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
.cfg-card-item{
  background:var(--surface-glass);backdrop-filter:blur(20px);border:1px solid var(--border);
  border-radius:var(--radius-lg);padding:0;overflow:hidden;
  transition:all .35s cubic-bezier(.4,0,.2,1);position:relative;
  animation:staggerIn .4s cubic-bezier(.4,0,.2,1) both;
}
.cfg-card-item::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--gradient-accent);opacity:0;transition:opacity .3s}
.cfg-card-item:hover::before{opacity:1}
.cfg-card-item:hover{border-color:rgba(6,182,212,.15);transform:translateY(-2px);box-shadow:0 8px 30px rgba(6,182,212,.06)}
.cfg-card-top{padding:14px 16px 10px;display:flex;align-items:flex-start;justify-content:space-between;gap:8px}
.cfg-card-label{font-size:13px;font-weight:700;color:var(--text-primary)}
.cfg-card-body{padding:0 16px 12px}
.cfg-code{background:rgba(0,0,0,.2);border:1px solid var(--border);border-radius:var(--radius-sm);padding:10px 12px;font-family:'Inter',monospace;font-size:9.5px;color:var(--neon-cyan);word-break:break-all;line-height:1.7;max-height:70px;overflow-y:auto;margin-bottom:8px}
[data-theme="light"] .cfg-code{background:rgba(0,0,0,.03);color:var(--neon-blue)}
.cfg-card-actions{display:flex;gap:5px;flex-wrap:wrap;padding:0 16px 12px}

/* â”€â”€ LOG TIMELINE â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
.log-list{display:flex;flex-direction:column}
.log-row{display:flex;gap:10px;padding:10px 0;border-bottom:1px solid var(--border);animation:staggerIn .3s cubic-bezier(.4,0,.2,1) both}
.log-row:last-child{border-bottom:none}
.log-icon-s{width:30px;height:30px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:13px;flex-shrink:0}
.log-icon-s.info{background:rgba(6,182,212,.08);color:var(--neon-cyan)}
.log-icon-s.ok{background:rgba(16,185,129,.08);color:var(--neon-emerald)}
.log-icon-s.warn{background:rgba(245,158,11,.08);color:var(--warning)}
.log-icon-s.err{background:rgba(239,68,68,.08);color:var(--wp-red)}
.log-content{flex:1;min-width:0}
.log-msg{font-size:12px;color:var(--text-primary);line-height:1.6}
.log-time{font-size:9px;color:var(--text-secondary);margin-top:2px;display:flex;align-items:center;gap:4px;font-family:'Inter',sans-serif}

/* â”€â”€ TOAST â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
.toast{
  position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(40px);
  background:rgba(10,15,30,.9);backdrop-filter:blur(30px) saturate(200%);
  border:1px solid rgba(255,255,255,.06);color:var(--text-primary);
  border-radius:var(--radius);padding:10px 20px;font-size:12px;font-weight:500;
  opacity:0;transition:all .4s cubic-bezier(.4,0,.2,1);z-index:999;
  pointer-events:none;display:flex;align-items:center;gap:7px;
  box-shadow:0 12px 40px rgba(0,0,0,.4);white-space:nowrap;
}
[data-theme="light"] .toast{background:rgba(255,255,255,.85);border:1px solid rgba(0,0,0,.06)}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,.2);color:var(--neon-emerald);box-shadow:0 12px 40px rgba(16,185,129,.08)}
.toast.err{border-color:rgba(239,68,68,.2);color:var(--wp-red);box-shadow:0 12px 40px rgba(239,68,68,.08)}

/* â”€â”€ EMPTY STATE â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
.empty-state{text-align:center;padding:50px 20px;color:var(--text-secondary)}
.empty-state i{font-size:40px;opacity:.2;display:block;margin-bottom:12px}
.empty-state p{font-size:12px}

/* â”€â”€ TRAFFIC CHART â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
.chart-card{
  background:var(--surface-glass);backdrop-filter:blur(24px);border:1px solid var(--border);
  border-radius:var(--radius-lg);padding:18px 20px;margin-bottom:20px;
  box-shadow:var(--shadow-sm);position:relative;overflow:hidden;
  animation:staggerIn .5s cubic-bezier(.4,0,.2,1) .55s both;
}
.chart-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--gradient-accent)}
.chart-title{font-size:13px;font-weight:800;color:var(--text-primary);margin-bottom:14px;display:flex;align-items:center;gap:7px}
.chart-title i{font-size:15px;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.chart-canvas-wrap{position:relative;height:280px}

/* â”€â”€ SKELETON LOADER â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
.skeleton{background:linear-gradient(90deg,rgba(255,255,255,.03) 25%,rgba(255,255,255,.06) 50%,rgba(255,255,255,.03) 75%);background-size:200% 100%;animation:skeletonShimmer 1.5s infinite;border-radius:6px}
[data-theme="light"] .skeleton{background:linear-gradient(90deg,rgba(0,0,0,.04) 25%,rgba(0,0,0,.07) 50%,rgba(0,0,0,.04) 75%);background-size:200% 100%}
@keyframes skeletonShimmer{0%{background-position:200% 0}100%{background-position:-200% 0}}

/* â”€â”€ RESPONSIVE â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
@media(max-width:1100px){
  .stats-grid{grid-template-columns:repeat(2,1fr)}
  .server-bars{grid-template-columns:repeat(2,1fr)}
}
@media(max-width:860px){
  .sidebar{transform:translateX(100%)}
  .sidebar.open{transform:translateX(0);box-shadow:-10px 0 40px rgba(0,0,0,.4)}
  .main{margin-right:0;padding-top:64px}
  .mobile-top{display:flex}
  .quick-actions{grid-template-columns:repeat(2,1fr)}
  .stats-grid{grid-template-columns:1fr 1fr}
}
@media(max-width:520px){
  .stats-grid{grid-template-columns:1fr}
  .quick-actions{grid-template-columns:1fr}
  .main{padding:58px 10px 40px}
  .server-bars{grid-template-columns:1fr}
  .cfg-grid{grid-template-columns:1fr}
  .form-row{flex-direction:column}
}
</style>
</head>
<body data-theme="dark">
<canvas id="bg-canvas"></canvas>
<div class="toast" id="toast"></div>
<div class="overlay" id="overlay"></div>

<!-- MODALS -->
<div class="modal-overlay" id="modal-create-user">
  <div class="modal-card">
    <div class="modal-head">
      <div class="modal-title"><i class="ti ti-user-plus"></i> Ø§ÛŒØ¬Ø§Ø¯ Ú©Ø§Ø±Ø¨Ø± Ø¬Ø¯ÛŒØ¯</div>
      <button class="modal-close" onclick="closeModal('modal-create-user')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <form id="create-user-form">
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-user"></i> Ù†Ø§Ù… Ú©Ø§Ø±Ø¨Ø±ÛŒ</label><input class="form-input" id="cu-username" placeholder="username" required></div>
          <div class="form-field"><label><i class="ti ti-lock"></i> Ø±Ù…Ø² Ø¹Ø¨ÙˆØ±</label><input class="form-input" id="cu-password" type="password" placeholder="â€¢â€¢â€¢â€¢" required></div>
        </div>
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-plug-connected"></i> Ù¾Ø±ÙˆØªÚ©Ù„</label><select class="form-select" id="cu-protocol"><option value="vless">VLESS</option><option value="vmess">VMess</option><option value="trojan">Trojan</option><option value="shadowsocks">Shadowsocks</option><option value="wireguard">WireGuard</option></select></div>
          <div class="form-field"><label><i class="ti ti-server"></i> Ø³Ø±ÙˆØ±</label><select class="form-select" id="cu-server"><option value="">Ø§Ù†ØªØ®Ø§Ø¨ Ø³Ø±ÙˆØ±...</option></select></div>
        </div>
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-gauge"></i> Ù…Ø­Ø¯ÙˆØ¯ÛŒØª ØªØ±Ø§ÙÛŒÚ©</label><input class="form-input" id="cu-traffic" type="number" min="0" step="0.1" placeholder="Ù…Ù‚Ø¯Ø§Ø±"></div>
          <div class="form-field"><label>ÙˆØ§Ø­Ø¯</label><select class="form-select" id="cu-traffic-unit"><option value="GB">GB</option><option value="MB">MB</option><option value="TB">TB</option><option value="unlimited">Ù†Ø§Ù…Ø­Ø¯ÙˆØ¯</option></select></div>
        </div>
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-calendar"></i> Ø±ÙˆØ²Ù‡Ø§ÛŒ Ø§Ù†Ù‚Ø¶Ø§</label><input class="form-input" id="cu-expire" type="number" min="0" placeholder="0 = Ù†Ø§Ù…Ø­Ø¯ÙˆØ¯"></div>
          <div class="form-field"><label><i class="ti ti-users"></i> Ø§ØªØµØ§Ù„ Ù‡Ù…Ø²Ù…Ø§Ù†</label><input class="form-input" id="cu-concurrent" type="number" min="1" value="1"></div>
        </div>
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-route"></i> Ø§ÛŒÙ†Ø¨Ø§Ù†Ø¯</label><select class="form-select" id="cu-inbound"><option value="">Ø§Ù†ØªØ®Ø§Ø¨ Ø§ÛŒÙ†Ø¨Ø§Ù†Ø¯...</option></select></div>
          <div class="form-field" id="cu-worker-country-wrap" style="display:none"><label><i class="ti ti-map-pin"></i> Ú©Ø´ÙˆØ± ÙˆØ±Ú©Ø±</label><select class="form-select" id="cu-worker-country"><option value="">Ø§Ù†ØªØ®Ø§Ø¨ Ú©Ø´ÙˆØ±...</option></select></div>
        </div>
        <div class="form-field"><label><i class="ti ti-notes"></i> ÛŒØ§Ø¯Ø¯Ø§Ø´Øª</label><textarea class="form-textarea" id="cu-notes" placeholder="ÛŒØ§Ø¯Ø¯Ø§Ø´Øª Ø§Ø®ØªÛŒØ§Ø±ÛŒ..."></textarea></div>
        <div class="toggle-wrap">
          <button type="button" class="toggle-switch on" id="cu-active-toggle" onclick="this.classList.toggle('on')"></button>
          <span class="toggle-label">ÙØ¹Ø§Ù„</span>
        </div>
      </form>
    </div>
    <div class="modal-footer">
      <button class="btn btn-ghost" onclick="closeModal('modal-create-user')">Ø§Ù†ØµØ±Ø§Ù</button>
      <button class="btn btn-primary" onclick="createUser()"><i class="ti ti-user-plus"></i> Ø§ÛŒØ¬Ø§Ø¯ Ú©Ø§Ø±Ø¨Ø±</button>
    </div>
  </div>
</div>

<div class="modal-overlay" id="modal-config">
  <div class="modal-card" style="max-width:440px">
    <div class="modal-head">
      <div class="modal-title"><i class="ti ti-link"></i> Ú©Ø§Ù†ÙÛŒÚ¯</div>
      <button class="modal-close" onclick="closeModal('modal-config')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <div class="cfg-code" style="max-height:none;font-size:10.5px" id="config-text"></div>
      <div style="margin-top:12px;display:flex;gap:6px">
        <button class="btn btn-primary" onclick="copyConfigText()"><i class="ti ti-copy"></i> Ú©Ù¾ÛŒ</button>
        <button class="btn btn-ghost" onclick="showQRCode()"><i class="ti ti-qrcode"></i> QR Code</button>
      </div>
      <div id="config-qr" style="margin-top:12px;text-align:center;display:none">
        <img id="config-qr-img" src="" alt="QR" style="max-width:180px;border-radius:10px;background:#fff;padding:6px">
      </div>
    </div>
  </div>
</div>

<!-- MOBILE TOP -->
<div class="mobile-top">
  <div class="mobile-brand">
    <svg width="26" height="26" viewBox="0 0 100 100"><defs><linearGradient id="mg1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#06b6d4"/><stop offset="50%" style="stop-color:#a855f7"/><stop offset="100%" style="stop-color:#10b981"/></linearGradient></defs><path d="M50 5 L90 22 L90 55 C90 78 72 93 50 98 C28 93 10 78 10 55 L10 22 Z" fill="url(#mg1)" opacity="0.95"/><path d="M50 18 L75 30 L75 54 C75 70 63 80 50 85 C37 80 25 70 25 54 L25 30 Z" fill="rgba(255,255,255,0.12)"/><rect x="43" y="38" width="14" height="22" rx="2" fill="rgba(255,255,255,0.9)"/><circle cx="50" cy="33" r="5" fill="rgba(255,255,255,0.9)"/></svg>
    <span>White Panel</span>
  </div>
  <div class="mobile-actions">
    <button class="mob-btn" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-icon-mob"></i></button>
    <button class="mob-btn" id="menu-toggle" onclick="toggleSidebar()"><i class="ti ti-menu-2"></i></button>
  </div>
</div>

<!-- SIDEBAR -->
<aside class="sidebar" id="sidebar">
  <div class="sidebar-logo">
    <svg width="32" height="32" viewBox="0 0 100 100"><defs><linearGradient id="sg1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#06b6d4"/><stop offset="50%" style="stop-color:#a855f7"/><stop offset="100%" style="stop-color:#10b981"/></linearGradient></defs><path d="M50 5 L90 22 L90 55 C90 78 72 93 50 98 C28 93 10 78 10 55 L10 22 Z" fill="url(#sg1)" opacity="0.95"/><path d="M50 18 L75 30 L75 54 C75 70 63 80 50 85 C37 80 25 70 25 54 L25 30 Z" fill="rgba(255,255,255,0.12)"/><rect x="43" y="38" width="14" height="22" rx="2" fill="rgba(255,255,255,0.9)"/><circle cx="50" cy="33" r="5" fill="rgba(255,255,255,0.9)"/></svg>
    <div><div class="sidebar-logo-text">White Panel</div><div class="sidebar-logo-sub">ENTERPRISE</div></div>
  </div>
  <div class="sidebar-nav">
    <div class="nav-section">Ù…Ù†ÙˆÛŒ Ø§ØµÙ„ÛŒ</div>
    <div class="nav-item active" data-page="dash"><i class="ti ti-layout-dashboard"></i> Ø¯Ø§Ø´Ø¨ÙˆØ±Ø¯</div>
    <div class="nav-item" data-page="users"><i class="ti ti-users"></i> Ú©Ø§Ø±Ø¨Ø±Ø§Ù† <span class="nav-badge" id="users-count">0</span></div>
    <div class="nav-item" data-page="configs"><i class="ti ti-link-plus"></i> Ú©Ø§Ù†ÙÛŒÚ¯â€ŒÙ‡Ø§ <span class="nav-badge" id="configs-count">0</span></div>
    <div class="nav-item" data-page="servers"><i class="ti ti-server-2"></i> Ø³Ø±ÙˆØ±Ù‡Ø§</div>
    <div class="nav-item" data-page="plans"><i class="ti ti-receipt-2"></i> Ù¾Ù„Ù†â€ŒÙ‡Ø§</div>
    <div class="nav-item" data-page="groups"><i class="ti ti-folders"></i> Ú¯Ø±ÙˆÙ‡â€ŒÙ‡Ø§</div>
    <div class="nav-item" data-page="traffic"><i class="ti ti-chart-area"></i> ØªØ±Ø§ÙÛŒÚ©</div>
    <div class="nav-item" data-page="logs"><i class="ti ti-history"></i> Ù„Ø§Ú¯â€ŒÙ‡Ø§</div>
    <div class="nav-section">Ø³ÛŒØ³ØªÙ…</div>
    <div class="nav-item" data-page="worker"><i class="ti ti-cloud"></i> Cloudflare Worker</div>
    <div class="nav-item" data-page="api"><i class="ti ti-api"></i> API</div>
    <div class="nav-item" data-page="tools"><i class="ti ti-tools"></i> Ø§Ø¨Ø²Ø§Ø±Ù‡Ø§</div>
    <div class="nav-item" data-page="settings"><i class="ti ti-settings"></i> ØªÙ†Ø¸ÛŒÙ…Ø§Øª</div>
    <div class="nav-item" data-page="logout" style="color:var(--wp-red)"><i class="ti ti-logout"></i> Ø®Ø±ÙˆØ¬</div>
  </div>
  <div class="sidebar-footer">
    <div class="sidebar-user">
      <div class="sidebar-avatar"><i class="ti ti-user"></i></div>
      <div><div class="sidebar-user-name">Ø§Ø¯Ù…ÛŒÙ†</div><div class="sidebar-user-role">Ù…Ø¯ÛŒØ± Ø³ÛŒØ³ØªÙ…</div></div>
    </div>
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-moon" id="theme-icon"></i> <span id="theme-label">ØªÙ… ØªØ§Ø±ÛŒÚ©</span></button>
    <button class="logout-btn" onclick="doLogout()"><i class="ti ti-logout"></i> Ø®Ø±ÙˆØ¬ Ø§Ø² Ø­Ø³Ø§Ø¨</button>
  </div>
</aside>

<!-- MAIN CONTENT -->
<main class="main">
  <!-- DASHBOARD PAGE -->
  <section class="page active" id="page-dash">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-layout-dashboard"></i> Ø¯Ø§Ø´Ø¨ÙˆØ±Ø¯</div><div class="topbar-sub" id="last-updated">Ø¯Ø± Ø­Ø§Ù„ Ø¨Ø§Ø±Ú¯Ø°Ø§Ø±ÛŒ...</div></div>
      <div class="topbar-right">
        <span class="welcome-text">Ø³Ù„Ø§Ù… Ø§Ø¯Ù…ÛŒÙ† <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 11a2 2 0 0 0 0-4H7.5a2.5 2.5 0 0 1 0-5h.5a3.5 3.5 0 1 1 0 7"/><path d="M22 9a6 6 0 0 1-6 6"/></svg></span>
        <button class="bell-btn" title="Ø§Ø¹Ù„Ø§Ù†â€ŒÙ‡Ø§"><i class="ti ti-bell"></i></button>
        <button class="btn btn-primary" onclick="openModal('modal-create-user')"><i class="ti ti-user-plus"></i> Ø§ÛŒØ¬Ø§Ø¯ Ú©Ø§Ø±Ø¨Ø± Ø¬Ø¯ÛŒØ¯</button>
      </div>
    </div>
    <div class="stats-grid">
      <div class="stat-card"><div class="stat-icon blue"><i class="ti ti-users"></i></div><div class="stat-label">Ú©Ø§Ø±Ø¨Ø±Ø§Ù† ÙØ¹Ø§Ù„</div><div class="stat-value" id="s-active-users">â€”</div><div class="stat-sub up" id="s-users-trend"><i class="ti ti-trending-up"></i> â€”</div></div>
      <div class="stat-card"><div class="stat-icon green"><i class="ti ti-link"></i></div><div class="stat-label">Ú©Ø§Ù†ÙÛŒÚ¯â€ŒÙ‡Ø§ÛŒ ÙØ¹Ø§Ù„</div><div class="stat-value" id="s-active-configs">â€”</div></div>
      <div class="stat-card"><div class="stat-icon purple"><i class="ti ti-transfer"></i></div><div class="stat-label">Ù…ØµØ±Ù ØªØ±Ø§ÙÛŒÚ©</div><div class="stat-value" id="s-traffic">â€”<span style="font-size:13px;font-weight:500;color:var(--text-secondary)">GB</span></div></div>
      <div class="stat-card"><div class="stat-icon green"><i class="ti ti-server-2"></i></div><div class="stat-label">Ø³Ø±ÙˆØ±Ù‡Ø§ÛŒ Ø¢Ù†Ù„Ø§ÛŒÙ†</div><div class="stat-value" id="s-online-servers">â€”</div><div class="stat-sub"><span class="dot dot-green pulse"></span> Ø¢Ù†Ù„Ø§ÛŒÙ†</div></div>
    </div>
    <div class="quick-actions">
      <button class="qa-btn" onclick="openModal('modal-create-user')"><i class="ti ti-user-plus"></i> Ø§ÙØ²ÙˆØ¯Ù† Ú©Ø§Ø±Ø¨Ø±</button>
      <button class="qa-btn" onclick="switchPage('configs')"><i class="ti ti-link-plus"></i> Ø³Ø§Ø®Øª Ú©Ø§Ù†ÙÛŒÚ¯</button>
      <button class="qa-btn" onclick="switchPage('traffic')"><i class="ti ti-chart-bar"></i> Ú¯Ø²Ø§Ø±Ø´ ØªØ±Ø§ÙÛŒÚ©</button>
      <button class="qa-btn"><i class="ti ti-database"></i> Ø¨Ú©Ø§Ù¾</button>
    </div>
    <div class="server-panel">
      <div class="server-title"><i class="ti ti-activity"></i> ÙˆØ¶Ø¹ÛŒØª Ø³Ø±ÙˆØ±</div>
      <div class="server-bars">
        <div class="srv-bar-item"><div class="srv-bar-label"><span class="srv-bar-name">CPU</span><span class="srv-bar-pct" id="srv-cpu">â€”%</span></div><div class="srv-bar-track"><div class="srv-bar-fill blue" id="srv-cpu-bar" style="width:0%"></div></div></div>
        <div class="srv-bar-item"><div class="srv-bar-label"><span class="srv-bar-name">RAM</span><span class="srv-bar-pct" id="srv-ram">â€”%</span></div><div class="srv-bar-track"><div class="srv-bar-fill purple" id="srv-ram-bar" style="width:0%"></div></div></div>
        <div class="srv-bar-item"><div class="srv-bar-label"><span class="srv-bar-name">Disk</span><span class="srv-bar-pct" id="srv-disk">â€”%</span></div><div class="srv-bar-track"><div class="srv-bar-fill amber" id="srv-disk-bar" style="width:0%"></div></div></div>
        <div class="srv-bar-item"><div class="srv-bar-label"><span class="srv-bar-name">Network</span><span class="srv-bar-pct" id="srv-net">â€” MB/s</span></div><div class="srv-bar-track"><div class="srv-bar-fill green" id="srv-net-bar" style="width:0%"></div></div></div>
      </div>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Ù†Ø§Ù… Ú©Ø§Ø±Ø¨Ø±ÛŒ</th><th>Ù¾Ø±ÙˆØªÚ©Ù„</th><th>Ù…ØµØ±Ù</th><th>Ø§Ù†Ù‚Ø¶Ø§</th><th>ÙˆØ¶Ø¹ÛŒØª</th><th>Ø¹Ù…Ù„ÛŒØ§Øª</th></tr></thead>
        <tbody id="dash-users-table"><tr><td colspan="6" style="text-align:center;padding:30px;color:var(--text-secondary)">Ø¯Ø± Ø­Ø§Ù„ Ø¨Ø§Ø±Ú¯Ø°Ø§Ø±ÛŒ...</td></tr></tbody>
      </table>
    </div>
  </section>

  <!-- USERS PAGE -->
  <section class="page" id="page-users">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-users"></i> Ú©Ø§Ø±Ø¨Ø±Ø§Ù†</div><div class="topbar-sub">Ù…Ø¯ÛŒØ±ÛŒØª Ú©Ø§Ø±Ø¨Ø±Ø§Ù† Ùˆ Ú©Ø§Ù†ÙÛŒÚ¯â€ŒÙ‡Ø§</div></div>
      <div class="topbar-right">
        <button class="btn btn-primary" onclick="openModal('modal-create-user')"><i class="ti ti-user-plus"></i> Ø§ÛŒØ¬Ø§Ø¯ Ú©Ø§Ø±Ø¨Ø± Ø¬Ø¯ÛŒØ¯</button>
      </div>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Ù†Ø§Ù… Ú©Ø§Ø±Ø¨Ø±ÛŒ</th><th>Ù¾Ø±ÙˆØªÚ©Ù„</th><th>Ù…ØµØ±Ù</th><th>Ø§Ù†Ù‚Ø¶Ø§</th><th>ÙˆØ¶Ø¹ÛŒØª</th><th>Ø¹Ù…Ù„ÛŒØ§Øª</th></tr></thead>
        <tbody id="users-table"><tr><td colspan="6" style="text-align:center;padding:30px;color:var(--text-secondary)">Ø¯Ø± Ø­Ø§Ù„ Ø¨Ø§Ø±Ú¯Ø°Ø§Ø±ÛŒ...</td></tr></tbody>
      </table>
    </div>
  </section>

  <!-- CONFIGS PAGE -->
  <section class="page" id="page-configs">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-link-plus"></i> Ú©Ø§Ù†ÙÛŒÚ¯â€ŒÙ‡Ø§</div><div class="topbar-sub">Ù…Ø¯ÛŒØ±ÛŒØª Ú©Ø§Ù†ÙÛŒÚ¯â€ŒÙ‡Ø§ÛŒ Ú©Ø§Ø±Ø¨Ø±Ø§Ù†</div></div>
      <div class="topbar-right"><span class="badge badge-blue" id="cfg-total">Û° Ú©Ø§Ù†ÙÛŒÚ¯</span></div>
    </div>
    <div class="cfg-grid" id="configs-grid"></div>
    <div class="empty-state" id="configs-empty" style="display:none"><i class="ti ti-link-off"></i><p>Ù‡Ù†ÙˆØ² Ú©Ø§Ù†ÙÛŒÚ¯ÛŒ ÙˆØ¬ÙˆØ¯ Ù†Ø¯Ø§Ø±Ø¯</p></div>
  </section>

  <!-- TRAFFIC PAGE -->
  <section class="page" id="page-traffic">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-chart-area"></i> ØªØ±Ø§ÙÛŒÚ©</div><div class="topbar-sub">Ø¢Ù…Ø§Ø± Ù…ØµØ±Ù Ù¾Ù‡Ù†Ø§ÛŒ Ø¨Ø§Ù†Ø¯</div></div>
      <div class="topbar-right"><button class="btn btn-ghost" onclick="refreshAll()"><i class="ti ti-refresh"></i> Ø¨Ø±ÙˆØ²Ø±Ø³Ø§Ù†ÛŒ</button></div>
    </div>
    <div class="chart-card">
      <div class="chart-title"><i class="ti ti-chart-line"></i> Ù†Ù…ÙˆØ¯Ø§Ø± ØªØ±Ø§ÙÛŒÚ©</div>
      <div class="chart-canvas-wrap"><canvas id="traffic-chart"></canvas></div>
    </div>
    <div class="stats-grid" style="grid-template-columns:repeat(3,1fr)">
      <div class="stat-card"><div class="stat-icon blue"><i class="ti ti-clock"></i></div><div class="stat-label">Ù…ÛŒØ§Ù†Ú¯ÛŒÙ† Ø³Ø§Ø¹ØªÛŒ</div><div class="stat-value" id="t-avg">â€”</div></div>
      <div class="stat-card"><div class="stat-icon purple"><i class="ti ti-trending-up"></i></div><div class="stat-label">Ø§ÙˆØ¬ Ù…ØµØ±Ù</div><div class="stat-value" id="t-peak">â€”</div></div>
      <div class="stat-card"><div class="stat-icon green"><i class="ti ti-database"></i></div><div class="stat-label">Ú©Ù„ ØªØ±Ø§ÙÛŒÚ©</div><div class="stat-value" id="t-total">â€”</div></div>
    </div>
  </section>

  <!-- LOGS PAGE -->
  <section class="page" id="page-logs">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-history"></i> Ù„Ø§Ú¯â€ŒÙ‡Ø§</div><div class="topbar-sub">ØªØ§Ø±ÛŒØ®Ú†Ù‡ ÙØ¹Ø§Ù„ÛŒØªâ€ŒÙ‡Ø§</div></div>
      <div class="topbar-right"><button class="btn btn-ghost" onclick="loadLogs()"><i class="ti ti-refresh"></i> Ø¨Ø±ÙˆØ²Ø±Ø³Ø§Ù†ÛŒ</button></div>
    </div>
    <div class="table-wrap" style="padding:16px">
      <div class="log-list" id="logs-list"><div class="empty-state"><i class="ti ti-history-toggle"></i><p>Ù‡Ù†ÙˆØ² Ù„Ø§Ú¯ÛŒ Ø«Ø¨Øª Ù†Ø´Ø¯Ù‡</p></div></div>
    </div>
  </section>

  <!-- SERVERS PAGE -->
  <section class="page" id="page-servers">
    <div class="topbar"><div><div class="topbar-title"><i class="ti ti-server-2"></i> Ø³Ø±ÙˆØ±Ù‡Ø§</div><div class="topbar-sub">Ù…Ø¯ÛŒØ±ÛŒØª Ø³Ø±ÙˆØ±Ù‡Ø§</div></div></div>
    <div class="empty-state"><i class="ti ti-server-2"></i><p>Ø¨Ù‡ Ø²ÙˆØ¯ÛŒ...</p></div>
  </section>

  <!-- PLANS PAGE -->
  <section class="page" id="page-plans">
    <div class="topbar"><div><div class="topbar-title"><i class="ti ti-receipt-2"></i> Ù¾Ù„Ù†â€ŒÙ‡Ø§</div><div class="topbar-sub">Ù…Ø¯ÛŒØ±ÛŒØª Ù¾Ù„Ù†â€ŒÙ‡Ø§</div></div></div>
    <div class="empty-state"><i class="ti ti-receipt-2"></i><p>Ø¨Ù‡ Ø²ÙˆØ¯ÛŒ...</p></div>
  </section>

  <!-- GROUPS PAGE -->
  <section class="page" id="page-groups">
    <div class="topbar"><div><div class="topbar-title"><i class="ti ti-folders"></i> Ú¯Ø±ÙˆÙ‡â€ŒÙ‡Ø§</div><div class="topbar-sub">Ù…Ø¯ÛŒØ±ÛŒØª Ú¯Ø±ÙˆÙ‡â€ŒÙ‡Ø§</div></div></div>
    <div class="empty-state"><i class="ti ti-folders"></i><p>Ø¨Ù‡ Ø²ÙˆØ¯ÛŒ...</p></div>
  </section>

  <!-- SETTINGS PAGE -->
  <section class="page" id="page-settings">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-settings"></i> ØªÙ†Ø¸ÛŒÙ…Ø§Øª</div><div class="topbar-sub">Ù¾ÛŒÚ©Ø±Ø¨Ù†Ø¯ÛŒ Ù¾Ù†Ù„</div></div>
      <div class="topbar-right"><button class="btn btn-primary" onclick="saveSettings()"><i class="ti ti-device-floppy"></i> Ø°Ø®ÛŒØ±Ù‡ ØªÙ†Ø¸ÛŒÙ…Ø§Øª</button></div>
    </div>
    <div class="server-panel" style="animation:none">
      <div class="server-title"><i class="ti ti-world"></i> ØªÙ†Ø¸ÛŒÙ…Ø§Øª Ø¹Ù…ÙˆÙ…ÛŒ</div>
      <div class="form-row">
        <div class="form-field"><label><i class="ti ti-world"></i> Ø¯Ø§Ù…Ù†Ù‡ Ø§ØµÙ„ÛŒ</label><input class="form-input" id="set-domain" placeholder="example.com"></div>
      </div>
      <div class="form-row">
        <div class="form-field"><label><i class="ti ti-route"></i> ØªØ±Ù†Ø²Ù¾ÙˆØ±Øª Ù¾ÛŒØ´â€ŒÙØ±Ø¶</label>
          <select class="form-select" id="set-transport"><option value="ws">WebSocket</option><option value="xhttp">XHTTP</option><option value="grpc">gRPC</option><option value="tcp">TCP</option></select>
        </div>
        <div class="form-field"><label><i class="ti ti-settings-2"></i> Ø­Ø§Ù„Øª Ø§ØªØµØ§Ù„</label>
          <select class="form-select" id="set-conn-mode"><option value="ws">WebSocket</option><option value="xhttp">XHTTP</option><option value="tcp">TCP</option></select>
        </div>
      </div>
      <div style="margin-top:10px">
        <label style="font-size:10px;font-weight:800;color:var(--text-secondary);text-transform:uppercase;letter-spacing:.05em;display:block;margin-bottom:8px">Ù¾Ø±ÙˆØªÚ©Ù„â€ŒÙ‡Ø§ÛŒ ÙØ¹Ø§Ù„</label>
        <div style="display:flex;gap:14px;flex-wrap:wrap">
          <label style="display:flex;align-items:center;gap:5px;font-size:11.5px;color:var(--text-primary);cursor:pointer"><input type="checkbox" id="set-proto-vless" style="accent-color:var(--neon-cyan)"> VLESS</label>
          <label style="display:flex;align-items:center;gap:5px;font-size:11.5px;color:var(--text-primary);cursor:pointer"><input type="checkbox" id="set-proto-vmess" style="accent-color:var(--neon-purple)"> VMess</label>
          <label style="display:flex;align-items:center;gap:5px;font-size:11.5px;color:var(--text-primary);cursor:pointer"><input type="checkbox" id="set-proto-trojan" style="accent-color:var(--wp-red)"> Trojan</label>
          <label style="display:flex;align-items:center;gap:5px;font-size:11.5px;color:var(--text-primary);cursor:pointer"><input type="checkbox" id="set-proto-reality" style="accent-color:var(--neon-emerald)"> Reality</label>
        </div>
      </div>
      <div style="margin-top:14px;display:flex;gap:16px;flex-wrap:wrap">
        <div class="toggle-wrap"><button type="button" class="toggle-switch on" id="set-ws-mode" onclick="this.classList.toggle('on')"></button><span class="toggle-label">WebSocket Mode</span></div>
        <div class="toggle-wrap"><button type="button" class="toggle-switch on" id="set-xhttp-mode" onclick="this.classList.toggle('on')"></button><span class="toggle-label">XHTTP Mode</span></div>
      </div>
    </div>

    <div class="server-panel" style="animation:none">
      <div class="server-title"><i class="ti ti-shield-lock"></i> ØªÙ†Ø¸ÛŒÙ…Ø§Øª Reality</div>
      <div class="form-row">
        <div class="form-field"><label><i class="ti ti-plug"></i> Ù¾ÙˆØ±Øª</label><input class="form-input" id="set-real-port" type="number"></div>
        <div class="form-field"><label><i class="ti ti-target"></i> Ù…Ù‚ØµØ¯</label><input class="form-input" id="set-real-dest" placeholder="google.com:443"></div>
      </div>
      <div class="form-row">
        <div class="form-field"><label><i class="ti ti-key"></i> Public Key</label><input class="form-input" id="set-real-pbk" style="font-family:'JetBrains Mono',monospace;font-size:11px"></div>
        <div class="form-field"><label><i class="ti ti-hash"></i> Short ID</label><input class="form-input" id="set-real-sid" style="font-family:'JetBrains Mono',monospace;font-size:11px"></div>
      </div>
      <div class="form-row">
        <div class="form-field"><label><i class="ti ti-route"></i> KMX</label><input class="form-input" id="set-real-spx" placeholder="/"></div>
        <div class="form-field"><label><i class="ti ti-letter-s"></i> SNI</label><input class="form-input" id="set-real-sni"></div>
      </div>
      <div class="form-row">
        <div class="form-field"><label><i class="ti ti-world"></i> Ø¯Ø§Ù…Ù†Ù‡ Ø®Ø§Ø±Ø¬ÛŒ</label><input class="form-input" id="set-real-ext-domain"></div>
        <div class="form-field"><label><i class="ti ti-plug-connected"></i> Ù¾ÙˆØ±Øª Ø®Ø§Ø±Ø¬ÛŒ</label><input class="form-input" id="set-real-ext-port" type="number"></div>
      </div>
      <div style="margin-top:12px;display:flex;gap:8px">
        <button class="btn btn-purple" onclick="generateRealityKeys()"><i class="ti ti-key"></i> ØªÙˆÙ„ÛŒØ¯ Ú©Ù„ÛŒØ¯ Ø¬Ø¯ÛŒØ¯</button>
        <button class="btn btn-primary" onclick="saveRealitySettings()"><i class="ti ti-device-floppy"></i> Ø°Ø®ÛŒØ±Ù‡</button>
      </div>
    </div>

    <div class="server-panel" style="animation:none">
      <div class="server-title"><i class="ti ti-palette"></i> ØµÙØ­Ù‡ Ø§Ø´ØªØ±Ø§Ú© Ø³ÙØ§Ø±Ø´ÛŒ</div>
      <div class="custom-sub-dropdown-wrap" id="custom-sub-dropdown-wrap">
        <div class="custom-sub-dropdown" id="custom-sub-dropdown" onclick="toggleCustomSubMenu()">
          <span id="custom-sub-selected-label">Ù¾ÛŒØ´â€ŒÙØ±Ø¶</span>
          <i class="ti ti-chevron-down" id="custom-sub-chevron"></i>
        </div>
        <input type="hidden" id="set-custom-sub-default" value="">
        <input type="hidden" id="set-custom-sub-options" value="[]">
        <div class="custom-sub-dropdown-menu" id="custom-sub-dropdown-menu"></div>
      </div>
    </div>
  </section>

  <!-- WORKER PAGE -->
  <section class="page" id="page-worker">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-cloud"></i> Cloudflare Worker</div><div class="topbar-sub">Ù…Ø¯ÛŒØ±ÛŒØª ÙˆØ±Ú©Ø± Ú©Ù„ÙˆØ¯ÙÙ„Ø±</div></div>
      <div class="topbar-right"><button class="btn btn-primary" id="worker-sync-btn" onclick="syncWorkerProxies()" style="display:none"><i class="ti ti-refresh"></i> Ù‡Ù…Ú¯Ø§Ù…â€ŒØ³Ø§Ø²ÛŒ Ù¾Ø±ÙˆÚ©Ø³ÛŒâ€ŒÙ‡Ø§</button></div>
    </div>

    <div class="server-panel" id="worker-connect-form" style="animation:none">
      <div class="server-title"><i class="ti ti-cloud-upload"></i> Ø§ØªØµØ§Ù„ ÙˆØ±Ú©Ø±</div>
      <div class="form-row">
        <div class="form-field"><label><i class="ti ti-key"></i> Cloudflare API Token</label><input class="form-input" id="worker-token" type="password" placeholder="API Token"></div>
        <div class="form-field"><label><i class="ti ti-mail"></i> Ø§ÛŒÙ…ÛŒÙ„ Cloudflare</label><input class="form-input" id="worker-email" type="email" placeholder="email@example.com"></div>
      </div>
      <div class="form-row">
        <div class="form-field"><label><i class="ti ti-id"></i> Account ID</label><input class="form-input" id="worker-account-id" placeholder="Account ID"></div>
        <div class="form-field"><label><i class="ti ti-cloud"></i> Ù†Ø§Ù… ÙˆØ±Ú©Ø±</label><input class="form-input" id="worker-name" value="white-proxy"></div>
      </div>
      <div style="margin-top:10px"><button class="btn btn-primary" onclick="connectWorker()"><i class="ti ti-cloud-upload"></i> Ø§ØªØµØ§Ù„ Ùˆ Ø§Ø³ØªÙ‚Ø±Ø§Ø±</button></div>
    </div>

    <div class="server-panel" id="worker-connected-info" style="display:none;animation:none">
      <div class="server-title"><i class="ti ti-cloud-check"></i> ÙˆØ±Ú©Ø± Ù…ØªØµÙ„</div>
      <button class="btn btn-danger" id="worker-disconnect-btn" onclick="disconnectWorker()" style="margin-bottom:12px"><i class="ti ti-cloud-off"></i> Ù‚Ø·Ø¹ Ø§ØªØµØ§Ù„</button>
      <div class="form-row">
        <div class="form-field"><label>Ø¯Ø§Ù…Ù†Ù‡ ÙˆØ±Ú©Ø±</label><input class="form-input" id="worker-domain-display" readonly></div>
        <div class="form-field"><label>Account ID</label><input class="form-input" id="worker-account-display" readonly></div>
      </div>
      <div class="form-row">
        <div class="form-field"><label>Ù†Ø§Ù… ÙˆØ±Ú©Ø±</label><input class="form-input" id="worker-name-display" readonly></div>
        <div class="form-field"><label>ØªÙˆÚ©Ù† Ú©Ù†ØªØ±Ù„</label><input class="form-input" id="worker-control-token-display" readonly></div>
      </div>
      <div style="margin-top:10px;display:flex;gap:8px">
        <button class="btn btn-primary" onclick="syncWorkerProxies()"><i class="ti ti-refresh"></i> Ù‡Ù…Ú¯Ø§Ù…â€ŒØ³Ø§Ø²ÛŒ</button>
        <button class="btn btn-ghost" onclick="deployWorker()"><i class="ti ti-cloud-upload"></i> Ø¨Ø§Ø²Ø§Ø³ØªÙ‚Ø±Ø§Ø±</button>
      </div>
    </div>

    <div class="server-panel" style="animation:none">
      <div class="server-title"><i class="ti ti-settings"></i> ØªÙ†Ø¸ÛŒÙ…Ø§Øª ÙˆØ±Ú©Ø±</div>
      <div class="form-row">
        <div class="form-field"><label><i class="ti ti-link"></i> Ù„ÛŒÙ†Ú© Ù…Ù†Ø¨Ø¹ Ù¾Ø±ÙˆÚ©Ø³ÛŒâ€ŒÙ‡Ø§</label><input class="form-input" id="worker-source-url" placeholder="https://..."></div>
      </div>
      <div style="margin-top:8px;display:flex;gap:12px;align-items:center">
        <div class="toggle-wrap"><button type="button" class="toggle-switch on" id="worker-auto-sync" onclick="this.classList.toggle('on')"></button><span class="toggle-label">Ù‡Ù…Ú¯Ø§Ù…â€ŒØ³Ø§Ø²ÛŒ Ø®ÙˆØ¯Ú©Ø§Ø±</span></div>
        <button class="btn btn-primary btn-sm" onclick="saveWorkerSettings()"><i class="ti ti-device-floppy"></i> Ø°Ø®ÛŒØ±Ù‡</button>
      </div>
    </div>

    <div class="table-wrap" id="worker-proxies-section">
      <table>
        <thead><tr><th>Ú©Ø¯ Ú©Ø´ÙˆØ±</th><th>Ú©Ø´ÙˆØ±</th><th>Ù¾Ø±ÙˆÚ©Ø³ÛŒ</th><th>Ù¾ÙˆØ±Øª</th><th>Ø¹Ù…Ù„ÛŒØ§Øª</th></tr></thead>
        <tbody id="worker-proxies-table"><tr><td colspan="5" style="text-align:center;padding:20px;color:var(--text-secondary)">Ù‡Ù†ÙˆØ² Ù¾Ø±ÙˆÚ©Ø³ÛŒâ€ŒØ§ÛŒ Ø§Ø¶Ø§ÙÙ‡ Ù†Ø´Ø¯Ù‡</td></tr></tbody>
      </table>
      <div style="padding:12px"><button class="btn btn-ghost" onclick="openAddProxyModal()"><i class="ti ti-plus"></i> Ø§ÙØ²ÙˆØ¯Ù† Ù¾Ø±ÙˆÚ©Ø³ÛŒ</button></div>
    </div>

    <div class="table-wrap" id="worker-last-sync" style="margin-top:14px">
      <div style="padding:16px"><div class="server-title" style="margin-bottom:8px"><i class="ti ti-clock"></i> Ø¢Ø®Ø±ÛŒÙ† Ù‡Ù…Ú¯Ø§Ù…â€ŒØ³Ø§Ø²ÛŒ</div><div id="worker-last-sync-info" style="font-size:12px;color:var(--text-secondary)">Ù‡Ù†ÙˆØ² Ù‡Ù…Ú¯Ø§Ù…â€ŒØ³Ø§Ø²ÛŒ Ø§Ù†Ø¬Ø§Ù… Ù†Ø´Ø¯Ù‡</div></div>
    </div>
  </section>

  <!-- API PAGE -->
  <section class="page" id="page-api">
    <div class="topbar"><div><div class="topbar-title"><i class="ti ti-api"></i> API</div><div class="topbar-sub">Ù…Ø³ØªÙ†Ø¯Ø§Øª API Ù¾Ù†Ù„</div></div></div>
    <div class="empty-state"><i class="ti ti-api"></i><p>Ø¨Ù‡ Ø²ÙˆØ¯ÛŒ...</p></div>
  </section>

  <!-- TOOLS PAGE -->
  <section class="page" id="page-tools">
    <div class="topbar"><div><div class="topbar-title"><i class="ti ti-tools"></i> Ø§Ø¨Ø²Ø§Ø±Ù‡Ø§</div><div class="topbar-sub">Ø§Ø¨Ø²Ø§Ø±Ù‡Ø§ÛŒ Ù…Ø¯ÛŒØ±ÛŒØªÛŒ</div></div></div>
    <div class="empty-state"><i class="ti ti-tools"></i><p>Ø¨Ù‡ Ø²ÙˆØ¯ÛŒ...</p></div>
  </section>
</main>

<script>
/* â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
   WEBGL FLUID MESH BACKGROUND
   â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• */
(function(){
  var c=document.getElementById('bg-canvas');
  if(!c)return;
  var gl=c.getContext('webgl')||c.getContext('experimental-webgl');
  if(!gl)return;
  var mx=0.5,my=0.5;
  function resize(){c.width=window.innerWidth;c.height=window.innerHeight;gl.viewport(0,0,c.width,c.height)}
  resize();window.addEventListener('resize',resize);
  document.addEventListener('mousemove',function(e){mx=e.clientX/c.width;my=1-e.clientY/c.height});

  var vsrc='attribute vec2 p;void main(){gl_Position=vec4(p,0,1);}';
  var fsrc='precision mediump float;uniform float t;uniform vec2 r;uniform vec2 m;'+
    'void main(){vec2 uv=gl_FragCoord.xy/r;'+
    'float d=length(uv-m)*0.8;'+
    'float v1=sin(uv.x*6.0+t*0.3)*0.5+0.5;'+
    'float v2=cos(uv.y*5.0+t*0.2)*0.5+0.5;'+
    'float v3=sin((uv.x+uv.y)*4.0+t*0.25)*0.5+0.5;'+
    'vec3 c1=vec3(0.024,0.714,0.831);'+
    'vec3 c2=vec3(0.659,0.333,0.969);'+
    'vec3 c3=vec3(0.063,0.725,0.506);'+
    'vec3 col=mix(c1,c2,v1)*v2+mix(c2,c3,v3)*0.3;'+
    'col*=0.08*(1.0-d*0.5);'+
    'col+=vec3(0.01)*sin(t*0.5);'+
    'gl_FragColor=vec4(col,1);}';

  function cs(src,type){var s=gl.createShader(type);gl.shaderSource(s,src);gl.compileShader(s);return s}
  var pg=gl.createProgram();gl.attachShader(pg,cs(vsrc,gl.VERTEX_SHADER));gl.attachShader(pg,cs(fsrc,gl.FRAGMENT_SHADER));gl.linkProgram(pg);gl.useProgram(pg);
  var buf=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buf);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);
  var pl=gl.getAttribLocation(pg,'p');gl.enableVertexAttribArray(pl);gl.vertexAttribPointer(pl,2,gl.FLOAT,false,0,0);
  var ut=gl.getUniformLocation(pg,'t'),ur=gl.getUniformLocation(pg,'r'),um=gl.getUniformLocation(pg,'m');
  function draw(t){gl.uniform1f(ut,t*0.001);gl.uniform2f(ur,c.width,c.height);gl.uniform2f(um,mx,my);gl.drawArrays(gl.TRIANGLE_STRIP,0,4);requestAnimationFrame(draw)}
  requestAnimationFrame(draw);
})();

/* â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
   APPLICATION LOGIC (PRESERVED IDENTICALLY)
   â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• */

/* ============ GLOBALS ============ */
var isDark=localStorage.getItem('wp-theme')==='dark';
var currentPage='dash';
var currentConfigText='';
var allUsers=[],allLinks=[];

function applyTheme(dark){
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  var ti=document.getElementById('theme-icon'),tm=document.getElementById('theme-icon-mob'),tl=document.getElementById('theme-label');
  if(ti)ti.className='ti '+(dark?'ti-sun':'ti-moon');
  if(tm)tm.className='ti '+(dark?'ti-sun':'ti-moon');
  if(tl)tl.textContent=dark?'ØªÙ… Ø±ÙˆØ´Ù†':'ØªÙ… ØªØ§Ø±ÛŒÚ©';
}
function toggleTheme(){isDark=!isDark;localStorage.setItem('wp-theme',isDark?'dark':'light');applyTheme(isDark)}
applyTheme(isDark);

/* ============ TOAST ============ */
function toast(msg,type){
  var t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(function(){t.classList.remove('show')},2500);
}
function esc(s){return String(s||'').replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\d/g,function(d){return'Û°Û±Û²Û³Û´ÛµÛ¶Û·Û¸Û¹'[d]})}

/* ============ AUTH ============ */
async function authFetch(url,opts){
  var r=await fetch(url,opts);
  if(r.status===401){location.href='/login';throw new Error('unauthorized')}
  return r;
}
async function checkAuth(){
  try{var r=await fetch('/api/me');var d=await r.json();if(!d.authenticated)location.href='/login'}catch(e){}
}
async function doLogout(){
  try{await fetch('/api/logout',{method:'POST'})}catch(e){}
  location.href='/login';
}

/* ============ SIDEBAR ============ */
function toggleSidebar(){
  var sb=document.getElementById('sidebar'),ov=document.getElementById('overlay');
  sb.classList.toggle('open');ov.classList.toggle('show');
}
document.getElementById('menu-toggle').onclick=toggleSidebar;
document.getElementById('overlay').onclick=toggleSidebar;

function switchPage(name){
  if(name==='logout'){doLogout();return}
  currentPage=name;
  document.querySelectorAll('.nav-item').forEach(function(el){el.classList.toggle('active',el.dataset.page===name)});
  document.querySelectorAll('.page').forEach(function(el){el.classList.toggle('active',el.id==='page-'+name)});
  toggleSidebar();window.scrollTo({top:0,behavior:'smooth'});
  var loaders={users:loadUsers,configs:loadConfigs,traffic:loadTraffic,logs:loadLogs,dash:loadDashboard,settings:loadSettings,worker:loadWorker};
  if(loaders[name])loaders[name]();
}
document.querySelectorAll('.nav-item').forEach(function(el){el.onclick=function(){switchPage(el.dataset.page)}});

/* ============ MODALS ============ */
function openModal(id){
  document.getElementById(id).classList.add('open');
  if(id === 'modal-create-user'){
    loadInbounds();
  }
}
function closeModal(id){document.getElementById(id).classList.remove('open')}
document.querySelectorAll('.modal-overlay').forEach(function(m){m.addEventListener('click',function(e){if(e.target===m)m.classList.remove('open')})});

/* ============ LOAD INBOUNDS FOR CREATE USER ============ */
async function loadInbounds(){
  try{
    var r=await authFetch('/api/inbounds'),d=await r.json();
    var inbounds=d.inbounds||[];
    var inboundSelect=document.getElementById('cu-inbound');
    var workerCountryWrap=document.getElementById('cu-worker-country-wrap');
    var workerCountrySelect=document.getElementById('cu-worker-country');
    if(!inboundSelect)return;

    inboundSelect.innerHTML = '<option value="">Ø§Ù†ØªØ®Ø§Ø¨ Ø§ÛŒÙ†Ø¨Ø§Ù†Ø¯...</option>' +
      inbounds.map(function(ib){
        return '<option value="'+esc(ib.inbound_id)+'">'+esc(ib.name)+' ('+esc(ib.protocol)+' '+esc(ib.network)+')</option>';
      }).join('');

    inboundSelect.onchange = function(){
      var selectedId = this.value;
      var selectedInbound = inbounds.find(function(ib){ return ib.inbound_id === selectedId; });
      if(selectedInbound && selectedInbound.protocol === 'worker'){
        loadWorkerCountries(selectedId);
        workerCountryWrap.style.display = 'block';
      }else{
        workerCountryWrap.style.display = 'none';
      }
    };
  }catch(e){console.error(e)}
}

async function loadWorkerCountries(inboundId){
  try{
    var r=await authFetch('/api/worker/inbounds'),d=await r.json();
    var workerInbounds=d.inbounds||[];
    var workerCountryWrap=document.getElementById('cu-worker-country-wrap');
    var workerCountrySelect=document.getElementById('cu-worker-country');
    if(!workerCountrySelect)return;

    var selectedInbound = workerInbounds.find(function(ib){ return ib.inbound_id === inboundId; });
    if(selectedInbound && selectedInbound.countries && selectedInbound.countries.length > 0){
      workerCountrySelect.innerHTML = '<option value="">Ø§Ù†ØªØ®Ø§Ø¨ Ú©Ø´ÙˆØ±...</option>' +
        selectedInbound.countries.map(function(c){
          return '<option value="'+esc(c.code)+'">'+esc(c.country)+' ('+esc(c.code)+')</option>';
        }).join('');
      workerCountryWrap.style.display = 'block';
    }else{
      workerCountryWrap.style.display = 'none';
    }
  }catch(e){console.error(e)}
}

/* ============ CREATE USER ============ */
async function createUser(){
  var form=document.getElementById('create-user-form');
  var traffic=document.getElementById('cu-traffic').value;
  var unit=document.getElementById('cu-traffic-unit').value;
  var active=document.getElementById('cu-active-toggle').classList.contains('on');
  var inboundId=document.getElementById('cu-inbound').value;
  var inboundIds = inboundId ? [inboundId] : [];
  var body={
    label:document.getElementById('cu-username').value.trim(),
    password:document.getElementById('cu-password').value,
    protocol:document.getElementById('cu-protocol').value,
    limit_value:traffic||'0',
    limit_unit:unit==='unlimited'?'GB':unit,
    expires_days:document.getElementById('cu-expire').value||'0',
    concurrent:document.getElementById('cu-concurrent').value||'1',
    server_id:document.getElementById('cu-server').value||null,
    note:document.getElementById('cu-notes').value.trim(),
    active:active,
    inbound_id: inboundId,
    inbound_ids: inboundIds,
  };
  var workerCountryWrap = document.getElementById('cu-worker-country-wrap');
  if(workerCountryWrap && workerCountryWrap.style.display !== 'none'){
    var proxyCountry = document.getElementById('cu-worker-country').value;
    if(proxyCountry){
      body.proxy_countries = [proxyCountry.toLowerCase()];
    }
  }
  if(!body.label){toast('Ù†Ø§Ù… Ú©Ø§Ø±Ø¨Ø±ÛŒ Ø§Ù„Ø²Ø§Ù…ÛŒ Ø§Ø³Øª','err');return}
  try{
    var r=await authFetch('/api/users',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok){var d=await r.json().catch(function(){return{}});throw new Error(d.detail||'Ø®Ø·Ø§')}
    toast('Ú©Ø§Ø±Ø¨Ø± Ø¨Ø§ Ù…ÙˆÙÙ‚ÛŒØª Ø§ÛŒØ¬Ø§Ø¯ Ø´Ø¯ âœ“','ok');
    closeModal('modal-create-user');
    ['cu-username','cu-password','cu-traffic','cu-expire','cu-concurrent','cu-notes'].forEach(function(id){document.getElementById(id).value=''});
    loadUsers();loadConfigs();loadDashboard();
  }catch(e){toast(e.message,'err')}
}

/* ============ LOAD USERS ============ */
async function loadUsers(){
  try{
    var r=await authFetch('/api/links'),d=await r.json();
    allLinks=d.links||[];
    document.getElementById('users-count').textContent=allLinks.length;
    renderUsersTable(allLinks,'users-table');
  }catch(e){console.error(e)}
}

function renderUsersTable(links,tableId){
  var tbody=document.getElementById(tableId);
  if(!links.length){tbody.innerHTML='<tr><td colspan="6"><div class="empty-state"><i class="ti ti-users-off"></i><p>Ú©Ø§Ø±Ø¨Ø±ÛŒ ÙˆØ¬ÙˆØ¯ Ù†Ø¯Ø§Ø±Ø¯</p></div></td></tr>';return}
  tbody.innerHTML=links.map(function(l){
    var pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
    var bc=pct>90?'var(--wp-red)':pct>70?'var(--warning)':'var(--neon-cyan)';
    var lim=l.limit_bytes===0?'âˆž':fmtB(l.limit_bytes);
    var protoClass=l.protocol==='vless'||l.protocol==='vless-ws'?'pb-vless':l.protocol==='vmess'?'pb-vmess':l.protocol==='trojan'?'pb-trojan':l.protocol==='shadowsocks'?'pb-ss':'pb-wg';
    var protoFa=l.protocol==='vless-ws'?'VLESS':l.protocol==='vmess'?'VMess':l.protocol==='trojan'?'Trojan':l.protocol==='shadowsocks'?'Shadowsocks':l.protocol==='wireguard'?'WireGuard':l.protocol||'VLESS';
    var isActive=l.active&&!l.expired;
    var expText=l.expired?'Ù…Ù†Ù‚Ø¶ÛŒ':l.expires_at?new Date(l.expires_at).toLocaleDateString('fa-IR'):'Ù†Ø§Ù…Ø­Ø¯ÙˆØ¯';
    var expCls=l.expired?'exp-bad':l.expires_at?'exp-ok':'exp-ok';
    return '<tr><td style="font-weight:600">'+esc(l.label)+'</td>'+
      '<td><span class="proto-badge '+protoClass+'">'+protoFa+'</span></td>'+
      '<td><div class="usage-bar-wrap"><div class="usage-bar"><div class="usage-fill" style="width:'+pct+'%;background:'+bc+'"></div></div><div class="usage-text"><span>'+fmtB(l.used_bytes)+'</span><span>'+lim+'</span></div></div></td>'+
      '<td><span class="exp-chip '+expCls+'">'+expText+'</span></td>'+
      '<td><div class="status-dot '+(isActive?'active':'expired')+'"><span class="dot '+(isActive?'dot-green':'dot-red')+' '+(isActive?'pulse':'')+'"></span>'+(isActive?'ÙØ¹Ø§Ù„':'ØºÛŒØ±ÙØ¹Ø§Ù„')+'</div></td>'+
      '<td><div class="action-btns">'+
        '<button class="btn btn-sm btn-ghost btn-icon" onclick="viewConfig(\''+l.uuid+'\')" title="Ù…Ø´Ø§Ù‡Ø¯Ù‡"><i class="ti ti-eye"></i></button>'+
        '<button class="btn btn-sm btn-ghost btn-icon" onclick="copyLink(\''+l.uuid+'\')" title="Ú©Ù¾ÛŒ"><i class="ti ti-copy"></i></button>'+
        '<button class="btn btn-sm btn-ghost btn-icon" onclick="toggleUser(\''+l.uuid+'\')" title="ÙØ¹Ø§Ù„/ØºÛŒØ±ÙØ¹Ø§Ù„"><i class="ti ti-toggle-'+(isActive?'right':'left')+'"></i></button>'+
        '<button class="btn btn-sm btn-danger btn-icon" onclick="deleteUser(\''+l.uuid+'\')" title="Ø­Ø°Ù"><i class="ti ti-trash"></i></button>'+
      '</div></td></tr>';
  }).join('');
}

/* ============ USER ACTIONS ============ */
async function viewConfig(uuid){
  var link=allLinks.find(function(l){return l.uuid===uuid});
  if(!link){toast('Ú©Ø§Ù†ÙÛŒÚ¯ ÛŒØ§ÙØª Ù†Ø´Ø¯','err');return}
  currentConfigText=link.vless_link||'';
  document.getElementById('config-text').textContent=currentConfigText;
  document.getElementById('config-qr').style.display='none';
  openModal('modal-config');
}
function copyConfigText(){
  if(!currentConfigText)return;
  navigator.clipboard.writeText(currentConfigText).then(function(){toast('Ú©Ø§Ù†ÙÛŒÚ¯ Ú©Ù¾ÛŒ Ø´Ø¯ âœ“','ok')});
}
function showQRCode(){
  if(!currentConfigText)return;
  var img='https://api.qrserver.com/v1/create-qr-code/?size=220x220&data='+encodeURIComponent(currentConfigText);
  document.getElementById('config-qr-img').src=img;
  document.getElementById('config-qr').style.display='block';
}
function copyLink(uuid){
  var link=allLinks.find(function(l){return l.uuid===uuid});
  if(!link||!link.vless_link)return;
  navigator.clipboard.writeText(link.vless_link).then(function(){toast('Ù„ÛŒÙ†Ú© Ú©Ù¾ÛŒ Ø´Ø¯ âœ“','ok')});
}
async function toggleUser(uuid){
  var link=allLinks.find(function(l){return l.uuid===uuid});
  if(!link)return;
  try{
    var r=await authFetch('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:!link.active})});
    if(!r.ok)throw new Error();
    toast('ÙˆØ¶Ø¹ÛŒØª ØªØºÛŒÛŒØ± Ú©Ø±Ø¯ âœ“','ok');loadUsers();loadDashboard();
  }catch(e){toast('Ø®Ø·Ø§ Ø¯Ø± ØªØºÛŒÛŒØ± ÙˆØ¶Ø¹ÛŒØª','err')}
}
async function deleteUser(uuid){
  if(!confirm('Ø¢ÛŒØ§ Ø§Ø² Ø­Ø°Ù Ø§ÛŒÙ† Ú©Ø§Ø±Ø¨Ø± Ø§Ø·Ù…ÛŒÙ†Ø§Ù† Ø¯Ø§Ø±ÛŒØ¯ØŸ'))return;
  try{
    var r=await authFetch('/api/links/'+uuid,{method:'DELETE'});
    if(!r.ok)throw new Error();
    toast('Ú©Ø§Ø±Ø¨Ø± Ø­Ø°Ù Ø´Ø¯ âœ“','ok');loadUsers();loadDashboard();loadConfigs();
  }catch(e){toast('Ø®Ø·Ø§ Ø¯Ø± Ø­Ø°Ù','err')}
}

/* ============ CONFIGS PAGE ============ */
async function loadConfigs(){
  try{
    var r=await authFetch('/api/links'),d=await r.json();
    allLinks=d.links||[];
    document.getElementById('configs-count').textContent=allLinks.length;
    document.getElementById('cfg-total').textContent=toFa(allLinks.length)+' Ú©Ø§Ù†ÙÛŒÚ¯';
    var grid=document.getElementById('configs-grid'),empty=document.getElementById('configs-empty');
    if(!allLinks.length){grid.innerHTML='';empty.style.display='block';return}
    empty.style.display='none';
    grid.innerHTML=allLinks.map(function(l){
      var protoFa=l.protocol==='vless-ws'?'VLESS':l.protocol==='vmess'?'VMess':l.protocol==='trojan'?'Trojan':l.protocol||'VLESS';
      var protoClass=l.protocol==='vless-ws'?'pb-vless':l.protocol==='vmess'?'pb-vmess':l.protocol==='trojan'?'pb-trojan':'pb-vless';
      var isActive=l.active&&!l.expired;
      var pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
      return '<div class="cfg-card-item">'+
        '<div class="cfg-card-top"><span class="cfg-card-label">'+esc(l.label)+'</span><span class="badge '+(isActive?'badge-green':'badge-red')+'"><span class="dot '+(isActive?'dot-green':'dot-red')+' '+(isActive?'pulse':'')+'"></span> '+(isActive?'ÙØ¹Ø§Ù„':'ØºÛŒØ±ÙØ¹Ø§Ù„')+'</span></div>'+
        '<div class="cfg-card-body"><span class="proto-badge '+protoClass+'" style="margin-bottom:6px;display:inline-block">'+protoFa+'</span>'+
        '<div class="usage-bar-wrap" style="margin-bottom:6px"><div class="usage-bar"><div class="usage-fill" style="width:'+pct+'%"></div></div><div class="usage-text"><span>'+fmtB(l.used_bytes)+'</span><span>'+(l.limit_bytes===0?'âˆž':fmtB(l.limit_bytes))+'</span></div></div></div>'+
        '<div class="cfg-card-actions">'+
        '<button class="btn btn-sm btn-ghost" onclick="viewConfig(\''+l.uuid+'\')"><i class="ti ti-eye"></i> Ù…Ø´Ø§Ù‡Ø¯Ù‡</button>'+
        '<button class="btn btn-sm btn-ghost" onclick="copyLink(\''+l.uuid+'\')"><i class="ti ti-copy"></i> Ú©Ù¾ÛŒ</button>'+
        '<button class="btn btn-sm btn-ghost btn-icon" onclick="showQRForLink(\''+l.uuid+'\')"><i class="ti ti-qrcode"></i></button>'+
        '</div></div>';
    }).join('');
  }catch(e){console.error(e)}
}
function showQRForLink(uuid){
  var link=allLinks.find(function(l){return l.uuid===uuid});
  if(!link||!link.vless_link)return;
  currentConfigText=link.vless_link;
  document.getElementById('config-text').textContent=currentConfigText;
  showQRCode();
  openModal('modal-config');
}

/* ============ TRAFFIC ============ */
var trafficChart=null;
async function loadTraffic(){
  try{
    var r=await authFetch('/stats'),d=await r.json();
    document.getElementById('t-total').textContent=d.total_traffic_mb.toFixed(1)+' MB';
    if(d.hourly){
      var labels=Object.keys(d.hourly).sort(),vals=labels.map(function(k){return +(d.hourly[k]/1024**2).toFixed(2)});
      if(vals.length){
        var total=vals.reduce(function(a,b){return a+b},0);
        var avg=total/vals.length;
        var peak=Math.max.apply(null,vals);
        document.getElementById('t-avg').textContent=avg.toFixed(2)+' MB';
        document.getElementById('t-peak').textContent=peak.toFixed(2)+' MB';
      }
      var canvas=document.getElementById('traffic-chart');
      if(!canvas)return;
      var ctx=canvas.getContext('2d');
      if(trafficChart){trafficChart.data.labels=labels;trafficChart.data.datasets[0].data=vals;trafficChart.update()}
      else{
        var grad=ctx.createLinearGradient(0,0,0,280);
        grad.addColorStop(0,'rgba(6,182,212,.35)');grad.addColorStop(0.5,'rgba(168,85,247,.15)');grad.addColorStop(1,'rgba(6,182,212,0)');
        trafficChart=new Chart(ctx,{
          type:'line',data:{labels:labels,datasets:[{data:vals,borderColor:'#06b6d4',backgroundColor:grad,fill:true,tension:.4,pointRadius:0,borderWidth:2,pointHoverRadius:4,pointHoverBackgroundColor:'#06b6d4',pointHoverBorderColor:'#fff',pointHoverBorderWidth:2}]},
          options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false},tooltip:{backgroundColor:'rgba(10,15,30,.9)',titleColor:'#06b6d4',bodyColor:'#f0f0f0',borderColor:'rgba(6,182,212,.2)',borderWidth:1,cornerRadius:10,padding:10,titleFont:{family:'Inter'},bodyFont:{family:'Inter'}}},
            scales:{x:{grid:{display:false},ticks:{font:{size:9,family:'Inter'},color:'rgba(100,116,139,.5)'}},y:{grid:{color:'rgba(6,182,212,.04)'},ticks:{font:{size:9,family:'Inter'},color:'rgba(100,116,139,.5)',callback:function(v){return v+' MB'}}}},
            interaction:{mode:'index',intersect:false}}
        });
      }
    }
  }catch(e){console.error(e)}
}

/* ============ LOGS ============ */
async function loadLogs(){
  try{
    var r=await authFetch('/api/activity'),d=await r.json();
    var logs=(d.logs||[]).slice().reverse();
    var el=document.getElementById('logs-list');
    if(!logs.length){el.innerHTML='<div class="empty-state"><i class="ti ti-history-toggle"></i><p>Ù‡Ù†ÙˆØ² Ù„Ø§Ú¯ÛŒ Ø«Ø¨Øª Ù†Ø´Ø¯Ù‡</p></div>';return}
    var icMap={ok:'ti-circle-check ok',err:'ti-circle-x err',warn:'ti-alert-triangle warn',info:'ti-info-circle info'};
    el.innerHTML=logs.map(function(l){
      return '<div class="log-row"><div class="log-icon-s '+(l.level||'info')+'"><i class="ti '+(icMap[l.level]||'ti-info-circle')+'"></i></div><div class="log-content"><div class="log-msg">'+esc(l.message)+'</div><div class="log-time"><i class="ti ti-clock"></i> '+new Date(l.time).toLocaleString('fa-IR')+'</div></div></div>';
    }).join('');
  }catch(e){console.error(e)}
}

/* ============ DASHBOARD DATA ============ */
async function loadDashboard(){
  try{
    var r=await authFetch('/stats'),d=await r.json();
    document.getElementById('s-active-users').textContent=d.active_links||'0';
    document.getElementById('s-active-configs').textContent=d.active_links||'0';
    document.getElementById('s-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span style="font-size:13px;font-weight:500;color:var(--text-secondary)">GB</span>';
    document.getElementById('s-online-servers').textContent='1';
    document.getElementById('s-users-trend').innerHTML='<i class="ti ti-trending-up"></i> '+toFa(d.active_connections||0)+' Ø§ØªØµØ§Ù„';
    document.getElementById('last-updated').textContent='Ø¢Ø®Ø±ÛŒÙ† Ø¨Ø±ÙˆØ²Ø±Ø³Ø§Ù†ÛŒ: '+new Date().toLocaleTimeString('fa-IR');
    document.getElementById('srv-cpu').textContent='32%';document.getElementById('srv-cpu-bar').style.width='32%';
    document.getElementById('srv-ram').textContent='58%';document.getElementById('srv-ram-bar').style.width='58%';
    document.getElementById('srv-disk').textContent='41%';document.getElementById('srv-disk-bar').style.width='41%';
    document.getElementById('srv-net').textContent='12 MB/s';document.getElementById('srv-net-bar').style.width='24%';
    var lr=await authFetch('/api/links'),ld=await lr.json();
    allLinks=ld.links||[];
    document.getElementById('users-count').textContent=allLinks.length;
    renderUsersTable(allLinks,'dash-users-table');
  }catch(e){console.error(e)}
}

/* ============ SETTINGS ============ */
async function loadSettings(){
  try{
    var r=await authFetch('/api/tools/settings'),d=await r.json();
    document.getElementById('set-domain').value=d.domain||'';
    document.getElementById('set-transport').value=d.default_transport||'ws';
    document.getElementById('set-conn-mode').value=d.default_connection_mode||'ws';
    var protos=d.enabled_protocols||['vless'];
    document.getElementById('set-proto-vless').checked=protos.includes('vless');
    document.getElementById('set-proto-vmess').checked=protos.includes('vmess');
    document.getElementById('set-proto-trojan').checked=protos.includes('trojan');
    document.getElementById('set-proto-reality').checked=protos.includes('reality');
    var wsEl=document.getElementById('set-ws-mode');
    d.websocket_mode!==false?wsEl.classList.add('on'):wsEl.classList.remove('on');
    var xhEl=document.getElementById('set-xhttp-mode');
    d.xhttp_mode!==false?xhEl.classList.add('on'):xhEl.classList.remove('on');
    var real=d.reality||{};
    document.getElementById('set-real-port').value=real.port||1234;
    document.getElementById('set-real-dest').value=real.dest||'google.com:443';
    document.getElementById('set-real-pbk').value=real.public_key||'';
    document.getElementById('set-real-sid').value=real.short_id||'6ba85179e30d4fc2';
    document.getElementById('set-real-spx').value=real.kmx||'/';
    document.getElementById('set-real-sni').value=real.sni||d.domain||'';
    document.getElementById('set-real-ext-domain').value=real.external_domain||d.domain||'';
    document.getElementById('set-real-ext-port').value=real.external_port||443;
    document.getElementById('set-custom-sub-default').value=d.custom_sub_default||'';
    loadCustomSubs(d.custom_sub_default||'');
    var lbl=document.getElementById('custom-sub-selected-label');
    if(lbl&&d.custom_sub_default){
      var opts=document.getElementById('set-custom-sub-options').value;
      try{var arr=JSON.parse(opts);var found=arr.find(function(o){return o.file===d.custom_sub_default});if(found){lbl.textContent=found.label||found.file}}catch(e){}
    }
  }catch(e){console.error(e)}
}

async function loadCustomSubs(selected){
  try{
    var r=await authFetch('/api/custom-subs');var d=await r.json();
    var opts=d.subs||[];var menu=document.getElementById('custom-sub-dropdown-menu');
    var input=document.getElementById('set-custom-sub-options');
    if(!menu||!input)return;
    input.value=JSON.stringify(opts);
    var html='';
    if(!opts.length){
      html+='<div class="custom-sub-option" style="color:var(--text-secondary)">Ù‡ÛŒÚ† ØµÙØ­Ù‡â€ŒØ§ÛŒ ÛŒØ§ÙØª Ù†Ø´Ø¯</div>';
    }else{
      html=opts.map(function(o){
        var active=o.file===selected?' active':'';
        return '<div class="custom-sub-option'+active+'" onclick="selectCustomSub(\''+esc(o.file)+'\', \''+esc(o.label)+'\')"><span class="sub-preview"></span>'+esc(o.label||o.file)+'</div>';
      }).join('');
    }
    menu.innerHTML=html;
  }catch(e){console.error(e)}
}

function toggleCustomSubMenu(){
  var wrap=document.getElementById('custom-sub-dropdown-wrap');
  wrap.classList.toggle('open');
}
function selectCustomSub(file,label){
  document.getElementById('set-custom-sub-default').value=file;
  document.getElementById('custom-sub-selected-label').textContent=label||file;
  document.querySelectorAll('.custom-sub-option').forEach(function(el){el.classList.remove('active')});
  event.currentTarget.classList.add('active');
  document.getElementById('custom-sub-dropdown-wrap').classList.remove('open');
}

async function saveSettings(){
  var body={
    domain:document.getElementById('set-domain').value.trim(),
    default_transport:document.getElementById('set-transport').value,
    default_connection_mode:document.getElementById('set-conn-mode').value,
    enabled_protocols:[],
    websocket_mode:document.getElementById('set-ws-mode').classList.contains('on'),
    xhttp_mode:document.getElementById('set-xhttp-mode').classList.contains('on'),
    custom_sub_default:document.getElementById('set-custom-sub-default').value,
  };
  if(document.getElementById('set-proto-vless').checked)body.enabled_protocols.push('vless');
  if(document.getElementById('set-proto-vmess').checked)body.enabled_protocols.push('vmess');
  if(document.getElementById('set-proto-trojan').checked)body.enabled_protocols.push('trojan');
  if(document.getElementById('set-proto-reality').checked)body.enabled_protocols.push('reality');
  try{
    var r=await authFetch('/api/tools/settings',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    toast('ØªÙ†Ø¸ÛŒÙ…Ø§Øª Ø°Ø®ÛŒØ±Ù‡ Ø´Ø¯ âœ“','ok');
  }catch(e){toast('Ø®Ø·Ø§ Ø¯Ø± Ø°Ø®ÛŒØ±Ù‡ ØªÙ†Ø¸ÛŒÙ…Ø§Øª','err')}
}

async function saveRealitySettings(){
  var body={
    port:parseInt(document.getElementById('set-real-port').value)||1234,
    dest:document.getElementById('set-real-dest').value.trim(),
    public_key:document.getElementById('set-real-pbk').value.trim(),
    short_id:document.getElementById('set-real-sid').value.trim(),
    kmx:document.getElementById('set-real-spx').value.trim(),
    sni:document.getElementById('set-real-sni').value.trim(),
    external_domain:document.getElementById('set-real-ext-domain').value.trim(),
    external_port:parseInt(document.getElementById('set-real-ext-port').value)||443,
  };
  try{
    var r=await authFetch('/api/tools/reality-settings',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    toast('ØªÙ†Ø¸ÛŒÙ…Ø§Øª Reality Ø°Ø®ÛŒØ±Ù‡ Ø´Ø¯ âœ“','ok');
  }catch(e){toast('Ø®Ø·Ø§ Ø¯Ø± Ø°Ø®ÛŒØ±Ù‡ ØªÙ†Ø¸ÛŒÙ…Ø§Øª Reality','err')}
}

async function generateRealityKeys(){
  try{
    var r=await authFetch('/api/tools/generate-reality-keys',{method:'POST'});
    var d=await r.json();
    if(d.public_key)document.getElementById('set-real-pbk').value=d.public_key;
    if(d.private_key)document.getElementById('set-real-sid').value=d.short_id||'';
    toast('Ú©Ù„ÛŒØ¯ Reality ØªÙˆÙ„ÛŒØ¯ Ø´Ø¯ âœ“','ok');
  }catch(e){toast('Ø®Ø·Ø§ Ø¯Ø± ØªÙˆÙ„ÛŒØ¯ Ú©Ù„ÛŒØ¯','err')}
}
function updateProtoCheckboxes(){}

/* ============ WORKER ============ */
async function loadWorker(){
  try{
    var r=await authFetch('/api/worker'),d=await r.json();
    var connectForm=document.getElementById('worker-connect-form');
    var connectedInfo=document.getElementById('worker-connected-info');
    var syncBtn=document.getElementById('worker-sync-btn');
    if(d.connected){
      connectForm.style.display='none';
      connectedInfo.style.display='block';
      syncBtn.style.display='inline-flex';
      document.getElementById('worker-domain-display').value=d.worker_domain||'';
      document.getElementById('worker-account-display').value=d.account_id||'';
      document.getElementById('worker-name-display').value=d.worker_name||'';
      document.getElementById('worker-control-token-display').value=d.control_token||'';
      document.getElementById('worker-source-url').value=d.source_url||'';
      var autoEl=document.getElementById('worker-auto-sync');
      d.auto_sync!==false?autoEl.classList.add('on'):autoEl.classList.remove('on');
      if(d.proxies)renderWorkerProxies(d.proxies);
      if(d.last_sync){
        document.getElementById('worker-last-sync-info').innerHTML=
          '<div style="display:flex;flex-direction:column;gap:4px">'+
          '<div><span style="color:var(--text-secondary)">Ø²Ù…Ø§Ù†:</span> '+new Date(d.last_sync).toLocaleString('fa-IR')+'</div>'+
          '<div><span style="color:var(--text-secondary)">ØªØ¹Ø¯Ø§Ø¯:</span> '+toFa(Object.keys(d.proxies||{}).length)+' Ú©Ø´ÙˆØ±</div>'+
          (d.last_error?'<div style="color:var(--wp-red)"><span>Ø®Ø·Ø§:</span> '+esc(d.last_error)+'</div>':'')+
          '</div>';
      }
    }else{
      connectForm.style.display='block';
      connectedInfo.style.display='none';
      syncBtn.style.display='none';
      document.getElementById('worker-source-url').value=d.source_url||'';
    }
  }catch(e){console.error(e)}
}

function renderWorkerProxies(proxies){
  var tbody=document.getElementById('worker-proxies-table');
  var codes=Object.keys(proxies);
  if(!codes.length){tbody.innerHTML='<tr><td colspan="5" style="text-align:center;padding:20px;color:var(--text-secondary)">Ù‡Ù†ÙˆØ² Ù¾Ø±ÙˆÚ©Ø³ÛŒâ€ŒØ§ÛŒ Ø§Ø¶Ø§ÙÙ‡ Ù†Ø´Ø¯Ù‡</td></tr>';return}
  tbody.innerHTML=codes.map(function(code){
    var p=proxies[code];
    return '<tr><td style="font-weight:600">'+esc(code.toUpperCase())+'</td>'+
      '<td>'+esc(p.country)+'</td>'+
      '<td style="font-family:JetBrains Mono,monospace;font-size:11px">'+esc(p.proxy)+'</td>'+
      '<td>'+esc(p.port)+'</td>'+
      '<td><button class="btn btn-sm btn-danger btn-icon" onclick="deleteWorkerProxy(\''+esc(code)+'\')" title="Ø­Ø°Ù"><i class="ti ti-trash"></i></button></td></tr>';
  }).join('');
}

async function connectWorker(){
  var body={
    token:document.getElementById('worker-token').value.trim(),
    email:document.getElementById('worker-email').value.trim(),
    account_id:document.getElementById('worker-account-id').value.trim(),
    worker_name:document.getElementById('worker-name').value.trim()||'white-proxy',
  };
  if(!body.token||!body.email||!body.account_id){toast('Ù‡Ù…Ù‡ ÙÛŒÙ„Ø¯Ù‡Ø§ Ø§Ù„Ø²Ø§Ù…ÛŒ Ù‡Ø³ØªÙ†Ø¯','err');return}
  try{
    var r=await authFetch('/api/worker/setup',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok){var d=await r.json().catch(function(){return{}});throw new Error(d.detail||'Ø®Ø·Ø§')}
    toast('ÙˆØ±Ú©Ø± Ø¨Ø§ Ù…ÙˆÙÙ‚ÛŒØª Ù…ØªØµÙ„ Ø´Ø¯ âœ“','ok');loadWorker();
  }catch(e){toast(e.message,'err')}
}

async function disconnectWorker(){
  if(!confirm('Ø¢ÛŒØ§ Ø§Ø² Ù‚Ø·Ø¹ Ø§ØªØµØ§Ù„ ÙˆØ±Ú©Ø± Ø§Ø·Ù…ÛŒÙ†Ø§Ù† Ø¯Ø§Ø±ÛŒØ¯ØŸ'))return;
  try{
    var r=await authFetch('/api/worker',{method:'DELETE'});
    if(!r.ok)throw new Error();
    toast('ÙˆØ±Ú©Ø± Ù‚Ø·Ø¹ Ø´Ø¯ âœ“','ok');loadWorker();
  }catch(e){toast('Ø®Ø·Ø§ Ø¯Ø± Ù‚Ø·Ø¹ Ø§ØªØµØ§Ù„','err')}
}

async function deployWorker(){
  try{
    var r=await authFetch('/api/worker/sync',{method:'POST'});
    if(!r.ok)throw new Error();
    toast('ÙˆØ±Ú©Ø± Ø¨Ø§Ø²Ø§Ø³ØªÙ‚Ø±Ø§Ø± Ø´Ø¯ âœ“','ok');
  }catch(e){toast('Ø®Ø·Ø§ Ø¯Ø± Ø¨Ø§Ø²Ø§Ø³ØªÙ‚Ø±Ø§Ø±','err')}
}

async function syncWorkerProxies(){
  try{
    var r=await authFetch('/api/worker/sync-source',{method:'POST'});
    if(!r.ok)throw new Error();
    toast('Ù‡Ù…Ú¯Ø§Ù…â€ŒØ³Ø§Ø²ÛŒ Ø§Ù†Ø¬Ø§Ù… Ø´Ø¯ âœ“','ok');loadWorker();
  }catch(e){toast('Ø®Ø·Ø§ Ø¯Ø± Ù‡Ù…Ú¯Ø§Ù…â€ŒØ³Ø§Ø²ÛŒ','err')}
}

async function saveWorkerSettings(){
  var body={
    source_url:document.getElementById('worker-source-url').value.trim(),
    auto_sync:document.getElementById('worker-auto-sync').classList.contains('on'),
  };
  try{
    var r=await authFetch('/api/worker/settings',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    toast('ØªÙ†Ø¸ÛŒÙ…Ø§Øª Ø°Ø®ÛŒØ±Ù‡ Ø´Ø¯ âœ“','ok');
  }catch(e){toast('Ø®Ø·Ø§ Ø¯Ø± Ø°Ø®ÛŒØ±Ù‡','err')}
}

async function deleteWorkerProxy(code){
  if(!confirm('Ø¢ÛŒØ§ Ø§Ø² Ø­Ø°Ù Ø§ÛŒÙ† Ù¾Ø±ÙˆÚ©Ø³ÛŒ Ø§Ø·Ù…ÛŒÙ†Ø§Ù† Ø¯Ø§Ø±ÛŒØ¯ØŸ'))return;
  try{
    var r=await authFetch('/api/worker/proxies/'+code,{method:'DELETE'});
    if(!r.ok)throw new Error();
    toast('Ú©Ø´ÙˆØ± Ø­Ø°Ù Ø´Ø¯ âœ“','ok');loadWorker();
  }catch(e){toast(e.message,'err')}
}

async function openAddProxyModal(){
  var code=prompt('Ú©Ø¯ Ú©Ø´ÙˆØ± (Ù…Ø«Ù„Ø§Ù‹: de, us, nl):');
  if(!code)return;
  var country=prompt('Ù†Ø§Ù… Ú©Ø´ÙˆØ± (Ù…Ø«Ù„Ø§Ù‹: Germany):');
  if(!country)return;
  var proxy=prompt('Ø¢Ø¯Ø±Ø³ Ù¾Ø±ÙˆÚ©Ø³ÛŒ (IP ÛŒØ§ Ø¯Ø§Ù…Ù†Ù‡):');
  if(!proxy)return;
  var port=prompt('Ù¾ÙˆØ±Øª:', '443');
  if(!port)port='443';
  try{
    var r=await authFetch('/api/worker/proxies',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({code:code.trim().toLowerCase(),country:country.trim(),proxy:proxy.trim(),port:parseInt(port)})});
    var d=await r.json();
    if(!d.ok)throw new Error(d.detail||'Ø®Ø·Ø§');
    toast('Ú©Ø´ÙˆØ± Ø§Ø¶Ø§ÙÙ‡ Ø´Ø¯ âœ“','ok');
    loadWorker();
  }catch(e){toast(e.message,'err')}
}

/* ============ REFRESH ============ */
function refreshAll(){
  loadDashboard();loadUsers();loadConfigs();loadTraffic();loadLogs();loadWorker();
  toast('Ø¨Ø±ÙˆØ²Ø±Ø³Ø§Ù†ÛŒ Ø´Ø¯ âœ“','ok');
}

/* ============ INIT ============ */
document.addEventListener('DOMContentLoaded',async function(){
  await checkAuth();
  loadDashboard();
  setInterval(function(){
    if(currentPage==='dash')loadDashboard();
    if(currentPage==='users')loadUsers();
    if(currentPage==='configs')loadConfigs();
    if(currentPage==='traffic')loadTraffic();
    if(currentPage==='logs')loadLogs();
    if(currentPage==='settings')loadSettings();
    if(currentPage==='worker')loadWorker();
  },5000);
});
</script>
</body></html>"""



def get_public_page_html(uuid_key: str, sub_url: str = "", announcement: str = "") -> str:
    """Public subscription group page with OS detection, One-Click Import, and Announcements."""
    ann_html = ""
    if announcement:
        from html import escape as _esc
        ann_html = (
            '<div class="announcement-bar" id="announcement-bar">'
            '<i class="ti ti-broadcast"></i>'
            f'<span id="ann-text">{_esc(announcement)}</span>'
            '<button onclick="this.parentElement.remove()" style="background:none;border:none;color:var(--text-secondary);cursor:pointer;font-size:16px;padding:0 4px">&times;</button>'
            '</div>'
        )
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>White Panel</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Estedad:wght@300;400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
:root{{
  --neon-cyan:#06b6d4;--neon-purple:#a855f7;--neon-emerald:#10b981;
  --neon-blue:#6366f1;--wp-blue:#6366f1;--wp-purple:#8b5cf6;--wp-red:#ef4444;
  --success:#10b981;--warning:#f59e0b;
  --text-primary:#f0f0f0;--text-secondary:#64748b;
  --bg:#000000;--surface:rgba(255,255,255,.03);--surface-glass:rgba(255,255,255,.04);
  --border:rgba(255,255,255,.06);
  --gradient:linear-gradient(135deg,#06b6d4,#a855f7,#10b981);
  --gradient-accent:linear-gradient(90deg,#06b6d4,#a855f7,#10b981);
  --radius-sm:10px;--radius:14px;--radius-lg:18px;--radius-xl:22px;
  --shadow-sm:0 1px 2px rgba(0,0,0,.4);--shadow-md:0 4px 16px rgba(0,0,0,.5);
  --shadow-lg:0 12px 40px rgba(0,0,0,.6);
  --transition:.3s cubic-bezier(.4,0,.2,1);
}}
[data-theme="light"]{{
  --text-primary:#0f172a;--text-secondary:#64748b;
  --bg:#f8fafc;--surface:rgba(255,255,255,.7);--surface-glass:rgba(255,255,255,.65);
  --border:rgba(0,0,0,.06);
  --shadow-sm:0 1px 3px rgba(0,0,0,.04);--shadow-md:0 4px 16px rgba(0,0,0,.06);
  --shadow-lg:0 12px 40px rgba(0,0,0,.08);
}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{min-height:100%;background:var(--bg);font-family:'Estedad','Inter',sans-serif;color:var(--text-primary);font-size:14px;transition:background var(--transition),color var(--transition)}}
::-webkit-scrollbar{{width:5px}}
::-webkit-scrollbar-track{{background:transparent}}
::-webkit-scrollbar-thumb{{background:rgba(6,182,212,.15);border-radius:10px}}
#bg-canvas{{position:fixed;inset:0;z-index:0;pointer-events:none;opacity:.6}}
[data-theme="light"] #bg-canvas{{opacity:.3}}
@keyframes staggerIn{{from{{opacity:0;transform:translateY(16px) scale(.97)}}to{{opacity:1;transform:none}}}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
@keyframes float{{0%,100%{{transform:translateY(0) scale(1)}}50%{{transform:translateY(-25px) scale(1.04)}}}}

.announcement-bar{{display:flex;align-items:center;gap:10px;padding:12px 18px;background:linear-gradient(135deg,rgba(6,182,212,.08),rgba(168,85,247,.06));backdrop-filter:blur(20px);border:1px solid rgba(6,182,212,.12);border-radius:var(--radius);margin-bottom:16px;font-size:12px;color:var(--neon-cyan);animation:staggerIn .5s cubic-bezier(.4,0,.2,1) both}}
.announcement-bar i{{font-size:16px;flex-shrink:0}}
.announcement-bar span{{flex:1;color:var(--text-primary);font-weight:500}}

.wrap{{position:relative;z-index:10;max-width:680px;margin:0 auto;padding:28px 16px 60px}}
.top-bar{{display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;gap:10px}}
.brand{{display:flex;align-items:center;gap:10px}}
.brand svg{{width:38px;height:38px;filter:drop-shadow(0 0 12px rgba(6,182,212,.4))}}
.brand-name{{font-size:14px;font-weight:800;color:var(--text-primary);letter-spacing:-.02em}}
.brand-sub{{font-size:8.5px;color:var(--text-secondary);letter-spacing:.04em}}
.theme-toggle{{width:38px;height:38px;border-radius:var(--radius);background:var(--surface-glass);backdrop-filter:blur(12px);border:1px solid var(--border);color:var(--text-secondary);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:16px;transition:all .25s}}
.theme-toggle:hover{{background:rgba(6,182,212,.08);color:var(--neon-cyan);border-color:rgba(6,182,212,.15);box-shadow:0 0 16px rgba(6,182,212,.08)}}

.info-card{{background:var(--surface-glass);backdrop-filter:blur(24px) saturate(200%);border:1px solid var(--border);border-radius:var(--radius-xl);padding:28px 26px 24px;margin-bottom:18px;box-shadow:var(--shadow-lg);position:relative;overflow:hidden;animation:staggerIn .5s cubic-bezier(.4,0,.2,1) both}}
.info-card::before{{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--gradient-accent)}}
.info-card::after{{content:'';position:absolute;top:0;right:0;width:180px;height:180px;background:radial-gradient(circle,rgba(6,182,212,.04),transparent 70%);pointer-events:none}}
.info-name{{font-size:22px;font-weight:800;color:var(--text-primary);position:relative;z-index:1;letter-spacing:-.02em}}
.info-desc{{font-size:12.5px;color:var(--text-secondary);margin-top:6px;position:relative;z-index:1;line-height:1.7}}
.info-stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:18px;position:relative;z-index:1}}
.info-stat{{text-align:center;padding:12px 8px;background:rgba(6,182,212,.04);border-radius:var(--radius);border:1px solid var(--border);transition:all .25s}}
.info-stat:hover{{border-color:rgba(6,182,212,.15);box-shadow:0 4px 16px rgba(6,182,212,.06)}}
.info-s-val{{font-size:18px;font-weight:800;color:var(--text-primary);font-family:'Inter',sans-serif}}
.info-s-label{{font-size:9px;color:var(--text-secondary);margin-top:3px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}}

.import-section{{margin-bottom:20px;animation:staggerIn .5s cubic-bezier(.4,0,.2,1) .1s both}}
.import-title{{font-size:12px;font-weight:800;color:var(--text-secondary);margin-bottom:10px;display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.06em}}
.import-title i{{font-size:14px;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
.import-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}}
.import-btn{{display:flex;align-items:center;gap:10px;padding:12px 14px;border-radius:var(--radius);border:1px solid var(--border);background:var(--surface-glass);backdrop-filter:blur(16px);color:var(--text-primary);font-size:12px;font-weight:600;cursor:pointer;transition:all .3s cubic-bezier(.4,0,.2,1);text-decoration:none}}
.import-btn:hover{{background:linear-gradient(135deg,rgba(6,182,212,.12),rgba(168,85,247,.08));border-color:rgba(6,182,212,.2);box-shadow:0 8px 24px rgba(6,182,212,.1);transform:translateY(-2px)}}
.import-btn .ico{{width:32px;height:32px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0}}
.import-btn .ico.ico-android{{background:rgba(6,182,212,.1);color:var(--neon-cyan)}}
.import-btn .ico.ico-ios{{background:rgba(168,85,247,.1);color:var(--neon-purple)}}
.import-btn .ico.ico-windows{{background:rgba(99,102,241,.1);color:var(--neon-blue)}}
.import-btn .ico.ico-macos{{background:rgba(16,185,129,.1);color:var(--neon-emerald)}}
.import-btn .lbl{{font-size:9px;color:var(--text-secondary);margin-top:1px}}

.section-title{{font-size:12.5px;font-weight:800;color:var(--text-secondary);margin-bottom:12px;display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.06em}}
.section-title i{{font-size:15px;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
.cfg-card{{background:var(--surface-glass);backdrop-filter:blur(20px);border:1px solid var(--border);border-radius:var(--radius-lg);padding:20px 20px 18px;margin-bottom:12px;box-shadow:var(--shadow-sm);transition:all .35s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden;animation:staggerIn .4s cubic-bezier(.4,0,.2,1) both}}
.cfg-card::before{{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--gradient-accent);opacity:0;transition:opacity .3s}}
.cfg-card:hover::before{{opacity:1}}
.cfg-card:hover{{border-color:rgba(6,182,212,.15);transform:translateY(-2px);box-shadow:0 8px 30px rgba(6,182,212,.06)}}
.cfg-head{{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:12px}}
.cfg-name{{font-size:14px;font-weight:700;color:var(--text-primary)}}
.cfg-status{{font-size:10px;padding:3px 10px;border-radius:20px;font-weight:700;white-space:nowrap;display:inline-flex;align-items:center;gap:4px}}
.cfg-status.ok{{background:rgba(16,185,129,.1);color:var(--neon-emerald)}}
.cfg-status.no{{background:rgba(239,68,68,.1);color:var(--wp-red)}}
.cfg-code{{background:rgba(0,0,0,.2);border:1px solid var(--border);border-radius:var(--radius);padding:12px 14px;font-family:'JetBrains Mono','Inter',monospace;font-size:10px;color:var(--neon-cyan);word-break:break-all;line-height:1.7;margin-bottom:10px;max-height:80px;overflow-y:auto}}
[data-theme="light"] .cfg-code{{background:rgba(0,0,0,.03);color:var(--neon-blue)}}
.cfg-actions{{display:flex;gap:7px;flex-wrap:wrap}}

.btn{{font-family:'Estedad','Inter',sans-serif;font-size:11.5px;font-weight:700;border-radius:var(--radius);padding:8px 15px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;border:none;transition:all .25s cubic-bezier(.4,0,.2,1);white-space:nowrap}}
.btn i{{font-size:13px}}
.btn-p{{background:linear-gradient(135deg,#06b6d4,#a855f7);color:#fff;box-shadow:0 4px 20px rgba(6,182,212,.25);position:relative;overflow:hidden}}
.btn-p::before{{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.12),transparent);transition:left .5s}}
.btn-p:hover{{transform:translateY(-2px);box-shadow:0 8px 30px rgba(6,182,212,.35)}}
.btn-p:hover::before{{left:100%}}
.btn-ghost{{background:rgba(6,182,212,.05);color:var(--neon-cyan);border:1px solid rgba(6,182,212,.1)}}
.btn-ghost:hover{{background:rgba(6,182,212,.1);border-color:rgba(6,182,212,.2);box-shadow:0 0 12px rgba(6,182,212,.06)}}

.lock-page{{display:flex;align-items:center;justify-content:center;min-height:60vh}}
.lock-card{{background:var(--surface-glass);backdrop-filter:blur(30px) saturate(200%);border:1px solid var(--border);border-radius:var(--radius-xl);padding:40px 32px 34px;text-align:center;max-width:380px;width:100%;box-shadow:var(--shadow-lg);position:relative;overflow:hidden;animation:staggerIn .5s cubic-bezier(.4,0,.2,1) both}}
.lock-card::before{{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--gradient-accent)}}
.lock-card::after{{content:'';position:absolute;top:0;right:0;width:120px;height:120px;background:radial-gradient(circle,rgba(6,182,212,.04),transparent 70%);pointer-events:none}}
.lock-icon{{width:64px;height:64px;border-radius:18px;background:linear-gradient(135deg,rgba(6,182,212,.1),rgba(168,85,247,.08));border:1px solid rgba(6,182,212,.15);display:flex;align-items:center;justify-content:center;margin:0 auto 18px;font-size:28px;color:var(--neon-cyan);box-shadow:0 0 24px rgba(6,182,212,.1)}}
.lock-title{{font-size:18px;font-weight:800;margin-bottom:6px;position:relative;z-index:1}}
.lock-sub{{font-size:12px;color:var(--text-secondary);margin-bottom:20px;line-height:1.7;position:relative;z-index:1}}
.lock-field{{position:relative;margin-bottom:14px}}
.lock-input{{width:100%;padding:13px 44px;border-radius:var(--radius);border:1.5px solid var(--border);background:rgba(255,255,255,.03);backdrop-filter:blur(8px);color:var(--text-primary);font-family:inherit;font-size:14px;text-align:center;outline:none;transition:all .25s;letter-spacing:.1em}}
.lock-input:focus{{border-color:var(--neon-cyan);box-shadow:0 0 0 3px rgba(6,182,212,.08),0 0 16px rgba(6,182,212,.04)}}
.lock-icon-left{{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--text-secondary);font-size:16px;pointer-events:none}}
.lock-err{{color:var(--wp-red);font-size:11px;margin-bottom:10px;min-height:18px}}

.toast{{position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(40px);background:rgba(10,15,30,.9);backdrop-filter:blur(30px);border:1px solid rgba(255,255,255,.06);color:var(--text-primary);border-radius:var(--radius);padding:10px 20px;font-size:12px;font-weight:500;opacity:0;transition:all .4s cubic-bezier(.4,0,.2,1);z-index:999;pointer-events:none;display:flex;align-items:center;gap:7px;box-shadow:0 12px 40px rgba(0,0,0,.4);white-space:nowrap}}
[data-theme="light"] .toast{{background:rgba(255,255,255,.85);border:1px solid rgba(0,0,0,.06)}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(16,185,129,.2);color:var(--neon-emerald)}}
.toast.err{{border-color:rgba(239,68,68,.2);color:var(--wp-red)}}

.empty{{text-align:center;padding:60px 20px;color:var(--text-secondary)}}
.empty i{{font-size:40px;opacity:.2;display:block;margin-bottom:12px}}
.footer{{text-align:center;padding-top:30px;font-size:10.5px;color:var(--text-secondary);position:relative;z-index:10}}

@media(max-width:500px){{
  .info-stats{{grid-template-columns:1fr 1fr}}
  .wrap{{padding:20px 12px 50px}}
  .import-grid{{grid-template-columns:1fr}}
}}
</style>
</head>
<body data-theme="dark">
<canvas id="bg-canvas"></canvas>
<div class="toast" id="toast"></div>
<div class="wrap">
  {ann_html}
  <div class="top-bar">
    <div class="brand">
      <svg width="38" height="38" viewBox="0 0 100 100"><defs><linearGradient id="bgg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#06b6d4"/><stop offset="50%" style="stop-color:#a855f7"/><stop offset="100%" style="stop-color:#10b981"/></linearGradient></defs><path d="M50 5 L90 22 L90 55 C90 78 72 93 50 98 C28 93 10 78 10 55 L10 22 Z" fill="url(#bgg)" opacity="0.95"/><path d="M50 18 L75 30 L75 54 C75 70 63 80 50 85 C37 80 25 70 25 54 L25 30 Z" fill="rgba(255,255,255,0.12)"/><rect x="43" y="38" width="14" height="22" rx="2" fill="rgba(255,255,255,0.9)"/><circle cx="50" cy="33" r="5" fill="rgba(255,255,255,0.9)"/></svg>
      <div><div class="brand-name">White Panel</div><div class="brand-sub">ENTERPRISE</div></div>
    </div>
    <button class="theme-toggle" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-icon"></i></button>
  </div>
  <div id="root"><div class="empty"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i><p>در حال بارگذاری...</p></div></div>
  <div class="footer">White Panel</div>
</div>
<script>
(function(){{
  var c=document.getElementById('bg-canvas');
  if(!c)return;
  var gl=c.getContext('webgl')||c.getContext('experimental-webgl');
  if(!gl)return;
  var mx=0.5,my=0.5;
  function resize(){{c.width=window.innerWidth;c.height=window.innerHeight;gl.viewport(0,0,c.width,c.height)}}
  resize();window.addEventListener('resize',resize);
  document.addEventListener('mousemove',function(e){{mx=e.clientX/c.width;my=1-e.clientY/c.height}});
  var vsrc='attribute vec2 p;void main(){{gl_Position=vec4(p,0,1);}}';
  var fsrc='precision mediump float;uniform float t;uniform vec2 r;uniform vec2 m;'+
    'void main(){{vec2 uv=gl_FragCoord.xy/r;'+
    'float d=length(uv-m)*0.8;'+
    'float v1=sin(uv.x*6.0+t*0.3)*0.5+0.5;'+
    'float v2=cos(uv.y*5.0+t*0.2)*0.5+0.5;'+
    'float v3=sin((uv.x+uv.y)*4.0+t*0.25)*0.5+0.5;'+
    'vec3 c1=vec3(0.024,0.714,0.831);'+
    'vec3 c2=vec3(0.659,0.333,0.969);'+
    'vec3 c3=vec3(0.063,0.725,0.506);'+
    'vec3 col=mix(c1,c2,v1)*v2+mix(c2,c3,v3)*0.3;'+
    'col*=0.08*(1.0-d*0.5);'+
    'col+=vec3(0.01)*sin(t*0.5);'+
    'gl_FragColor=vec4(col,1);}}';
  function cs(src,type){{var s=gl.createShader(type);gl.shaderSource(s,src);gl.compileShader(s);return s}}
  var pg=gl.createProgram();gl.attachShader(pg,cs(vsrc,gl.VERTEX_SHADER));gl.attachShader(pg,cs(fsrc,gl.FRAGMENT_SHADER));gl.linkProgram(pg);gl.useProgram(pg);
  var buf=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buf);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);
  var pl=gl.getAttribLocation(pg,'p');gl.enableVertexAttribArray(pl);gl.vertexAttribPointer(pl,2,gl.FLOAT,false,0,0);
  var ut=gl.getUniformLocation(pg,'t'),ur=gl.getUniformLocation(pg,'r'),um=gl.getUniformLocation(pg,'m');
  function draw(t){{gl.uniform1f(ut,t*0.001);gl.uniform2f(ur,c.width,c.height);gl.uniform2f(um,mx,my);gl.drawArrays(gl.TRIANGLE_STRIP,0,4);requestAnimationFrame(draw)}}
  requestAnimationFrame(draw);
}})();
</script>
<script>
var UUID_KEY='{uuid_key}',SUB_URL='{sub_url}',savedPw='',currentData=null;
var isDark=localStorage.getItem('wp-pub-theme')==='dark';
function applyTheme(d){{document.documentElement.setAttribute('data-theme',d?'dark':'light');document.getElementById('theme-icon').className='ti '+(d?'ti-sun':'ti-moon')}}
function toggleTheme(){{isDark=!isDark;localStorage.setItem('wp-pub-theme',isDark?'dark':'light');applyTheme(isDark)}}
applyTheme(isDark);
function toast(m,t){{var el=document.getElementById('toast');el.textContent=m;el.className='toast show'+(t?' '+t:'');setTimeout(function(){{el.classList.remove('show')}},2400)}}
function esc(s){{return String(s||'').replace(/[&<>"']/g,function(c){{return{{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]}})}}
function fmtB(b){{if(!b)return'0 B';if(b<1024)return b+' B';if(b<1024**2)return(b/1024).toFixed(1)+' KB';if(b<1024**3)return(b/1024**2).toFixed(2)+' MB';return(b/1024**3).toFixed(2)+' GB'}}
function toFa(n){{return String(n).replace(/\d/g,function(d){{return'\u06f0\u06f1\u06f2\u06f3\u06f4\u06f5\u06f6\u06f7\u06f8\u06f9'[d]}})}}

function detectOS(){{
  var ua=navigator.userAgent||'';
  if(/android/i.test(ua))return'android';
  if(/iPad|iPhone|iPod/.test(ua)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1))return'ios';
  if(/Win\d/.test(ua))return'windows';
  if(/Macintosh|Mac OS X/.test(ua))return'macos';
  return'other';
}}
function getImportApps(){{
  var os=detectOS(),apps=[];
  if(os==='android'){{
    apps.push({{name:'v2rayNG',icon:'ti ti-brand-android',cls:'ico-android',href:'v2rayng://install-sub?url='+encodeURIComponent(SUB_URL)}});
    apps.push({{name:'Hiddify',icon:'ti ti-shield',cls:'ico-android',href:'hiddify://import?url='+encodeURIComponent(SUB_URL)}});
    apps.push({{name:'V2Box',icon:'ti ti-box',cls:'ico-android',href:'v2box://import?url='+encodeURIComponent(SUB_URL)}});
  }}else if(os==='ios'){{
    apps.push({{name:'V2Box',icon:'ti ti-box',cls:'ico-ios',href:'v2box://import?url='+encodeURIComponent(SUB_URL)}});
    apps.push({{name:'Hiddify',icon:'ti ti-shield',cls:'ico-ios',href:'hiddify://import?url='+encodeURIComponent(SUB_URL)}});
    apps.push({{name:'Streisand',icon:'ti ti-bolt',cls:'ico-ios',href:'streisand://import?url='+encodeURIComponent(SUB_URL)}});
  }}else if(os==='windows'){{
    apps.push({{name:'v2rayN',icon:'ti ti-brand-windows',cls:'ico-windows',href:'v2rayn://import?url='+encodeURIComponent(SUB_URL)}});
    apps.push({{name:'Hiddify',icon:'ti ti-shield',cls:'ico-windows',href:'hiddify://import?url='+encodeURIComponent(SUB_URL)}});
  }}else if(os==='macos'){{
    apps.push({{name:'V2rayU',icon:'ti ti-brand-apple',cls:'ico-macos',href:'v2rayu://import?url='+encodeURIComponent(SUB_URL)}});
    apps.push({{name:'Hiddify',icon:'ti ti-shield',cls:'ico-macos',href:'hiddify://import?url='+encodeURIComponent(SUB_URL)}});
  }}
  return apps;
}}
function buildImportHtml(){{
  var apps=getImportApps();
  if(!apps.length)return'';
  var h='<div class="import-section"><div class="import-title"><i class="ti ti-download"></i> \u0648\u0627\u0631\u062f \u06a9\u0631\u062f\u0646 \u0633\u0631\u06cc\u0639</div><div class="import-grid">';
  apps.forEach(function(a){{
    h+='<a class="import-btn" href="'+esc(a.href)+'"><div class="ico '+a.cls+'"><i class="ti '+a.icon+'"></i></div><div><div>'+esc(a.name)+'</div><div class="lbl">\u06cc\u06a9 \u06a9\u0644\u06cc\u06a9</div></div></a>';
  }});
  h+='</div></div>';return h;
}}

async function loadData(pw){{var u='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');var r=await fetch(u);return r.json()}}

function renderLock(name,err){{
  document.getElementById('root').innerHTML='<div class="lock-page"><div class="lock-card"><div class="lock-icon"><i class="ti ti-shield-lock"></i></div><div class="lock-title">'+esc(name)+'</div><div class="lock-sub">\u0627\u06cc\u0646 \u06af\u0631\u0648\u0647 \u0628\u0627 \u0631\u0645\u0632 \u0645\u062d\u0627\u0641\u0638\u062a \u0645\u06cc\u200c\u0634\u0648\u062f</div><div class="lock-err" id="lock-err">'+(err?'<i class="ti ti-alert-circle"></i> '+esc(err):'')+'</div><div class="lock-field"><i class="ti ti-lock lock-icon-left"></i><input class="lock-input" type="password" id="lock-pw" placeholder="\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022" autofocus></div><button class="btn btn-p" style="width:100%;justify-content:center;padding:12px" onclick="submitLock()"><i class="ti ti-lock-open"></i> \u0648\u0631\u0648\u062f</button></div></div>';
  document.getElementById('lock-pw').addEventListener('keydown',function(e){{if(e.key==='Enter')submitLock()}});
}}

async function submitLock(){{var pw=document.getElementById('lock-pw').value;var d=await loadData(pw);if(d.locked){{renderLock(d.name,'\u0631\u0645\u0632 \u0627\u0634\u062a\u0628\u0627\u0647 \u0627\u0633\u062a');return}}savedPw=pw;renderContent(d)}}

function renderContent(d){{
  currentData=d;
  var active=d.links.filter(function(l){{return l.active}}).length;
  var subUrl=d.sub_url||SUB_URL;
  subUrl+=savedPw?'?pw='+encodeURIComponent(savedPw):'';
  var importHtml=buildImportHtml();
  document.getElementById('root').innerHTML=
    '<div class="info-card"><div class="info-name">'+esc(d.name)+'</div>'+
    (d.desc?'<div class="info-desc">'+esc(d.desc)+'</div>':'')+
    '<div class="info-stats">'+
    '<div class="info-stat"><div class="info-s-val">'+toFa(active)+'</div><div class="info-s-label">\u06a9\u0627\u0646\u0641\u06cc\u06af \u0641\u0639\u0627\u0644</div></div>'+
    '<div class="info-stat"><div class="info-s-val">'+toFa(d.links.length)+'</div><div class="info-s-label">\u06a9\u0644 \u06a9\u0627\u0646\u0641\u06cc\u06af\u200c\u0647\u0627</div></div>'+
    '<div class="info-stat"><div class="info-s-val">'+esc(d.total_used_fmt||'0')+'</div><div class="info-s-label">\u0645\u0635\u0631\u0641</div></div>'+
    '</div></div>'+
    importHtml+
    '<div class="section-title"><i class="ti ti-link"></i> \u06a9\u0627\u0646\u0641\u06cc\u06af\u200c\u0647\u0627 ('+toFa(d.links.length)+' \u0639\u062f\u062f)</div>'+
    (d.links.length?d.links.map(function(l){{
      return '<div class="cfg-card"><div class="cfg-head"><div class="cfg-name">'+esc(l.label)+'</div>'+
        '<span class="cfg-status '+(l.active?'ok':'no')+'">'+(l.active?'<i class="ti ti-circle-check"></i> \u0641\u0639\u0627\u0644':'<i class="ti ti-circle-x"></i> \u063a\u06cc\u0631\u0641\u0639\u0627\u0644')+'</span></div>'+
        '<div class="cfg-code">'+esc(l.vless_link)+'</div>'+
        '<div class="cfg-actions">'+
        '<button class="btn btn-p" onclick="navigator.clipboard.writeText(\''+esc(l.vless_link).replace(/'/g,"\\'")+'\').then(function(){{toast(\'\u06a9\u067e\u06cc \u0634\u062f \u2713\',\'ok\')}})"><i class="ti ti-copy"></i> \u06a9\u067e\u06cc \u0644\u06cc\u0646\u06a9</button>'+
        '<button class="btn btn-ghost" onclick="window.open(\'https://api.qrserver.com/v1/create-qr-code/?size=220x220&data='+encodeURIComponent(l.vless_link)+'\',\'_blank\')"><i class="ti ti-qrcode"></i> QR Code</button>'+
        '</div></div>';
    }}).join(''):'<div class="empty"><i class="ti ti-link-off"></i><p>\u06a9\u0627\u0646\u0641\u06cc\u06af\u06cc \u062f\u0631 \u0627\u06cc\u0646 \u06af\u0631\u0648\u0647 \u0648\u062c\u0648\u062f \u0646\u062f\u0627\u0631\u062f</p></div>')+
    '<div style="margin-top:16px;text-align:center"><button class="btn btn-ghost" style="justify-content:center" onclick="location.reload()"><i class="ti ti-refresh"></i> \u0628\u0631\u0648\u0632\u0631\u0633\u0627\u0646\u06cc</button></div>';
}}

async function init(){{try{{var d=await loadData();if(d.locked){{renderLock(d.name);return}}renderContent(d)}}catch(e){{document.getElementById('root').innerHTML='<div class="empty"><i class="ti ti-alert-circle" style="color:var(--wp-red)"></i><p>\u062e\u0637\u0627 \u062f\u0631 \u0628\u0627\u0631\u06af\u0630\u0627\u0631\u06cc</p></div>'}}}}
init();
</script>
</body></html>"""
