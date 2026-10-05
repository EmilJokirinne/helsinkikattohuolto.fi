#!/usr/bin/env python3
"""HelsinkiKattoHuolto.fi – staattisen sivuston koonti.

Käyttö:  python3 build.py
Tuottaa kaikki .html-sivut, sitemap.xml:n ja robots.txt:n samaan kansioon.
Sisältö: content_pages.py, content_articles.py, content_faq.py
Yritysdata: companies.json (päivittyy sivulle myös ilman uudelleenkoontia).
"""
import json, html, os, datetime
from content_faq import FAQ_ALL, faq_by_ids
import components as C

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://helsinkikattohuolto.fi"
BRAND = "HelsinkiKattoHuolto.fi"
TODAY = datetime.date.today().isoformat()

with open(os.path.join(ROOT, "companies.json"), encoding="utf-8") as f:
    COMPANIES = json.load(f)
C.COMPANIES = COMPANIES

NAV = [
    ("/kattohuolto", "Kattohuolto"),
    ("/katon-pesu", "Katon pesu"),
    ("/katon-kuntotarkastus", "Katon kuntotarkastus"),
    ("/hinnat", "Hinnat"),
    ("/yritykset", "Palveluntarjoajat"),
    ("/kattotyypit", "Kattotyypit"),
    ("/usein-kysyttya", "Usein kysyttyä"),
]

LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="8" fill="#13213a"/>'
        '<path d="M6 17.5 16 9l10 8.5" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M10 16v8h12v-8" fill="none" stroke="#c9d2df" stroke-width="2" stroke-linejoin="round"/>'
        '<path d="M21 9.5v3" stroke="#d1774c" stroke-width="2.4" stroke-linecap="round"/></svg>')


def esc(s):
    return html.escape(s, quote=True)


def header(current):
    cur = ' aria-current="page"'
    items = "".join(
        f'<li><a href="{u}"{cur if u == current else ""}>{t}</a></li>' for u, t in NAV)
    return f'''<a class="skip" href="#main">Siirry sisältöön</a>
<header class="site-header">
  <div class="wrap hdr">
    <a class="logo" href="/" aria-label="{BRAND} – etusivu">{LOGO}<span>HelsinkiKatto<b>Huolto</b>.fi</span></a>
    <nav class="nav" aria-label="Päävalikko"><ul>{items}</ul></nav>
    <a class="btn btn-primary btn-sm hdr-cta" href="/tarjouspyynto">Pyydä tarjouksia</a>
    <button class="menu-btn" id="menu-btn" type="button" aria-expanded="false" aria-controls="mnav" aria-label="Avaa valikko">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
  </div>
  <nav class="mnav" id="mnav" aria-label="Mobiilivalikko"><ul>{items}<li><a href="/katto-opas">Katto-opas</a></li><li><a href="/tietoa-sivustosta">Tietoa sivustosta</a></li></ul></nav>
</header>'''


def footer():
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="fgrid-foot">
      <div>
        <p class="foot-brand">{BRAND}</p>
        <p>Opas katon huoltoon, hintoihin ja palveluntarjoajiin Helsingissä.</p>
        <p style="font-size:.88rem">Sivusto ei itse tee kattotöitä. Hinnat ovat suuntaa-antavia, ja ne on koottu yritysten julkaisemista hinnastoista.</p>
      </div>
      <nav aria-label="Palvelut"><h2>Palvelut</h2><ul>
        <li><a href="/kattohuolto">Kattohuolto</a></li><li><a href="/katon-pesu">Katon pesu</a></li>
        <li><a href="/sammaleen-poisto">Sammaleen poisto</a></li><li><a href="/katon-kuntotarkastus">Kuntotarkastus</a></li>
        <li><a href="/katon-pinnoitus">Pinnoitus ja maalaus</a></li><li><a href="/rannien-puhdistus">Rännien puhdistus</a></li></ul></nav>
      <nav aria-label="Tieto"><h2>Tieto</h2><ul>
        <li><a href="/hinnat">Hinnat</a></li><li><a href="/yritykset">Yritykset</a></li>
        <li><a href="/katto-opas">Katto-opas</a></li><li><a href="/usein-kysyttya">FAQ</a></li>
        <li><a href="/kattotyypit">Kattotyypit</a></li></ul></nav>
      <nav aria-label="Sivusto"><h2>Sivusto</h2><ul>
        <li><a href="/tietoa-sivustosta">Tietoa sivustosta</a></li><li><a href="/yhteystiedot">Yhteystiedot</a></li>
        <li><a href="/tietosuojaseloste">Tietosuojaseloste</a></li><li><a href="/evastekaytannot">Evästekäytännöt</a></li>
        <li><button type="button" class="linkbtn" data-open-consent>Evästeasetukset</button></li></ul></nav>
    </div>
    <div class="foot-bottom"><span>© {datetime.date.today().year} {BRAND}</span><span>Hintatiedot tarkistettu {C.fdate(COMPANIES["updatedAt"])}</span></div>
  </div>
</footer>
<div class="sticky-cta"><a class="btn btn-secondary" href="/hinnat#laskuri">Laske arvio</a><a class="btn btn-primary" href="/tarjouspyynto">Pyydä tarjouksia</a></div>
<div class="cookie" id="cookie" role="dialog" aria-live="polite" aria-label="Evästeasetukset" hidden>
  <p><b>Evästeet.</b> Käytämme välttämättömien evästeiden lisäksi analytiikkaa vain, jos hyväksyt sen. Analytiikalla kehitämme sivuston sisältöä. <a href="/evastekaytannot">Lue lisää</a>.</p>
  <div class="btn-row"><button class="btn btn-primary btn-sm" type="button" data-consent="all">Hyväksy analytiikka</button><button class="btn btn-secondary btn-sm" type="button" data-consent="necessary">Vain välttämättömät</button></div>
</div>'''


def crumbs_html(crumbs):
    if not crumbs:
        return ""
    lis = '<li><a href="/">Etusivu</a></li>'
    for i, (u, t) in enumerate(crumbs):
        lis += f'<li><a href="{u}" aria-current="page">{t}</a></li>' if i == len(crumbs) - 1 else f'<li><a href="{u}">{t}</a></li>'
    return f'<nav class="crumbs" aria-label="Murupolku"><ol>{lis}</ol></nav>'


def schema_for(p):
    url = SITE + (p["slug"] if p["slug"] != "/" else "/")
    graph = [
        {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": BRAND, "inLanguage": "fi-FI",
         "description": "Puolueeton opas katon huoltoon, hintoihin ja palveluntarjoajiin Helsingissä ja pääkaupunkiseudulla.",
         "publisher": {"@id": SITE + "/#organization"}},
        {"@type": "Organization", "@id": SITE + "/#organization", "name": BRAND, "url": SITE + "/",
         "logo": SITE + "/favicon-512.png"},
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p["title"], "description": p["desc"],
         "isPartOf": {"@id": SITE + "/#website"}, "inLanguage": "fi-FI", "dateModified": p.get("modified", TODAY)},
    ]
    if p.get("crumbs"):
        items = [{"@type": "ListItem", "position": 1, "name": "Etusivu", "item": SITE + "/"}]
        for i, (u, t) in enumerate(p["crumbs"]):
            items.append({"@type": "ListItem", "position": i + 2, "name": t, "item": SITE + u})
        graph.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": items})
        graph[2]["breadcrumb"] = {"@id": url + "#breadcrumb"}
    if p.get("article"):
        graph.append({"@type": "Article", "@id": url + "#article", "headline": p["h1"], "description": p["desc"],
                      "inLanguage": "fi-FI", "datePublished": p["article"]["published"], "dateModified": p.get("modified", TODAY),
                      "author": {"@type": "Organization", "name": BRAND + " toimitus", "url": SITE + "/tietoa-sivustosta"},
                      "publisher": {"@id": SITE + "/#organization"}, "mainEntityOfPage": {"@id": url + "#webpage"},
                      "image": SITE + "/og-image.png"})
    if p.get("faq"):
        graph.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": C.strip_tags(a)}} for q, a in p["faq"]]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))


def render(p):
    slug = p["slug"]
    url = SITE + (slug if slug != "/" else "/")
    noindex = p.get("noindex")
    hero = p.get("hero_html")
    if hero is None:
        meta = f'<p class="meta-line">{p["meta_line"]}</p>' if p.get("meta_line") else ""
        hero = f'''<section class="page-hero"><div class="wrap">{crumbs_html(p.get("crumbs"))}
<h1>{p["h1"]}</h1>{f'<p class="lead">{p["lead"]}</p>' if p.get("lead") else ""}{meta}</div></section>'''
    body = p["body"]
    if p.get("faq") and p.get("faq_section", True):
        body += C.faq_section(p["faq"], p.get("faq_title", "Usein kysyttyä"))
    body += p.get("after_faq", "")
    doc = f'''<!doctype html>
<html lang="fi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["desc"])}">
<link rel="canonical" href="{url}">
{'<meta name="robots" content="noindex, follow">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'}
<meta property="og:type" content="{"article" if p.get("article") else "website"}">
<meta property="og:locale" content="fi_FI">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{esc(p.get("og_title", p["title"]))}">
<meta property="og:description" content="{esc(p["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="HelsinkiKattoHuolto.fi – opas katon huoltoon Helsingissä">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(p.get("og_title", p["title"]))}">
<meta name="twitter:description" content="{esc(p["desc"])}">
<meta name="twitter:image" content="{SITE}/og-image.png">
<meta name="theme-color" content="#13213a">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="stylesheet" href="/styles.css">
<script src="/config.js" defer></script>
<script src="/app.js" defer></script>
<script type="application/ld+json">{schema_for(p)}</script>
</head>
<body>
{header(p.get("nav", slug))}
<main id="main">
{hero}
{body}
</main>
{footer()}
</body>
</html>
'''
    name = "index.html" if slug == "/" else slug.strip("/") + ".html"
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(doc)
    return name


def main():
    from content_pages import PAGES
    from content_articles import ARTICLES, articles_index_page
    pages = list(PAGES) + list(ARTICLES) + [articles_index_page()]
    written, urls = [], []
    for p in pages:
        written.append(render(p))
        if not p.get("noindex"):
            urls.append((p["slug"], p.get("priority", "0.6")))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, pr in urls:
        loc = SITE + ("/" if u == "/" else u)
        sm.append(f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(sm) + "\n")
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /kiitos\n\nSitemap: {SITE}/sitemap.xml\n")
    print(f"{len(written)} sivua, {len(urls)} URL:ää sitemapissa")


if __name__ == "__main__":
    main()
