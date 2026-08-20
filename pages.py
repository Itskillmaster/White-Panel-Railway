# -*- coding: utf-8 -*-
# pages.py — White Panel Enterprise Theme (Persian Fixed)
# Exports: LOGIN_HTML, DASHBOARD_HTML, get_public_page_html()

import json

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl" class="dark">
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
<body data-theme="dark">
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
  var saved=localStorage.getItem('wp-theme')||'dark';
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
<html lang="fa" dir="rtl" class="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>White Panel</title>
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        sans: ['Estedad', '-apple-system', 'BlinkMacSystemFont', 'SF Pro Text', 'Segoe UI', 'Tahoma', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'Consolas', 'Menlo', 'monospace']
      }
    }
  }
};
</script>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Estedad:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<style>
:root{
  color-scheme:dark;
  --neon:#00e1c1;--neon2:#2ef2d6;--teal:#00e1c1;--green:#00e1c1;--success:#00e1c1;
  --red:#ff6b6b;--wp-red:#ff6b6b;--danger:#ff6b6b;
  --blue:#9db4ff;--wp-blue:#9db4ff;--purple:#c4b5fd;--wp-purple:#b9a6ff;
  --gold:#00e1c1;--warning:#ffab00;
  --txt:#ffffff;--txt2:rgba(255,255,255,.6);--text-secondary:rgba(255,255,255,.6);
  --border:rgba(255,255,255,.1);--bg3:rgba(255,255,255,.08);
  --radius:14px;--radius-lg:16px;--radius-xl:24px;
  --glass:rgba(255,255,255,.06);--surface-glass:rgba(9,15,33,.6);
  --nav-bg:rgba(255,255,255,.05);--input-bg:rgba(255,255,255,.06);
  --border-glow:rgba(0,225,193,.4);--input-glow:rgba(0,225,193,.14);
  --grad1:#00e1c1;--grad2:#8b5cf6;
  --grad:linear-gradient(135deg,#00e1c1,#2ef2d6);
  --gradient:linear-gradient(135deg,#00e1c1,#8b5cf6);
  --shadow-sm:0 4px 20px rgba(0,0,0,.3);--shadow-md:0 12px 40px rgba(0,0,0,.4);
  --shadow-lg:0 20px 56px rgba(0,0,0,.5);
}
:root:not(.dark){
  color-scheme:light;
  --neon:#0aa892;--neon2:#0aa892;--teal:#0aa892;--green:#0aa892;--success:#0aa892;
  --red:#e5484d;--wp-red:#e5484d;--danger:#e5484d;
  --blue:#2563eb;--wp-blue:#2563eb;--purple:#7c3aed;--wp-purple:#5e4ec4;
  --gold:#0aa892;--warning:#b45309;
  --txt:#0f172a;--txt2:rgba(15,23,42,.62);--text-secondary:rgba(15,23,42,.62);
  --border:rgba(15,23,42,.12);--bg3:rgba(15,23,42,.06);
  --radius:14px;--radius-lg:16px;--radius-xl:24px;
  --glass:rgba(255,255,255,.65);--surface-glass:rgba(255,255,255,.72);
  --nav-bg:rgba(15,23,42,.04);--input-bg:rgba(255,255,255,.85);
  --border-glow:rgba(10,168,146,.35);--input-glow:rgba(10,168,146,.12);
  --grad1:#0aa892;--grad2:#7c3aed;
  --grad:linear-gradient(135deg,#0aa892,#34d399);
  --gradient:linear-gradient(135deg,#0aa892,#7c3aed);
  --shadow-sm:0 2px 12px rgba(15,23,42,.06);--shadow-md:0 10px 30px rgba(15,23,42,.08);
  --shadow-lg:0 16px 48px rgba(15,23,42,.1);
}

*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'Estedad',-apple-system,BlinkMacSystemFont,'SF Pro Text','Segoe UI','Tahoma',system-ui,sans-serif;background:#050a18;color:#fff;transition:background .4s ease,color .4s ease;-webkit-font-smoothing:antialiased}
:root:not(.dark) body{background:#eef2f7}
input,select,button,textarea{font-family:inherit}
::selection{background:rgba(0,225,193,.28)}
::-webkit-scrollbar{width:8px;height:8px}::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:rgba(128,128,128,.28);border-radius:99px}
::-webkit-scrollbar-thumb:hover{background:rgba(128,128,128,.5)}
::-webkit-scrollbar-button{display:none}

/* ── Live animated background (matches /sub) ── */
.bg-fx{position:fixed;inset:0;z-index:-2;overflow:hidden;pointer-events:none;background:
  radial-gradient(ellipse 900px 600px at 25% 20%,rgba(0,225,193,.08) 0%,transparent 70%),
  radial-gradient(ellipse 700px 500px at 75% 15%,rgba(139,92,246,.08) 0%,transparent 60%),
  radial-gradient(ellipse 600px 400px at 60% 75%,rgba(99,102,241,.06) 0%,transparent 60%),
  radial-gradient(ellipse 500px 400px at 10% 80%,rgba(0,225,193,.05) 0%,transparent 55%)}
.bg-grid{position:fixed;inset:-2px;z-index:-2;pointer-events:none;
  background-image:linear-gradient(rgba(99,102,241,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(99,102,241,.04) 1px,transparent 1px);
  background-size:48px 48px;
  mask-image:radial-gradient(ellipse 90% 80% at 50% 45%,black 20%,transparent 70%);
  -webkit-mask-image:radial-gradient(ellipse 90% 80% at 50% 45%,black 20%,transparent 70%);
  animation:grid-drift 36s linear infinite}
@keyframes grid-drift{from{background-position:0 0}to{background-position:48px 48px}}

/* ── Animations ── */
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes slideUp{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
@keyframes scaleIn{from{opacity:0;transform:scale(.94)}to{opacity:1;transform:scale(1)}}

/* ── Shared glass surface ── */
.glass{background:var(--surface-glass);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:1px solid var(--border)}

/* ── Panels ── */
.panel{background:var(--surface-glass);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:1px solid var(--border);border-radius:var(--radius-xl);padding:20px;box-shadow:var(--shadow-sm)}
.panel-h{display:flex;align-items:center;gap:8px;margin-bottom:16px;font-size:18px;font-weight:800}
.glow{background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}

/* ── Stats ── */
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px}
.stat{background:var(--surface-glass);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:1px solid var(--border);border-radius:20px;padding:18px;transition:all .2s}
.stat:hover{transform:translateY(-3px);border-color:var(--border-glow);box-shadow:var(--shadow-md)}
.stat-icon{margin-bottom:8px;color:var(--neon)}
.stat-v{font-size:26px;font-weight:800;color:var(--neon)}
.stat-l{font-size:11px;color:var(--txt2);margin-top:4px}

/* ── Server bars ── */
.srv-bar{margin-bottom:6px}
.srv-bar-h{display:flex;justify-content:space-between;font-size:10px;margin-bottom:4px}
.srv-bar-h strong{font-size:11px;color:var(--txt)}
.srv-bar-h span{color:var(--txt2)}
.srv-bar-bg{height:7px;background:var(--bg3);border-radius:4px;overflow:hidden}
.srv-bar-f{height:100%;border-radius:4px;transition:width .5s ease;background:linear-gradient(90deg,var(--neon),var(--grad2))}
.pbar{height:6px;background:var(--bg3);border-radius:3px;overflow:hidden;margin-top:5px}
.pbar-f{height:100%;background:var(--gradient);border-radius:3px;transition:width .5s ease}

/* ── Buttons ── */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:6px;padding:9px 16px;border-radius:14px;font-size:12px;font-weight:700;cursor:pointer;border:1px solid transparent;transition:all .2s;line-height:1;white-space:nowrap}
.btn:disabled{opacity:.5;cursor:not-allowed;pointer-events:none}
.btn-p{background:var(--gradient);color:#fff;box-shadow:0 6px 20px rgba(0,225,193,.28)}
.btn-p:hover{filter:brightness(1.12);transform:translateY(-1px)}
.btn-g{background:var(--nav-bg);color:var(--txt);border-color:var(--border)}
.btn-g:hover{background:var(--input-bg);color:var(--neon);border-color:var(--border-glow)}
.btn-r{background:rgba(239,68,68,.12);color:var(--red);border-color:rgba(239,68,68,.25)}
.btn-r:hover{background:rgba(239,68,68,.22)}
.btn-b{background:rgba(99,102,241,.12);color:var(--blue);border-color:rgba(99,102,241,.25)}
.btn-b:hover{background:rgba(99,102,241,.22)}
.btn-gr{background:rgba(22,163,74,.12);color:var(--green);border-color:rgba(22,163,74,.25)}
.btn-sm{padding:5px 12px;font-size:11px;border-radius:10px}
.btn-icon{width:36px;height:36px;padding:0;border-radius:12px}

/* ── Badges ── */
.badge{display:inline-block;padding:4px 10px;border-radius:20px;font-size:10px;font-weight:600}
.badge-g{background:rgba(22,163,74,.15);color:var(--green)}
.badge-r{background:rgba(239,68,68,.15);color:var(--red)}
.badge-b{background:rgba(99,102,241,.15);color:var(--blue)}
.badge-p{background:rgba(139,92,246,.15);color:var(--purple)}

/* ── Tables / user cards ── */
.tbl{overflow-x:auto;-webkit-overflow-scrolling:touch;max-width:100%;border-radius:var(--radius-lg);border:1px solid var(--border);background:var(--glass)}
.tbl table{width:100%;border-collapse:collapse}
.tbl th{font-size:10px;text-transform:uppercase;letter-spacing:.5px;color:var(--txt2);text-align:right;padding:10px 12px;background:var(--nav-bg)}
.tbl td{padding:10px 12px;font-size:12px;color:var(--txt);border-top:1px solid var(--border)}
.tbl tr:hover td{background:var(--nav-bg)}
.u-cards{display:none;flex-direction:column;gap:10px}
.u-card{background:var(--surface-glass);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:1px solid var(--border);border-radius:16px;padding:14px;display:flex;flex-direction:column;gap:10px;box-shadow:var(--shadow-sm)}
.u-card-top{display:flex;align-items:center;justify-content:space-between;gap:8px}
.u-card-name{font-size:15px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.u-card-traffic{font-size:12px}
.u-card-meta{display:grid;grid-template-columns:1fr 1fr;gap:8px;border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:8px 0}
.u-card-meta span{display:flex;flex-direction:column;gap:2px}
.u-card-meta i{font-style:normal;font-size:9px;color:var(--txt2);text-transform:uppercase;letter-spacing:.5px}
.u-card-meta b{font-size:12px;font-weight:600}
.act-row{display:flex;gap:6px;flex-wrap:wrap}
.empty{text-align:center;padding:40px;color:var(--txt2);font-size:13px}

/* ── Forms ── */
.f-g{display:flex;flex-direction:column;gap:6px;margin-bottom:14px;flex:1}
.f-g label{font-size:11px;font-weight:600;color:var(--txt2);letter-spacing:.4px}
.f-g input,.f-g select,.f-g textarea,select.f-g{
  width:100%;background:var(--input-bg);border:1px solid var(--border);border-radius:12px;
  padding:10px 12px;font-size:13px;color:var(--txt);outline:none;transition:all .2s}
.f-g input:hover,.f-g select:hover,.f-g textarea:hover{border-color:var(--border-glow)}
.f-g input:focus,.f-g select:focus,.f-g textarea:focus{border-color:var(--neon);box-shadow:0 0 0 3px var(--input-glow)}
.f-g input::placeholder,.f-g textarea::placeholder{color:var(--txt2);opacity:.7}
.f-g select,select.f-g{appearance:none;-webkit-appearance:none;cursor:pointer;padding-left:30px;
  background-image:linear-gradient(45deg,transparent 50%,var(--neon) 50%),linear-gradient(135deg,var(--neon) 50%,transparent 50%);
  background-position:calc(100% - 16px) 50%,calc(100% - 11px) 50%;background-size:5px 5px;background-repeat:no-repeat}
.f-g select option{background:#0a1022;color:#fff}
:root:not(.dark) .f-g select option{background:#fff;color:#0f172a}
.f-r{display:flex;gap:10px;flex-wrap:wrap}
.px-hint{font-size:10px;color:var(--txt2);margin:6px 0 8px;line-height:1.7}
.divider{height:1px;background:var(--border);margin:14px 0}
.set-row{display:flex;justify-content:space-between;align-items:center;padding:14px 0;border-bottom:1px solid var(--border);gap:8px}
.set-row:last-child{border-bottom:none}
.set-lbl{font-size:13px;color:var(--txt2)}
.set-val{font-size:13px;font-weight:600}

/* ── iOS-style switch ── */
.ios-switch{width:51px;height:31px;border-radius:999px;background:#39393d;border:none;position:relative;cursor:pointer;flex-shrink:0;transition:background .25s ease;padding:0;margin:0;-webkit-tap-highlight-color:transparent}
.ios-switch::after{content:'';position:absolute;top:2px;left:2px;width:27px;height:27px;border-radius:50%;background:#fff;box-shadow:0 3px 8px rgba(0,0,0,.35),0 0 1px rgba(0,0,0,.4);transition:transform .25s cubic-bezier(.3,1.4,.5,1)}
.ios-switch.on{background:#34c759}
.ios-switch.on::after{transform:translateX(20px)}
:root:not(.dark) .ios-switch{background:#e5e5ea}
:root:not(.dark) .ios-switch.on{background:#34c759}

/* ── Modal ── */
.modal{display:flex;position:fixed;inset:0;z-index:80;align-items:flex-start;justify-content:center;padding:20px;opacity:0;visibility:hidden;pointer-events:none;transition:opacity .2s,visibility .2s;background:rgba(3,7,18,.6);backdrop-filter:blur(8px)}
.modal.show{opacity:1;visibility:visible;pointer-events:auto}
.modal-c{width:100%;max-width:520px;max-height:calc(100vh - 40px);overflow-y:auto;background:var(--surface-glass);backdrop-filter:blur(28px);-webkit-backdrop-filter:blur(28px);border:1px solid var(--border);border-radius:var(--radius-xl);padding:24px;box-shadow:var(--shadow-lg);animation:scaleIn .25s ease;position:relative}
.modal-t{font-size:21px;font-weight:800;margin-bottom:18px;display:flex;align-items:center;justify-content:space-between;gap:8px}
.modal-btns{display:flex;gap:8px;margin-top:18px}
.modal-btns .btn{flex:1;justify-content:center;padding:11px}
.modal-x{position:absolute;top:-14px;right:-14px;width:34px;height:34px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:var(--nav-bg);border:1px solid var(--border);color:var(--txt2);cursor:pointer;transition:all .2s}
.modal-x:hover{background:var(--red);color:#fff;border-color:var(--red);transform:rotate(90deg)}

/* ── Toast ── */
#toast{position:fixed;bottom:24px;left:0;right:0;z-index:150;display:flex;justify-content:center;pointer-events:none}
.toast{background:var(--surface-glass);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:1px solid var(--border);border-radius:16px;padding:12px 22px;font-size:13px;font-weight:600;color:var(--txt);box-shadow:var(--shadow-md);opacity:0;transform:translateY(16px);transition:all .25s;max-width:92vw;text-align:center}
.toast.show{opacity:1;transform:translateY(0)}

/* ── Config viewer ── */
.cfg-code{background:#050a18;border:1px solid var(--border);border-radius:14px;padding:16px;font-size:11px;direction:ltr;text-align:left;max-height:420px;overflow:auto;white-space:pre-wrap;word-break:break-all;color:#7ee6d4;font-family:Consolas,Menlo,monospace}
:root:not(.dark) .cfg-code{background:#0f172a}

/* ── Inbound pick chips ── */
.ib-pick{position:relative;display:flex;align-items:center;gap:10px;padding:10px 12px;background:var(--nav-bg);border:1.5px solid var(--border);border-radius:14px;cursor:pointer;transition:all .2s;min-width:0;flex:1 1 200px}
.ib-pick:hover{border-color:var(--border-glow)}
.ib-pick.selected{border-color:var(--neon);box-shadow:0 0 0 1px var(--neon)}
.ib-pick-ic{color:var(--neon);display:flex}
.ib-pick-info{flex:1;min-width:0}
.ib-pick-name{font-size:12.5px;font-weight:700;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.ib-pick-meta{font-size:10px;color:var(--txt2);direction:ltr;text-align:left;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.ib-pick-check{width:20px;height:20px;border-radius:50%;border:2px solid var(--border);flex-shrink:0;display:flex;align-items:center;justify-content:center;color:transparent;transition:all .2s;font-size:12px}
.ib-pick.selected .ib-pick-check{background:var(--gradient);border-color:transparent;color:#fff}
.ib-pick-check .material-symbols-outlined{font-size:14px}
.ib-opts{flex-basis:100%;margin-top:4px;padding:10px 12px;background:var(--glass);border:1px solid var(--border);border-radius:var(--radius);display:flex;flex-direction:column;gap:8px}

/* ── Country tick chips ── */
.country-tick{display:flex;align-items:center;gap:6px;cursor:pointer;user-select:none;padding:5px 10px;background:var(--surface-glass);border:1.5px solid var(--border);border-radius:999px;font-size:12px;color:var(--txt);transition:all .2s}
.country-tick:hover{box-shadow:var(--shadow-sm)}
.country-tick .ck{width:18px;height:18px;border-radius:50%;border:2px solid var(--border);flex-shrink:0;display:flex;align-items:center;justify-content:center;color:transparent;transition:all .2s;font-size:11px}
.country-tick.selected{border-color:var(--neon);box-shadow:0 0 0 1px var(--neon)}
.country-tick.selected .ck{background:var(--gradient);border-color:transparent;color:#fff}

/* ── IP Scanner ── */
.scn-tabs{display:flex;gap:8px;margin:14px 0;background:var(--glass);padding:5px;border-radius:14px;border:1px solid var(--border)}
.scn-tab{flex:1;padding:10px 6px;border:none;border-radius:10px;background:transparent;color:var(--txt2);font-size:12px;font-weight:700;cursor:pointer;transition:all .2s;display:flex;align-items:center;justify-content:center;gap:6px}
.scn-tab:hover{color:var(--txt)}
.scn-tab.active{background:var(--gradient);color:#fff;box-shadow:0 4px 16px rgba(0,225,193,.3)}
.scn-pane{display:none;animation:fadeIn .25s ease}
.scn-pane.active{display:block}
.scn-cfg{display:flex;gap:10px;align-items:flex-end;flex-wrap:wrap}
.scn-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:12px 0}
.scn-chip{display:flex;flex-direction:column;align-items:center;gap:2px;padding:10px 6px;background:var(--glass);border:1px solid var(--border);border-radius:12px;font-size:10px;color:var(--txt2)}
.scn-chip b{font-size:16px;font-weight:800;color:var(--txt);font-family:monospace;direction:ltr}
.scn-progress{height:6px;background:var(--bg3);border-radius:99px;overflow:hidden;margin:10px 0}
.scn-bar{height:100%;width:0%;background:var(--gradient);border-radius:99px;transition:width .4s ease}
.scn-list{display:flex;flex-direction:column;gap:6px;max-height:340px;overflow-y:auto}
.scn-item{display:flex;align-items:center;gap:10px;padding:8px 12px;background:var(--glass);border:1px solid var(--border);border-radius:10px;font-size:12px}
.scn-empty{color:var(--txt2);font-size:12px;padding:14px;text-align:center;display:block}
.scn-saved-t{display:flex;align-items:center;justify-content:space-between;font-size:11px;color:var(--txt2);margin-bottom:6px;gap:6px;flex-wrap:wrap}
.scn-saved-tags{display:flex;flex-wrap:wrap;gap:6px}
.scn-tag{display:inline-block;padding:4px 10px;border-radius:8px;background:var(--nav-bg);border:1px solid var(--border);font-size:11px;color:var(--txt);direction:ltr}

/* ── Contact bubbles ── */
.contact-panel{text-align:center;display:flex;flex-direction:column;align-items:center;gap:6px}
.contact-sub{font-size:12px;color:var(--txt2);margin-bottom:18px}
.contact-bubbles{display:flex;gap:28px;justify-content:center;align-items:center;flex-wrap:wrap;padding:16px 0 8px}
.contact-bubble{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;width:150px;height:150px;border-radius:50%;background:var(--surface-glass);backdrop-filter:blur(24px);border:1.5px solid var(--border);color:var(--txt);text-decoration:none;box-shadow:var(--shadow-md);transition:all .3s ease;position:relative;overflow:hidden}
.contact-bubble svg{width:40px;height:40px;color:var(--neon);transition:transform .3s ease}
.contact-bubble span{font-size:13px;font-weight:700}
.contact-bubble small{font-size:10px;color:var(--txt2);direction:ltr}
.contact-bubble:hover{transform:translateY(-6px);border-color:var(--border-glow);box-shadow:var(--shadow-lg)}

/* ── Sidebar ── */
.sidebar-backdrop{display:none;position:fixed;inset:0;background:rgba(2,6,16,.55);backdrop-filter:blur(4px);z-index:40}
@media(max-width:1023px){.sidebar-backdrop.show{display:block}}
.sidebar{transform:translateX(100%);transition:transform .3s ease}
.sidebar.open{transform:translateX(0)}
@media(min-width:1024px){.sidebar{transform:none}}
.sb-brand-t{font-size:17px;font-weight:800;letter-spacing:3px;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.sb-brand-s{font-size:10px;color:var(--txt2);letter-spacing:5px;margin-top:2px}
.nav-item{display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:14px;color:var(--txt2);font-size:13px;font-weight:600;cursor:pointer;transition:all .2s;border:1px solid transparent;margin-bottom:2px}
.nav-item:hover{color:var(--txt);background:var(--nav-bg)}
.nav-item.active{color:#fff;background:linear-gradient(135deg,rgba(0,225,193,.16),rgba(139,92,246,.12));border:1px solid rgba(0,225,193,.3);box-shadow:0 0 20px rgba(0,225,193,.1)}
:root:not(.dark) .nav-item.active{color:#0f172a}
.sb-foot{font-size:11px;color:var(--txt2);display:flex;align-items:center;gap:8px}

.topbar-greet{font-size:14px}
.lang-btn{display:inline-flex;align-items:center;gap:6px;padding:6px 12px;border-radius:20px;background:var(--glass);border:1px solid var(--border);color:var(--txt);font-size:12px;font-weight:700;cursor:pointer;transition:all .2s}

/* ── Custom Sub dropdown ── */
.custom-sub-dropdown-wrap{position:relative;margin-top:8px;flex:1}
.custom-sub-dropdown{display:flex;align-items:center;justify-content:space-between;background:var(--glass);border:1.5px solid var(--border);border-radius:var(--radius);padding:10px 14px;cursor:pointer}
.custom-sub-dropdown-menu{position:absolute;top:100%;left:0;right:0;background:var(--surface-glass);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:1.5px solid var(--border);border-radius:var(--radius);max-height:220px;overflow-y:auto;z-index:30;opacity:0;visibility:hidden;transform:translateY(-6px);transition:all .2s}
.custom-sub-dropdown-wrap.open .custom-sub-dropdown-menu{opacity:1;visibility:visible;transform:translateY(0)}
.custom-sub-option{padding:10px 14px;cursor:pointer;font-size:12.5px;transition:all .2s;display:flex;align-items:center;gap:8px}

.hidden{display:none!important}
@media(max-width:1023px){
  .stats{grid-template-columns:repeat(2,1fr);gap:8px}
  .scn-stats{grid-template-columns:repeat(2,1fr)}
}
@media(max-width:640px){
  #tab-users .tbl{display:none}
  .u-cards{display:flex}
}
</style>
</head>
<body class="min-h-screen text-slate-900 dark:text-white transition-colors overflow-x-hidden">

<div class="bg-fx"></div>
<div class="bg-grid"></div>

<div id="app-wrap" class="min-h-screen relative z-10 overflow-x-hidden flex">
  <!-- SIDEBAR -->
  <div class="sidebar-backdrop" id="sidebar-backdrop" onclick="closeSidebar()"></div>
  <aside id="sidebar" class="sidebar fixed top-0 bottom-0 right-0 z-50 w-[260px] flex flex-col glass lg:border-l dark:border-white/10 border-slate-900/10 lg:border-r-0">
    <div class="flex items-center gap-3 px-5 py-5 border-b border-slate-900/10 dark:border-white/10">
      <svg width="42" height="42" viewBox="0 0 100 100"><defs><linearGradient id="sg1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#00e1c1"/><stop offset="100%" style="stop-color:#8b5cf6"/></linearGradient></defs><path d="M50 5 L90 22 L90 55 C90 78 72 93 50 98 C28 93 10 78 10 55 L10 22 Z" fill="url(#sg1)" opacity="0.95"/><path d="M50 18 L75 30 L75 54 C75 70 63 80 50 85 C37 80 25 70 25 54 L25 30 Z" fill="rgba(255,255,255,0.12)"/><rect x="43" y="38" width="14" height="22" rx="2" fill="rgba(255,255,255,0.9)"/><circle cx="50" cy="33" r="5" fill="rgba(255,255,255,0.9)"/></svg>
      <div><div class="sb-brand-t"><span>W</span>HITE</div><div class="sb-brand-s">PANEL</div></div>
    </div>
    <nav class="flex-1 p-2.5 overflow-y-auto overflow-x-hidden">
      <div class="nav-item active" onclick="switchTab('dashboard',this)"><span class="nav-ic"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg></span><span data-i18n="dash">داشبورد</span></div>
      <div class="nav-item" onclick="switchTab('users',this)"><span class="nav-ic"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2m8-10a4 4 0 100-8 4 4 0 000 8zm13 10v-2a4 4 0 00-3-3.87m-4-12a4 4 0 010 7.75"/></svg></span><span data-i18n="users">کاربران</span></div>
      <div class="nav-item" onclick="switchTab('inbounds',this)"><span class="nav-ic"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg></span><span data-i18n="inbounds">اینباندها</span></div>
      <div class="nav-item" onclick="switchTab('scanner',this)"><span class="nav-ic"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/><path d="M11 8v3l2 2"/></svg></span><span data-i18n="scanner">اسکنر IP</span></div>
      <div class="nav-item" onclick="switchTab('worker',this)"><span class="nav-ic"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg></span><span data-i18n="worker">Worker</span></div>
      <div class="nav-item" onclick="switchTab('settings',this)"><span class="nav-ic"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M12 1v2m0 18v2M4.22 4.22l1.42 1.42m12.72 12.72l1.42 1.42M1 12h2m18 0h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg></span><span data-i18n="settings">تنظیمات</span></div>
      <div class="nav-item" onclick="switchTab('contact',this)"><span class="nav-ic"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg></span><span data-i18n="contact">Contact Me</span></div>
      <div class="nav-item" onclick="doLogout()" style="color:var(--red)!important"><span class="nav-ic"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 01-2-2V5a2 2 0 012-2h4m7 14l5-5-5-5m5 5H9"/></svg></span><span data-i18n="logout">خروج</span></div>
    </nav>
  </aside>

  <!-- MAIN -->
  <div class="main-area flex-1 min-w-0 flex flex-col relative z-10 lg:mr-[260px]">
    <div class="topbar sticky top-0 z-30 glass px-4 py-3 lg:px-6 flex items-center justify-between gap-3">
      <div class="flex items-center gap-3 min-w-0">
        <button class="btn btn-sm btn-g lg:hidden" onclick="toggleSidebar()" aria-label="menu">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
        <div class="topbar-greet" id="grt">سلام <strong>ادمین</strong></div>
      </div>
      <div class="flex items-center gap-2">
        <button class="lang-btn" id="theme-btn" onclick="toggleThemeMode()" title="حالت روشن/تاریک"><span id="theme-ic" class="material-symbols-outlined" style="font-size:18px">light_mode</span><span id="theme-label">روشن</span></button>
      </div>
    </div>

    <div class="content flex-1 min-w-0 p-4 lg:p-6 overflow-x-hidden">

      <!-- DASHBOARD TAB -->
      <div class="tab-content" id="tab-dashboard">
        <div class="panel"><div class="panel-h"><span class="glow" data-i18n="tab.dash">داشبورد</span></div><div id="dashboard-content"><div class="empty" data-i18n="loading">در حال بارگذاری...</div></div></div>
      </div>

      <!-- USERS TAB -->
      <div class="tab-content hidden" id="tab-users">
        <div class="panel">
          <div class="panel-h" style="justify-content:space-between">
            <span class="glow" data-i18n="tab.users">مدیریت کاربران</span>
            <button class="btn btn-p" onclick="openCreateUser()"><span data-i18n="newUser">کاربر جدید</span></button>
          </div>
          <div id="users-list"><div class="empty" data-i18n="loading">در حال بارگذاری...</div></div>
        </div>
      </div>

      <!-- INBOUNDS TAB -->
      <div class="tab-content hidden" id="tab-inbounds">
        <div class="panel">
          <div class="panel-h" style="justify-content:space-between">
            <span class="glow" data-i18n="tab.inbounds">مدیریت اینباندها</span>
            <button class="btn btn-p" onclick="openCreateInbound()"><span data-i18n="newInbound">اینباند جدید</span></button>
          </div>
          <div id="inbounds-list"><div class="empty" data-i18n="loading">در حال بارگذاری...</div></div>
        </div>
      </div>

      <!-- WORKER TAB -->
      <div class="tab-content hidden" id="tab-worker">
        <div class="panel">
          <div class="panel-h" style="justify-content:space-between"><span class="glow">⚡ <span data-i18n="worker">Worker</span></span><span id="worker-badge" class="badge badge-g" style="margin-right:auto"></span></div>
          <div id="worker-setup">
            <div class="scn-hint px-hint" data-i18n="workerSetupTip">پنل را به Cloudflare Worker متصل کنید...</div>
            <div class="f-g" style="margin-top:10px"><label data-i18n="cfToken">Cloudflare API Token</label>
              <div style="display:flex;gap:8px"><input type="password" id="wk-token" dir="ltr" style="flex:1" autocomplete="off"></div>
            </div>
            <div class="f-g"><label data-i18n="cfAccountId">Account ID</label><input type="text" id="wk-account" dir="ltr" placeholder="e.g. 1a2b3c..."></div>
            <div class="f-g"><label data-i18n="cfEmail">Cloudflare Email</label><input type="email" id="wk-email" dir="ltr" placeholder="you@example.com" autocomplete="email"></div>
            <button class="btn btn-p" style="width:100%;margin-top:10px" onclick="workerSetup()"><span data-i18n="cfConnect">اتصال و Deploy</span></button>
          </div>
          <div id="worker-managed" class="hidden">
            <div class="set-row"><span class="set-lbl" data-i18n="workerStatus">وضعیت</span><span id="worker-status" class="badge badge-g"></span></div>
            <div class="set-row"><span class="set-lbl" data-i18n="workerUrl">Worker URL</span><a id="worker-url" href="#" target="_blank" rel="noopener" dir="ltr" style="color:var(--neon);font-size:12px"></a></div>
            <div class="panel-h" style="margin-top:18px;border-top:1px solid var(--border);padding-top:14px;font-size:15px"><span class="glow" data-i18n="proxyPool">Proxy IP Pool</span><button class="btn btn-sm btn-p" onclick="workerAddProxy()" style="margin-left:auto">+ <span data-i18n="addProxy">افزودن کشور</span></button></div>
            <div id="worker-proxies"></div>
            <button class="btn btn-sm btn-r" onclick="workerDisconnect()" style="margin-top:16px"><span data-i18n="removeConn">حذف اتصال Worker</span></button>
          </div>
        </div>
      </div>

      <!-- SETTINGS TAB -->
      <div class="tab-content hidden" id="tab-settings">
        <div class="panel" style="margin-bottom:14px">
          <div class="panel-h"><span class="glow" data-i18n="serverResources">Server Resources</span></div>
          <div id="neon-bars">
            <div class="set-row" style="flex-direction:column;align-items:stretch;gap:6px">
              <div style="display:flex;justify-content:space-between;font-size:11px"><span style="color:var(--txt2)">CPU</span><span id="cpu-val" style="color:var(--neon);font-family:monospace">--</span></div>
              <div class="pbar" style="height:8px;border-radius:4px"><div class="pbar-f" id="cpu-bar" style="width:0%;background:linear-gradient(90deg,var(--neon),#ff6b6b);border-radius:4px;transition:width .5s"></div></div>
            </div>
            <div class="set-row" style="flex-direction:column;align-items:stretch;gap:6px;margin-top:10px">
              <div style="display:flex;justify-content:space-between;font-size:11px"><span style="color:var(--txt2)">RAM</span><span id="ram-val" style="color:#ffab00;font-family:monospace">--</span></div>
              <div class="pbar" style="height:8px;border-radius:4px"><div class="pbar-f" id="ram-bar" style="width:0%;background:linear-gradient(90deg,#ffab00,#ff6b00);border-radius:4px;transition:width .5s"></div></div>
            </div>
            <div class="set-row" style="flex-direction:column;align-items:stretch;gap:6px;margin-top:10px">
              <div style="display:flex;justify-content:space-between;font-size:11px"><span style="color:var(--txt2)">Disk</span><span id="disk-val" style="color:var(--blue);font-family:monospace">--</span></div>
              <div class="pbar" style="height:8px;border-radius:4px"><div class="pbar-f" id="disk-bar" style="width:0%;background:linear-gradient(90deg,var(--blue),var(--purple));border-radius:4px;transition:width .5s"></div></div>
            </div>
          </div>
        </div>

        <div class="panel" style="margin-top:14px">
          <div class="panel-h"><span class="glow" data-i18n="changePassword">Change Password</span></div>
          <form onsubmit="changePassword(event)">
            <div class="f-g"><label data-i18n="curPass">رمز فعلی</label><input type="password" id="cp-old" required></div>
            <div class="f-g"><label data-i18n="newPass">رمز جدید</label><input type="password" id="cp-new" required minlength="4"></div>
            <button class="btn btn-p" style="width:100%"><span data-i18n="changePassBtn">تغییر رمز</span></button>
          </form>
        </div>
      </div>

    </div>
  </div>
</div>

<!-- ═══════ MODALS ═══════ -->
<!-- CREATE USER -->
<div class="modal" id="mod-user"><div class="modal-c" style="max-width:680px">
  <div class="modal-t"><span class="glow" data-i18n="createUser">ایجاد کاربر جدید</span></div>
  <form onsubmit="submitCreateUser(event)">
    <div class="f-r">
      <div class="f-g"><label data-i18n="username">نام کاربری</label><input type="text" id="cu-name" required></div>
      <div class="f-g"><label data-i18n="conn">اتصال همزمان</label><input type="number" id="cu-conn" value="2"></div>
    </div>
    <div class="f-r">
      <div class="f-g"><label data-i18n="volume">حجم</label><input type="number" id="cu-vol" value="20"></div>
      <div class="f-g"><label data-i18n="unit">واحد</label><select id="cu-vol-u"><option value="GB">GB</option><option value="MB">MB</option></select></div>
      <div class="f-g"><label data-i18n="expire">اعتبار</label><input type="number" id="cu-exp" value="30"></div>
      <div class="f-g"><label data-i18n="unit">واحد</label><select id="cu-exp-u"><option value="days" data-i18n="day">روز</option><option value="months" data-i18n="month">ماه</option></select></div>
    </div>
    <div class="f-g">
      <label data-i18n="inboundsMulti">اینباندها (چندتایی)</label>
      <div id="cu-inbound" class="f-r" style="gap:8px;margin-top:6px"></div>
    </div>
    <div class="modal-btns">
      <button type="button" class="btn btn-g" onclick="closeModal('mod-user')"><span data-i18n="cancel">انصراف</span></button>
      <button type="submit" class="btn btn-p" id="cu-submit"><span data-i18n="submitUser">ایجاد کاربر</span></button>
    </div>
  </form>
</div></div>

<!-- INBOUND MODAL -->
<div class="modal" id="mod-inbound"><div class="modal-c" style="max-width:560px">
  <div class="modal-t"><span class="glow" id="ib-title">ایجاد اینباند جدید</span></div>
  <form onsubmit="submitInbound(event)">
    <input type="hidden" id="ib-id">
    <div class="f-g"><label data-i18n="inboundName">نام اینباند</label><input type="text" id="ib-name" required data-i18n-placeholder="inboundName" placeholder="مثال: Main-WS"></div>
    <div class="f-g"><label data-i18n="intPort">پورت اصلی</label><input type="number" id="ib-port" required placeholder="8443" dir="ltr"></div>
    <div class="f-g"><label data-i18n="securityType">امنیت</label><select id="ib-security" onchange="onSecurityChange()"><option value="tls">TLS</option><option value="reality">Reality</option></select></div>
    <div class="f-g"><label data-i18n="extDomain">دامنه خارجی</label><input type="text" id="ib-extdomain" dir="ltr" data-i18n-placeholder="extDomainPlace" placeholder="مثال: tokaido.proxy.rlwy.net"></div>
    <div class="f-r">
      <div class="f-g"><label data-i18n="extPortCfg">پورت خارجی</label><input type="number" id="ib-extport" value="443" dir="ltr" placeholder="443"></div>
      <div class="f-g"><label>SNI</label><input type="text" id="ib-sni" value="is1-ssl.mzstatic.com" dir="ltr" readonly></div>
    </div>
    <!-- Reality-only fields -->
    <div id="ib-reality-fields" class="hidden">
      <div class="divider"></div>
      <div style="font-size:11px;color:var(--neon);font-weight:700;margin-bottom:8px" data-i18n="realitySettings">تنظیمات Reality</div>
      <div class="f-r">
        <div class="f-g"><label>Private Key</label><input type="text" id="ib-privkey" dir="ltr" data-i18n-placeholder="autoGen" placeholder="تولید خودکار"></div>
        <div class="f-g"><label>Public Key</label><input type="text" id="ib-pubkey" dir="ltr" data-i18n-placeholder="autoGen" placeholder="تولید خودکار" readonly></div>
      </div>
      <button type="button" class="btn btn-sm btn-b" onclick="generateRealityKeysUI()" style="width:100%;margin-bottom:10px"><span data-i18n="genRealityKey">تولید کلید Reality</span></button>
      <div class="f-g"><label data-i18n="dest">Destination</label><input type="text" id="ib-dest" value="is1-ssl.mzstatic.com:443" dir="ltr"></div>
      <div class="f-g"><label data-i18n="serverNames">Server Names (SNI)</label><input type="text" id="ib-servernames" value="is1-ssl.mzstatic.com" dir="ltr"></div>
      <div class="f-g"><label data-i18n="shortIds">Short IDs</label><div style="display:flex;gap:6px"><input type="text" id="ib-shortids" value="" dir="ltr" style="flex:1"><button type="button" class="btn btn-sm" onclick="generateShortId()"><span data-i18n="generate">+ تولید</span></button></div></div>
      <div class="f-g"><label data-i18n="kmx">KMX</label><input type="text" id="ib-kmx" dir="ltr" placeholder="/" value="/"></div>
    </div>
    <div class="divider"></div>
    <div id="ib-net-wrap">
      <div class="f-g"><label data-i18n="network">نوع انتقال</label><select id="ib-network" onchange="onNetworkChange()"><option value="tcp">TCP</option><option value="ws">WebSocket</option><option value="xhttp">XHTTP</option><option value="grpc">gRPC</option></select></div>
      <div id="ib-ws-fields" class="hidden"><div class="f-g"><label>Path</label><input type="text" id="ib-wspath" value="/" dir="ltr"></div></div>
      <div id="ib-xhttp-fields" class="hidden"><div class="f-g"><label>Path</label><input type="text" id="ib-xhttppath" value="/" dir="ltr"></div><div class="f-r"><div class="f-g"><label>Mode</label><select id="ib-xhttp-mode"><option value="auto">auto</option><option value="packet-up">packet-up</option><option value="stream-one">stream-one</option></select></div></div></div>
      <div id="ib-grpc-fields" class="hidden"><div class="f-g"><label data-i18n="serviceName">Service Name</label><input type="text" id="ib-grpc-svc" value="grpc" dir="ltr"></div></div>
    </div>
    <div class="modal-btns">
      <button type="button" class="btn btn-g" onclick="closeModal('mod-inbound')"><span data-i18n="cancel">انصراف</span></button>
      <button type="submit" class="btn btn-p" id="ib-submit"><span data-i18n="createInbound">ایجاد اینباند</span></button>
    </div>
  </form>
</div></div>

<!-- CONFIG VIEWER -->
<div class="modal" id="mod-cfg"><div class="modal-c">
  <div class="modal-t"><span class="glow" data-i18n="config">کانفیگ</span></div>
  <pre class="cfg-code" id="cfg-code"></pre>
  <div class="modal-btns">
    <button class="btn btn-p" onclick="copyCfg()"><span data-i18n="copy">کپی</span></button>
    <button class="btn btn-g" onclick="closeModal('mod-cfg')"><span data-i18n="close">بستن</span></button>
  </div>
</div></div>

<!-- TOAST -->
<div id="toast"></div>

<script>
var $ = qs => document.querySelector(qs);
var $id = id => document.getElementById(id);
var curCfg = '';
var ALL_IB = [];
var ALL_USERS = [];
var LANG = localStorage.getItem('wp-lang') || 'fa';
var I18N = {
  fa: {
    'dash': 'داشبورد', 'users': 'کاربران', 'inbounds': 'اینباندها', 'scanner': 'اسکنر IP', 'worker': 'Worker', 'settings': 'تنظیمات', 'contact': 'Contact Me', 'logout': 'خروج',
    'tab.dash': 'داشبورد', 'tab.users': 'مدیریت کاربران', 'tab.inbounds': 'مدیریت اینباندها', 'tab.scanner': 'اسکنر آی‌پی', 'tab.settings': 'تنظیمات',
    'newUser': 'کاربر جدید', 'newInbound': 'اینباند جدید', 'loading': 'در حال بارگذاری...', 'noUsers': 'هیچ کاربری وجود ندارد', 'noInbounds': 'هیچ اینباندی وجود ندارد',
    'srv': 'وضعیت زنده سرور', 'cpu': 'پردازنده', 'ram': 'حافظه رم', 'disk': 'دیسک', 'sent': 'ارسال', 'recv': 'دریافت', 'activeUsers': 'کاربران فعال/کل', 'trafficUsed': 'ترافیک مصرفی', 'activeConns': 'اتصالات فعال', 'uptime': 'زمان فعالیت',
    'createUser': 'ایجاد کاربر جدید', 'username': 'نام کاربری', 'conn': 'اتصال همزمان', 'volume': 'حجم', 'unit': 'واحد', 'expire': 'اعتبار', 'day': 'روز', 'month': 'ماه',
    'inboundsMulti': 'اینباندها (چندتایی)', 'cancel': 'انصراف', 'submitUser': 'ایجاد کاربر', 'creatingUser': 'در حال ایجاد...', 'userCreated': 'با موفقیت ایجاد شد',
    'inboundName': 'نام اینباند', 'intPort': 'پورت اصلی', 'securityType': 'امنیت', 'extDomain': 'دامنه خارجی', 'extPortCfg': 'پورت خارجی', 'realitySettings': 'تنظیمات Reality', 'dest': 'Destination', 'serverNames': 'Server Names (SNI)', 'shortIds': 'Short IDs', 'kmx': 'KMX', 'network': 'نوع انتقال', 'serviceName': 'Service Name', 'createInbound': 'ایجاد اینباند', 'updateInbound': 'ویرایش اینباند', 'editInbound': 'ویرایش اینباند', 'inboundCreated': 'اینباند ذخیره شد', 'inboundUpdated': 'اینباند ویرایش شد',
    'config': 'کانفیگ', 'copy': 'کپی', 'close': 'بستن', 'copied': 'کپی شد', 'noCfg': 'کانفیگی وجود ندارد', 'delete': 'حذف', 'edit': 'ویرایش',
    'workerSetupTip': 'اتصال به Cloudflare Worker...', 'cfToken': 'API Token', 'cfAccountId': 'Account ID', 'cfEmail': 'Email', 'cfConnect': 'اتصال و Deploy', 'workerStatus': 'وضعیت', 'workerUrl': 'URL', 'proxyPool': 'Proxy IP Pool', 'addProxy': 'افزودن کشور', 'removeConn': 'حذف اتصال',
    'serverResources': 'منابع سرور', 'changePassword': 'تغییر رمز', 'curPass': 'رمز فعلی', 'newPass': 'رمز جدید', 'changePassBtn': 'تغییر رمز'
  },
  en: {
    'dash': 'Dashboard', 'users': 'Users', 'inbounds': 'Inbounds', 'scanner': 'IP Scanner', 'worker': 'Worker', 'settings': 'Settings', 'contact': 'Contact', 'logout': 'Logout',
    'tab.dash': 'Dashboard', 'tab.users': 'Manage Users', 'tab.inbounds': 'Manage Inbounds', 'tab.scanner': 'IP Scanner', 'tab.settings': 'Settings',
    'newUser': 'New User', 'newInbound': 'New Inbound', 'loading': 'Loading...', 'noUsers': 'No users', 'noInbounds': 'No inbounds',
    'srv': 'Live Server Status', 'cpu': 'CPU', 'ram': 'RAM', 'disk': 'Disk', 'sent': 'Sent', 'recv': 'Received', 'activeUsers': 'Active Users', 'trafficUsed': 'Traffic Used', 'activeConns': 'Active Conns', 'uptime': 'Uptime',
    'createUser': 'Create User', 'username': 'Username', 'conn': 'Connections', 'volume': 'Traffic', 'unit': 'Unit', 'expire': 'Expiry', 'day': 'Days', 'month': 'Months',
    'inboundsMulti': 'Inbounds', 'cancel': 'Cancel', 'submitUser': 'Create User', 'creatingUser': 'Creating...', 'userCreated': 'User created successfully',
    'inboundName': 'Inbound Name', 'intPort': 'Internal Port', 'securityType': 'Security', 'extDomain': 'External Domain', 'extPortCfg': 'External Port', 'realitySettings': 'Reality Settings', 'dest': 'Destination', 'serverNames': 'Server Names (SNI)', 'shortIds': 'Short IDs', 'kmx': 'KMX', 'network': 'Network', 'serviceName': 'Service Name', 'createInbound': 'Create Inbound', 'updateInbound': 'Update Inbound', 'editInbound': 'Edit Inbound', 'inboundCreated': 'Inbound saved', 'inboundUpdated': 'Inbound updated',
    'config': 'Config', 'copy': 'Copy', 'close': 'Close', 'copied': 'Copied', 'noCfg': 'No config', 'delete': 'Delete', 'edit': 'Edit',
    'workerSetupTip': 'Connect to Cloudflare Worker...', 'cfToken': 'API Token', 'cfAccountId': 'Account ID', 'cfEmail': 'Email', 'cfConnect': 'Connect & Deploy', 'workerStatus': 'Status', 'workerUrl': 'URL', 'proxyPool': 'Proxy Pool', 'addProxy': 'Add Country', 'removeConn': 'Remove Connection',
    'serverResources': 'Server Resources', 'changePassword': 'Change Password', 'curPass': 'Current Password', 'newPass': 'New Password', 'changePassBtn': 'Change Password'
  }
};
function t(key) { return (I18N[LANG] || I18N.fa)[key] || (I18N.fa[key] || key); }
function applyLang() {
  document.documentElement.lang = LANG; document.documentElement.dir = 'rtl';
  document.querySelectorAll('[data-i18n]').forEach(el => {
    var k = el.getAttribute('data-i18n');
    if(el.tagName==='INPUT' || el.tagName==='TEXTAREA') el.placeholder = t(k); else el.textContent = t(k);
  });
  if($id('lang-label')) $id('lang-label').textContent = LANG === 'en' ? 'FA' : 'EN';
  if(ALL_USERS.length) renderUsers();
  if(ALL_IB.length) renderInbounds();
}
function toggleLang() { LANG = LANG === 'fa' ? 'en' : 'fa'; localStorage.setItem('wp-lang', LANG); applyLang(); }

// ─── API & Core ───
async function api(url, opts) {
  opts = opts || {}; opts.credentials = 'same-origin'; opts.headers = opts.headers || {};
  if(opts.body && typeof opts.body === 'object') { opts.headers['Content-Type'] = 'application/json'; opts.body = JSON.stringify(opts.body); }
  var r = await fetch(url, opts);
  if(!r.ok) { var txt = await r.text(); try{ var j=JSON.parse(txt); throw new Error(j.detail || j.error || txt); }catch(e){ throw e; } }
  return r.json();
}

function toast(msg, type) {
  var el = $id('toast'); el.textContent = msg; el.style.color = type === 'err' ? 'var(--red)' : type === 'ok' ? 'var(--neon)' : 'var(--txt)';
  el.classList.add('show'); setTimeout(() => el.classList.remove('show'), 2800);
}

function esc(s) { return String(s||'').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
function fmtBytes(b) { if(!b) return '0 B'; var u=['B','KB','MB','GB','TB'], i=0; while(b>=1024 && i<4){b/=1024; i++;} return b.toFixed(2)+' '+u[i]; }
function fmtUptime(s) { if(!s) return '۰s'; var d=Math.floor(s/86400), h=Math.floor((s%86400)/3600), m=Math.floor((s%3600)/60); return (d?d+'d ':'')+h+'h '+m+'m'; }

async function checkAuth() { try { var r = await api('/api/me'); if(!r.authenticated) window.location.href = '/login'; else loadAll(); } catch(e){} }
async function doLogout() { try { await api('/api/logout', {method:'POST'}); } catch(e){} window.location.href = '/login'; }

function switchTab(tab, el) {
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active')); if(el) el.classList.add('active');
  document.querySelectorAll('.tab-content').forEach(t => t.classList.add('hidden')); var target = $id('tab-'+tab); if(target) target.classList.remove('hidden');
  closeSidebar();
  if(tab==='dashboard') loadDashboard();
  if(tab==='users') loadUsers();
  if(tab==='inbounds') loadInbounds();
  if(tab==='worker') loadWorker();
}
function toggleSidebar() { $id('sidebar').classList.toggle('open'); $id('sidebar-backdrop').classList.toggle('show'); }
function closeSidebar() { $id('sidebar').classList.remove('open'); $id('sidebar-backdrop').classList.remove('show'); }

async function loadAll() { loadDashboard(); loadUsers(); loadInbounds(); loadWorker(); setTimeout(updateNeonBars, 500); }

var liveInterval = null;
async function loadDashboard() {
  try {
    var s = await api('/stats');
    $id('s-active-users').textContent = s.active_users + ' / ' + s.total_users;
    $id('s-traffic').textContent = (s.traffic_usage_gb || 0).toFixed(2);
    $id('s-active-configs').textContent = s.active_links || 0;
    $id('s-online-servers').textContent = '1';
    renderUsersTable(ALL_USERS, 'dash-users-table');
    if(!liveInterval) liveInterval = setInterval(refreshLiveStats, 4000);
  } catch(e) {}
}
async function refreshLiveStats() {
  try {
    var st = await api('/api/server/stats');
    if($id('bar-cpu')) $id('bar-cpu').style.width = Math.min(st.cpu_percent||0, 100) + '%';
    if($id('bar-ram')) $id('bar-ram').style.width = Math.min(st.ram_percent||0, 100) + '%';
    if($id('bar-disk')) $id('bar-disk').style.width = Math.min(st.disk_percent||0, 100) + '%';
    if($id('live-cpu')) $id('live-cpu').textContent = (st.cpu_percent||'--');
    if($id('srv-cpu')) $id('srv-cpu').textContent = (st.cpu_percent||'--') + '%';
    if($id('srv-ram')) $id('srv-ram').textContent = (st.ram_used_gb||'?') + '/' + (st.ram_total_gb||'?') + ' GB';
    if($id('srv-disk')) $id('srv-disk').textContent = (st.disk_used_gb||'?') + '/' + (st.disk_total_gb||'?') + ' GB';
    if($id('srv-net')) $id('srv-net').textContent = (st.net_sent_mb||0) + ' MB/s';
  } catch(e) {}
}
function updateNeonBars() {
  api('/api/server/resources').then(d => {
    if(d.error) return;
    if($id('cpu-val')) $id('cpu-val').textContent = d.cpu_percent.toFixed(0)+'% / '+d.cpu_count+' cores';
    if($id('cpu-bar')) $id('cpu-bar').style.width = d.cpu_percent+'%';
    if($id('ram-val')) $id('ram-val').textContent = d.ram_used_gb.toFixed(1)+' / '+d.ram_total_gb.toFixed(1)+' GB';
    if($id('ram-bar')) $id('ram-bar').style.width = d.ram_percent+'%';
    if($id('disk-val')) $id('disk-val').textContent = d.disk_percent.toFixed(0)+'% / '+d.disk_total_gb.toFixed(0)+' GB';
    if($id('disk-bar')) $id('disk-bar').style.width = d.disk_percent+'%';
  }).catch(()=>{});
  setTimeout(updateNeonBars, 3000);
}

// ─── Users ───
async function loadUsers() {
  try { var d = await api('/api/users'); ALL_USERS = d.users || []; renderUsers(); } catch(e) {}
}
function renderUsers() {
  var el = $id('users-list'); if(!ALL_USERS.length) { el.innerHTML = '<div class="empty">'+t('noUsers')+'</div>'; return; }
  var html = '<div class="tbl"><table><thead><tr><th>'+t('username')+'</th><th>'+t('proto')+'</th><th>'+t('volume')+'</th><th>'+t('expiry')+'</th><th>'+t('status')+'</th><th>'+t('action')+'</th></tr></thead><tbody>';
  html += ALL_USERS.map(u => {
    var pct = u.traffic_limit_bytes ? Math.min((u.traffic_used_bytes/u.traffic_limit_bytes)*100, 100) : 0;
    var exp = u.expire_at ? Math.ceil((new Date(u.expire_at)-new Date())/86400000) : null;
    var expT = exp===null ? t('unlimited') : exp<=0 ? t('expired') : exp+t('daysUnit');
    return `<tr><td><b>${esc(u.username)}</b></td>
      <td><span class="badge badge-p">${esc(u.protocol.toUpperCase())}</span></td>
      <td><div style="font-size:11px">${fmtBytes(u.traffic_used_bytes)} / ${u.traffic_limit_bytes ? fmtBytes(u.traffic_limit_bytes) : t('unlimited')}</div><div class="pbar"><div class="pbar-f" style="width:${pct}%"></div></div></td>
      <td>${expT}</td>
      <td><span class="badge ${u.status==='active'?'badge-g':'badge-r'}">${t(u.status)}</span></td>
      <td><div class="act-row">
        <button class="btn btn-sm btn-g" onclick="viewCfg('${esc(u.user_id)}')">${t('config')}</button>
        <button class="btn btn-sm btn-r" onclick="deleteUser('${esc(u.user_id)}')">${t('delete')}</button>
      </div></td></tr>`;
  }).join('');
  html += '</tbody></table></div>';
  el.innerHTML = html;
}
function renderUsersTable(users, id) {
  var el = $id(id); if(!el) return;
  if(!users.length) { el.innerHTML = `<tr><td colspan="6" style="text-align:center;padding:20px">${t('noUsers')}</td></tr>`; return; }
  el.innerHTML = users.slice(0,5).map(u => {
    var pct = u.traffic_limit_bytes ? Math.min((u.traffic_used_bytes/u.traffic_limit_bytes)*100, 100) : 0;
    var exp = u.expire_at ? Math.ceil((new Date(u.expire_at)-new Date())/86400000) : null;
    var expT = exp===null ? t('unlimited') : exp<=0 ? t('expired') : exp+t('daysUnit');
    return `<tr><td><b>${esc(u.username)}</b></td>
      <td><span class="badge badge-p">${esc(u.protocol.toUpperCase())}</span></td>
      <td><div style="font-size:11px">${fmtBytes(u.traffic_used_bytes)} / ${u.traffic_limit_bytes ? fmtBytes(u.traffic_limit_bytes) : t('unlimited')}</div><div class="pbar"><div class="pbar-f" style="width:${pct}%"></div></div></td>
      <td>${expT}</td>
      <td><span class="badge ${u.status==='active'?'badge-g':'badge-r'}">${t(u.status)}</span></td>
      <td><button class="btn btn-sm btn-g" onclick="viewCfg('${esc(u.user_id)}')">${t('config')}</button></td></tr>`;
  }).join('');
}

var cuInboundState = { picks: {} };
function openCreateUser() {
  $id('cu-name').value = ''; $id('cu-vol').value = '20'; $id('cu-exp').value = '30'; $id('cu-conn').value = '2';
  cuInboundState.picks = {}; ALL_IB.forEach(ib => cuInboundState.picks[ib.inbound_id] = true); cuRenderInbounds();
  openModal('mod-user');
}
function cuRenderInbounds() {
  var wrap = $id('cu-inbound'); if(!wrap) return;
  wrap.innerHTML = ALL_IB.map(ib => {
    var sel = cuInboundState.picks[ib.inbound_id] ? 'selected' : '';
    return `<div class="ib-pick ${sel}" data-id="${esc(ib.inbound_id)}" onclick="cuToggleIbPick(this)">
      <div class="ib-pick-ic"><span class="material-symbols-outlined">cloud</span></div>
      <div class="ib-pick-info"><div class="ib-pick-name">${esc(ib.name)}</div><div class="ib-pick-meta">${esc((ib.protocol||'').toUpperCase())}</div></div>
      <div class="ib-pick-check"><span class="material-symbols-outlined">check</span></div>
    </div>`;
  }).join('') || `<span style="font-size:11px;color:var(--txt2)">${t('noInbounds')}</span>`;
}
function cuToggleIbPick(el) { el.classList.toggle('selected'); cuInboundState.picks[el.getAttribute('data-id')] = el.classList.contains('selected'); }
async function submitCreateUser(e) {
  e.preventDefault(); var btn = $id('cu-submit'); btn.disabled = true;
  var ibs = Object.keys(cuInboundState.picks).filter(k => cuInboundState.picks[k]);
  try {
    var r = await api('/api/users', {method: 'POST', body: {
      username: $id('cu-name').value,
      traffic_limit_gb: $id('cu-vol-u').value==='GB' ? parseFloat($id('cu-vol').value) : parseFloat($id('cu-vol').value)/1024,
      expire_days: $id('cu-exp-u').value==='months' ? parseInt($id('cu-exp').value)*30 : parseInt($id('cu-exp').value),
      concurrent_connections: parseInt($id('cu-conn').value) || 2,
      inbound_ids: ibs
    }});
    toast(t('userCreated'), 'ok'); closeModal('mod-user'); loadAll();
  } catch(e) { toast(e.message, 'err'); }
  btn.disabled = false;
}
async function deleteUser(uid) {
  if(!confirm(t('confirmDeleteUser'))) return;
  try { await api('/api/users/'+uid, {method:'DELETE'}); toast(t('toast.userDeleted'), 'ok'); loadAll(); } catch(e) { toast(e.message, 'err'); }
}
async function viewCfg(uid) {
  try {
    var r = await api('/api/users/'+uid+'/config');
    $id('cfg-code').textContent = r.config || t('noCfg');
    openModal('mod-cfg');
  } catch(e) { toast(e.message, 'err'); }
}
function copyCfg() { navigator.clipboard.writeText($id('cfg-code').textContent).then(() => toast(t('copied'), 'ok')); }

// ─── Inbounds ───
async function loadInbounds() {
  try { var d = await api('/api/inbounds'); ALL_IB = d.inbounds || []; renderInbounds(); } catch(e) {}
}
function renderInbounds() {
  var el = $id('inbounds-list'); if(!ALL_IB.length) { el.innerHTML = '<div class="empty">'+t('noInbounds')+'</div>'; return; }
  el.innerHTML = '<div class="stats" style="grid-template-columns:repeat(auto-fill,minmax(280px,1fr))">' + ALL_IB.map(ib => `
    <div class="stat glass" style="text-align:right">
      <div style="display:flex;justify-content:space-between;margin-bottom:12px;border-bottom:1px solid var(--border);padding-bottom:12px">
        <strong style="font-size:16px">${esc(ib.name)}</strong><span class="badge ${ib.protocol==='reality'?'badge-p':'badge-b'}">${(ib.protocol||'vless').toUpperCase()}</span>
      </div>
      <div style="font-size:12px;color:var(--txt2);line-height:2">
        🌍 <b>دامنه:</b> <span dir="ltr">${ib.external_domain||'—'}</span><br>
        🔌 <b>پورت:</b> ${ib.port||'—'}<br>
        🛡️ <b>شبکه:</b> ${(ib.network||'tcp').toUpperCase()} | <b>امنیت:</b> ${(ib.security||'none').toUpperCase()}<br>
        👥 <b>کاربران متصل:</b> ${ib.users_count||0}
      </div>
      <div style="margin-top:16px;display:flex;gap:8px;border-top:1px solid var(--border);padding-top:16px">
        <button class="btn btn-sm btn-b" style="flex:1;justify-content:center" onclick="editInbound('${ib.inbound_id}')">${t('edit')}</button>
        <button class="btn btn-sm btn-r" style="flex:1;justify-content:center" onclick="deleteInbound('${ib.inbound_id}')">${t('delete')}</button>
      </div>
    </div>
  `).join('') + '</div>';
}
function openCreateInbound() {
  $id('ib-title').textContent = t('createInbound'); $id('ib-id').value = ''; $id('ib-name').value = '';
  $id('ib-port').value = '8443'; $id('ib-security').value = 'tls'; $id('ib-network').value = 'ws';
  $id('ib-extdomain').value = ''; $id('ib-extport').value = '443'; $id('ib-sni').value = 'is1-ssl.mzstatic.com';
  onSecurityChange(); onNetworkChange(); openModal('mod-inbound');
}
function editInbound(iid) {
  var ib = ALL_IB.find(x => x.inbound_id === iid); if(!ib) return;
  $id('ib-title').textContent = t('editInbound'); $id('ib-id').value = iid; $id('ib-name').value = ib.name || '';
  $id('ib-port').value = ib.port || '8443'; $id('ib-security').value = (ib.protocol==='reality'||ib.security==='reality')?'reality':(ib.security||'tls');
  $id('ib-network').value = ib.network || 'ws'; $id('ib-extdomain').value = ib.external_domain || '';
  $id('ib-extport').value = ib.external_port || '443'; $id('ib-sni').value = ib.sni || 'is1-ssl.mzstatic.com';
  var rs = ib.reality_settings || {};
  $id('ib-privkey').value = rs.private_key || ''; $id('ib-pubkey').value = rs.public_key || '';
  $id('ib-shortids').value = rs.short_id || ''; $id('ib-kmx').value = rs.kmx || '/';
  $id('ib-dest').value = rs.dest || 'is1-ssl.mzstatic.com:443'; $id('ib-servernames').value = rs.sni || 'is1-ssl.mzstatic.com';
  $id('ib-wspath').value = (ib.ws_settings||{}).path || '/'; $id('ib-xhttppath').value = (ib.xhttp_settings||{}).path || '/';
  $id('ib-xhttp-mode').value = (ib.xhttp_settings||{}).mode || 'auto'; $id('ib-grpc-svc').value = (ib.grpc_settings||{}).serviceName || 'grpc';
  onSecurityChange(); onNetworkChange(); openModal('mod-inbound');
}
async function submitInbound(e) {
  e.preventDefault(); var btn = $id('ib-submit'); btn.disabled = true;
  var iid = $id('ib-id').value, sec = $id('ib-security').value, net = $id('ib-network').value;
  var body = {
    name: $id('ib-name').value, protocol: 'vless', port: parseInt($id('ib-port').value) || 8443,
    external_port: parseInt($id('ib-extport').value) || null, external_domain: $id('ib-extdomain').value || '',
    network: net, security: sec, sni: $id('ib-sni').value || 'is1-ssl.mzstatic.com'
  };
  if(sec === 'reality') {
    body.reality_settings = { private_key: $id('ib-privkey').value, public_key: $id('ib-pubkey').value, dest: $id('ib-dest').value, server_names: ($id('ib-servernames').value||'').split(',').map(s=>s.trim()).filter(Boolean), short_ids: $id('ib-shortids').value, kmx: $id('ib-kmx').value };
  }
  if(net === 'ws') body.ws_settings = { path: $id('ib-wspath').value };
  else if(net === 'xhttp') body.xhttp_settings = { path: $id('ib-xhttppath').value, mode: $id('ib-xhttp-mode').value };
  else if(net === 'grpc') body.grpc_settings = { serviceName: $id('ib-grpc-svc').value };
  
  try {
    await api('/api/inbounds' + (iid ? '/'+iid : ''), {method: iid ? 'PATCH' : 'POST', body: body});
    toast(iid ? t('inboundUpdated') : t('inboundCreated'), 'ok'); closeModal('mod-inbound'); loadInbounds();
  } catch(e) { toast(e.message, 'err'); }
  btn.disabled = false;
}
async function deleteInbound(iid) {
  if(!confirm(t('confirmDeleteInbound'))) return;
  try { await api('/api/inbounds/'+iid, {method:'DELETE'}); toast(t('inboundDeleted'), 'ok'); loadInbounds(); } catch(e) { toast(e.message, 'err'); }
}
function onSecurityChange() { $id('ib-reality-fields').classList.toggle('hidden', $id('ib-security').value !== 'reality'); }
function onNetworkChange() { var net = $id('ib-network').value; $id('ib-ws-fields').classList.toggle('hidden', net!=='ws'); $id('ib-xhttp-fields').classList.toggle('hidden', net!=='xhttp'); $id('ib-grpc-fields').classList.toggle('hidden', net!=='grpc'); }
async function generateRealityKeysUI() { try { var r = await api('/api/tools/generate-reality-keys', {method:'POST'}); $id('ib-privkey').value = r.private_key; $id('ib-pubkey').value = r.public_key; toast(t('keysGenerated'), 'ok'); } catch(e) { toast(t('errKeyGen'), 'err'); } }
async function generateShortId() { var iid = $id('ib-id').value; if(!iid) { var h=''; for(var i=0;i<10;i++) h+='0123456789abcdef'[Math.floor(Math.random()*16)]; $id('ib-shortids').value=h; toast(t('shortIdGen'),'ok'); return; } try { var r = await api('/api/inbounds/'+iid+'/generate-short-id', {method:'POST'}); $id('ib-shortids').value = r.short_id; toast(t('shortIdNew'),'ok'); } catch(e) {} }

// ─── Worker ───
var WK_STATE = {connected: false};
async function loadWorker() {
  try {
    var w = await api('/api/worker'); WK_STATE = w; var conn = !!w.connected;
    if($id('worker-setup')) $id('worker-setup').classList.toggle('hidden', conn);
    if($id('worker-managed')) $id('worker-managed').classList.toggle('hidden', !conn);
    if($id('worker-badge')) { $id('worker-badge').textContent = conn ? t('connected') : t('disconnected'); $id('worker-badge').className = 'badge '+(conn?'badge-g':'badge-r'); }
    if(conn) {
      if($id('worker-status')) { $id('worker-status').textContent = t('connected'); $id('worker-status').className = 'badge badge-g'; }
      if($id('worker-url')) { $id('worker-url').textContent = w.worker_url; $id('worker-url').href = w.worker_url; }
      renderWorkerProxies();
    }
  } catch(e) {}
}
function renderWorkerProxies() {
  var el = $id('worker-proxies'); if(!el) return;
  var list = WK_STATE.proxies || [];
  if(!list.length) { el.innerHTML = '<div class="empty">'+t('noProxyYet')+'</div>'; return; }
  el.innerHTML = '<div class="tbl"><table><thead><tr><th>Code</th><th>Country</th><th>Proxy</th><th>Port</th><th>Action</th></tr></thead><tbody>' +
    list.map(p => `<tr><td dir="ltr"><b>${esc(p.code.toUpperCase())}</b></td><td>${esc(p.country)}</td><td dir="ltr" style="font-family:monospace">${esc(p.proxy)}</td><td>${p.port}</td><td><button class="btn btn-sm btn-r" onclick="workerDelProxy('${p.code}')">${t('delete')}</button></td></tr>`).join('') +
    '</tbody></table></div>';
}
async function workerSetup() {
  var t = $id('wk-token').value.trim(), a = $id('wk-account').value.trim(), e = $id('wk-email').value.trim();
  if(!t || !a) { toast(t('workerFillAll'), 'err'); return; }
  try { await api('/api/worker/setup', {method:'POST', body:{token:t, account_id:a, email:e}}); $id('wk-token').value=''; toast(t('workerConnected'), 'ok'); loadWorker(); } catch(e) { toast(e.message, 'err'); }
}
async function workerDisconnect() { if(!confirm(t('confirmRemoveWorker'))) return; try { await api('/api/worker', {method:'DELETE'}); toast(t('workerRemoved'), 'ok'); loadWorker(); } catch(e) { toast(e.message, 'err'); } }
async function workerAddProxy() {
  var c = prompt(t('proxyCodePrompt')); if(!c) return; var co = prompt(t('proxyCountryPrompt')); if(!co) return;
  var pr = prompt(t('proxyHostPrompt')); if(!pr) return; var po = prompt(t('proxyPortPrompt'), '443');
  try { await api('/api/worker/proxies', {method:'POST', body:{code:c.trim().toLowerCase(), country:co, proxy:pr, port:parseInt(po)||443}}); toast(t('proxySaved'), 'ok'); loadWorker(); } catch(e) { toast(e.message, 'err'); }
}
async function workerDelProxy(code) { if(!confirm(t('confirmDelProxy'))) return; try { await api('/api/worker/proxies/'+code, {method:'DELETE'}); toast(t('proxyDeleted'), 'ok'); loadWorker(); } catch(e) { toast(e.message, 'err'); } }

// ─── Settings ───
async function changePassword(e) {
  e.preventDefault();
  try { await api('/api/change-password', {method:'POST', body:{current_password: $id('cp-old').value, new_password: $id('cp-new').value}}); toast(t('toast.passChanged'), 'ok'); $id('cp-old').value=''; $id('cp-new').value=''; } catch(e) { toast(e.message, 'err'); }
}
function toggleThemeMode() { setTheme(document.documentElement.classList.contains('dark') ? 'light' : 'dark'); }

document.addEventListener('DOMContentLoaded', () => { checkAuth(); });
function openModal(id) { $id(id).classList.add('show'); }
function closeModal(id) { $id(id).classList.remove('show'); }
document.querySelectorAll('.modal').forEach(m => {
  var x = document.createElement('button'); x.className = 'modal-x'; x.innerHTML = '✕'; x.onclick = (e) => { e.stopPropagation(); closeModal(m.id); };
  m.querySelector('.modal-c').appendChild(x);
  m.addEventListener('click', e => { if(e.target === m) closeModal(m.id); });
});

</script>
</body>
</html>
"""

PUBLIC_HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl" class="dark">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
<title>White Panel</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet"/>
<script>
tailwind.config = {
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: { sans: ['Inter', 'sans-serif'], mono: ['JetBrains Mono', 'monospace'] }
    }
  }
};
</script>
<style>
    body { background-color: #000000; color: #ffffff; font-family: 'Inter', sans-serif; -webkit-font-smoothing: antialiased; overflow-x: hidden; }
    .bg-ambient {
        position: fixed; inset: 0; z-index: -2;
        background: radial-gradient(circle at 50% 0%, rgba(99, 102, 241, 0.15), transparent 60%);
    }
    .glass-panel {
        background: rgba(255, 255, 255, 0.02); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08); box-shadow: 0 20px 40px rgba(0,0,0,0.5);
    }
    .btn-neon {
        display: flex; align-items: center; justify-content: center; gap: 8px; width: 100%;
        padding: 14px; border-radius: 14px; font-weight: 600; font-size: 14px; color: #fff;
        background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.3s cubic-bezier(0.22, 1, 0.36, 1); cursor: pointer;
    }
    .btn-neon:hover {
        background: rgba(255,255,255,0.1); border-color: rgba(99, 102, 241, 0.5);
        transform: translateY(-2px); box-shadow: 0 8px 20px rgba(99,102,241,0.2);
    }
    .btn-primary { background: #ffffff; color: #000000; }
    .btn-primary:hover { background: #e5e5e5; box-shadow: 0 0 20px rgba(255,255,255,0.2); }
    
    .progress-ring { transform: rotate(-90deg); transform-origin: 50% 50%; stroke-linecap: round; transition: stroke-dashoffset 1s ease-out; }
    .cfg-card {
        background: rgba(0,0,0,0.4); border: 1px solid rgba(255,255,255,0.05); border-radius: 16px;
        padding: 16px; margin-bottom: 12px; transition: border-color 0.2s;
    }
    .cfg-card:hover { border-color: rgba(99,102,241,0.3); }
    
    @keyframes fade-in { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    .animate-in { animation: fade-in 0.6s cubic-bezier(0.22, 1, 0.36, 1) both; }
    
    #toast {
        position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%) translateY(20px);
        background: #fff; color: #000; padding: 12px 24px; border-radius: 99px;
        font-weight: 600; font-size: 13px; opacity: 0; transition: all 0.3s; z-index: 100; box-shadow: 0 10px 30px rgba(255,255,255,0.2);
    }
    #toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }
</style>
</head>
<body>
<div class="bg-ambient"></div>
<div class="max-w-xl mx-auto px-4 py-8 min-h-screen flex flex-col gap-6 animate-in">

    __ANNOUNCEMENT_BLOCK__

    <div class="flex items-center justify-center gap-3 mb-2">
        <span class="material-symbols-outlined text-3xl text-indigo-400">cloud</span>
        <h1 class="text-2xl font-bold tracking-tight">Subscription</h1>
    </div>

    <!-- Stats Card -->
    <div id="stats-container" class="glass-panel rounded-3xl p-8 flex flex-col items-center justify-center relative overflow-hidden">
        <div class="text-center text-gray-500 mb-8">Loading secure profile...</div>
    </div>

    <!-- Smart Import Card -->
    <div class="glass-panel rounded-3xl p-6 hidden" id="import-card">
        <h2 class="text-lg font-bold mb-1">One-Click Import</h2>
        <p class="text-xs text-gray-400 mb-4">Auto-detected OS: <span id="os-name" class="text-indigo-400 font-semibold">Unknown</span></p>
        <div class="flex flex-col gap-3" id="import-buttons"></div>
        
        <div class="mt-4 pt-4 border-t border-white/10">
            <button onclick="copySubLink()" class="btn-neon"><span class="material-symbols-outlined text-lg">link</span> Copy Subscription Link</button>
        </div>
    </div>

    <!-- Configs List -->
    <div class="glass-panel rounded-3xl p-6 hidden" id="configs-card">
        <h2 class="text-lg font-bold mb-4">Manual Configs</h2>
        <div id="configs-list" class="flex flex-col gap-2"></div>
    </div>

</div>

<div id="toast"></div>

<script>
const UUID_KEY = '__UUID_KEY__';
const SUB_URL = '__SUB_URL__' || (location.protocol + '//' + location.host + '/sub-group/' + UUID_KEY);

function getOS() {
    let ua = navigator.userAgent;
    if (/iPad|iPhone|iPod/.test(ua) && !window.MSStream) return "iOS";
    if (/android/i.test(ua)) return "Android";
    if (/Mac/i.test(ua)) return "macOS";
    if (/Win/i.test(ua)) return "Windows";
    return "Unknown";
}

function toast(msg) {
    let t = document.getElementById('toast');
    t.textContent = msg; t.classList.add('show');
    setTimeout(() => t.classList.remove('show'), 2500);
}

function copySubLink() {
    navigator.clipboard.writeText(SUB_URL).then(() => toast('Subscription Link Copied!')).catch(()=>toast('Copy failed'));
}

function copyText(txt) {
    navigator.clipboard.writeText(txt).then(() => toast('Config Copied!')).catch(()=>toast('Copy failed'));
}

function fmtB(b) { if(!b) return '0 B'; let u=['B','KB','MB','GB','TB'], i=0; while(b>=1024){b/=1024; i++;} return b.toFixed(2)+' '+u[i]; }

async function init() {
    try {
        let r = await fetch('/api/public/sub/' + UUID_KEY);
        if(!r.ok) {
            let userReq = await fetch('/api/sub/' + encodeURIComponent(UUID_KEY));
            if(!userReq.ok) throw new Error('Profile not found');
            renderUser(await userReq.json());
        } else {
            renderGroup(await r.json());
        }
    } catch(e) {
        document.getElementById('stats-container').innerHTML = `<div class="text-red-400 font-semibold"><span class="material-symbols-outlined align-middle">error</span> ${e.message}</div>`;
    }
}

function renderUser(d) {
    let used = d.traffic_used_bytes || 0, limit = d.traffic_limit_bytes || 0;
    let pct = limit ? Math.min(100, (used/limit)*100) : 0;
    let days = (d.expire_days === null || d.expire_days === undefined) ? '∞' : d.expire_days;
    
    // Circle Math
    let circ = 2 * Math.PI * 46;
    let off = circ - ((limit ? (100-pct)/100 : 1) * circ);

    document.getElementById('stats-container').innerHTML = `
        <h2 class="text-sm font-semibold text-gray-400 tracking-widest mb-6">TIME LEFT</h2>
        <div class="relative w-36 h-36 flex items-center justify-center mb-6">
            <svg class="w-full h-full" viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="46" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="6"></circle>
                <circle cx="50" cy="50" r="46" fill="none" stroke="#6366f1" stroke-width="6" stroke-dasharray="${circ}" stroke-dashoffset="${off}" class="progress-ring" style="filter:drop-shadow(0 0 8px rgba(99,102,241,0.6));"></circle>
            </svg>
            <div class="absolute flex flex-col items-center">
                <span class="text-3xl font-extrabold" style="text-shadow: 0 0 15px rgba(255,255,255,0.3);">${days}</span>
                <span class="text-[10px] text-gray-400 uppercase tracking-widest mt-1">Days</span>
            </div>
        </div>
        <div class="w-full bg-black/40 rounded-2xl p-4 border border-white/5 flex flex-col gap-3">
            <div class="flex justify-between items-center">
                <span class="text-xs text-gray-400 font-semibold tracking-wider">USAGE</span>
                <span class="text-sm font-bold">${fmtB(used)} <span class="text-gray-500">/ ${limit?fmtB(limit):'∞'}</span></span>
            </div>
            <div class="h-1.5 w-full bg-white/10 rounded-full overflow-hidden">
                <div class="h-full bg-gradient-to-r from-indigo-500 to-purple-500 rounded-full shadow-[0_0_10px_rgba(99,102,241,0.8)]" style="width:${pct}%"></div>
            </div>
        </div>
    `;

    renderSmartImport();
    
    let cfgs = (d.configs || []).filter(c => c && !c.includes('%F0%9F%93%8A')); // remove status config
    if(!cfgs.length && d.vless_link) cfgs = [d.vless_link];
    
    if(cfgs.length) {
        document.getElementById('configs-card').classList.remove('hidden');
        document.getElementById('configs-list').innerHTML = cfgs.map((c, i) => `
            <div class="cfg-card cursor-pointer group" onclick="copyText('${esc(c).replace(/'/g,"\\'")}')">
                <div class="flex justify-between items-center mb-2">
                    <span class="font-bold text-sm group-hover:text-indigo-400 transition-colors">Node #${i+1}</span>
                    <span class="material-symbols-outlined text-gray-500 group-hover:text-indigo-400 transition-colors text-sm">content_copy</span>
                </div>
                <div class="text-[10px] text-gray-500 font-mono truncate">${esc(c)}</div>
            </div>
        `).join('');
    }
}

function renderGroup(d) {
    document.getElementById('stats-container').innerHTML = `
        <div class="text-center">
            <h2 class="text-3xl font-extrabold tracking-tight mb-2">${esc(d.name)}</h2>
            <p class="text-sm text-gray-400 mb-6">${esc(d.desc||'Premium Group Subscription')}</p>
            <div class="flex gap-4 justify-center">
                <div class="bg-black/40 border border-white/5 rounded-2xl p-4 min-w-[100px]">
                    <div class="text-2xl font-bold text-indigo-400">${d.links ? d.links.length : 0}</div>
                    <div class="text-[10px] text-gray-500 uppercase tracking-widest mt-1">Nodes</div>
                </div>
                <div class="bg-black/40 border border-white/5 rounded-2xl p-4 min-w-[100px]">
                    <div class="text-2xl font-bold text-purple-400">${esc(d.total_used_fmt||'0 B')}</div>
                    <div class="text-[10px] text-gray-500 uppercase tracking-widest mt-1">Usage</div>
                </div>
            </div>
        </div>
    `;
    renderSmartImport();
}

function renderSmartImport() {
    let os = getOS();
    document.getElementById('os-name').textContent = os;
    document.getElementById('import-card').classList.remove('hidden');
    let enc = encodeURIComponent(SUB_URL);
    let html = '';
    
    if(os === 'iOS') {
        html += `<a href="v2box://install-sub?url=${enc}" class="btn-neon btn-primary"><img src="https://raw.githubusercontent.com/v2rayA/v2rayA/master/gui/public/favicon.ico" class="w-5 h-5 rounded-md grayscale opacity-80"/> Open in V2Box</a>`;
        html += `<a href="streisand://import/${enc}" class="btn-neon"><span class="material-symbols-outlined text-lg">flight_takeoff</span> Open in Streisand</a>`;
    } else if(os === 'Android') {
        html += `<a href="v2rayng://install-sub?url=${enc}" class="btn-neon btn-primary"><span class="material-symbols-outlined text-lg">android</span> Open in v2rayNG</a>`;
        html += `<a href="hiddify://install-sub?url=${enc}" class="btn-neon"><span class="material-symbols-outlined text-lg">rocket_launch</span> Open in Hiddify</a>`;
    } else {
        html += `<a href="v2rayn://install-sub?url=${enc}" class="btn-neon btn-primary"><span class="material-symbols-outlined text-lg">desktop_windows</span> Open in v2rayN</a>`;
        html += `<a href="hiddify://install-sub?url=${enc}" class="btn-neon"><span class="material-symbols-outlined text-lg">rocket_launch</span> Open in Hiddify</a>`;
    }
    document.getElementById('import-buttons').innerHTML = html;
}

init();
</script>
</body></html>"""

def get_public_page_html(uuid_key: str, sub_url: str = "", announcement: str = "") -> str:
    html = PUBLIC_HTML_TEMPLATE
    html = html.replace("__UUID_KEY__", str(uuid_key))
    html = html.replace("__SUB_URL__", str(sub_url))
    
    if announcement:
        ann_block = f"""
        <div style="background: rgba(99, 102, 241, 0.1); border: 1px solid rgba(99, 102, 241, 0.3); color: #818cf8; padding: 16px 24px; border-radius: 20px; text-align: center; font-weight: 600; font-size: 13px; backdrop-filter: blur(12px); box-shadow: 0 10px 30px rgba(0,0,0,0.5); animation: pulse 2s infinite;">
            <span class="material-symbols-outlined align-middle mr-2" style="font-size: 18px;">campaign</span> {announcement}
        </div>
        """
        html = html.replace("__ANNOUNCEMENT_BLOCK__", ann_block)
    else:
        html = html.replace("__ANNOUNCEMENT_BLOCK__", "")
        
    return html