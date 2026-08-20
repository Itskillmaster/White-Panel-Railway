# pages.py — White Panel Enterprise Theme
# Exports: LOGIN_HTML, DASHBOARD_HTML, get_public_page_html()

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ورود · White Panel</title>
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
    <div class="login-sub">به پنل مدیریت خوش آمدید<br>برای ادامه رمز عبور را وارد کنید</div>
    <div class="error-msg" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <div class="login-hint">
      <span class="hint-label"><i class="ti ti-key"></i> رمز پیش‌فرض</span>
      <span class="hint-value" onclick="document.getElementById('pw').value='123456';document.getElementById('pw').focus()">123456</span>
    </div>
    <form id="form">
      <div class="field-group">
        <div class="field-label"><i class="ti ti-lock"></i> رمز عبور</div>
        <div class="input-wrap">
          <input type="password" id="pw" placeholder="••••••••" autofocus required>
          <i class="ti ti-lock input-icon"></i>
          <button type="button" class="eye-toggle" id="eye-btn" title="نمایش رمز">
            <i class="ti ti-eye"></i>
          </button>
        </div>
      </div>
      <button type="submit" class="login-btn" id="btn">
        <span class="spinner"></span>
        <span class="btn-text"><i class="ti ti-login-2"></i> ورود به داشبورد</span>
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
      if(!r.ok){var d=await r.json().catch(function(){return{}});throw new Error(d.detail||'خطا در ورود');}
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
<title>White Panel · داشبورد</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Estedad:wght@300;400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
/* ============ CSS VARIABLES ============ */
:root{
  --wp-blue:#6366f1;--wp-purple:#8b5cf6;--wp-red:#ef4444;
  --success:#16A34A;--warning:#F59E0B;--danger:#DC2626;
  --text-primary:#0F172A;--text-secondary:#475569;
  --bg:#F8FAFC;--surface:#FFFFFF;--surface-glass:rgba(255,255,255,.75);
  --border:rgba(226,232,240,.8);--border-solid:#E2E8F0;
  --gradient:linear-gradient(135deg,#6366f1,#8b5cf6,#a78bfa);
  --gradient-purple:linear-gradient(135deg,#8b5cf6,#6366f1);
  --gradient-blue:linear-gradient(135deg,#6366f1,#818cf8);
  --gradient-accent:linear-gradient(90deg,#6366f1,#8b5cf6,#a78bfa);
  --radius-sm:12px;--radius:18px;--radius-lg:24px;--radius-xl:28px;
  --shadow-sm:0 1px 3px rgba(0,0,0,.04);--shadow-md:0 4px 16px rgba(0,0,0,.06);
  --shadow-lg:0 12px 40px rgba(0,0,0,.08);--shadow-hover:0 8px 30px rgba(0,0,0,.1);
  --sidebar-w:260px;--topbar-h:68px;--transition:.3s ease;
}
[data-theme="dark"]{
  --text-primary:#F1F5F9;--text-secondary:#94A3B8;
  --bg:#050a15;--surface:rgba(10,18,36,.95);--surface-glass:rgba(10,18,36,.85);
  --border:rgba(99,102,241,.08);--border-solid:rgba(99,102,241,.12);
  --shadow-sm:0 1px 3px rgba(0,0,0,.3);--shadow-md:0 4px 16px rgba(0,0,0,.4);
  --shadow-lg:0 12px 40px rgba(0,0,0,.5);--shadow-hover:0 8px 30px rgba(99,102,241,.12);
}

/* ============ RESET ============ */
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{font-family:'Estedad',sans-serif;background:var(--bg);color:var(--text-primary);min-height:100vh;display:flex;font-size:14px;transition:background var(--transition),color var(--transition);overflow-x:hidden}
::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:rgba(99,102,241,.2);border-radius:10px}
::-webkit-scrollbar-thumb:hover{background:rgba(99,102,241,.4)}
*{scrollbar-width:thin;scrollbar-color:rgba(99,102,241,.25) transparent}
a{color:inherit;text-decoration:none}

/* ============ PARTICLES BG ============ */
.bg-particles{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.bg-p{position:absolute;border-radius:50%;animation:bgDrift linear infinite;filter:blur(1px)}
@keyframes bgDrift{0%{transform:translate(0,0) scale(1);opacity:0}10%{opacity:.18}90%{opacity:.18}100%{transform:translate(60px,-45px) scale(.15);opacity:0}}

/* ============ SIDEBAR ============ */
.sidebar{width:var(--sidebar-w);min-height:100vh;background:linear-gradient(180deg,rgba(99,102,241,.04) 0%,var(--surface-glass) 40%);backdrop-filter:blur(24px) saturate(180%);-webkit-backdrop-filter:blur(24px) saturate(180%);border-left:1px solid var(--border);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform var(--transition),background var(--transition),border-color var(--transition);box-shadow:-4px 0 24px rgba(99,102,241,.04)}
.sidebar-logo{display:flex;align-items:center;gap:12px;padding:22px 18px 18px;border-bottom:1px solid var(--border);flex-shrink:0}
.sidebar-logo svg{width:36px;height:36px;filter:drop-shadow(0 2px 12px rgba(99,102,241,.35));flex-shrink:0}
.sidebar-logo-text{font-size:16px;font-weight:800;color:var(--text-primary);letter-spacing:-.02em}
.sidebar-logo-sub{font-size:9.5px;color:var(--text-secondary);margin-top:1px}
.sidebar-nav{flex:1;overflow-y:auto;padding:8px 0}
.nav-section{padding:16px 18px 6px;font-size:9px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--text-secondary);opacity:.6}
.nav-item{display:flex;align-items:center;gap:10px;padding:10px 14px;color:var(--text-secondary);font-size:12.5px;font-weight:500;cursor:pointer;border-right:3px solid transparent;transition:all .25s cubic-bezier(.4,0,.2,1);margin:1px 8px;border-radius:0 var(--radius-sm) var(--radius-sm) 0;position:relative}
.nav-item i{font-size:17px;width:22px;text-align:center;flex-shrink:0;transition:color .25s}
.nav-item:hover{background:rgba(99,102,241,.06);color:var(--text-primary)}
.nav-item.active{background:linear-gradient(135deg,rgba(139,92,246,.12),rgba(99,102,241,.08));color:var(--wp-purple);border-right-color:var(--wp-purple);font-weight:700;box-shadow:inset 0 0 20px rgba(99,102,241,.06),0 0 15px rgba(139,92,246,.08)}
.nav-item.active i{color:var(--wp-purple);filter:drop-shadow(0 0 6px rgba(139,92,246,.4))}
.nav-badge{margin-right:auto;background:rgba(99,102,241,.1);color:var(--wp-blue);font-size:9px;padding:2px 7px;border-radius:20px;font-weight:700}
.sidebar-footer{padding:12px 16px;border-top:1px solid var(--border);flex-shrink:0}
.sidebar-user{display:flex;align-items:center;gap:10px;margin-bottom:10px}
.sidebar-avatar{width:38px;height:38px;border-radius:var(--radius-sm);background:var(--gradient-purple);display:flex;align-items:center;justify-content:center;color:#fff;font-size:16px;flex-shrink:0;box-shadow:0 4px 14px rgba(139,92,246,.35)}
.sidebar-user-name{font-size:12.5px;font-weight:700;color:var(--text-primary)}
.sidebar-user-role{font-size:9.5px;color:var(--text-secondary)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;width:100%;padding:9px;border:none;border-radius:var(--radius-sm);background:rgba(99,102,241,.06);color:var(--text-secondary);font-family:inherit;font-size:11.5px;font-weight:600;cursor:pointer;transition:all .25s;border:1px solid var(--border)}
.theme-btn:hover{background:rgba(99,102,241,.12);color:var(--text-primary);border-color:rgba(99,102,241,.2)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;width:100%;padding:9px;border:none;border-radius:var(--radius-sm);background:rgba(239,68,68,.06);color:var(--wp-red);font-family:inherit;font-size:11.5px;font-weight:600;cursor:pointer;transition:all .25s;margin-top:6px;border:1px solid rgba(239,68,68,.1)}
.logout-btn:hover{background:rgba(239,68,68,.12);border-color:rgba(239,68,68,.2)}

/* ============ MOBILE ============ */
.mobile-top{display:none;position:fixed;top:0;right:0;left:0;height:56px;background:var(--surface-glass);backdrop-filter:blur(24px) saturate(180%);border-bottom:1px solid var(--border);z-index:150;align-items:center;justify-content:space-between;padding:0 14px}
.mobile-brand{display:flex;align-items:center;gap:9px}
.mobile-brand svg{width:28px;height:28px;filter:drop-shadow(0 2px 8px rgba(99,102,241,.3))}
.mobile-brand span{font-size:13px;font-weight:700;color:var(--text-primary)}
.mobile-actions{display:flex;gap:6px}
.mob-btn{background:rgba(99,102,241,.06);border:1px solid var(--border);color:var(--text-secondary);width:34px;height:34px;border-radius:10px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .2s}
.mob-btn:hover{background:rgba(99,102,241,.12);color:var(--wp-blue)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:190;backdrop-filter:blur(6px)}
.overlay.show{display:block}

/* ============ MAIN ============ */
.main{margin-right:var(--sidebar-w);flex:1;padding:24px 28px 40px;min-width:0;transition:margin var(--transition);position:relative;z-index:1}
.page{display:none;animation:fadeIn .25s ease}
.page.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

/* ============ TOPBAR ============ */
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:12px}
.topbar-title{font-size:22px;font-weight:800;color:var(--text-primary);display:flex;align-items:center;gap:9px;letter-spacing:-.03em}
.topbar-title i{color:var(--wp-blue);font-size:23px}
.topbar-sub{font-size:11px;color:var(--text-secondary);margin-top:3px}
.topbar-right{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.welcome-text{font-size:12.5px;color:var(--text-secondary);display:flex;align-items:center;gap:5px;font-weight:500}
.bell-btn{width:38px;height:38px;border-radius:var(--radius-sm);background:rgba(99,102,241,.06);border:1px solid var(--border);color:var(--text-secondary);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:17px;transition:all .25s;position:relative}
.bell-btn:hover{background:rgba(99,102,241,.12);color:var(--wp-blue);border-color:rgba(99,102,241,.2);box-shadow:0 0 12px rgba(99,102,241,.1)}
.bell-btn::after{content:'';position:absolute;top:8px;left:8px;width:7px;height:7px;border-radius:50%;background:var(--wp-red);border:2px solid var(--surface)}

/* ============ BUTTONS ============ */
.btn{font-family:'Estedad',sans-serif;font-size:12px;font-weight:600;border-radius:var(--radius);padding:9px 16px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;border:none;transition:all .25s cubic-bezier(.4,0,.2,1);white-space:nowrap}
.btn i{font-size:13px}
.btn-primary{background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;box-shadow:0 4px 16px rgba(99,102,241,.3);position:relative;overflow:hidden}
.btn-primary::before{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.15),transparent);transition:left .5s}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(99,102,241,.4)}
.btn-primary:hover::before{left:100%}
.btn-primary:active{transform:translateY(0);box-shadow:0 4px 12px rgba(99,102,241,.25)}
.btn-ghost{background:rgba(99,102,241,.06);color:var(--wp-blue);border:1px solid rgba(99,102,241,.15)}
.btn-ghost:hover{background:rgba(99,102,241,.12);border-color:rgba(99,102,241,.25);box-shadow:0 0 12px rgba(99,102,241,.08)}
.btn-danger{background:rgba(239,68,68,.06);color:var(--wp-red);border:1px solid rgba(239,68,68,.15)}
.btn-danger:hover{background:rgba(239,68,68,.12);border-color:rgba(239,68,68,.25);box-shadow:0 0 12px rgba(239,68,68,.08)}
.btn-sm{padding:5px 10px;font-size:10.5px;border-radius:10px}
.btn-icon{width:32px;height:32px;padding:0;justify-content:center;border-radius:10px}
.btn-purple{background:rgba(139,92,246,.08);color:var(--wp-purple);border:1px solid rgba(139,92,246,.15)}
.btn-purple:hover{background:rgba(139,92,246,.15);border-color:rgba(139,92,246,.25)}
.btn-success{background:rgba(22,163,74,.08);color:var(--success);border:1px solid rgba(22,163,74,.15)}
.btn-success:hover{background:rgba(22,163,74,.15);border-color:rgba(22,163,74,.25)}

/* ============ BADGES ============ */
.badge{font-size:9.5px;padding:3px 10px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:4px;white-space:nowrap}
.badge-blue{background:rgba(99,102,241,.1);color:var(--wp-blue)}
.badge-green{background:rgba(22,163,74,.1);color:var(--success)}
.badge-red{background:rgba(239,68,68,.1);color:var(--wp-red)}
.badge-purple{background:rgba(139,92,246,.1);color:var(--wp-purple)}
.badge-amber{background:rgba(245,158,11,.1);color:var(--warning)}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dot-green{background:var(--success)}
.dot-red{background:var(--wp-red)}
.dot-blue{background:var(--wp-blue)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}

/* ============ STATS CARDS ============ */
.stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px}
.stat-card{background:var(--surface-glass);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius-lg);padding:20px 18px 16px;transition:all .35s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden;cursor:default}
.stat-card::before{content:'';position:absolute;top:0;left:0;right:0;height:4px;background:var(--gradient-accent);opacity:0;transition:opacity .3s}
.stat-card:hover::before{opacity:1}
.stat-card:hover{transform:translateY(-4px) scale(1.01);border-color:rgba(99,102,241,.2);box-shadow:0 12px 40px rgba(99,102,241,.1)}
.stat-card::after{content:'';position:absolute;top:0;right:0;width:4px;height:40px;background:var(--gradient-accent);border-radius:0 0 0 6px;transition:height .35s cubic-bezier(.4,0,.2,1)}
.stat-card:hover::after{height:60px}
.stat-icon{width:42px;height:42px;border-radius:var(--radius-sm);display:flex;align-items:center;justify-content:center;font-size:19px;margin-bottom:12px;transition:all .3s}
.stat-card:hover .stat-icon{filter:drop-shadow(0 0 10px currentColor);transform:scale(1.08)}
.stat-icon.blue{background:rgba(99,102,241,.1);color:var(--wp-blue)}
.stat-icon.purple{background:rgba(139,92,246,.1);color:var(--wp-purple)}
.stat-icon.green{background:rgba(22,163,74,.1);color:var(--success)}
.stat-icon.red{background:rgba(239,68,68,.1);color:var(--wp-red)}
.stat-label{font-size:10.5px;font-weight:700;color:var(--text-secondary);text-transform:uppercase;letter-spacing:.08em;margin-bottom:5px}
.stat-value{font-size:28px;font-weight:800;color:var(--text-primary);line-height:1;letter-spacing:-.03em}
.stat-sub{font-size:10px;color:var(--text-secondary);margin-top:7px;display:flex;align-items:center;gap:4px}
.stat-sub.up{color:var(--success)}

/* ============ QUIICK ACTIONS ============ */
.quick-actions{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px}
.qa-btn{display:flex;align-items:center;gap:10px;padding:14px 16px;border-radius:var(--radius);border:1px solid var(--border);background:var(--surface-glass);backdrop-filter:blur(12px);color:var(--text-primary);font-family:inherit;font-size:12.5px;font-weight:600;cursor:pointer;transition:all .3s cubic-bezier(.4,0,.2,1)}
.qa-btn:hover{background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;border-color:transparent;box-shadow:0 8px 24px rgba(99,102,241,.3);transform:translateY(-3px)}
.qa-btn i{font-size:18px;transition:transform .3s}
.qa-btn:hover i{transform:scale(1.1)}

/* ============ SERVER INFO ============ */
.server-panel{background:var(--surface-glass);backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius-lg);padding:22px 24px 20px;margin-bottom:20px;box-shadow:var(--shadow-sm);position:relative;overflow:hidden}
.server-panel::before{content:'';position:absolute;top:0;left:0;right:0;height:4px;background:var(--gradient-accent)}
.server-title{font-size:15px;font-weight:800;color:var(--text-primary);margin-bottom:16px;display:flex;align-items:center;gap:8px}
.server-title i{color:var(--wp-blue);font-size:18px}
.server-bars{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.srv-bar-item{display:flex;flex-direction:column;gap:7px}
.srv-bar-label{display:flex;justify-content:space-between;font-size:10.5px;font-weight:600}
.srv-bar-name{color:var(--text-secondary)}
.srv-bar-pct{color:var(--text-primary)}
.srv-bar-track{height:8px;border-radius:4px;background:rgba(99,102,241,.08);overflow:hidden}
.srv-bar-fill{height:100%;border-radius:4px;transition:width .8s cubic-bezier(.4,0,.2,1);position:relative}
.srv-bar-fill::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.4),transparent);width:50%;animation:shimmer 2.5s linear infinite}
.srv-bar-fill.blue{background:linear-gradient(90deg,#6366f1,#818cf8)}
.srv-bar-fill.purple{background:linear-gradient(90deg,#8b5cf6,#a78bfa)}
.srv-bar-fill.amber{background:linear-gradient(90deg,#F59E0B,#FCD34D)}
.srv-bar-fill.green{background:linear-gradient(90deg,#16A34A,#4ADE80)}
@keyframes shimmer{0%{transform:translateX(-100%)}100%{transform:translateX(200%)}}

/* ============ TABLE ============ */
.table-wrap{background:var(--surface-glass);backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-sm);position:relative}
.table-wrap::before{content:'';position:absolute;top:0;left:0;right:0;height:4px;background:var(--gradient-accent)}
.table-wrap table{width:100%;border-collapse:collapse}
.table-wrap th{background:rgba(99,102,241,.04);font-size:10px;font-weight:800;color:var(--text-secondary);text-transform:uppercase;letter-spacing:.08em;padding:12px 14px;text-align:right;border-bottom:1px solid var(--border);position:sticky;top:0;z-index:1}
.table-wrap td{padding:12px 14px;font-size:12px;color:var(--text-primary);border-bottom:1px solid var(--border);transition:all .2s}
.table-wrap tbody tr:nth-child(even){background:rgba(99,102,241,.02)}
.table-wrap tbody tr:nth-child(even):hover td{background:rgba(99,102,241,.05)}
.table-wrap tr:hover td{background:rgba(99,102,241,.04);box-shadow:inset 0 0 20px rgba(99,102,241,.03)}
.table-wrap tr:last-child td{border-bottom:none}
.proto-badge{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700}
.pb-vless{background:rgba(99,102,241,.1);color:var(--wp-blue)}
.pb-vmess{background:rgba(139,92,246,.1);color:var(--wp-purple)}
.pb-trojan{background:rgba(239,68,68,.1);color:var(--wp-red)}
.pb-ss{background:rgba(22,163,74,.1);color:var(--success)}
.pb-wg{background:rgba(245,158,11,.1);color:var(--warning)}
.usage-bar-wrap{width:100%;min-width:100px}
.usage-bar{height:6px;border-radius:3px;background:rgba(99,102,241,.08);overflow:hidden;margin-bottom:3px}
.usage-fill{height:100%;border-radius:3px;background:var(--gradient-blue);transition:width .5s ease}
.usage-text{font-size:9.5px;color:var(--text-secondary);display:flex;justify-content:space-between}
.status-dot{display:flex;align-items:center;gap:5px;font-weight:600;font-size:11px}
.status-dot.active{color:var(--success)}
.status-dot.expired{color:var(--wp-red)}
.exp-chip{font-size:9px;padding:2px 8px;border-radius:6px;font-weight:700}
.exp-ok{background:rgba(22,163,74,.1);color:var(--success)}
.exp-warn{background:rgba(245,158,11,.1);color:var(--warning)}
.exp-bad{background:rgba(239,68,68,.1);color:var(--wp-red)}
.action-btns{display:flex;gap:4px}

/* ============ MODALS ============ */
.modal-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(8px);padding:20px}
.modal-overlay.open{display:flex}
.modal-card{background:var(--surface-glass);backdrop-filter:blur(32px) saturate(200%);-webkit-backdrop-filter:blur(32px) saturate(200%);border:1px solid var(--border);border-radius:var(--radius-xl);padding:0;max-width:540px;width:100%;max-height:90vh;overflow-y:auto;box-shadow:0 24px 80px rgba(99,102,241,.12),var(--shadow-lg);animation:modalIn .35s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden}
.modal-card::before{content:'';position:absolute;top:0;left:0;right:0;height:4px;background:var(--gradient-accent)}
@keyframes modalIn{from{opacity:0;transform:scale(.92) translateY(16px)}to{opacity:1;transform:scale(1) translateY(0)}}
.modal-head{padding:22px 26px 18px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;position:relative}
.modal-head::before{content:'';position:absolute;top:0;right:0;width:150px;height:150px;background:radial-gradient(circle,rgba(139,92,246,.06),transparent 70%);pointer-events:none}
.modal-title{font-size:17px;font-weight:800;color:var(--text-primary);display:flex;align-items:center;gap:8px;position:relative;z-index:1}
.modal-title i{color:var(--wp-purple);font-size:19px}
.modal-close{width:32px;height:32px;border-radius:10px;background:rgba(99,102,241,.06);border:1px solid var(--border);color:var(--text-secondary);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:16px;transition:all .25s}
.modal-close:hover{background:rgba(239,68,68,.1);color:var(--wp-red);border-color:rgba(239,68,68,.2);box-shadow:0 0 12px rgba(239,68,68,.1)}
.modal-body{padding:20px 26px}
.modal-footer{padding:16px 26px 20px;border-top:1px solid var(--border);display:flex;gap:10px;justify-content:flex-end}
/* Form fields */
.form-field{margin-bottom:14px}
.form-field label{display:flex;align-items:center;gap:5px;font-size:10px;font-weight:800;color:var(--text-secondary);text-transform:uppercase;letter-spacing:.05em;margin-bottom:6px}
.form-field label i{color:var(--wp-purple);font-size:13px}
.form-input{width:100%;padding:10px 14px;border-radius:var(--radius);border:1.5px solid var(--border);background:rgba(255,255,255,.5);backdrop-filter:blur(8px);color:var(--text-primary);font-family:inherit;font-size:12.5px;outline:none;transition:all .25s}
[data-theme="dark"] .form-input{background:rgba(10,18,36,.5);color:var(--text-primary)}
.form-input:focus{border-color:var(--wp-blue);box-shadow:0 0 0 3px rgba(99,102,241,.1),0 0 16px rgba(99,102,241,.06)}
.form-input::placeholder{color:var(--text-secondary);opacity:.5}
.form-row{display:flex;gap:10px;flex-wrap:wrap}
.form-row .form-field{flex:1;min-width:120px}
.form-select{width:100%;padding:10px 14px;border-radius:var(--radius);border:1.5px solid var(--border);background:rgba(255,255,255,.5);backdrop-filter:blur(8px);color:var(--text-primary);font-family:inherit;font-size:12.5px;outline:none;cursor:pointer;transition:all .25s}
[data-theme="dark"] .form-select{background:rgba(10,18,36,.5);color:var(--text-primary)}
.form-select:focus{border-color:var(--wp-blue);box-shadow:0 0 0 3px rgba(99,102,241,.1)}
.form-textarea{width:100%;padding:10px 14px;border-radius:var(--radius);border:1.5px solid var(--border);background:rgba(255,255,255,.5);backdrop-filter:blur(8px);color:var(--text-primary);font-family:inherit;font-size:12.5px;outline:none;resize:vertical;min-height:70px;transition:all .25s}
.form-textarea:focus{border-color:var(--wp-blue);box-shadow:0 0 0 3px rgba(99,102,241,.1)}
[data-theme="dark"] .form-textarea{background:rgba(10,18,36,.5)}
/* Toggle switch */
.toggle-wrap{display:flex;align-items:center;gap:10px}
.toggle-switch{width:44px;height:24px;border-radius:12px;background:rgba(100,116,139,.25);position:relative;cursor:pointer;transition:all .3s;border:none;flex-shrink:0}
.toggle-switch::after{content:'';position:absolute;width:18px;height:18px;border-radius:50%;background:#fff;right:3px;top:3px;transition:all .3s;box-shadow:0 1px 3px rgba(0,0,0,.2)}
.toggle-switch.on{background:var(--success)}
.toggle-switch.on::after{right:23px}
.toggle-label{font-size:11.5px;color:var(--text-secondary);font-weight:600}

/* ============ CONFIG CARDS ============ */
.cfg-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.cfg-card-item{background:var(--surface-glass);backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius-lg);padding:0;overflow:hidden;transition:all .35s cubic-bezier(.4,0,.2,1);position:relative}
.cfg-card-item::before{content:'';position:absolute;top:0;left:0;right:0;height:4px;background:var(--gradient-accent);opacity:0;transition:opacity .3s}
.cfg-card-item:hover::before{opacity:1}
.cfg-card-item:hover{border-color:rgba(99,102,241,.2);transform:translateY(-3px);box-shadow:0 12px 40px rgba(99,102,241,.08)}
.cfg-card-top{padding:16px 18px 12px;display:flex;align-items:flex-start;justify-content:space-between;gap:10px}
.cfg-card-label{font-size:14px;font-weight:700;color:var(--text-primary)}
.cfg-card-body{padding:0 18px 14px}
.cfg-code{background:rgba(10,18,36,.06);border:1px solid var(--border);border-radius:var(--radius-sm);padding:11px 13px;font-family:'Inter',monospace;font-size:10px;color:var(--wp-blue);word-break:break-all;line-height:1.7;max-height:80px;overflow-y:auto;margin-bottom:10px}
[data-theme="dark"] .cfg-code{background:rgba(0,0,0,.3);color:#818cf8}
.cfg-card-actions{display:flex;gap:6px;flex-wrap:wrap;padding:0 18px 14px}

/* ============ LOG TIMELINE ============ */
.log-list{display:flex;flex-direction:column}
.log-row{display:flex;gap:12px;padding:12px 0;border-bottom:1px solid var(--border)}
.log-row:last-child{border-bottom:none}
.log-icon-s{width:34px;height:34px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0}
.log-icon-s.info{background:rgba(99,102,241,.1);color:var(--wp-blue)}
.log-icon-s.ok{background:rgba(22,163,74,.1);color:var(--success)}
.log-icon-s.warn{background:rgba(245,158,11,.1);color:var(--warning)}
.log-icon-s.err{background:rgba(239,68,68,.1);color:var(--wp-red)}
.log-content{flex:1;min-width:0}
.log-msg{font-size:12.5px;color:var(--text-primary);line-height:1.6}
.log-time{font-size:9.5px;color:var(--text-secondary);margin-top:3px;display:flex;align-items:center;gap:5px}

/* ============ TOAST ============ */
.toast{position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--surface-glass);backdrop-filter:blur(24px) saturate(180%);border:1px solid var(--border);color:var(--text-primary);border-radius:var(--radius);padding:12px 22px;font-size:12.5px;font-weight:500;opacity:0;transition:all .4s cubic-bezier(.4,0,.2,1);z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:0 12px 40px rgba(99,102,241,.1),var(--shadow-lg);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(22,163,74,.3);background:rgba(22,163,74,.08);color:var(--success);box-shadow:0 12px 40px rgba(22,163,74,.1)}
.toast.err{border-color:rgba(239,68,68,.3);background:rgba(239,68,68,.06);color:var(--wp-red);box-shadow:0 12px 40px rgba(239,68,68,.1)}

/* ============ EMPTY STATE ============ */
.empty-state{text-align:center;padding:60px 20px;color:var(--text-secondary)}
.empty-state i{font-size:44px;opacity:.3;display:block;margin-bottom:14px}
.empty-state p{font-size:13px}

/* ============ TRAFFIC CHART ============ */
.chart-card{background:var(--surface-glass);backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius-lg);padding:20px 22px;margin-bottom:20px;box-shadow:var(--shadow-sm);position:relative;overflow:hidden}
.chart-card::before{content:'';position:absolute;top:0;left:0;right:0;height:4px;background:var(--gradient-accent)}
.chart-title{font-size:14px;font-weight:800;color:var(--text-primary);margin-bottom:16px;display:flex;align-items:center;gap:8px}
.chart-title i{color:var(--wp-blue)}
.chart-canvas-wrap{position:relative;height:300px}

/* ============ RESPONSIVE ============ */
@media(max-width:1100px){
  .stats-grid{grid-template-columns:repeat(2,1fr)}
  .server-bars{grid-template-columns:repeat(2,1fr)}
}
@media(max-width:860px){
  .sidebar{transform:translateX(100%)}
  .sidebar.open{transform:translateX(0);box-shadow:-10px 0 40px rgba(0,0,0,.3)}
  .main{margin-right:0;padding-top:72px}
  .mobile-top{display:flex}
  .quick-actions{grid-template-columns:repeat(2,1fr)}
  .stats-grid{grid-template-columns:1fr 1fr}
}
@media(max-width:520px){
  .stats-grid{grid-template-columns:1fr}
  .quick-actions{grid-template-columns:1fr}
  .main{padding:62px 12px 40px}
  .server-bars{grid-template-columns:1fr}
  .cfg-grid{grid-template-columns:1fr}
  .form-row{flex-direction:column}
}
</style>
</head>
<body data-theme="light">
<div class="bg-particles">
  <div class="bg-p" style="width:4px;height:4px;background:var(--wp-blue);top:10%;left:20%;animation-duration:18s"></div>
  <div class="bg-p" style="width:3px;height:3px;background:var(--wp-purple);top:70%;left:40%;animation-duration:22s;animation-delay:-6s"></div>
  <div class="bg-p" style="width:5px;height:5px;background:var(--wp-purple);top:40%;left:70%;animation-duration:16s;animation-delay:-10s;opacity:.3"></div>
  <div class="bg-p" style="width:3px;height:3px;background:var(--wp-blue);top:80%;left:15%;animation-duration:20s;animation-delay:-3s"></div>
  <div class="bg-p" style="width:4px;height:4px;background:var(--wp-purple);top:25%;left:55%;animation-duration:19s;animation-delay:-8s"></div>
</div>
<div class="toast" id="toast"></div>
<div class="overlay" id="overlay"></div>

<!-- MODALS -->
<div class="modal-overlay" id="modal-create-user">
  <div class="modal-card">
    <div class="modal-head">
      <div class="modal-title"><i class="ti ti-user-plus"></i> ایجاد کاربر جدید</div>
      <button class="modal-close" onclick="closeModal('modal-create-user')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <form id="create-user-form">
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-user"></i> نام کاربری</label><input class="form-input" id="cu-username" placeholder="username" required></div>
          <div class="form-field"><label><i class="ti ti-lock"></i> رمز عبور</label><input class="form-input" id="cu-password" type="password" placeholder="••••" required></div>
        </div>
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-plug-connected"></i> پروتکل</label><select class="form-select" id="cu-protocol"><option value="vless">VLESS</option><option value="vmess">VMess</option><option value="trojan">Trojan</option><option value="shadowsocks">Shadowsocks</option><option value="wireguard">WireGuard</option></select></div>
          <div class="form-field"><label><i class="ti ti-server"></i> سرور</label><select class="form-select" id="cu-server"><option value="">انتخاب سرور...</option></select></div>
        </div>
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-gauge"></i> محدودیت ترافیک</label><input class="form-input" id="cu-traffic" type="number" min="0" step="0.1" placeholder="مقدار"></div>
          <div class="form-field"><label>واحد</label><select class="form-select" id="cu-traffic-unit"><option value="GB">GB</option><option value="MB">MB</option><option value="TB">TB</option><option value="unlimited">نامحدود</option></select></div>
        </div>
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-calendar"></i> روزهای انقضا</label><input class="form-input" id="cu-expire" type="number" min="0" placeholder="0 = نامحدود"></div>
          <div class="form-field"><label><i class="ti ti-users"></i> اتصال همزمان</label><input class="form-input" id="cu-concurrent" type="number" min="1" value="1"></div>
        </div>
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-route"></i> اینباند</label><select class="form-select" id="cu-inbound"><option value="">انتخاب اینباند...</option></select></div>
          <div class="form-field" id="cu-worker-country-wrap" style="display:none"><label><i class="ti ti-map-pin"></i> کشور ورکر</label><select class="form-select" id="cu-worker-country"><option value="">انتخاب کشور...</option></select></div>
        </div>
        <div class="form-field"><label><i class="ti ti-notes"></i> یادداشت</label><textarea class="form-textarea" id="cu-notes" placeholder="یادداشت اختیاری..."></textarea></div>
        <div class="toggle-wrap">
          <button type="button" class="toggle-switch on" id="cu-active-toggle" onclick="this.classList.toggle('on')"></button>
          <span class="toggle-label">فعال</span>
        </div>
      </form>
    </div>
    <div class="modal-footer">
      <button class="btn btn-ghost" onclick="closeModal('modal-create-user')">انصراف</button>
      <button class="btn btn-primary" onclick="createUser()"><i class="ti ti-user-plus"></i> ایجاد کاربر</button>
    </div>
  </div>
</div>

<div class="modal-overlay" id="modal-config">
  <div class="modal-card" style="max-width:460px">
    <div class="modal-head">
      <div class="modal-title"><i class="ti ti-link"></i> کانفیگ</div>
      <button class="modal-close" onclick="closeModal('modal-config')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <div class="cfg-code" style="max-height:none;font-size:11px" id="config-text"></div>
      <div style="margin-top:14px;display:flex;gap:8px">
        <button class="btn btn-primary" onclick="copyConfigText()"><i class="ti ti-copy"></i> کپی</button>
        <button class="btn btn-ghost" onclick="showQRCode()"><i class="ti ti-qrcode"></i> QR Code</button>
      </div>
      <div id="config-qr" style="margin-top:14px;text-align:center;display:none">
        <img id="config-qr-img" src="" alt="QR" style="max-width:200px;border-radius:12px;background:#fff;padding:8px">
      </div>
    </div>
  </div>
</div>

<!-- MOBILE TOP -->
<div class="mobile-top">
  <div class="mobile-brand">
    <svg width="28" height="28" viewBox="0 0 100 100"><defs><linearGradient id="mg1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#6366f1"/><stop offset="50%" style="stop-color:#8b5cf6"/><stop offset="100%" style="stop-color:#a78bfa"/></linearGradient></defs><path d="M50 5 L90 22 L90 55 C90 78 72 93 50 98 C28 93 10 78 10 55 L10 22 Z" fill="url(#mg1)" opacity="0.95"/><path d="M50 18 L75 30 L75 54 C75 70 63 80 50 85 C37 80 25 70 25 54 L25 30 Z" fill="rgba(255,255,255,0.12)"/><rect x="43" y="38" width="14" height="22" rx="2" fill="rgba(255,255,255,0.9)"/><circle cx="50" cy="33" r="5" fill="rgba(255,255,255,0.9)"/></svg>
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
    <svg width="36" height="36" viewBox="0 0 100 100"><defs><linearGradient id="sg1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#6366f1"/><stop offset="50%" style="stop-color:#8b5cf6"/><stop offset="100%" style="stop-color:#a78bfa"/></linearGradient></defs><path d="M50 5 L90 22 L90 55 C90 78 72 93 50 98 C28 93 10 78 10 55 L10 22 Z" fill="url(#sg1)" opacity="0.95"/><path d="M50 18 L75 30 L75 54 C75 70 63 80 50 85 C37 80 25 70 25 54 L25 30 Z" fill="rgba(255,255,255,0.12)"/><rect x="43" y="38" width="14" height="22" rx="2" fill="rgba(255,255,255,0.9)"/><circle cx="50" cy="33" r="5" fill="rgba(255,255,255,0.9)"/></svg>
    <div><div class="sidebar-logo-text">White Panel</div><div class="sidebar-logo-sub">White Panel</div></div>
  </div>
  <div class="sidebar-nav">
    <div class="nav-section">منوی اصلی</div>
    <div class="nav-item active" data-page="dash"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
    <div class="nav-item" data-page="users"><i class="ti ti-users"></i> کاربران <span class="nav-badge" id="users-count">0</span></div>
    <div class="nav-item" data-page="configs"><i class="ti ti-link-plus"></i> کانفیگ‌ها <span class="nav-badge" id="configs-count">0</span></div>
    <div class="nav-item" data-page="servers"><i class="ti ti-server-2"></i> سرورها</div>
    <div class="nav-item" data-page="plans"><i class="ti ti-receipt-2"></i> پلن‌ها</div>
    <div class="nav-item" data-page="groups"><i class="ti ti-folders"></i> گروه‌ها</div>
    <div class="nav-item" data-page="traffic"><i class="ti ti-chart-area"></i> ترافیک</div>
    <div class="nav-item" data-page="logs"><i class="ti ti-history"></i> لاگ‌ها</div>
    <div class="nav-section">سیستم</div>
    <div class="nav-item" data-page="worker"><i class="ti ti-cloud"></i> Cloudflare Worker</div>
    <div class="nav-item" data-page="api"><i class="ti ti-api"></i> API</div>
    <div class="nav-item" data-page="tools"><i class="ti ti-tools"></i> ابزارها</div>
    <div class="nav-item" data-page="settings"><i class="ti ti-settings"></i> تنظیمات</div>
    <div class="nav-item" data-page="logout" style="color:var(--wp-red)"><i class="ti ti-logout"></i> خروج</div>
  </div>
  <div class="sidebar-footer">
    <div class="sidebar-user">
      <div class="sidebar-avatar"><i class="ti ti-user"></i></div>
      <div><div class="sidebar-user-name">ادمین</div><div class="sidebar-user-role">مدیر سیستم</div></div>
    </div>
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-moon" id="theme-icon"></i> <span id="theme-label">تم تاریک</span></button>
    <button class="logout-btn" onclick="doLogout()"><i class="ti ti-logout"></i> خروج از حساب</button>
  </div>
</aside>

<!-- MAIN CONTENT -->
<main class="main">
  <!-- DASHBOARD PAGE -->
  <section class="page active" id="page-dash">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-layout-dashboard"></i> داشبورد</div><div class="topbar-sub" id="last-updated">در حال بارگذاری...</div></div>
      <div class="topbar-right">
        <span class="welcome-text">سلام ادمین <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 11a2 2 0 0 0 0-4H7.5a2.5 2.5 0 0 1 0-5h.5a3.5 3.5 0 1 1 0 7"/><path d="M22 9a6 6 0 0 1-6 6"/></svg></span>
        <button class="bell-btn" title="اعلان‌ها"><i class="ti ti-bell"></i></button>
        <button class="btn btn-primary" onclick="openModal('modal-create-user')"><i class="ti ti-user-plus"></i> ایجاد کاربر جدید</button>
      </div>
    </div>
    <div class="stats-grid">
      <div class="stat-card"><div class="stat-icon blue"><i class="ti ti-users"></i></div><div class="stat-label">کاربران فعال</div><div class="stat-value" id="s-active-users">—</div><div class="stat-sub up" id="s-users-trend"><i class="ti ti-trending-up"></i> —</div></div>
      <div class="stat-card"><div class="stat-icon green"><i class="ti ti-link"></i></div><div class="stat-label">کانفیگ‌های فعال</div><div class="stat-value" id="s-active-configs">—</div></div>
      <div class="stat-card"><div class="stat-icon purple"><i class="ti ti-transfer"></i></div><div class="stat-label">مصرف ترافیک</div><div class="stat-value" id="s-traffic">—<span style="font-size:14px;font-weight:500;color:var(--text-secondary)">GB</span></div></div>
      <div class="stat-card"><div class="stat-icon green"><i class="ti ti-server-2"></i></div><div class="stat-label">سرورهای آنلاین</div><div class="stat-value" id="s-online-servers">—</div><div class="stat-sub"><span class="dot dot-green pulse"></span> آنلاین</div></div>
    </div>
    <div class="quick-actions">
      <button class="qa-btn" onclick="openModal('modal-create-user')"><i class="ti ti-user-plus"></i> افزودن کاربر</button>
      <button class="qa-btn" onclick="switchPage('configs')"><i class="ti ti-link-plus"></i> ساخت کانفیگ</button>
      <button class="qa-btn" onclick="switchPage('traffic')"><i class="ti ti-chart-bar"></i> گزارش ترافیک</button>
      <button class="qa-btn"><i class="ti ti-database"></i> بکاپ</button>
    </div>
    <div class="server-panel">
      <div class="server-title"><i class="ti ti-activity"></i> وضعیت سرور</div>
      <div class="server-bars">
        <div class="srv-bar-item"><div class="srv-bar-label"><span class="srv-bar-name">CPU</span><span class="srv-bar-pct" id="srv-cpu">—%</span></div><div class="srv-bar-track"><div class="srv-bar-fill blue" id="srv-cpu-bar" style="width:0%"></div></div></div>
        <div class="srv-bar-item"><div class="srv-bar-label"><span class="srv-bar-name">RAM</span><span class="srv-bar-pct" id="srv-ram">—%</span></div><div class="srv-bar-track"><div class="srv-bar-fill purple" id="srv-ram-bar" style="width:0%"></div></div></div>
        <div class="srv-bar-item"><div class="srv-bar-label"><span class="srv-bar-name">Disk</span><span class="srv-bar-pct" id="srv-disk">—%</span></div><div class="srv-bar-track"><div class="srv-bar-fill amber" id="srv-disk-bar" style="width:0%"></div></div></div>
        <div class="srv-bar-item"><div class="srv-bar-label"><span class="srv-bar-name">Network</span><span class="srv-bar-pct" id="srv-net">— MB/s</span></div><div class="srv-bar-track"><div class="srv-bar-fill green" id="srv-net-bar" style="width:0%"></div></div></div>
      </div>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>نام کاربری</th><th>پروتکل</th><th>مصرف</th><th>انقضا</th><th>وضعیت</th><th>عملیات</th></tr></thead>
        <tbody id="dash-users-table"><tr><td colspan="6" style="text-align:center;padding:30px;color:var(--text-secondary)">در حال بارگذاری...</td></tr></tbody>
      </table>
    </div>
  </section>

  <!-- USERS PAGE -->
  <section class="page" id="page-users">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-users"></i> کاربران</div><div class="topbar-sub">مدیریت کاربران و کانفیگ‌ها</div></div>
      <div class="topbar-right">
        <button class="btn btn-primary" onclick="openModal('modal-create-user')"><i class="ti ti-user-plus"></i> ایجاد کاربر جدید</button>
      </div>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>نام کاربری</th><th>پروتکل</th><th>مصرف</th><th>انقضا</th><th>وضعیت</th><th>عملیات</th></tr></thead>
        <tbody id="users-table"><tr><td colspan="6" style="text-align:center;padding:30px;color:var(--text-secondary)">در حال بارگذاری...</td></tr></tbody>
      </table>
    </div>
  </section>

  <!-- CONFIGS PAGE -->
  <section class="page" id="page-configs">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div><div class="topbar-sub">مدیریت کانفیگ‌های کاربران</div></div>
      <div class="topbar-right"><span class="badge badge-blue" id="cfg-total">۰ کانفیگ</span></div>
    </div>
    <div class="cfg-grid" id="configs-grid"></div>
    <div class="empty-state" id="configs-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
  </section>

  <!-- TRAFFIC PAGE -->
  <section class="page" id="page-traffic">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-chart-area"></i> ترافیک</div><div class="topbar-sub">آمار مصرف پهنای باند</div></div>
      <div class="topbar-right"><button class="btn btn-ghost" onclick="refreshAll()"><i class="ti ti-refresh"></i> بروزرسانی</button></div>
    </div>
    <div class="chart-card">
      <div class="chart-title"><i class="ti ti-activity"></i> روند مصرف ترافیک (MB)</div>
      <div class="chart-canvas-wrap"><canvas id="traffic-chart"></canvas></div>
    </div>
    <div class="stats-grid" style="grid-template-columns:repeat(3,1fr)">
      <div class="stat-card"><div class="stat-icon blue"><i class="ti ti-arrow-up-right"></i></div><div class="stat-label">میانگین ساعتی</div><div class="stat-value" id="t-avg" style="font-size:20px">—</div></div>
      <div class="stat-card"><div class="stat-icon purple"><i class="ti ti-chart-bar"></i></div><div class="stat-label">پیک مصرف</div><div class="stat-value" id="t-peak" style="font-size:20px">—</div></div>
      <div class="stat-card"><div class="stat-icon green"><i class="ti ti-database"></i></div><div class="stat-label">کل مصرف</div><div class="stat-value" id="t-total" style="font-size:20px">—</div></div>
    </div>
  </section>

  <!-- LOGS PAGE -->
  <section class="page" id="page-logs">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-history"></i> لاگ‌ها</div><div class="topbar-sub">تاریخچه فعالیت‌های سیستم</div></div>
      <div class="topbar-right"><button class="btn btn-ghost" onclick="loadLogs()"><i class="ti ti-refresh"></i> بروزرسانی</button></div>
    </div>
    <div class="table-wrap">
      <div class="log-list" id="logs-list"><div class="empty-state"><i class="ti ti-history-toggle"></i><p>در حال بارگذاری...</p></div></div>
    </div>
  </section>

  <!-- SERVERS PAGE -->
  <section class="page" id="page-servers">
    <div class="topbar"><div><div class="topbar-title"><i class="ti ti-server-2"></i> سرورها</div></div></div>
    <div class="empty-state"><i class="ti ti-server-off"></i><p>بخش مدیریت سرورها</p></div>
  </section>

  <!-- PLANS PAGE -->
  <section class="page" id="page-plans">
    <div class="topbar"><div><div class="topbar-title"><i class="ti ti-receipt-2"></i> پلن‌ها</div></div></div>
    <div class="empty-state"><i class="ti ti-package-off"></i><p>بخش مدیریت پلن‌ها</p></div>
  </section>

  <!-- GROUPS PAGE -->
  <section class="page" id="page-groups">
    <div class="topbar"><div><div class="topbar-title"><i class="ti ti-folders"></i> گروه‌ها</div></div></div>
    <div class="empty-state"><i class="ti ti-folders-off"></i><p>بخش مدیریت گروه‌ها</p></div>
  </section>

  <!-- SETTINGS PAGE -->
  <section class="page" id="page-settings">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-settings"></i> تنظیمات</div><div class="topbar-sub">تنظیمات عمومی پنل</div></div>
      <div class="topbar-right"><button class="btn btn-primary" onclick="saveSettings()"><i class="ti ti-device-floppy"></i> ذخیره تغییرات</button></div>
    </div>

    <div class="table-wrap" style="margin-bottom:18px">
      <div style="padding:18px 22px;border-bottom:1px solid var(--border)">
        <div class="server-title" style="margin-bottom:0"><i class="ti ti-world"></i> دامنه و شبکه</div>
      </div>
      <div style="padding:18px 22px">
        <div class="form-field">
          <label><i class="ti ti-world-www"></i> دامنه اصلی</label>
          <input class="form-input" id="set-domain" placeholder="example.com" dir="ltr">
        </div>
        <div class="form-row">
          <div class="form-field">
            <label><i class="ti ti-route"></i> نوع انتقال پیش‌فرض</label>
            <select class="form-select" id="set-transport">
              <option value="ws">WebSocket (WS)</option>
              <option value="xhttp">XHTTP</option>
              <option value="tcp">TCP</option>
            </select>
          </div>
          <div class="form-field">
            <label><i class="ti ti-plug-connected"></i> مد اتصال پیش‌فرض</label>
            <select class="form-select" id="set-conn-mode">
              <option value="ws">WebSocket</option>
              <option value="xhttp">XHTTP</option>
              <option value="tcp">TCP</option>
            </select>
          </div>
        </div>
      </div>
    </div>

    <div class="table-wrap" style="margin-bottom:18px">
      <div style="padding:18px 22px;border-bottom:1px solid var(--border)">
        <div class="server-title" style="margin-bottom:0"><i class="ti ti-toggle-right"></i> پروتکل‌ها و مدها</div>
      </div>
      <div style="padding:18px 22px">
        <div class="form-row" style="margin-bottom:12px">
          <div class="form-field">
            <label><i class="ti ti-protocol"></i> پروتکل‌های فعال</label>
            <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:6px">
              <label style="display:flex;align-items:center;gap:5px;font-size:12px;cursor:pointer;padding:6px 12px;background:rgba(43,127,255,.06);border-radius:8px;border:1px solid var(--border)"><input type="checkbox" id="set-proto-vless" checked onchange="updateProtoCheckboxes()"> VLESS</label>
              <label style="display:flex;align-items:center;gap:5px;font-size:12px;cursor:pointer;padding:6px 12px;background:rgba(123,97,255,.06);border-radius:8px;border:1px solid var(--border)"><input type="checkbox" id="set-proto-vmess" onchange="updateProtoCheckboxes()"> VMess</label>
              <label style="display:flex;align-items:center;gap:5px;font-size:12px;cursor:pointer;padding:6px 12px;background:rgba(255,35,82,.06);border-radius:8px;border:1px solid var(--border)"><input type="checkbox" id="set-proto-trojan" onchange="updateProtoCheckboxes()"> Trojan</label>
              <label style="display:flex;align-items:center;gap:5px;font-size:12px;cursor:pointer;padding:6px 12px;background:rgba(245,158,11,.06);border-radius:8px;border:1px solid var(--border)"><input type="checkbox" id="set-proto-reality" onchange="updateProtoCheckboxes()"> Reality</label>
            </div>
          </div>
        </div>
        <div class="toggle-wrap" style="margin-bottom:10px">
          <button type="button" class="toggle-switch on" id="set-ws-mode" onclick="this.classList.toggle('on')"></button>
          <span class="toggle-label">WebSocket Mode</span>
        </div>
        <div class="toggle-wrap">
          <button type="button" class="toggle-switch on" id="set-xhttp-mode" onclick="this.classList.toggle('on')"></button>
          <span class="toggle-label">XHTTP Mode</span>
        </div>
      </div>
    </div>

    <div class="table-wrap" style="margin-bottom:18px">
      <div style="padding:18px 22px;border-bottom:1px solid var(--border)">
        <div class="server-title" style="margin-bottom:0"><i class="ti ti-shield-lock"></i> تنظیمات Reality</div>
      </div>
      <div style="padding:18px 22px">
        <div class="form-row">
          <div class="form-field">
            <label><i class="ti ti-plug"></i> پورت Reality</label>
            <input class="form-input" id="set-real-port" type="number" placeholder="1234">
          </div>
          <div class="form-field">
            <label><i class="ti ti-globe"></i> Destination (dest)</label>
            <input class="form-input" id="set-real-dest" placeholder="google.com:443" dir="ltr">
          </div>
        </div>
        <div class="form-row">
          <div class="form-field">
            <label><i class="ti ti-key"></i> Public Key</label>
            <input class="form-input" id="set-real-pbk" placeholder="x25519 public key" dir="ltr">
          </div>
          <div class="form-field">
            <label><i class="ti ti-hash"></i> Short ID</label>
            <input class="form-input" id="set-real-sid" placeholder="6ba85179e30d4fc2" dir="ltr">
          </div>
        </div>
        <div class="form-row">
          <div class="form-field">
            <label><i class="ti ti-link"></i> KMX Path</label>
            <input class="form-input" id="set-real-spx" placeholder="/" dir="ltr">
          </div>
          <div class="form-field">
            <label><i class="ti ti-globe"></i> SNI (Reality)</label>
            <input class="form-input" id="set-real-sni" placeholder="www.google.com" dir="ltr">
          </div>
        </div>
        <div class="form-row">
          <div class="form-field">
            <label><i class="ti ti-world"></i> دامنه خارجی</label>
            <input class="form-input" id="set-real-ext-domain" placeholder="ext.example.com" dir="ltr">
          </div>
          <div class="form-field">
            <label><i class="ti ti-plug"></i> پورت خارجی</label>
            <input class="form-input" id="set-real-ext-port" type="number" placeholder="443">
          </div>
        </div>
        <div style="margin-top:12px;display:flex;gap:8px">
          <button class="btn btn-ghost" onclick="generateRealityKeys()"><i class="ti ti-key"></i> تولید کلید Reality</button>
          <button class="btn btn-ghost" onclick="saveRealitySettings()"><i class="ti ti-device-floppy"></i> ذخیره Reality</button>
        </div>
      </div>
    </div>

    <!-- Custom Sub Pages -->
    <div class="table-wrap" style="margin-bottom:18px">
      <div style="padding:18px 22px;border-bottom:1px solid var(--border)">
        <div class="server-title" style="margin-bottom:0"><i class="ti ti-layout"></i> صفحات سفارشی ساب</div>
      </div>
      <div style="padding:18px 22px">
        <div class="form-field">
          <label><i class="ti ti-checkup"></i> صفحه ساب پیش‌فرض</label>
          <div class="custom-sub-dropdown-wrap" style="margin-top:8px" id="custom-sub-dropdown-wrap">
            <div class="custom-sub-dropdown" id="custom-sub-dropdown" onclick="toggleCustomSubMenu()">
              <span id="custom-sub-selected-label">انتخاب صفحه...</span>
              <i class="ti ti-chevron-down" id="custom-sub-chevron"></i>
              <input type="hidden" id="set-custom-sub-default" value="">
            </div>
            <div class="custom-sub-dropdown-menu" id="custom-sub-dropdown-menu">
              <!-- Options populated dynamically -->
            </div>
            <input type="hidden" id="set-custom-sub-options" value="">
          </div>
          <div style="margin-top:10px;color:var(--text-secondary);font-size:12px">
            <i class="ti ti-info-circle"></i> این صفحه برای لینک <code>/sub/{username}</code> سرو می‌شود.
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- WORKER PAGE -->
  <section class="page" id="page-worker">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-cloud"></i> Cloudflare Worker</div><div class="topbar-sub">تنظیم و مدیریت Worker برای پروکسی‌های توزیع‌شده</div></div>
      <div class="topbar-right"><button class="btn btn-primary" id="worker-sync-btn" onclick="syncWorkerProxies()"><i class="ti ti-refresh-cw"></i> همگام‌سازی پروکسی‌ها</button></div>
    </div>
    <div class="table-wrap" style="margin-bottom:18px">
      <div style="padding:18px 22px;border-bottom:1px solid var(--border)">
        <div class="server-title" style="margin-bottom:0"><i class="ti ti-link"></i> اتصال Cloudflare</div>
      </div>
      <div style="padding:18px 22px" id="worker-connect-form">
        <div class="form-row">
          <div class="form-field">
            <label><i class="ti ti-key"></i> توکن API Cloudflare</label>
            <input class="form-input" id="worker-token" type="password" placeholder="توکن API (Bearer یا Global Key)" dir="ltr">
          </div>
          <div class="form-field">
            <label><i class="ti ti-at"></i> ایمیل (برای Global Key)</label>
            <input class="form-input" id="worker-email" type="email" placeholder="email@example.com" dir="ltr">
          </div>
        </div>
        <div class="form-row">
          <div class="form-field">
            <label><i class="ti ti-database"></i> Account ID</label>
            <input class="form-input" id="worker-account-id" placeholder="Account ID از داشبورد Cloudflare" dir="ltr">
          </div>
          <div class="form-field">
            <label><i class="ti ti-brand-cloudflare"></i> نام Worker (اختیاری)</label>
            <input class="form-input" id="worker-name" value="white-proxy" placeholder="white-proxy" dir="ltr">
          </div>
        </div>
        <div style="margin-top:12px;display:flex;gap:8px">
          <button class="btn btn-primary" onclick="connectWorker()"><i class="ti ti-cloud-plus"></i> اتصال و دیپلوی</button>
          <button class="btn btn-ghost" id="worker-disconnect-btn" onclick="disconnectWorker()" style="display:none"><i class="ti ti-cloud-minus"></i> قطع اتصال</button>
        </div>
      </div>
      <div style="padding:18px 22px;display:none" id="worker-connected-info">
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-link"></i> دامنه Worker</label><input class="form-input" id="worker-domain-display" readonly dir="ltr"></div>
          <div class="form-field"><label><i class="ti ti-database"></i> Account ID</label><input class="form-input" id="worker-account-display" readonly dir="ltr"></div>
        </div>
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-tag"></i> نام Worker</label><input class="form-input" id="worker-name-display" readonly dir="ltr"></div>
          <div class="form-field"><label><i class="ti ti-key"></i> توکن کنترل</label><input class="form-input" id="worker-control-token-display" readonly dir="ltr" style="font-family:monospace;font-size:12px"></div>
        </div>
        <div style="margin-top:12px;display:flex;gap:8px">
          <button class="btn btn-primary" onclick="syncWorkerProxies()"><i class="ti ti-refresh-cw"></i> همگام‌سازی پروکسی‌ها</button>
          <button class="btn btn-ghost" onclick="deployWorker()"><i class="ti ti-upload"></i> دیپلوی مجدد</button>
          <button class="btn btn-danger" onclick="disconnectWorker()"><i class="ti ti-cloud-minus"></i> قطع اتصال</button>
        </div>
        <div class="form-row" style="margin-top:12px">
          <div class="form-field">
            <label><i class="ti ti-globe"></i> منبع پروکسی روزانه (ProxyIP-Daily.md)</label>
            <input class="form-input" id="worker-source-url" placeholder="https://raw.githubusercontent.com/NiREvil/vless/main/sub/ProxyIP-Daily.md" dir="ltr">
          </div>
          <div class="form-field">
            <label>
              <button type="button" class="toggle-switch on" id="worker-auto-sync" onclick="this.classList.toggle('on')"></button>
              <span class="toggle-label">همگام‌سازی خودکار هر ساعت</span>
            </label>
          </div>
        </div>
        <div style="margin-top:12px;display:flex;gap:8px">
          <button class="btn btn-ghost" onclick="saveWorkerSettings()"><i class="ti ti-device-floppy"></i> ذخیره تنظیمات</button>
        </div>
      </div>
    </div>
    <div class="table-wrap" style="margin-bottom:18px" id="worker-proxies-section" style="display:none">
      <div style="padding:18px 22px;border-bottom:1px solid var(--border)">
        <div class="server-title" style="margin-bottom:0"><i class="ti ti-map-pin"></i> موقعیت‌های پروکسی (کشورها)</div>
      </div>
      <div style="padding:18px 22px">
        <div class="table-wrap">
          <table>
            <thead><tr><th>پرچم</th><th>کشور</th><th>کد</th><th>پروکسی اصلی</th><th>پورت</th><th>تعداد پروکسی‌ها</th><th>عملیات</th></tr></thead>
            <tbody id="worker-proxies-table"><tr><td colspan="7" style="text-align:center;padding:30px;color:var(--text-secondary)">در حال بارگذاری...</td></tr></tbody>
          </table>
        </div>
        <div style="margin-top:12px;display:flex;gap:8px">
          <button class="btn btn-primary" onclick="openAddProxyModal()"><i class="ti ti-plus"></i> افزودن کشور/پروکسی</button>
        </div>
      </div>
    </div>
    <div class="table-wrap" id="worker-last-sync" style="display:none">
      <div style="padding:18px 22px;border-bottom:1px solid var(--border)">
        <div class="server-title" style="margin-bottom:0"><i class="ti ti-clock"></i> آخرین همگام‌سازی</div>
      </div>
      <div style="padding:18px 22px">
        <div id="worker-last-sync-info"></div>
      </div>
    </div>
  </section>
</main>

<script>
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
  if(tl)tl.textContent=dark?'تم روشن':'تم تاریک';
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
function toFa(n){return String(n).replace(/\d/g,function(d){return'۰۱۲۳۴۵۶۷۸۹'[d]})}

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

    // Populate inbounds dropdown
    inboundSelect.innerHTML = '<option value="">انتخاب اینباند...</option>' +
      inbounds.map(function(ib){
        return '<option value="'+esc(ib.inbound_id)+'">'+esc(ib.name)+' ('+esc(ib.protocol)+' '+esc(ib.network)+')</option>';
      }).join('');

    // Handle inbound change
    inboundSelect.onchange = function(){
      var selectedId = this.value;
      var selectedInbound = inbounds.find(function(ib){ return ib.inbound_id === selectedId; });
      if(selectedInbound && selectedInbound.protocol === 'worker'){
        // Fetch worker inbounds with countries
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
      workerCountrySelect.innerHTML = '<option value="">انتخاب کشور...</option>' +
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
  // If worker inbound is selected, add proxy_countries
  var workerCountryWrap = document.getElementById('cu-worker-country-wrap');
  if(workerCountryWrap && workerCountryWrap.style.display !== 'none'){
    var proxyCountry = document.getElementById('cu-worker-country').value;
    if(proxyCountry){
      body.proxy_countries = [proxyCountry.toLowerCase()];
    }
  }
  if(!body.label){toast('نام کاربری الزامی است','err');return}
  try{
    var r=await authFetch('/api/users',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok){var d=await r.json().catch(function(){return{}});throw new Error(d.detail||'خطا')}
    toast('کاربر با موفقیت ایجاد شد ✓','ok');
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
  if(!links.length){tbody.innerHTML='<tr><td colspan="6"><div class="empty-state"><i class="ti ti-users-off"></i><p>کاربری وجود ندارد</p></div></td></tr>';return}
  tbody.innerHTML=links.map(function(l){
    var pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
    var bc=pct>90?'var(--wp-red)':pct>70?'var(--warning)':'var(--wp-blue)';
    var lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);
    var protoClass=l.protocol==='vless'||l.protocol==='vless-ws'?'pb-vless':l.protocol==='vmess'?'pb-vmess':l.protocol==='trojan'?'pb-trojan':l.protocol==='shadowsocks'?'pb-ss':'pb-wg';
    var protoFa=l.protocol==='vless-ws'?'VLESS':l.protocol==='vmess'?'VMess':l.protocol==='trojan'?'Trojan':l.protocol==='shadowsocks'?'Shadowsocks':l.protocol==='wireguard'?'WireGuard':l.protocol||'VLESS';
    var isActive=l.active&&!l.expired;
    var expText=l.expired?'منقضی':l.expires_at?new Date(l.expires_at).toLocaleDateString('fa-IR'):'نامحدود';
    var expCls=l.expired?'exp-bad':l.expires_at?'exp-ok':'exp-ok';
    return '<tr><td style="font-weight:600">'+esc(l.label)+'</td>'+
      '<td><span class="proto-badge '+protoClass+'">'+protoFa+'</span></td>'+
      '<td><div class="usage-bar-wrap"><div class="usage-bar"><div class="usage-fill" style="width:'+pct+'%;background:'+bc+'"></div></div><div class="usage-text"><span>'+fmtB(l.used_bytes)+'</span><span>'+lim+'</span></div></div></td>'+
      '<td><span class="exp-chip '+expCls+'">'+expText+'</span></td>'+
      '<td><div class="status-dot '+(isActive?'active':'expired')+'"><span class="dot '+(isActive?'dot-green':'dot-red')+' '+(isActive?'pulse':'')+'"></span>'+(isActive?'فعال':'غیرفعال')+'</div></td>'+
      '<td><div class="action-btns">'+
        '<button class="btn btn-sm btn-ghost btn-icon" onclick="viewConfig(\''+l.uuid+'\')" title="مشاهده"><i class="ti ti-eye"></i></button>'+
        '<button class="btn btn-sm btn-ghost btn-icon" onclick="copyLink(\''+l.uuid+'\')" title="کپی"><i class="ti ti-copy"></i></button>'+
        '<button class="btn btn-sm btn-ghost btn-icon" onclick="toggleUser(\''+l.uuid+'\')" title="فعال/غیرفعال"><i class="ti ti-toggle-'+(isActive?'right':'left')+'"></i></button>'+
        '<button class="btn btn-sm btn-danger btn-icon" onclick="deleteUser(\''+l.uuid+'\')" title="حذف"><i class="ti ti-trash"></i></button>'+
      '</div></td></tr>';
  }).join('');
}

/* ============ USER ACTIONS ============ */
async function viewConfig(uuid){
  var link=allLinks.find(function(l){return l.uuid===uuid});
  if(!link){toast('کانفیگ یافت نشد','err');return}
  currentConfigText=link.vless_link||'';
  document.getElementById('config-text').textContent=currentConfigText;
  document.getElementById('config-qr').style.display='none';
  openModal('modal-config');
}
function copyConfigText(){
  if(!currentConfigText)return;
  navigator.clipboard.writeText(currentConfigText).then(function(){toast('کانفیگ کپی شد ✓','ok')});
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
  navigator.clipboard.writeText(link.vless_link).then(function(){toast('لینک کپی شد ✓','ok')});
}
async function toggleUser(uuid){
  var link=allLinks.find(function(l){return l.uuid===uuid});
  if(!link)return;
  try{
    var r=await authFetch('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:!link.active})});
    if(!r.ok)throw new Error();
    toast('وضعیت تغییر کرد ✓','ok');loadUsers();loadDashboard();
  }catch(e){toast('خطا در تغییر وضعیت','err')}
}
async function deleteUser(uuid){
  if(!confirm('آیا از حذف این کاربر اطمینان دارید؟'))return;
  try{
    var r=await authFetch('/api/links/'+uuid,{method:'DELETE'});
    if(!r.ok)throw new Error();
    toast('کاربر حذف شد ✓','ok');loadUsers();loadDashboard();loadConfigs();
  }catch(e){toast('خطا در حذف','err')}
}

/* ============ CONFIGS PAGE ============ */
async function loadConfigs(){
  try{
    var r=await authFetch('/api/links'),d=await r.json();
    allLinks=d.links||[];
    document.getElementById('configs-count').textContent=allLinks.length;
    document.getElementById('cfg-total').textContent=toFa(allLinks.length)+' کانفیگ';
    var grid=document.getElementById('configs-grid'),empty=document.getElementById('configs-empty');
    if(!allLinks.length){grid.innerHTML='';empty.style.display='block';return}
    empty.style.display='none';
    grid.innerHTML=allLinks.map(function(l){
      var protoFa=l.protocol==='vless-ws'?'VLESS':l.protocol==='vmess'?'VMess':l.protocol==='trojan'?'Trojan':l.protocol||'VLESS';
      var protoClass=l.protocol==='vless-ws'?'pb-vless':l.protocol==='vmess'?'pb-vmess':l.protocol==='trojan'?'pb-trojan':'pb-vless';
      var isActive=l.active&&!l.expired;
      var pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
      return '<div class="cfg-card-item">'+
        '<div class="cfg-card-top"><span class="cfg-card-label">'+esc(l.label)+'</span><span class="badge '+(isActive?'badge-green':'badge-red')+'"><span class="dot '+(isActive?'dot-green':'dot-red')+' '+(isActive?'pulse':'')+'"></span> '+(isActive?'فعال':'غیرفعال')+'</span></div>'+
        '<div class="cfg-card-body"><span class="proto-badge '+protoClass+'" style="margin-bottom:8px;display:inline-block">'+protoFa+'</span>'+
        '<div class="usage-bar-wrap" style="margin-bottom:8px"><div class="usage-bar"><div class="usage-fill" style="width:'+pct+'%"></div></div><div class="usage-text"><span>'+fmtB(l.used_bytes)+'</span><span>'+(l.limit_bytes===0?'∞':fmtB(l.limit_bytes))+'</span></div></div></div>'+
        '<div class="cfg-card-actions">'+
        '<button class="btn btn-sm btn-ghost" onclick="viewConfig(\''+l.uuid+'\')"><i class="ti ti-eye"></i> مشاهده</button>'+
        '<button class="btn btn-sm btn-ghost" onclick="copyLink(\''+l.uuid+'\')"><i class="ti ti-copy"></i> کپی</button>'+
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
        var grad=ctx.createLinearGradient(0,0,0,300);
        grad.addColorStop(0,'rgba(99,102,241,.45)');grad.addColorStop(1,'rgba(99,102,241,0)');
        trafficChart=new Chart(ctx,{
          type:'line',data:{labels:labels,datasets:[{data:vals,borderColor:'#6366f1',backgroundColor:grad,fill:true,tension:.4,pointRadius:0,borderWidth:2.5}]},
          options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},
            scales:{x:{grid:{display:false},ticks:{font:{size:9}}},y:{grid:{color:'rgba(99,102,241,.05)'},ticks:{font:{size:9},callback:function(v){return v+' MB'}}}},
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
    if(!logs.length){el.innerHTML='<div class="empty-state"><i class="ti ti-history-toggle"></i><p>هنوز لاگی ثبت نشده</p></div>';return}
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
    document.getElementById('s-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span style="font-size:14px;font-weight:500;color:var(--text-secondary)">GB</span>';
    document.getElementById('s-online-servers').textContent='1';
    document.getElementById('s-users-trend').innerHTML='<i class="ti ti-trending-up"></i> '+toFa(d.active_connections||0)+' اتصال';
    document.getElementById('last-updated').textContent='آخرین بروزرسانی: '+new Date().toLocaleTimeString('fa-IR');
    // Server bars (simulated from stats)
    document.getElementById('srv-cpu').textContent='32%';document.getElementById('srv-cpu-bar').style.width='32%';
    document.getElementById('srv-ram').textContent='58%';document.getElementById('srv-ram-bar').style.width='58%';
    document.getElementById('srv-disk').textContent='41%';document.getElementById('srv-disk-bar').style.width='41%';
    document.getElementById('srv-net').textContent='12 MB/s';document.getElementById('srv-net-bar').style.width='24%';
    // Load users table for dashboard
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
    // Reality
    var real=d.reality||{};
    document.getElementById('set-real-port').value=real.port||1234;
    document.getElementById('set-real-dest').value=real.dest||'google.com:443';
    document.getElementById('set-real-pbk').value=real.public_key||'';
    document.getElementById('set-real-sid').value=real.short_id||'6ba85179e30d4fc2';
    document.getElementById('set-real-spx').value=real.kmx||'/';
    document.getElementById('set-real-sni').value=real.sni||d.domain||'';
    document.getElementById('set-real-ext-domain').value=real.external_domain||d.domain||'';
    document.getElementById('set-real-ext-port').value=real.external_port||443;
    // Custom sub default
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
      html+='<div class="custom-sub-option" style="color:var(--text-secondary)">هیچ صفحه‌ای یافت نشد</div>';
    }else{
      html=opts.map(function(o){
        var active=o.file===selected?' active':'';
        return '<div class="custom-sub-option'+active+'" onclick="selectCustomSub(\''+esc(o.file)+'\', \''+esc(o.label)+'\')"><span class="sub-preview"></span>'+esc(o.label||o.file)+'</div>'
      }).join('');
    }
    menu.innerHTML=html;
  }catch(e){console.error(e)}
}
function toggleCustomSubMenu(){
  var wrap=document.getElementById('custom-sub-dropdown-wrap');
  var dd=document.getElementById('custom-sub-dropdown');
  if(wrap.classList.contains('open')){wrap.classList.remove('open')}else{wrap.classList.add('open')}
}
function selectCustomSub(file,label){
  document.getElementById('set-custom-sub-default').value=file;
  var lbl=document.getElementById('custom-sub-selected-label');if(lbl)lbl.textContent=label||file;
  var wrap=document.getElementById('custom-sub-dropdown-wrap');if(wrap)wrap.classList.remove('open');
  document.getElementById('custom-sub-chevron').style.transform='';
}
document.addEventListener('click',function(e){
  var wrap=document.getElementById('custom-sub-dropdown-wrap');
  if(!wrap||!wrap.contains(e.target)){wrap.classList.remove('open');}
});

async function saveSettings(){
  try{
    var protos=[];
    if(document.getElementById('set-proto-vless').checked)protos.push('vless');
    if(document.getElementById('set-proto-vmess').checked)protos.push('vmess');
    if(document.getElementById('set-proto-trojan').checked)protos.push('trojan');
    if(document.getElementById('set-proto-reality').checked)protos.push('reality');
    var body={
      domain:document.getElementById('set-domain').value.trim(),
      default_transport:document.getElementById('set-transport').value,
      default_connection_mode:document.getElementById('set-conn-mode').value,
      enabled_protocols:protos,
      websocket_mode:document.getElementById('set-ws-mode').classList.contains('on'),
      xhttp_mode:document.getElementById('set-xhttp-mode').classList.contains('on'),
      custom_sub_default:document.getElementById('set-custom-sub-default').value.trim()
    };
    var r=await authFetch('/api/tools/settings',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    toast('تنظیمات ذخیره شد ✓','ok');
  }catch(e){toast('خطا در ذخیره تنظیمات','err')}
}

async function saveRealitySettings(){
  try{
    var body={
      port:parseInt(document.getElementById('set-real-port').value)||1234,
      dest:document.getElementById('set-real-dest').value.trim(),
      public_key:document.getElementById('set-real-pbk').value.trim(),
      short_id:document.getElementById('set-real-sid').value.trim(),
      kmx:document.getElementById('set-real-spx').value.trim(),
      sni:document.getElementById('set-real-sni').value.trim(),
      external_domain:document.getElementById('set-real-ext-domain').value.trim(),
      external_port:parseInt(document.getElementById('set-real-ext-port').value)||443
    };
    var r=await authFetch('/api/tools/reality-settings',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    toast('تنظیمات Reality ذخیره شد ✓','ok');
  }catch(e){toast('خطا در ذخیره Reality','err')}
}

async function generateRealityKeys(){
  try{
    var r=await authFetch('/api/tools/generate-reality-keys',{method:'POST'});
    var d=await r.json();
    document.getElementById('set-real-pbk').value=d.public_key||'';
    toast('کلیدهای Reality تولید شد ✓','ok');
  }catch(e){toast('خطا در تولید کلید','err')}
}

function updateProtoCheckboxes(){/* no-op hook for UI */}

/* ============ WORKER PAGE ============ */
async function loadWorker(){
  try{
    var r=await authFetch('/api/worker'),d=await r.json();
    var connectForm=document.getElementById('worker-connect-form');
    var connectedInfo=document.getElementById('worker-connected-info');
    var proxiesSection=document.getElementById('worker-proxies-section');
    var lastSync=document.getElementById('worker-last-sync');
    var syncBtn=document.getElementById('worker-sync-btn');
    var disconnectBtn=document.getElementById('worker-disconnect-btn');

    if(d.connected){
      connectForm.style.display = 'none';
      connectedInfo.style.display = 'block';
      proxiesSection.style.display = 'block';
      lastSync.style.display = 'block';
      if(syncBtn)syncBtn.style.display = 'inline-flex';
      if(disconnectBtn)disconnectBtn.style.display = 'inline-flex';

      document.getElementById('worker-domain-display').value = d.worker_domain || '';
      document.getElementById('worker-account-display').value = d.account_id || '';
      document.getElementById('worker-name-display').value = d.worker_name || '';
      document.getElementById('worker-control-token-display').value = d.control_token || '';
      document.getElementById('worker-source-url').value = d.source_url || 'https://raw.githubusercontent.com/NiREvil/vless/main/sub/ProxyIP-Daily.md';
      document.getElementById('worker-auto-sync').classList.toggle('on', d.auto_sync);

      // Render proxies table
      renderWorkerProxies(d.proxies || []);

      // Last sync info
      if(d.last_sync){
        var ls=document.getElementById('worker-last-sync-info');
        var syncTime = new Date(d.last_sync).toLocaleString('fa-IR');
        var syncCount = d.sync_count || 0;
        var syncError = d.sync_error || '';
        ls.innerHTML = '<div style="font-size:13px;color:var(--text-secondary)">زمان: '+syncTime+'</div>' +
          '<div style="font-size:13px;color:var(--text-secondary);margin-top:4px">تعداد همگام‌سازی‌ها: '+syncCount+'</div>' +
          (syncError ? '<div style="font-size:13px;color:var(--wp-red);margin-top:4px">خطا: '+esc(syncError)+'</div>' : '');
      }
    }else{
      connectForm.style.display = 'block';
      connectedInfo.style.display = 'none';
      proxiesSection.style.display = 'none';
      lastSync.style.display = 'none';
      if(syncBtn)syncBtn.style.display = 'none';
      if(disconnectBtn)disconnectBtn.style.display = 'none';
    }
  }catch(e){console.error(e)}
}

function renderWorkerProxies(proxies){
  var tbody=document.getElementById('worker-proxies-table');
  if(!proxies || !proxies.length){
    tbody.innerHTML = '<tr><td colspan="7" style="text-align:center;padding:30px;color:var(--text-secondary)">کشوری اضافه نشده است</td></tr>';
    return;
  }
  tbody.innerHTML = proxies.map(function(p){
    var flag = p.flag || '';
    var country = p.country || p.code.toUpperCase();
    var code = p.code || '';
    var proxy = p.proxy || '';
    var port = p.port || 443;
    var count = (p.proxies && p.proxies.length) || 1;
    return '<tr>'+
      '<td style="font-size:18px;text-align:center">'+esc(flag)+'</td>'+
      '<td style="font-weight:500">'+esc(country)+'</td>'+
      '<td style="font-family:monospace;font-size:12px">'+esc(code)+'</td>'+
      '<td style="font-family:monospace;font-size:12px">'+esc(proxy)+'</td>'+
      '<td style="text-align:center">'+esc(port)+'</td>'+
      '<td style="text-align:center">'+esc(count)+'</td>'+
      '<td><button class="btn btn-sm btn-ghost btn-icon" onclick="deleteWorkerProxy(\''+esc(code)+'\')" title="حذف"><i class="ti ti-trash"></i></button></td>'+
      '</tr>';
  }).join('');
}

async function connectWorker(){
  var token=document.getElementById('worker-token').value.trim();
  var email=document.getElementById('worker-email').value.trim();
  var account_id=document.getElementById('worker-account-id').value.trim();
  var worker_name=document.getElementById('worker-name').value.trim()||'white-proxy';
  if(!token||!account_id){toast('توکن و Account ID الزامی هستند','err');return}
  try{
    var r=await authFetch('/api/worker/setup',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({token:token,account_id:account_id,email:email,worker_name:worker_name})});
    var d=await r.json();
    if(!d.ok)throw new Error(d.detail||'خطا');
    toast('Worker با موفقیت متصل و دیپلوی شد ✓','ok');
    loadWorker();
  }catch(e){toast(e.message,'err')}
}

async function disconnectWorker(){
  if(!confirm('آیا از قطع اتصال Worker اطمینان دارید؟'))return;
  try{
    var r=await authFetch('/api/worker',{method:'DELETE'});
    var d=await r.json();
    if(!d.ok)throw new Error();
    toast('Worker قطع شد ✓','ok');
    loadWorker();
  }catch(e){toast('خطا در قطع اتصال','err')}
}

async function deployWorker(){
  try{
    var r=await authFetch('/api/worker/sync',{method:'POST'});
    var d=await r.json();
    if(!d.ok)throw new Error(d.error||'deploy failed');
    toast('Worker دیپلوی شد ✓','ok');
    loadWorker();
  }catch(e){toast(e.message,'err')}
}

async function syncWorkerProxies(){
  try{
    var r=await authFetch('/api/worker/sync-source',{method:'POST'});
    var d=await r.json();
    if(!d.ok)throw new Error(d.error||'sync failed');
    toast('پروکسی‌ها همگام‌سازی شدند ✓ ('+d.sync.countries+' کشور)','ok');
    loadWorker();
  }catch(e){toast(e.message,'err')}
}

async function saveWorkerSettings(){
  var source_url=document.getElementById('worker-source-url').value.trim();
  var auto_sync=document.getElementById('worker-auto-sync').classList.contains('on');
  try{
    var r=await authFetch('/api/worker/settings',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({source_url:source_url,auto_sync:auto_sync})});
    var d=await r.json();
    if(!d.ok)throw new Error();
    toast('تنظیمات ذخیره شد ✓','ok');
    loadWorker();
  }catch(e){toast(e.message,'err')}
}

async function deleteWorkerProxy(code){
  if(!confirm('آیا از حذف این کشور اطمینان دارید؟'))return;
  try{
    var r=await authFetch('/api/worker/proxies/'+code,{method:'DELETE'});
    var d=await r.json();
    if(!d.ok)throw new Error();
    toast('کشور حذف شد ✓','ok');
    loadWorker();
  }catch(e){toast(e.message,'err')}
}

async function openAddProxyModal(){
  var code=prompt('کد کشور (مثلاً: de, us, nl):');
  if(!code)return;
  var country=prompt('نام کشور (مثلاً: Germany):');
  if(!country)return;
  var proxy=prompt('آدرس پروکسی (IP یا دامنه):');
  if(!proxy)return;
  var port=prompt('پورت:', '443');
  if(!port)port='443';
  try{
    var r=await authFetch('/api/worker/proxies',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({code:code.trim().toLowerCase(),country:country.trim(),proxy:proxy.trim(),port:parseInt(port)})});
    var d=await r.json();
    if(!d.ok)throw new Error(d.detail||'خطا');
    toast('کشور اضافه شد ✓','ok');
    loadWorker();
  }catch(e){toast(e.message,'err')}
}

/* ============ REFRESH ============ */
function refreshAll(){
  loadDashboard();loadUsers();loadConfigs();loadTraffic();loadLogs();loadWorker();
  toast('بروزرسانی شد ✓','ok');
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
<title>White Panel · اشتراک</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Estedad:wght@300;400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
:root{{
  --wp-blue:#6366f1;--wp-purple:#8b5cf6;--wp-red:#ef4444;
  --success:#16A34A;--warning:#F59E0B;--danger:#DC2626;
  --text-primary:#0F172A;--text-secondary:#475569;
  --bg:#F8FAFC;--surface:rgba(255,255,255,.8);--surface-glass:rgba(255,255,255,.75);
  --border:rgba(226,232,240,.7);
  --radius:18px;--radius-lg:24px;--radius-xl:28px;
  --shadow-sm:0 2px 8px rgba(0,0,0,.04);--shadow-md:0 8px 24px rgba(0,0,0,.06);
  --shadow-lg:0 16px 48px rgba(0,0,0,.08);
}}
[data-theme="dark"]{{
  --text-primary:#F1F5F9;--text-secondary:#94A3B8;
  --bg:#0B1121;--surface:rgba(15,23,42,.85);--surface-glass:rgba(15,23,42,.7);
  --border:rgba(226,232,240,.06);
  --shadow-sm:0 2px 8px rgba(0,0,0,.2);--shadow-md:0 8px 24px rgba(0,0,0,.3);
  --shadow-lg:0 16px 48px rgba(0,0,0,.4);
}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{min-height:100%;background:var(--bg);font-family:'Estedad',sans-serif;color:var(--text-primary);font-size:14px;transition:background .4s,color .4s}}
.bg-glow{{position:fixed;inset:0;z-index:0;pointer-events:none}}
.bg-orb{{position:absolute;border-radius:50%;filter:blur(120px);opacity:.15;animation:float 14s ease-in-out infinite}}
.bg-orb:nth-child(1){{width:450px;height:450px;background:var(--wp-blue);top:-150px;left:-100px}}
.bg-orb:nth-child(2){{width:350px;height:350px;background:var(--wp-purple);bottom:-100px;right:-80px;animation-delay:-7s}}
@keyframes float{{0%,100%{{transform:translateY(0) scale(1)}}50%{{transform:translateY(-25px) scale(1.04)}}}}
.wrap{{position:relative;z-index:10;max-width:680px;margin:0 auto;padding:28px 16px 60px}}
.top-bar{{display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;gap:10px}}
.brand{{display:flex;align-items:center;gap:10px}}
.brand svg{{width:38px;height:38px;filter:drop-shadow(0 3px 8px rgba(43,127,255,.3))}}
.brand-name{{font-size:14px;font-weight:800;color:var(--text-primary)}}
.brand-sub{{font-size:9.5px;color:var(--text-secondary)}}
.theme-toggle{{width:38px;height:38px;border-radius:var(--radius);background:var(--surface);backdrop-filter:blur(12px);border:1px solid var(--border);color:var(--text-secondary);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:16px;transition:all .2s}}
.theme-toggle:hover{{background:rgba(43,127,255,.1);color:var(--wp-blue)}}
/* Info card */
.info-card{{background:var(--surface);backdrop-filter:blur(20px) saturate(160%);-webkit-backdrop-filter:blur(20px) saturate(160%);border:1px solid var(--border);border-radius:var(--radius-xl);padding:28px 26px 24px;margin-bottom:18px;box-shadow:var(--shadow-lg);position:relative;overflow:hidden}}
.info-card::before{{content:'';position:absolute;top:0;right:0;width:180px;height:180px;background:radial-gradient(circle,rgba(123,97,255,.08),transparent 70%);pointer-events:none}}
.info-name{{font-size:22px;font-weight:800;color:var(--text-primary);position:relative;z-index:1;letter-spacing:-.02em}}
.info-desc{{font-size:12.5px;color:var(--text-secondary);margin-top:6px;position:relative;z-index:1;line-height:1.7}}
.info-stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:18px;position:relative;z-index:1}}
.info-stat{{text-align:center;padding:12px 8px;background:rgba(43,127,255,.04);border-radius:var(--radius);border:1px solid var(--border)}}
.info-s-val{{font-size:18px;font-weight:800;color:var(--text-primary)}}
.info-s-label{{font-size:9px;color:var(--text-secondary);margin-top:3px;font-weight:600;text-transform:uppercase;letter-spacing:.04em}}
/* Config cards */
.section-title{{font-size:12.5px;font-weight:800;color:var(--text-secondary);margin-bottom:12px;display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.06em}}
.section-title i{{color:var(--wp-blue);font-size:15px}}
.cfg-card{{background:var(--surface);backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius-lg);padding:20px 20px 18px;margin-bottom:12px;box-shadow:var(--shadow-sm);transition:all .3s}}
.cfg-card:hover{{border-color:rgba(43,127,255,.2);transform:translateY(-2px);box-shadow:var(--shadow-md)}}
.cfg-head{{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:12px}}
.cfg-name{{font-size:14px;font-weight:700;color:var(--text-primary)}}
.cfg-status{{font-size:10px;padding:3px 10px;border-radius:20px;font-weight:700;white-space:nowrap}}
.cfg-status.ok{{background:rgba(22,163,74,.1);color:var(--success)}}
.cfg-status.no{{background:rgba(255,35,82,.1);color:var(--wp-red)}}
.cfg-code{{background:rgba(15,23,42,.05);border:1px solid var(--border);border-radius:var(--radius);padding:12px 14px;font-family:'Inter',monospace;font-size:10px;color:var(--wp-blue);word-break:break-all;line-height:1.7;margin-bottom:10px;max-height:80px;overflow-y:auto}}
[data-theme="dark"] .cfg-code{{background:rgba(0,0,0,.2);color:#60A5FA}}
.cfg-actions{{display:flex;gap:7px;flex-wrap:wrap}}
.btn{{font-family:'Estedad',sans-serif;font-size:11.5px;font-weight:700;border-radius:var(--radius);padding:8px 15px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;border:none;transition:all .2s;white-space:nowrap}}
.btn i{{font-size:13px}}
.btn-p{{background:linear-gradient(90deg,var(--wp-blue),var(--wp-purple));color:#fff;box-shadow:0 4px 14px rgba(43,127,255,.25)}}
.btn-p:hover{{transform:translateY(-1px);box-shadow:0 6px 20px rgba(43,127,255,.35)}}
.btn-ghost{{background:rgba(43,127,255,.06);color:var(--wp-blue);border:1px solid rgba(43,127,255,.15)}}
.btn-ghost:hover{{background:rgba(43,127,255,.12)}}
/* Password lock */
.lock-page{{display:flex;align-items:center;justify-content:center;min-height:70vh}}
.lock-card{{background:var(--surface);backdrop-filter:blur(24px);border:1px solid var(--border);border-radius:var(--radius-xl);padding:40px 32px 34px;text-align:center;max-width:380px;width:100%;box-shadow:var(--shadow-lg)}}
.lock-icon{{width:64px;height:64px;border-radius:18px;background:rgba(43,127,255,.1);border:1px solid rgba(43,127,255,.2);display:flex;align-items:center;justify-content:center;margin:0 auto 18px;font-size:28px;color:var(--wp-blue)}}
.lock-title{{font-size:18px;font-weight:800;margin-bottom:6px}}
.lock-sub{{font-size:12px;color:var(--text-secondary);margin-bottom:20px;line-height:1.7}}
.lock-field{{position:relative;margin-bottom:14px}}
.lock-input{{width:100%;padding:13px 44px;border-radius:var(--radius);border:1.5px solid var(--border);background:rgba(255,255,255,.5);backdrop-filter:blur(8px);color:var(--text-primary);font-family:inherit;font-size:14px;text-align:center;outline:none;transition:all .2s;letter-spacing:.1em}}
.lock-input:focus{{border-color:var(--wp-blue);box-shadow:0 0 0 4px rgba(43,127,255,.1)}}
.lock-icon-left{{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--text-secondary);font-size:16px;pointer-events:none}}
.lock-err{{color:var(--wp-red);font-size:11px;margin-bottom:10px;min-height:18px}}
/* Toast */
.toast{{position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--surface);backdrop-filter:blur(16px);border:1px solid var(--border);color:var(--text-primary);border-radius:var(--radius);padding:10px 20px;font-size:12px;opacity:0;transition:all .3s;z-index:999;pointer-events:none;white-space:nowrap;box-shadow:var(--shadow-md)}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(22,163,74,.3);color:var(--success)}}
/* Empty */
.empty{{text-align:center;padding:60px 20px;color:var(--text-secondary)}}
.empty i{{font-size:40px;opacity:.3;display:block;margin-bottom:12px}}
.footer{{text-align:center;padding-top:30px;font-size:10.5px;color:var(--text-secondary)}}
@media(max-width:500px){{
  .info-stats{{grid-template-columns:1fr 1fr}}
  .wrap{{padding:20px 12px 50px}}
}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
/* Custom Sub Dropdown */
.custom-sub-dropdown-wrap{{position:relative;margin-top:8px}}
.custom-sub-dropdown{{
  display:flex;align-items:center;justify-content:space-between;
  background:var(--surface);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);
  border:1.5px solid var(--border);border-radius:var(--radius-lg);padding:10px 14px;cursor:pointer;
  transition:all .2s;gap:8px;overflow:hidden;position:relative;z-index:2
}}
.custom-sub-dropdown:hover{{border-color:rgba(43,127,255,.25)}}
.custom-sub-dropdown::after{{
  content:'';position:absolute;inset:0;border-radius:var(--radius-lg);
  background:linear-gradient(135deg,rgba(43,127,255,.05),transparent);opacity:0;transition:opacity .2s
}}
.custom-sub-dropdown:hover::after{{opacity:1}}
#custom-sub-selected-label{{font-size:13px;color:var(--text-primary);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
#custom-sub-chevron{{font-size:14px;color:var(--text-secondary);transition:transform .2s}}
.custom-sub-dropdown.open #custom-sub-chevron{{transform:rotate(180deg)}}
.custom-sub-dropdown-menu{{
  position:absolute;top:100%;left:0;right:0;
  background:var(--surface);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border:1.5px solid var(--border);border-radius:var(--radius-lg);
  max-height:220px;overflow-y:auto;overflow-x:hidden;
  z-index:10;margin-top:6px;box-shadow:var(--shadow-lg);
  opacity:0;visibility:hidden;transform:translateY(-6px);transition:all .2s;
  padding:6px
}}
.custom-sub-dropdown-wrap.open .custom-sub-dropdown-menu{{opacity:1;visibility:visible;transform:translateY(0)}}
.custom-sub-dropdown-menu::-webkit-scrollbar{{width:6px}}
.custom-sub-dropdown-menu::-webkit-scrollbar-track{{background:transparent}}
.custom-sub-dropdown-menu::-webkit-scrollbar-thumb{{background:rgba(43,127,255,.18);border-radius:3px}}
.custom-sub-dropdown-menu::-webkit-scrollbar-thumb:hover{{background:rgba(43,127,255,.28)}}
.custom-sub-option{{
  padding:10px 14px;cursor:pointer;border-radius:var(--radius);margin:4px 6px;
  font-size:12.5px;color:var(--text-primary);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
  transition:all .2s;display:flex;align-items:center;gap:8px
}}
.custom-sub-option:hover{{background:rgba(43,127,255,.08);color:var(--wp-blue)}}
.custom-sub-option.active{{background:rgba(43,127,255,.14);color:var(--wp-blue);border:1px solid rgba(43,127,255,.2);font-weight:600}}
.custom-sub-option .sub-preview{{
  display:inline-block;width:18px;height:18px;border-radius:4px;
  background:linear-gradient(135deg,var(--wp-blue),var(--wp-purple));
  flex-shrink:0;box-shadow:0 0 4px rgba(43,127,255,.4)
}}
</style>
</head>
<body data-theme="light">
<div class="bg-glow"><div class="bg-orb"></div><div class="bg-orb"></div></div>
<div class="toast" id="toast"></div>
<div class="wrap">
  {ann_html}
  <div class="top-bar">
    <div class="brand">
      <svg width="38" height="38" viewBox="0 0 100 100"><defs><linearGradient id="bgg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#6366f1"/><stop offset="50%" style="stop-color:#8b5cf6"/><stop offset="100%" style="stop-color:#a78bfa"/></linearGradient></defs><path d="M50 5 L90 22 L90 55 C90 78 72 93 50 98 C28 93 10 78 10 55 L10 22 Z" fill="url(#bgg)" opacity="0.95"/><path d="M50 18 L75 30 L75 54 C75 70 63 80 50 85 C37 80 25 70 25 54 L25 30 Z" fill="rgba(255,255,255,0.12)"/><rect x="43" y="38" width="14" height="22" rx="2" fill="rgba(255,255,255,0.9)"/><circle cx="50" cy="33" r="5" fill="rgba(255,255,255,0.9)"/></svg>
      <div><div class="brand-name">White Panel</div><div class="brand-sub">White Panel</div></div>
    </div>
    <button class="theme-toggle" onclick="toggleTheme()" title="تغییر تم"><i class="ti ti-sun" id="theme-icon"></i></button>
  </div>
  <div id="root"><div class="empty"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i><p>در حال بارگذاری...</p></div></div>
  <div class="footer">White Panel</div>
</div>
<script>
var UUID_KEY='{uuid_key}',SUB_URL='{sub_url}',savedPw='',currentData=null;
var isDark=localStorage.getItem('wp-pub-theme')==='dark';
function applyTheme(d){{document.documentElement.setAttribute('data-theme',d?'dark':'light');document.getElementById('theme-icon').className='ti '+(d?'ti-sun':'ti-moon')}}
function toggleTheme(){{isDark=!isDark;localStorage.setItem('wp-pub-theme',isDark?'dark':'light');applyTheme(isDark)}}
applyTheme(isDark);
function toast(m,t){{var el=document.getElementById('toast');el.textContent=m;el.className='toast show'+(t?' '+t:'');setTimeout(function(){{el.classList.remove('show')}},2400)}}
function esc(s){{return String(s||'').replace(/[&<>"']/g,function(c){{return{{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]}})}}
function fmtB(b){{if(!b)return'0 B';if(b<1024)return b+' B';if(b<1024**2)return(b/1024).toFixed(1)+' KB';if(b<1024**3)return(b/1024**2).toFixed(2)+' MB';return(b/1024**3).toFixed(2)+' GB'}}
function toFa(n){{return String(n).replace(/\\d/g,function(d){{return'۰۱۲۳۴۵۶۷۸۹'[d]}})}}

/* ── OS Detection & One-Click Import ──────────────────────────────────── */
function detectOS() {{
  var ua = navigator.userAgent || '';
  if (/android/i.test(ua)) return 'android';
  if (/iPad|iPhone|iPod/.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1)) return 'ios';
  if (/Win\\d/.test(ua)) return 'windows';
  if (/Macintosh|Mac OS X/.test(ua)) return 'macos';
  return 'other';
}}
function getImportApps() {{
  var os = detectOS();
  var apps = [];
  if (os === 'android') {{
    apps.push({{name:'v2rayNG', cls:'ico-android', icon:'ti ti-brand-android', href:'v2rayng://install-sub?url='+encodeURIComponent(SUB_URL)}});
    apps.push({{name:'Hiddify', cls:'ico-android', icon:'ti ti-shield', href:'hiddify://import?url='+encodeURIComponent(SUB_URL)}});
    apps.push({{name:'V2Box', cls:'ico-android', icon:'ti ti-box', href:'v2box://import?url='+encodeURIComponent(SUB_URL)}});
  }} else if (os === 'ios') {{
    apps.push({{name:'V2Box', cls:'ico-ios', icon:'ti ti-box', href:'v2box://import?url='+encodeURIComponent(SUB_URL)}});
    apps.push({{name:'Hiddify', cls:'ico-ios', icon:'ti ti-shield', href:'hiddify://import?url='+encodeURIComponent(SUB_URL)}});
    apps.push({{name:'Streisand', cls:'ico-ios', icon:'ti ti-bolt', href:'streisand://import?url='+encodeURIComponent(SUB_URL)}});
  }} else if (os === 'windows') {{
    apps.push({{name:'v2rayN', cls:'ico-windows', icon:'ti ti-brand-windows', href:'v2rayn://import?url='+encodeURIComponent(SUB_URL)}});
    apps.push({{name:'Hiddify', cls:'ico-windows', icon:'ti ti-shield', href:'hiddify://import?url='+encodeURIComponent(SUB_URL)}});
  }} else if (os === 'macos') {{
    apps.push({{name:'V2rayU', cls:'ico-macos', icon:'ti ti-brand-apple', href:'v2rayu://import?url='+encodeURIComponent(SUB_URL)}});
    apps.push({{name:'Hiddify', cls:'ico-macos', icon:'ti ti-shield', href:'hiddify://import?url='+encodeURIComponent(SUB_URL)}});
  }}
  return apps;
}}
function buildImportHtml() {{
  var apps = getImportApps();
  if (!apps.length) return '';
  var h = '<div class="import-section"><div class="import-title"><i class="ti ti-download"></i> وارد کردن سریع</div><div class="import-grid">';
  apps.forEach(function(a) {{
    h += '<a class="import-btn" href="'+esc(a.href)+'"><div class="ico '+a.cls+'"><i class="ti '+a.icon+'"></i></div><div><div>'+esc(a.name)+'</div><div class="lbl">یک کلیک</div></div></a>';
  }});
  h += '</div></div>';
  return h;
}}

async function loadData(pw){{var u='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');var r=await fetch(u);return r.json()}}

function renderLock(name,err){{document.getElementById('root').innerHTML='<div class="lock-page"><div class="lock-card"><div class="lock-icon"><i class="ti ti-shield-lock"></i></div><div class="lock-title">'+esc(name)+'</div><div class="lock-sub">این گروه با رمز محافظت می‌شود</div><div class="lock-err" id="lock-err">'+(err?'<i class="ti ti-alert-circle"></i> '+esc(err):'')+'</div><div class="lock-field"><i class="ti ti-lock lock-icon-left"></i><input class="lock-input" type="password" id="lock-pw" placeholder="••••••••" autofocus></div><button class="btn btn-p" style="width:100%;justify-content:center;padding:12px" onclick="submitLock()"><i class="ti ti-lock-open"></i> ورود</button></div></div>';document.getElementById('lock-pw').addEventListener('keydown',function(e){{if(e.key==='Enter')submitLock()}})}}

async function submitLock(){{var pw=document.getElementById('lock-pw').value;var d=await loadData(pw);if(d.locked){{renderLock(d.name,'رمز اشتباه است');return}}savedPw=pw;renderContent(d)}}

function renderContent(d){{currentData=d;var active=d.links.filter(function(l){{return l.active}}).length;var subUrl=d.sub_url||SUB_URL;subUrl+=savedPw?'?pw='+encodeURIComponent(savedPw):'';
var importHtml=buildImportHtml();
document.getElementById('root').innerHTML='<div class="info-card"><div class="info-name">'+esc(d.name)+'</div>'+(d.desc?'<div class="info-desc">'+esc(d.desc)+'</div>':'')+
'<div class="info-stats"><div class="info-stat"><div class="info-s-val">'+toFa(active)+'</div><div class="info-s-label">کانفیگ فعال</div></div><div class="info-stat"><div class="info-s-val">'+toFa(d.links.length)+'</div><div class="info-s-label">کل کانفیگ‌ها</div></div><div class="info-stat"><div class="info-s-val">'+esc(d.total_used_fmt||'0')+'</div><div class="info-s-label">مصرف</div></div></div></div>'+
importHtml+
'<div class="section-title"><i class="ti ti-link"></i> کانفیگ‌ها ('+toFa(d.links.length)+' عدد)</div>'+
(d.links.length?d.links.map(function(l){{return'<div class="cfg-card"><div class="cfg-head"><div class="cfg-name">'+esc(l.label)+'</div><span class="cfg-status '+(l.active?'ok':'no')+'">'+(l.active?'<i class="ti ti-circle-check"></i> فعال':'<i class="ti ti-circle-x"></i> غیرفعال')+'</span></div><div class="cfg-code">'+esc(l.vless_link)+'</div><div class="cfg-actions"><button class="btn btn-p" onclick="navigator.clipboard.writeText(\''+esc(l.vless_link).replace(/'/g,"\\'")+'\').then(function(){{toast(\'کپی شد ✓\',\'ok\')}})"><i class="ti ti-copy"></i> کپی لینک</button><button class="btn btn-ghost" onclick="window.open(\'https://api.qrserver.com/v1/create-qr-code/?size=220x220&data='+encodeURIComponent(l.vless_link)+'\',\'_blank\')"><i class="ti ti-qrcode"></i> QR Code</button></div></div>'}}).join(''):'<div class="empty"><i class="ti ti-link-off"></i><p>کانفیگی در این گروه وجود ندارد</p></div>')+
'<div style="margin-top:16px;text-align:center"><button class="btn btn-ghost" style="justify-content:center" onclick="location.reload()"><i class="ti ti-refresh"></i> بروزرسانی</button></div>';
}}

async function init(){{try{{var d=await loadData();if(d.locked){{renderLock(d.name);return}}renderContent(d)}}catch(e){{document.getElementById('root').innerHTML='<div class="empty"><i class="ti ti-alert-circle" style="color:var(--wp-red)"></i><p>خطا در بارگذاری</p></div>'}}}}
init();
</script>
</body></html>"""
