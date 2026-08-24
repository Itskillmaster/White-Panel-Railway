/* ═══════════════════════════════════════════════════════════════════
   WHITE PANEL · PREMIUM MOTION ENGINE (v2.1)
   - Staggered entrance reveals (MutationObserver, pre-paint = no flash)
   - Precise animated number counters (fa/ar digits aware)
   - Material ink ripples via Web Animations API
   - Pointer-tracked card spotlight (--wx/--wy)
   - Tab transition hook: WPfx.tabIn(el)
   Fully disabled under prefers-reduced-motion.
   ═══════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';
  if (window.WPfx) return;

  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var HOVER = window.matchMedia && window.matchMedia('(hover:hover) and (pointer:fine)').matches;
  if (RM) { window.WPfx = { tabIn: function(){}, counters: function(){}, reveal: function(){} }; return; }

  /* ── config ─────────────────────────────────────────────────────── */
  var STAG = 55, STAG_MAX = 520, COUNTER_MS = 850;

  var UNIT_SEL = '.panel,.stat,.u-card,.cfg-card,.info-card,.log-row,.empty,.lock-card';
  var RIPPLE_SEL = '.btn,.ctrl-btn,.qa-btn,.scn-tab,.theme-toggle,.theme-btn,.lang-btn,.mob-btn,.eye-toggle,.hint-value,.login-btn';
  var SPOT_SEL = '.panel,.stat,.u-card,.cfg-card,.info-card,.tbl';

  function slice(l) { return Array.prototype.slice.call(l); }
  function matches(el, sel) {
    var m = el.matches || el.msMatchesSelector || el.webkitMatchesSelector;
    return m ? m.call(el, sel) : false;
  }

  /* ── 1 · ENTRANCE REVEALS ───────────────────────────────────────── */
  var batch = [], flushTimer = null;

  function playUnit(el, i) {
    if (!el) return;
    var cls = el.tagName === 'TR' ? 'wp-go-row'
            : matches(el, '.modal-c,.login-card') ? 'wp-go-pop'
            : 'wp-go';
    el.style.setProperty('--wp-d', Math.min(i * STAG, STAG_MAX) + 'ms');
    el.classList.remove('wp-go', 'wp-go-row', 'wp-go-pop');
    void el.offsetWidth;              /* restart animation deterministically */
    el.classList.add(cls);
    el.addEventListener('animationend', function h(ev) {
      if (ev.animationName === 'wpUp' || ev.animationName === 'wpFade' || ev.animationName === 'wpPop') {
        el.classList.remove(cls);
        el.removeEventListener('animationend', h);
      }
    });
  }

  function flushBatch() {
    var units = batch; batch = []; flushTimer = null;
    units.forEach(function (el, i) { playUnit(el, i); });
  }

  function enqueue(units) {
    units.forEach(function (u) { if (u && u.nodeType === 1 && !u.classList.contains('wp-go')) batch.push(u); });
    if (batch.length && !flushTimer) flushTimer = requestAnimationFrame(flushBatch);
  }

  /* Map a freshly inserted node → list of animatable units */
  function unitsFor(node) {
    if (node.nodeType !== 1) return [];
    if (matches(node, '.stats')) return slice(node.children);
    if (matches(node, 'tbody')) return slice(node.children);
    if (matches(node, '.u-cards,.cfg-grid')) return slice(node.children);
    if (matches(node, '#dashboard-content,#users-list,#inbounds-list,#logs-list,.content'))
      return slice(node.children).filter(function (c) { return matches(c, UNIT_SEL + ',.stats'); })
        .reduce(function (acc, c) { return acc.concat(matches(c, '.stats') ? slice(c.children) : [c]); }, []);
    if (matches(node, UNIT_SEL)) return [node];
    return [];
  }

  var mo = new MutationObserver(function (muts) {
    for (var i = 0; i < muts.length; i++) {
      var added = muts[i].addedNodes;
      for (var j = 0; j < added.length; j++) enqueue(unitsFor(added[j]));
    }
  });

  /* ── 2 · PRECISE COUNTERS ───────────────────────────────────────── */
  var FA = '۰۱۲۳۴۵۶۷۸۹', AR = '٠١٢٣٤٥٦٧٨٩';
  function toFa(s) { return String(s).replace(/\d/g, function (d) { return FA[d]; }); }
  var TOKEN = /(\d+(?:\.\d+)?)|([۰-۹]+(?:\.[۰-۹]+)?)|([٠-٩]+(?:\.[٠-٩]+)?)/g;

  function easeOutExpo(p) { return p >= 1 ? 1 : 1 - Math.pow(2, -10 * p); }

  function animateText(el) {
    var text = el.textContent;
    if (!text || text.length > 32) return false;
    TOKEN.lastIndex = 0;
    var toks = [], m;
    while ((m = TOKEN.exec(text)) !== null) {
      var raw = m[0], isFa = !!m[2], isAr = !!m[3];
      var ascii = isFa ? raw.replace(/[۰-۹]/g, function (d) { return FA.indexOf(d); })
                  : isAr ? raw.replace(/[٠-٩]/g, function (d) { return AR.indexOf(d); }) : raw;
      var val = parseFloat(ascii);
      if (!isFinite(val)) continue;
      var dot = ascii.indexOf('.');
      toks.push({ s: m.index, e: m.index + raw.length, val: val,
                  dec: dot === -1 ? 0 : ascii.length - dot - 1,
                  fa: isFa });
    }
    if (!toks.length || toks.length > 4) return false;
    var start = performance.now();
    function frame(now) {
      var p = Math.min((now - start) / COUNTER_MS, 1), k = easeOutExpo(p), out = '', last = 0;
      for (var i = 0; i < toks.length; i++) {
        var t = toks[i], v = t.val * k;
        var s = t.dec ? v.toFixed(t.dec) : String(Math.round(v));
        out += text.slice(last, t.s) + (t.fa ? toFa(s) : s);
        last = t.e;
      }
      out += text.slice(last);
      el.textContent = out;
      if (p < 1) requestAnimationFrame(frame);
      else el.classList.add('wp-counted');
    }
    requestAnimationFrame(frame);
    return true;
  }

  function counters(scope) {
    setTimeout(function () {
      slice((scope || document).querySelectorAll('.stat-v,.info-s-val')).forEach(function (box) {
        var leaves = slice(box.querySelectorAll('*')).filter(function (n) {
          return !n.firstElementChild && /\d|[۰-۹]/.test(n.textContent);
        });
        if (leaves.length) leaves.forEach(animateText);
        else animateText(box);
      });
    }, 140);
  }

  /* ── 3 · INK RIPPLES ────────────────────────────────────────────── */
  document.addEventListener('pointerdown', function (e) {
    var t = e.target.closest && e.target.closest(RIPPLE_SEL);
    if (!t || t.disabled) return;
    var cs = getComputedStyle(t);
    if (cs.position === 'static') t.style.position = 'relative';
    if (cs.overflow !== 'hidden') t.style.overflow = 'hidden';
    t.classList.add('wp-rp');
    var r = t.getBoundingClientRect();
    var d = Math.max(r.width, r.height) * 2.2;
    var ink = document.createElement('span');
    ink.className = 'wp-ink';
    ink.style.width = ink.style.height = d + 'px';
    ink.style.left = (e.clientX - r.left - d / 2) + 'px';
    ink.style.top = (e.clientY - r.top - d / 2) + 'px';
    t.appendChild(ink);
    var inkOp = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--wp-ink')) || .16;
    var anim = ink.animate(
      [{ transform: 'scale(0)', opacity: inkOp },
       { transform: 'scale(1)', opacity: 0 }],
      { duration: 540, easing: 'cubic-bezier(.22,1,.36,1)' });
    anim.onfinish = function () { ink.remove(); };
  }, { passive: true });

  /* ── 4 · CARD SPOTLIGHT ─────────────────────────────────────────── */
  if (HOVER) {
    var pending = null;
    document.addEventListener('mousemove', function (e) {
      if (pending) return;
      pending = requestAnimationFrame(function () {
        pending = null;
        var t = e.target.closest && e.target.closest(SPOT_SEL);
        if (!t) return;
        if (!t.classList.contains('wp-spot')) t.classList.add('wp-spot');
        var r = t.getBoundingClientRect();
        t.style.setProperty('--wx', (e.clientX - r.left) + 'px');
        t.style.setProperty('--wy', (e.clientY - r.top) + 'px');
      });
    }, { passive: true });
  }

  /* ── public hooks ───────────────────────────────────────────────── */
  function tabIn(target) {
    if (!target) return;
    var units = slice(target.querySelectorAll(':scope > .panel, :scope > .stats'));
    if (!units.length) units = [target];
    enqueue(units);
    counters(target);
  }

  function reveal(root) {
    enqueue(slice((root || document).querySelectorAll(UNIT_SEL)).slice(0, 24));
  }

  window.WPfx = { tabIn: tabIn, counters: counters, reveal: reveal };

  /* ── boot ───────────────────────────────────────────────────────── */
  function boot() {
    mo.observe(document.body, { childList: true, subtree: true });
    /* first paint of static sections */
    setTimeout(function () { reveal(document); }, 60);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
