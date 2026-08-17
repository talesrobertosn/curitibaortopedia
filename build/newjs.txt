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
    var timer = null;
    g.addEventListener("mouseenter", function () {
      if (podeHover && !document.body.classList.contains("nav-mobile")) {
        if (timer) { clearTimeout(timer); timer = null; }
        g.setAttribute("data-hover", "true");
        open(true);
      }
    });
    g.addEventListener("mouseleave", function () {
      if (podeHover && !document.body.classList.contains("nav-mobile")) {
        /* atraso generoso: dá tempo de descer o mouse até o item desejado */
        if (timer) { clearTimeout(timer); }
        timer = setTimeout(function () {
          g.setAttribute("data-hover", "false");
          open(false);
          timer = null;
        }, 520);
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
    var a11y = barEl.querySelector(".a11y");
    var extraW = a11y ? a11y.offsetWidth + 18 : 0;
    var pad = 44 + 18; /* padding do bar + gap mínimo */
    if (navW > 0 && brandW > 0) { breakpoint = Math.ceil(navW + brandW + extraW + pad + 24); }
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

  /* ---- busca de áreas na página de encontrar ortopedista ---- */
  var campo = document.getElementById("busca-area");
  if (campo) {
    var cartoes = Array.prototype.slice.call(document.querySelectorAll("[data-chaves]"));
    var status = document.getElementById("busca-status");
    var vazio = document.querySelector(".busca-vazia");
    var limpar = document.querySelector(".finder-clear");
    var chips = Array.prototype.slice.call(document.querySelectorAll(".chip[data-grupo]"));
    var grupo = "todos";

    var normalizar = function (t) {
      return (t || "").normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
    };

    var filtrar = function () {
      var termo = normalizar(campo.value).trim();
      var visiveis = 0;
      cartoes.forEach(function (c) {
        var chaves = normalizar(c.getAttribute("data-chaves"));
        var g = c.getAttribute("data-grupo") || "";
        var casaTermo = !termo || chaves.indexOf(termo) !== -1 ||
          termo.split(/\s+/).every(function (parte) { return chaves.indexOf(parte) !== -1; });
        var casaGrupo = grupo === "todos" || g === grupo;
        var mostrar = casaTermo && casaGrupo;
        c.hidden = !mostrar;
        if (mostrar) { visiveis++; }
      });
      if (limpar) { limpar.hidden = !campo.value; }
      if (vazio) { vazio.classList.toggle("on", visiveis === 0); }
      if (status) {
        if (!termo && grupo === "todos") {
          status.textContent = "Mostrando todas as " + cartoes.length + " áreas da ortopedia.";
        } else if (visiveis === 0) {
          status.textContent = "Nada encontrado para essa busca. Tente uma palavra mais simples, como joelho, coluna, ombro, mão ou pé.";
        } else if (visiveis === 1) {
          status.textContent = "1 área encontrada.";
        } else {
          status.textContent = visiveis + " áreas encontradas.";
        }
      }
    };

    campo.addEventListener("input", filtrar);
    campo.addEventListener("search", filtrar);
    var form = campo.closest("form");
    if (form) {
      form.addEventListener("submit", function (ev) {
        ev.preventDefault();
        filtrar();
        var primeiro = cartoes.filter(function (c) { return !c.hidden; })[0];
        if (primeiro) { primeiro.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "center" }); }
      });
    }
    if (limpar) {
      limpar.addEventListener("click", function () {
        campo.value = "";
        filtrar();
        campo.focus();
      });
    }
    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        var alvo = chip.getAttribute("data-grupo");
        grupo = (grupo === alvo) ? "todos" : alvo;
        chips.forEach(function (c) {
          c.setAttribute("aria-pressed", c.getAttribute("data-grupo") === grupo ? "true" : "false");
        });
        filtrar();
      });
    });
    filtrar();
  }

  /* ---- controle de tamanho da letra ---- */
  var CHAVE = "co-escala";
  var escala = 1;
  try {
    var salvo = parseFloat(window.localStorage.getItem(CHAVE));
    if (salvo >= 0.9 && salvo <= 1.4) { escala = salvo; }
  } catch (e) { /* navegador sem armazenamento, segue com o padrão */ }

  var aplicarEscala = function (valor) {
    escala = Math.min(1.4, Math.max(0.9, Math.round(valor * 100) / 100));
    document.documentElement.style.setProperty("--escala", escala);
    try { window.localStorage.setItem(CHAVE, escala); } catch (e) { /* sem armazenamento */ }
    Array.prototype.forEach.call(document.querySelectorAll(".a11y"), function (c) {
      c.setAttribute("data-escala", Math.round(escala * 100) + "%");
    });
  };
  aplicarEscala(escala);
  Array.prototype.forEach.call(document.querySelectorAll(".a11y button"), function (b) {
    b.addEventListener("click", function () {
      aplicarEscala(escala + (b.classList.contains("mais") ? 0.1 : -0.1));
    });
  });

  /* ---- botão flutuante de busca no celular ---- */
  var fab = document.querySelector(".fab");
  if (fab) {
    var alvoFab = document.querySelector(".finder") || document.querySelector(".area-list");
    var mostrarFab = function (estado) { fab.classList.toggle("on", !!estado); };
    if (document.body.getAttribute("data-pagina") === "busca") {
      mostrarFab(false);
    } else if ("IntersectionObserver" in window && alvoFab) {
      var ioFab = new IntersectionObserver(function (ents) {
        mostrarFab(!ents[0].isIntersecting);
      }, { threshold: 0 });
      ioFab.observe(alvoFab);
    } else {
      var alternar = function () { mostrarFab(window.scrollY > 420); };
      window.addEventListener("scroll", alternar, { passive: true });
      alternar();
    }
  }

  /* ---- marca o link da página atual ---- */
  var here = location.pathname.split("/").pop() || "index.html";
  Array.prototype.forEach.call(document.querySelectorAll('nav.mainnav a[href], .mobile-panel a[href]'), function (a) {
    var target = a.getAttribute("href");
    if (target === here) { a.setAttribute("aria-current", "page"); }
  });
})();
