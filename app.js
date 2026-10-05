/* HelsinkiKattoHuolto.fi – sivuston JavaScript (ei riippuvuuksia). */
(function () {
  "use strict";
  var CFG = window.HKH_CONFIG || {};
  var CONSENT_KEY = "hkh_consent_v1";

  /* ---------- Analytiikka (vain suostumuksella) ---------- */
  window.dataLayer = window.dataLayer || [];
  function track(name, params) {
    try {
      window.dataLayer.push(Object.assign({ event: name }, params || {}));
      if (typeof window.gtag === "function") window.gtag("event", name, params || {});
    } catch (e) {}
  }
  window.hkhTrack = track;

  function getConsent() { try { return localStorage.getItem(CONSENT_KEY); } catch (e) { return null; } }
  function setConsent(v) { try { localStorage.setItem(CONSENT_KEY, v); } catch (e) {} }

  function loadGA() {
    if (!CFG.gaMeasurementId || window.__gaLoaded) return;
    window.__gaLoaded = true;
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(CFG.gaMeasurementId);
    document.head.appendChild(s);
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", CFG.gaMeasurementId, { anonymize_ip: true });
  }

  function initConsent() {
    var banner = document.getElementById("cookie");
    var c = getConsent();
    if (c === "all") loadGA();
    if (!banner) return;
    // Banneri näytetään vain, jos analytiikka on käytössä ja valintaa ei ole tehty.
    if (CFG.gaMeasurementId && !c) banner.hidden = false;
    banner.addEventListener("click", function (e) {
      var b = e.target.closest("[data-consent]");
      if (!b) return;
      setConsent(b.getAttribute("data-consent"));
      banner.hidden = true;
      if (b.getAttribute("data-consent") === "all") loadGA();
    });
    document.querySelectorAll("[data-open-consent]").forEach(function (el) {
      el.addEventListener("click", function () {
        try { localStorage.removeItem(CONSENT_KEY); } catch (e) {}
        if (CFG.gaMeasurementId) banner.hidden = false;
        else alert("Sivustolla ei tällä hetkellä käytetä analytiikka- tai markkinointievästeitä.");
      });
    });
  }

  /* ---------- Mobiilivalikko ---------- */
  function initMenu() {
    var btn = document.getElementById("menu-btn");
    var nav = document.getElementById("mnav");
    if (!btn || !nav) return;
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      btn.setAttribute("aria-label", open ? "Sulje valikko" : "Avaa valikko");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) { nav.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); btn.focus(); }
    });
  }

  /* ---------- Hintalaskuri ----------
   * Hintatasot perustuvat julkaistuihin hinnastoihin (tarkistettu 10/2026):
   * Kotikatto.fi: pesu 9 €/m², sammal 12–15 €/m², pinnoitus 29 €/m², rännit 270–370 €, kuntoarvio 290–390 €.
   * Ulkopesu: kattopesu sis. suojauksen 490–700 € (<80 m²), 700–1 200 € (80–150 m²), 1 200–1 800 € (150–250 m²), rännit alk. 149 €.
   * Säädä tarvittaessa alla olevia lukuja.
   */
  var CALC = {
    area: { s: 65, m: 100, l: 150, xl: 215 }, // laskennallinen pinta-ala kokoluokalle
    perM2: { // €/m², [min, max]
      pesu: [6, 9], sammal: [9, 15], suojaus: [7, 10.5], pinnoitus: [22, 30]
    },
    minimum: { pesu: 490, sammal: 490, suojaus: 490, pinnoitus: 1800 },
    fixed: {
      tarkastus: { s: [250, 400], m: [250, 400], l: [290, 450], xl: [350, 550] },
      rannit: { s: [150, 300], m: [170, 330], l: [220, 370], xl: [270, 450] }
    },
    type: { pelti: 1.0, tiili: 1.1, huopa: 1.05 },
    growth: { vahan: 0.92, kohtalainen: 1.0, paljon: 1.2 },
    growthApplies: { pesu: true, sammal: true, suojaus: true, pinnoitus: false }
  };
  function round50(n) { return Math.round(n / 50) * 50; }
  function fmt(n) { return n.toLocaleString("fi-FI").replace(/ /g, " ") + " €"; }

  function initCalc() {
    var form = document.getElementById("calc");
    if (!form) return;
    var out = document.getElementById("calc-out");
    var basis = document.getElementById("calc-basis");
    var used = false;
    function val(n) { var el = form.querySelector('input[name="' + n + '"]:checked'); return el ? el.value : null; }
    function compute() {
      var size = val("koko"), type = val("tyyppi"), svc = val("palvelu"), growth = val("kasvusto");
      var lo, hi, area = CALC.area[size];
      var growthBox = document.getElementById("growth-box");
      if (growthBox) growthBox.style.opacity = CALC.growthApplies[svc] ? "1" : ".45";
      if (CALC.fixed[svc]) {
        lo = CALC.fixed[svc][size][0]; hi = CALC.fixed[svc][size][1];
        if (svc === "tarkastus" && type === "tiili") { hi += 50; }
      } else {
        var r = CALC.perM2[svc], m = CALC.type[type] * (CALC.growthApplies[svc] ? CALC.growth[growth] : 1);
        lo = Math.max(area * r[0] * m, CALC.minimum[svc]);
        hi = Math.max(area * r[1] * m, CALC.minimum[svc] * 1.3);
      }
      lo = round50(lo); hi = round50(hi);
      if (hi <= lo) hi = lo + 100;
      out.textContent = fmt(lo) + " – " + fmt(hi);
      var svcLabel = form.querySelector('input[name="palvelu"]:checked + label').textContent;
      var sizeLabel = form.querySelector('input[name="koko"]:checked + label').textContent;
      basis.textContent = svcLabel + ", " + sizeLabel + ", " + form.querySelector('input[name="tyyppi"]:checked + label').textContent.toLowerCase() + "katto";
      if (!used) { used = true; } else { track("price_calculator_used", { service: svc, size: size, roof_type: type, growth: growth, estimate_low: lo, estimate_high: hi }); }
    }
    form.addEventListener("change", compute);
    compute();
  }

  /* ---------- Yritysvertailu: päivitys companies.json-tiedostosta ---------- */
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function fdate(iso) { var p = (iso || "").split("-"); return p.length === 3 ? (+p[2]) + "." + (+p[1]) + "." + p[0] : iso; }
  function priceCell(v, label) {
    return v ? '<td data-label="' + label + '">' + esc(v) + "</td>" : '<td data-label="' + label + '" class="np">Ei julkaistu</td>';
  }
  function priceDD(v) { return v ? "<dd>" + esc(v) + "</dd>" : '<dd class="np">Ei julkaistu</dd>'; }
  var COLS = [["roofWashPrice", "Katon pesu"], ["mossRemovalPrice", "Sammaleen poisto"], ["inspectionPrice", "Kuntotarkastus"], ["gutterCleaningPrice", "Rännit"], ["coatingPrice", "Pinnoitus"]];

  function renderComparison(root, data) {
    var rows = data.companies.map(function (c) {
      var name = c.website ? '<a href="' + esc(c.website) + '" rel="noopener nofollow" target="_blank" data-company="' + esc(c.id) + '">' + esc(c.name) + "</a>" : esc(c.name);
      return "<tr><th scope=\"row\">" + name + '<div class="source">' + esc(c.city) + ' · <a href="' + esc(c.priceSource) + '" rel="noopener nofollow" target="_blank">Lähde</a>, tarkistettu ' + fdate(c.priceCheckedAt) + "</div></th>" +
        COLS.map(function (k) { return priceCell(c[k[0]], k[1]); }).join("") +
        '<td data-label="Tarjous"><a class="btn btn-primary btn-sm" href="/tarjouspyynto?yritys=' + encodeURIComponent(c.id) + '" data-quote="' + esc(c.id) + '">Pyydä tarjous</a></td></tr>';
    }).join("");
    var cards = data.companies.map(function (c) {
      return '<article class="card cmp-card"><h3>' + esc(c.name) + '</h3><p class="muted mb0">' + esc(c.city) + "</p><dl class=\"mt2\">" +
        COLS.map(function (k) { return "<div><dt>" + k[1] + "</dt>" + priceDD(c[k[0]]) + "</div>"; }).join("") +
        '</dl><p class="source">Lähde: <a href="' + esc(c.priceSource) + '" rel="noopener nofollow" target="_blank">' + esc(c.priceSource.replace(/^https?:\/\/(www\.)?/, "").split("/")[0]) + "</a>, tarkistettu " + fdate(c.priceCheckedAt) + '</p><div class="btn-row">' +
        (c.website ? '<a class="btn btn-secondary btn-sm" href="' + esc(c.website) + '" rel="noopener nofollow" target="_blank" data-company="' + esc(c.id) + '">Katso yritys</a>' : "") +
        '<a class="btn btn-primary btn-sm" href="/tarjouspyynto?yritys=' + encodeURIComponent(c.id) + '" data-quote="' + esc(c.id) + '">Pyydä tarjous</a></div></article>';
    }).join("");
    var tb = root.querySelector("tbody"); if (tb) tb.innerHTML = rows;
    var cc = root.querySelector(".cmp-cards"); if (cc) cc.innerHTML = cards;
  }

  function initCompanies() {
    var roots = document.querySelectorAll("[data-companies]");
    if (!roots.length) return;
    var version = roots[0].getAttribute("data-version");
    fetch("/companies.json", { cache: "no-cache" }).then(function (r) { return r.ok ? r.json() : null; }).then(function (data) {
      if (!data || data.updatedAt === version) return; // esirenderöity HTML on ajan tasalla
      roots.forEach(function (root) { if (root.getAttribute("data-companies") === "compare") renderComparison(root, data); });
    }).catch(function () {});
  }

  function initFilters() {
    var bar = document.getElementById("co-filters");
    if (!bar) return;
    var cards = document.querySelectorAll("[data-cats]");
    bar.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-filter]");
      if (!b) return;
      var f = b.getAttribute("data-filter");
      bar.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); x.classList.toggle("btn-primary", x === b); x.classList.toggle("btn-secondary", x !== b); });
      var shown = 0;
      cards.forEach(function (c) { var ok = f === "all" || c.getAttribute("data-cats").split("|").indexOf(f) > -1; c.hidden = !ok; if (ok) shown++; });
      var st = document.getElementById("co-count"); if (st) st.textContent = shown + " yritystä näytetään";
      track("comparison_used", { filter: f });
    });
  }

  /* ---------- Tarjouspyyntölomake ---------- */
  function initForm() {
    var form = document.getElementById("quote-form");
    if (!form) return;
    var status = document.getElementById("form-status");
    var params = new URLSearchParams(location.search);
    var co = params.get("yritys"), svc = params.get("palvelu");
    if (co) { var h = form.querySelector('[name="toivottu_yritys"]'); if (h) h.value = co; var n = document.getElementById("co-note"); if (n) { n.hidden = false; var names = {}; try { names = JSON.parse(form.getAttribute("data-names") || "{}"); } catch (e) {} n.querySelector("b").textContent = names[co] || co; } }
    if (svc) { var s = form.querySelector('[name="palvelu"]'); if (s) s.value = svc; }

    form.addEventListener("submit", function (e) {
      var bad = null;
      form.querySelectorAll("[required]").forEach(function (el) {
        var ok = el.type === "checkbox" ? el.checked : el.value.trim() !== "" && el.checkValidity();
        el.setAttribute("aria-invalid", ok ? "false" : "true");
        if (!ok && !bad) bad = el;
      });
      var pc = form.querySelector('[name="postinumero"]');
      if (pc && pc.value && !/^\d{5}$/.test(pc.value.trim())) { pc.setAttribute("aria-invalid", "true"); bad = bad || pc; }
      if (bad) {
        e.preventDefault();
        status.className = "form-status err";
        status.textContent = "Tarkista merkityt kentät. Pakolliset kentät on merkitty tähdellä.";
        bad.focus();
        return;
      }
      track("quote_request", { service: form.palvelu.value, roof_type: form.kattotyyppi.value, size: form.koko.value });
      if (CFG.formEndpoint) {
        e.preventDefault();
        var btn = form.querySelector('button[type="submit"]'); btn.disabled = true;
        status.className = "form-status"; status.textContent = "Lähetetään…";
        fetch(CFG.formEndpoint, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
          .then(function (r) { if (!r.ok) throw new Error(); location.href = "/kiitos"; })
          .catch(function () { btn.disabled = false; status.className = "form-status err"; status.textContent = "Lähetys epäonnistui. Yritä hetken kuluttua uudelleen tai lähetä viesti osoitteeseen " + (CFG.contactEmail || "") + "."; });
      }
      // Muuten lomake lähtee natiivisti (Netlify Forms).
    });
  }

  /* ---------- Tapahtumat: klikkaukset ja artikkelin lukeminen ---------- */
  function initEvents() {
    document.addEventListener("click", function (e) {
      var a = e.target.closest("a");
      if (!a) return;
      var href = a.getAttribute("href") || "";
      if (a.hasAttribute("data-company")) track("company_clicked", { company: a.getAttribute("data-company") });
      if (href.indexOf("tel:") === 0) track("phone_clicked", {});
      if (href.indexOf("mailto:") === 0) track("email_clicked", {});
    });
    var art = document.querySelector("article[data-article]");
    if (art && "IntersectionObserver" in window) {
      var end = document.getElementById("article-end");
      if (end) {
        var io = new IntersectionObserver(function (en) {
          if (en[0].isIntersecting) { track("article_read", { article: art.getAttribute("data-article") }); io.disconnect(); }
        });
        io.observe(end);
      }
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    initMenu(); initConsent(); initCalc(); initCompanies(); initFilters(); initForm(); initEvents();
  });
})();
