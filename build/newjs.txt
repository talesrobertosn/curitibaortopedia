/* Curitiba Ortopedia — JavaScript compartilhado.
   Fonte única da verdade: newjs.txt, propagado por apply_polish.py. */
(function () {
  "use strict";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- barra de progresso de leitura ---- */
  var bar = document.querySelector(".readbar");
  if (bar) {
    var ticking = false;
    var draw = function () {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      var p = h > 0 ? (window.scrollY / h) * 100 : 0;
      bar.style.width = (p < 0 ? 0 : p > 100 ? 100 : p) + "%";
      ticking = false;
    };
    window.addEventListener("scroll", function () {
      if (!ticking) { ticking = true; window.requestAnimationFrame(draw); }
    }, { passive: true });
    window.addEventListener("resize", draw, { passive: true });
    draw();
  }

  /* ---- animação de entrada ---- */
  var revealables = document.querySelectorAll(".reveal");
  if (revealables.length) {
    if (reduce || !("IntersectionObserver" in window)) {
      Array.prototype.forEach.call(revealables, function (el) { el.classList.add("in"); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
        });
      }, { rootMargin: "0px 0px -8% 0px", threshold: 0.06 });
      Array.prototype.forEach.call(revealables, function (el) { io.observe(el); });
    }
  }

  /* ---- menus suspensos da nav ---- */
  var groups = document.querySelectorAll(".nav-group");
  var closeGroups = function (except) {
    Array.prototype.forEach.call(groups, function (g) {
      if (g !== except) {
        g.setAttribute("data-open", "false");
        var b = g.querySelector(".nav-btn");
        if (b) { b.setAttribute("aria-expanded", "false"); }
      }
    });
  };
  Array.prototype.forEach.call(groups, function (g) {
    var btn = g.querySelector(".nav-btn");
    if (!btn) { return; }
    var open = function (state) {
      g.setAttribute("data-open", state ? "true" : "false");
      btn.setAttribute("aria-expanded", state ? "true" : "false");
      if (state) { closeGroups(g); }
    };
    var podeHover = window.matchMedia && window.matchMedia("(hover: hover)").matches;
    btn.addEventListener("click", function (ev) {
      ev.preventDefault();
      var aberto = g.getAttribute("data-open") === "true";
      /* se abriu por passagem do mouse, o clique fixa o menu em vez de fechá-lo */
      if (aberto && g.getAttribute("data-hover") === "true") {
        g.setAttribute("data-hover", "false");
        return;
      }
      g.setAttribute("data-hover", "false");
      open(!aberto);
    });
    g.addEventListener("mouseenter", function () {
      if (podeHover && !document.body.classList.contains("nav-mobile")) {
        g.setAttribute("data-hover", "true");
        open(true);
      }
    });
    g.addEventListener("mouseleave", function () {
      if (podeHover && !document.body.classList.contains("nav-mobile")) {
        g.setAttribute("data-hover", "false");
        open(false);
      }
    });
    g.addEventListener("focusout", function (ev) {
      if (!g.contains(ev.relatedTarget)) { open(false); }
    });
  });
  document.addEventListener("click", function (ev) {
    if (!ev.target.closest || !ev.target.closest(".nav-group")) { closeGroups(null); }
  });
  document.addEventListener("keydown", function (ev) {
    if (ev.key === "Escape") {
      closeGroups(null);
      if (document.body.classList.contains("nav-open")) { setMobileOpen(false); }
    }
  });

  /* ---- menu mobile, com ponto de quebra medido na nav real ---- */
  var toggle = document.querySelector(".menu-toggle");
  var nav = document.querySelector("nav.mainnav");
  var brand = document.querySelector(".site-header .brand");
  var barEl = document.querySelector(".site-header .bar");

  function setMobileOpen(state) {
    document.body.classList.toggle("nav-open", !!state);
    if (toggle) { toggle.setAttribute("aria-expanded", state ? "true" : "false"); }
  }
  if (toggle) {
    toggle.addEventListener("click", function () {
      setMobileOpen(!document.body.classList.contains("nav-open"));
    });
  }

  var breakpoint = null;
  function measure() {
    if (!nav || !brand || !barEl) { return; }
    if (breakpoint !== null) { return; }
    var wasMobile = document.body.classList.contains("nav-mobile");
    document.body.classList.remove("nav-mobile");
    var navW = nav.scrollWidth;
    var brandW = brand.offsetWidth;
    var pad = 44 + 18; /* padding do bar + gap mínimo */
    if (navW > 0 && brandW > 0) { breakpoint = Math.ceil(navW + brandW + pad + 24); }
    if (wasMobile) { document.body.classList.add("nav-mobile"); }
  }
  function applyBreakpoint() {
    if (breakpoint === null) { measure(); }
    if (breakpoint === null) { return; }
    var isMobile = window.innerWidth < breakpoint;
    document.body.classList.toggle("nav-mobile", isMobile);
    if (!isMobile) { setMobileOpen(false); }
  }
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () { breakpoint = null; applyBreakpoint(); });
  }
  applyBreakpoint();
  window.addEventListener("resize", applyBreakpoint, { passive: true });
  window.addEventListener("orientationchange", applyBreakpoint);

  /* ---- fecha o painel mobile ao navegar por âncora ---- */
  Array.prototype.forEach.call(document.querySelectorAll('.mobile-panel a[href^="#"], .toc a[href^="#"]'), function (a) {
    a.addEventListener("click", function () { setMobileOpen(false); });
  });

  /* ---- marca o link da página atual ---- */
  var here = location.pathname.split("/").pop() || "index.html";
  Array.prototype.forEach.call(document.querySelectorAll('nav.mainnav a[href], .mobile-panel a[href]'), function (a) {
    var target = a.getAttribute("href");
    if (target === here) { a.setAttribute("aria-current", "page"); }
  });
})();
