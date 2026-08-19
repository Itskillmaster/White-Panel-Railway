/* ─────────────────────────────────────────────────────────
   SPiDER Sub Collection — shared animation/effects layer
   Drop right after your render() call in each theme file, or call
   FX.revealAll() at the end of render(d).
───────────────────────────────────────────────────────── */
(function (global) {
  'use strict';

  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function onReady(cb) {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', cb);
    } else {
      cb();
    }
  }

  /* 3D perspective container that lets children rotate in space */
  function initScene() {
    const scene = document.getElementById('scene');
    if (scene) {
      scene.style.perspective = '1400px';
      scene.style.perspectiveOrigin = '50% 40%';
    }
  }

  /* reveal a single element with cascading delay */
  function reveal(el, index) {
    if (!el) return;
    if (prefersReduced) { el.style.opacity = '1'; return; }
    const delay = 80 + (index ? index * 90 : 0);
    el.style.transitionDelay = delay + 'ms';
    el.classList.add('revealed');
  }

  /* reveal everything with .reveal */
  function revealAll(scope) {
    const root = scope || document.getElementById('app');
    if (!root) return;
    const items = root.querySelectorAll('.reveal');
    items.forEach((el, i) => reveal(el, i));
  }

  /* floating hover parallax on .parallax cards */
  function attachHover() {
    const cards = document.querySelectorAll('.parallax');
    cards.forEach(c => {
      c.style.transformStyle = 'preserve-3d';
      c.style.transition = 'transform .42s cubic-bezier(.22,1,.36,1),box-shadow .42s ease';
      c.style.cursor = 'pointer';
      c.addEventListener('mouseenter', () => {
        if (prefersReduced) return;
        c.style.transform = 'translateY(-6px) rotateX(3deg) rotateY(-2deg) scale(1.02)';
      });
      c.addEventListener('mouseleave', () => {
        if (prefersReduced) return;
        c.style.transform = '';
      });
    });
  }

  /* gentle idle sway for .sway elements */
  function startSway() {
    const items = document.querySelectorAll('.sway');
    if (prefersReduced || !items.length) return;
    let frame = 0;
    function loop() {
      frame++;
      const t = frame * 0.016;
      items.forEach((el, i) => {
        const phase = (i * 0.4 + t * 0.6) % (Math.PI * 2);
        const r = Math.sin(phase) * 0.5;
        el.style.transform = `rotateX(${r}deg) rotateY(${(Math.sin(phase * 0.7) * 0.4).toFixed(2)}deg)`;
      });
      requestAnimationFrame(loop);
    }
    requestAnimationFrame(loop);
  }

  /* expose */
  global.FX = { reveal, revealAll, attachHover, startSway, onReady, prefersReduced };
  onReady(() => {
    initScene();
    attachHover();
    startSway();
  });
})((typeof window !== 'undefined') ? window : {});

/* ── tiny CSS injected inline so themes don't need a second stylesheet ── */
(function injectFX() {
  if (document.getElementById('__fx__')) return;
  const style = document.createElement('style');
  style.id = '__fx__';
  style.textContent = `
/* shared reveal: fades + slides up from 24px, with deferred 3D snap */
.reveal{
  opacity:0;
  transform:translateY(26px) scale(.96);
  transition:
    opacity .62s ease,
    transform .64s cubic-bezier(.22,1,.36,1),
    box-shadow .58s ease;
}
.revealed{
  opacity:1;
  transform:translateY(0) scale(1);
  animation:sway .9s ease .24s both;
}
@media (prefers-reduced-motion: reduce){
  .reveal,.revealed{transition:none!important;transform:none!important;animation:none!important}
}
@keyframes sway{
  0%,100%{transform:rotateX(0) rotateY(0) scale(1)}
  50%{transform:rotateX(.4deg) rotateY(-.4deg) scale(1.004)}
}
/* shared 3D lift on hover for anything with .parallax */
.parallax{transform-style:preserve-3d;will-change:transform}
/* soft specular highlight that rides with the card so it looks lit */
.specular{
  position:absolute;top:0;left:0;right:0;height:34%;
  background:linear-gradient(180deg,rgba(255,255,255,.16),transparent);
  opacity:.0;pointer-events:none;transition:opacity .32s ease;border-radius:inherit
}
.parallax:hover .specular{opacity:.55}
.parallax:hover{box-shadow:0 22px 50px rgba(0,0,0,.55),0 0 26px rgba(0,225,193,.08)}
/* neon inner-glow helper */
.glow-cyan{box-shadow:0 0 10px rgba(0,225,193,.38),inset 0 0 8px rgba(0,225,193,.24)}
.glow-blue{box-shadow:0 0 10px rgba(90,200,250,.38),inset 0 0 8px rgba(90,200,250,.24)}
.glow-pink{box-shadow:0 0 10px rgba(255,64,129,.38),inset 0 0 8px rgba(255,64,129,.24)}
.glow-green{box-shadow:0 0 10px rgba(0,230,118,.38),inset 0 0 8px rgba(0,230,118,.24)}
`;
  (document.head || document.documentElement).appendChild(style);
})();
