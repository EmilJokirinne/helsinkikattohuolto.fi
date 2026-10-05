"""Uudelleenkäytettävät sivukomponentit (HTML-merkkijonot)."""
import html, re, json

COMPANIES = None  # asetetaan build.py:ssä


def esc(s):
    return html.escape(str(s), quote=True)


def fdate(iso):
    y, m, d = iso.split("-")
    return f"{int(d)}.{int(m)}.{y}"


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


# ---------- Ikonit (inline SVG, ei pyyntöjä) ----------
_I = {
    "check": '<path d="M5 12l5 5 9-10"/>',
    "drop": '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>',
    "leaf": '<path d="M5 19c8 0 14-6 14-14-8 0-14 6-14 14z"/><path d="M5 19l7-7"/>',
    "gutter": '<path d="M3 7h18v3a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3z"/><path d="M17 13v8"/>',
    "clip": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4h6v3H9zM9 12l2 2 4-4"/>',
    "brush": '<path d="M14 4l6 6-8 8-6-6z"/><path d="M6 12l-3 8 8-3"/>',
    "wrench": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.2L3 17.8 6.2 21l6.3-6.3a4 4 0 0 0 5.2-5.4l-2.5 2.5-2.6-.6-.6-2.6z"/>',
    "roof": '<path d="M3 12l9-8 9 8"/><path d="M6 10v10h12V10"/>',
    "map": '<path d="M12 21s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
    "list": '<path d="M9 6h12M9 12h12M9 18h12"/><path d="M4 6h.01M4 12h.01M4 18h.01"/>',
    "euro": '<path d="M18 6.5A7 7 0 1 0 18 17.5"/><path d="M4 10h10M4 14h10"/>',
    "scale": '<path d="M12 3v18M5 7h14"/><path d="M5 7l-3 7a3 3 0 0 0 6 0zM19 7l-3 7a3 3 0 0 0 6 0z"/>',
    "book": '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 19V5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "snow": '<path d="M12 2v20M4.9 7l14.2 10M4.9 17L19.1 7"/>',
}


def icon(name, size=24):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_I[name]}</svg>')


ARROW = icon("arrow", 18)


# ---------- Hero-kuvitus ----------
def hero_svg():
    seams = []
    for x0 in range(140, 446, 17):
        # saumat kattopinnan alareunasta harjalle (lappeen suuntaisesti)
        seams.append(f'<line x1="{x0}" y1="215" x2="{x0 + 45}" y2="141"/>')
    return f'''<svg viewBox="0 0 640 440" role="img" aria-labelledby="hero-t">
<title id="hero-t">Kuvitus: suomalainen omakotitalo, jossa hyväkuntoinen tumma konesaumattu peltikatto, lumiesteet ja räystäskourut</title>
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfdeea"/><stop offset="1" stop-color="#eef3f7"/></linearGradient>
<linearGradient id="roof" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a4452"/><stop offset="1" stop-color="#262d38"/></linearGradient></defs>
<rect width="640" height="440" fill="url(#sky)"/>
<circle cx="540" cy="78" r="30" fill="#fbf3e2" opacity=".9"/>
<g fill="#8fa5b8" opacity=".55"><path d="M0 300l70-60 60 40 80-70 90 70 80-40 90 55 70-45 100 60v90H0z"/></g>
<rect y="318" width="640" height="122" fill="#c9d6c2"/>
<path d="M0 352c120-14 260-10 360 2s200 10 280-4v90H0z" fill="#b9c9b1"/>
<g fill="#2f4a3a"><path d="M52 330l26-150 26 150z"/><path d="M40 330l38-110 38 110z"/><path d="M92 334l22-120 22 120z" fill="#3c5a47"/>
<path d="M590 330l22-130 22 130z"/><path d="M572 334l34-100 34 100z" fill="#3c5a47"/></g>
<rect x="74" y="320" width="8" height="18" fill="#4a3a2c"/><rect x="606" y="322" width="7" height="16" fill="#4a3a2c"/>
<!-- päätyseinä -->
<path d="M440 214 L490 146 L540 196 L540 322 L440 340Z" fill="#e6e1d6"/>
<g stroke="#d3cdbf" stroke-width="1.2">{''.join(f'<line x1="{x}" y1="{214 - (x-440)*0.6 if x<=490 else 146+(x-490)*1.0}" x2="{x}" y2="{340-(x-440)*0.18}"/>' for x in range(448, 540, 9))}</g>
<rect x="470" y="232" width="40" height="44" rx="2" fill="#1d2a3a" stroke="#fff" stroke-width="4"/>
<!-- pitkä seinä -->
<rect x="140" y="214" width="300" height="126" fill="#f6f3ec"/>
<g stroke="#e4ded2" stroke-width="1.2">{''.join(f'<line x1="{x}" y1="216" x2="{x}" y2="340"/>' for x in range(148, 440, 9))}</g>
<rect x="138" y="334" width="304" height="10" fill="#9aa39a"/>
<g fill="#1d2a3a" stroke="#fff" stroke-width="4"><rect x="170" y="244" width="58" height="52" rx="2"/><rect x="262" y="244" width="58" height="52" rx="2"/></g>
<g stroke="#fff" stroke-width="3"><line x1="199" y1="244" x2="199" y2="296"/><line x1="291" y1="244" x2="291" y2="296"/></g>
<rect x="356" y="250" width="44" height="88" rx="2" fill="#2b3a4f"/><circle cx="392" cy="296" r="2.5" fill="#d9b48f"/>
<rect x="348" y="244" width="60" height="6" fill="#2b3240"/>
<!-- katto -->
<path d="M122 218 L448 218 L492 140 L176 140Z" fill="url(#roof)"/>
<g stroke="#4a5566" stroke-width="1.4">{''.join(seams)}</g>
<path d="M448 218 L492 140 L548 196" fill="none" stroke="#1b212a" stroke-width="6" stroke-linejoin="round"/>
<line x1="176" y1="140" x2="492" y2="140" stroke="#1b212a" stroke-width="5" stroke-linecap="round"/>
<rect x="372" y="104" width="24" height="40" fill="#8a5a45"/><rect x="368" y="98" width="32" height="8" fill="#5f3d2f"/>
<line x1="130" y1="208" x2="440" y2="208" stroke="#c5ccd6" stroke-width="2.5"/>
<g stroke="#c5ccd6" stroke-width="2">{''.join(f'<line x1="{x}" y1="208" x2="{x+3}" y2="203"/>' for x in range(140, 440, 24))}</g>
<g stroke="#9aa6b5" stroke-width="2.2"><line x1="300" y1="212" x2="338" y2="146"/><line x1="312" y1="212" x2="350" y2="146"/></g>
<g stroke="#9aa6b5" stroke-width="1.6">{''.join(f'<line x1="{300+i*4.5}" y1="{204-i*7.7}" x2="{312+i*4.5}" y2="{204-i*7.7}"/>' for i in range(0, 8))}</g>
<rect x="118" y="218" width="334" height="7" rx="3" fill="#59616d"/>
<rect x="128" y="222" width="7" height="114" fill="#59616d"/><path d="M128 336h14v6h-14z" fill="#59616d"/>
</svg>'''


# ---------- Osiot ----------
def trust_bar():
    items = ["Hinta-arvioita", "Palveluntarjoajien vertailua", "Katon huolto-oppaat", "Helsinki ja pääkaupunkiseutu", "Käytännön tarkistuslistat"]
    lis = "".join(f'<li>{icon("check")}{t}</li>' for t in items)
    return f'<section class="trust" aria-labelledby="trust-h"><div class="wrap"><h2 id="trust-h">Puolueetonta tietoa katon huollosta</h2><ul>{lis}</ul></div></section>'


SYMPTOMS = [
    ("Sammal", "Kosteus, varjo ja orgaaninen lika", "Puhdistus ja sammaleenkäsittely", "/sammaleen-poisto"),
    ("Jäkälä tai levä", "Hidas kasvusto huokoisella pinnalla", "Pesu ja suojakäsittely", "/katon-pesu"),
    ("Lika, lehdet ja havunneulaset", "Puut katon lähellä", "Roskien poisto ja katon pesu", "/katon-pesu"),
    ("Ruoste peltikatolla", "Maalipinnan kuluminen tai vaurio", "Tarkastus ja tarvittaessa huoltomaalaus", "/peltikaton-huolto"),
    ("Rikkinäiset tiilet", "Mekaaninen vaurio, pakkasrapautuminen", "Tiilien vaihto", "/tiilikaton-huolto"),
    ("Löystyneet ruuvit tai kiinnikkeet", "Lämpöliike, vanhentuneet tiivisteet", "Kiinnitysten tarkistus ja uusiminen", "/katon-kuntotarkastus"),
    ("Vaurioituneet läpiviennit", "Tiivistemassan tai kumin vanheneminen", "Läpivientien tiivistys", "/katon-kuntotarkastus"),
    ("Tukkeutuneet rännit", "Lehdet, roskat ja sammal", "Rännien puhdistus", "/rannien-puhdistus"),
    ("Puuttuvat tai heiluvat lumiesteet, tikkaat", "Asennusvirhe tai vaurio", "Kattoturvatuotteiden tarkastus", "/katon-kuntotarkastus"),
    ("Vuotojälki sisäkatossa", "Läpivienti, pellitys tai kattorakenne", "Kuntotarkastus pikaisesti", "/katon-kuntotarkastus"),
    ("Kosteus tai huurre ullakolla", "Aluskatteen vaurio tai puutteellinen tuuletus", "Kuntotarkastus ja ullakon tuuletuksen arviointi", "/katon-kuntotarkastus"),
]


def symptoms_table(limit=None):
    rows = SYMPTOMS[:limit] if limit else SYMPTOMS
    trs = "".join(
        f'<tr><td data-label="Havainto">{a}</td><td data-label="Mahdollinen syy">{b}</td><td data-label="Mitä kannattaa tehdä"><a href="{u}">{c}</a></td></tr>'
        for a, b, c, u in rows)
    return f'''<div class="table-wrap"><table class="stack sym"><caption class="sr-only">Katon oireet, mahdolliset syyt ja suositellut toimenpiteet</caption>
<thead><tr><th scope="col">Havainto</th><th scope="col">Mahdollinen syy</th><th scope="col">Mitä kannattaa tehdä</th></tr></thead><tbody>{trs}</tbody></table></div>'''


SERVICES = [
    ("drop", "Katon pesu", "Pesussa katolta poistetaan lika, roskat sekä sammaleen ja jäkälän alut. Menetelmä ja paine valitaan kattomateriaalin mukaan, ja pesun jälkeen tehdään usein suojakäsittely, joka hidastaa kasvuston paluuta.", "/katon-pesu", "Lue katon pesusta"),
    ("leaf", "Sammaleen poisto", "Sammal pidättää kosteutta ja voi rapauttaa tiiliä, kuluttaa huopaa ja vaurioittaa pellin maalipintaa. Paksu kasvusto poistetaan ensin mekaanisesti ja käsitellään sitten aineella, joka sopii juuri sinun kattomateriaalillesi.", "/sammaleen-poisto", "Lue sammaleen poistosta"),
    ("gutter", "Rännien puhdistus", "Sadevesijärjestelmästä poistetaan lehdet, havut ja muut roskat, ja syöksytorvien vedenkulku tarkistetaan. Toimivat rännit ohjaavat veden pois julkisivulta ja perustuksilta.", "/rannien-puhdistus", "Lue rännien puhdistuksesta"),
    ("clip", "Katon kuntotarkastus", "Tarkastuksessa arvioidaan katon yleiskunto, läpiviennit, pellitykset, kiinnitykset, kattoturvatuotteet sekä mahdollisuuksien mukaan aluskatteen ja ullakon kunto. Tulos auttaa ajoittamaan huollon tai remontin oikein.", "/katon-kuntotarkastus", "Lue kuntotarkastuksesta"),
    ("brush", "Katon maalaus ja pinnoitus", "Huoltomaalaus tai pinnoitus voi pidentää peltikaton tai betonitiilikaton käyttöikää, kun alusta on vielä hyvässä kunnossa. Jos aluskate tai rakenteet ovat elinkaarensa päässä, kattoremontti on usein järkevämpi.", "/katon-pinnoitus", "Pinnoitus vai remontti?"),
    ("wrench", "Pienet kattokorjaukset", "Rikkinäisten tiilien vaihto, ruuvien ja kiinnikkeiden kiristys tai uusiminen, läpivientien tiivistys sekä pellitysten korjaukset. Pieni korjaus ajoissa voi estää kalliin vesivahingon.", "/kattohuolto#korjaukset", "Lue pienistä korjauksista"),
]


def service_cards():
    return '<div class="grid g3">' + "".join(
        f'<article class="card"><div class="icon">{icon(i)}</div><h3>{t}</h3><p>{d}</p><a class="more" href="{u}">{c} {ARROW}</a></article>'
        for i, t, d, u, c in SERVICES) + "</div>"


PRICE_ROWS = [
    ("Katon pesu", "noin 5–10 €/m²", "/katon-pesu"),
    ("Sammaleen poisto", "noin 5–15 €/m²", "/sammaleen-poisto"),
    ("Rännien puhdistus", "noin 150–400 €", "/rannien-puhdistus"),
    ("Katon kuntotarkastus", "noin 250–500 €", "/katon-kuntotarkastus"),
    ("Katon pinnoitus", "noin 20–30 €/m²", "/katon-pinnoitus"),
    ("Katon maalaus", "noin 20–30 €/m²", "/katon-pinnoitus"),
    ("Pienet kattokorjaukset", "tarjouskohtainen", "/kattohuolto#korjaukset"),
]


def price_table():
    trs = "".join(f'<tr><th scope="row"><a href="{u}">{s}</a></th><td class="num" data-label="Suuntaa-antava hinta">{p}</td></tr>' for s, p, u in PRICE_ROWS)
    return f'''<div class="table-wrap"><table><caption class="sr-only">Kattohuollon suuntaa-antavat hinnat Helsingissä</caption>
<thead><tr><th scope="col">Palvelu</th><th scope="col" style="text-align:right">Suuntaa-antava hinta</th></tr></thead><tbody>{trs}</tbody></table></div>
<div class="note"><p>Hintatiedot ovat suuntaa-antavia ja perustuvat julkaistuihin hinnastoihin ja markkinahavaintoihin. Todellinen hinta määräytyy kohteen, katon koon, kunnon ja työn laajuuden perusteella. Hinnat sisältävät ALV:n, ellei toisin mainita. Lähteet: <a href="https://www.kotikatto.fi/hinta" rel="noopener nofollow" target="_blank">Kotikatto.fi</a> ja <a href="https://www.ulkopesu.fi/palvelut/kattopesu" rel="noopener nofollow" target="_blank">Ulkopesu</a>, tarkistettu {fdate(COMPANIES["updatedAt"])}.</p></div>'''


PRICE_FACTORS = ["katon pinta-ala", "kattotyyppi ja materiaali", "katon jyrkkyys", "rakennuksen korkeus", "kasvuston määrä",
                 "katon kunto", "työn laajuus", "nostimet ja telineet", "kohteen sijainti ja saavutettavuus", "tarvittavat korjaukset"]


def price_factors():
    return '<ul class="checklist">' + "".join(f"<li>{x}</li>" for x in PRICE_FACTORS) + "</ul>"


def _chips(name, opts, checked):
    return '<div class="chips">' + "".join(
        f'<div class="chip"><input type="radio" id="{name}-{v}" name="{name}" value="{v}"{" checked" if v == checked else ""}><label for="{name}-{v}">{t}</label></div>'
        for v, t in opts) + "</div>"


def calculator(heading_level="h2"):
    h = heading_level
    return f'''<section class="section" id="laskuri" aria-labelledby="calc-h"><div class="wrap">
<div class="section-head"><p class="eyebrow">Hintalaskuri</p><{h} id="calc-h">Arvioi katon huollon kustannus</{h}>
<p>Valitse katon koko, tyyppi, palvelu ja kasvuston määrä. Laskuri näyttää hintahaarukan, joka perustuu pääkaupunkiseudulla julkaistuihin hinnastoihin.</p></div>
<div class="calc"><form id="calc" onsubmit="return false" aria-describedby="calc-disc">
<fieldset><legend>1. Katon koko</legend>{_chips("koko", [("s","alle 80 m²"),("m","80–120 m²"),("l","120–180 m²"),("xl","yli 180 m²")], "m")}</fieldset>
<fieldset><legend>2. Kattotyyppi</legend>{_chips("tyyppi", [("pelti","Pelti"),("tiili","Tiili"),("huopa","Huopa")], "tiili")}</fieldset>
<fieldset><legend>3. Palvelu</legend>{_chips("palvelu", [("pesu","Pesu"),("sammal","Sammaleen poisto"),("suojaus","Pesu + suojaus"),("tarkastus","Kuntotarkastus"),("pinnoitus","Pinnoitus"),("rannit","Rännien puhdistus")], "suojaus")}</fieldset>
<fieldset id="growth-box" class="mb0"><legend>4. Kasvuston määrä</legend>{_chips("kasvusto", [("vahan","Vähän"),("kohtalainen","Kohtalaisesti"),("paljon","Paljon")], "kohtalainen")}</fieldset>
</form>
<div class="calc-result" aria-live="polite"><span class="label">Arvioitu hintahaarukka</span><output id="calc-out" for="calc">–</output>
<span class="basis" id="calc-basis"></span>
<p class="disclaimer" id="calc-disc">Kyseessä on suuntaa-antava arvio. Lopullinen hinta selviää yrityksen tekemän kohdearvion perusteella.</p>
<p class="muted" style="font-size:.88rem">Arvio sisältää ALV:n. Kotitalousvähennys voi pienentää lopullista kustannusta työn osuudesta. <a href="/usein-kysyttya#kotitalousvahennys">Lue lisää</a>.</p>
<div class="btn-row"><a class="btn btn-primary" href="/tarjouspyynto">Pyydä tarjouksia</a></div></div></div>
</div></section>'''


COLS = [("roofWashPrice", "Katon pesu"), ("mossRemovalPrice", "Sammaleen poisto"), ("inspectionPrice", "Kuntotarkastus"),
        ("gutterCleaningPrice", "Rännit"), ("coatingPrice", "Pinnoitus")]


def _host(u):
    return re.sub(r"^https?://(www\.)?", "", u).split("/")[0]


def comparison():
    rows, cards = "", ""
    for c in COMPANIES["companies"]:
        name = (f'<a href="{esc(c["website"])}" rel="noopener nofollow" target="_blank" data-company="{c["id"]}">{esc(c["name"])}</a>'
                if c["website"] else esc(c["name"]))
        cells = "".join(f'<td data-label="{l}">{esc(c[k])}</td>' if c[k] else f'<td data-label="{l}" class="np">Ei julkaistu</td>' for k, l in COLS)
        rows += (f'<tr><th scope="row">{name}<div class="source">{esc(c["city"])} · <a href="{esc(c["priceSource"])}" rel="noopener nofollow" target="_blank">Lähde</a>, tarkistettu {fdate(c["priceCheckedAt"])}</div></th>'
                 f'{cells}<td data-label="Tarjous"><a class="btn btn-primary btn-sm" href="/tarjouspyynto?yritys={c["id"]}" data-quote="{c["id"]}">Pyydä tarjous</a></td></tr>')
        dds = "".join(f'<div><dt>{l}</dt>' + (f'<dd>{esc(c[k])}</dd>' if c[k] else '<dd class="np">Ei julkaistu</dd>') + "</div>" for k, l in COLS)
        site_btn = (f'<a class="btn btn-secondary btn-sm" href="{esc(c["website"])}" rel="noopener nofollow" target="_blank" data-company="{c["id"]}">Katso yritys</a>' if c["website"] else "")
        cards += (f'<article class="card cmp-card"><h3>{esc(c["name"])}</h3><p class="muted mb0">{esc(c["city"])}</p><dl class="mt2">{dds}</dl>'
                  f'<p class="source">Lähde: <a href="{esc(c["priceSource"])}" rel="noopener nofollow" target="_blank">{_host(c["priceSource"])}</a>, tarkistettu {fdate(c["priceCheckedAt"])}</p>'
                  f'<div class="btn-row">{site_btn}<a class="btn btn-primary btn-sm" href="/tarjouspyynto?yritys={c["id"]}" data-quote="{c["id"]}">Pyydä tarjous</a></div></article>')
    head = "".join(f'<th scope="col">{l}</th>' for _, l in COLS)
    return f'''<div data-companies="compare" data-version="{COMPANIES["updatedAt"]}">
<div class="table-wrap cmp-table"><table><caption class="sr-only">Kattohuoltoyritysten julkaistut hinnat</caption>
<thead><tr><th scope="col">Yritys</th>{head}<th scope="col">Tarjous</th></tr></thead><tbody>{rows}</tbody></table></div>
<div class="cmp-cards">{cards}</div></div>
<div class="note"><p><b>Miten luet vertailua:</b> hinnat ovat yritysten itse julkaisemia esimerkkejä, eivätkä ne tarkoita, että kaikki yritykset veloittavat saman hinnan. "Ei julkaistu" tarkoittaa, ettei yritys ole julkaissut hintaa – pyydä tarjous. Yritysten hinnoittelutavat eroavat: osa ilmoittaa €/m², osa kokonaishinnan katon koon mukaan, ja sisältö (esim. suojakäsittely) vaihtelee. Vertailussa ei ole maksettuja sijoituksia, ja järjestys perustuu julkaistujen hintatietojen määrään.</p></div>'''


def company_cards():
    out = ""
    for c in COMPANIES["companies"]:
        svc = "".join(f'<span class="tag">{esc(s)}</span>' for s in c["services"])
        price_bits = [(l, c[k]) for k, l in COLS if c[k]]
        prices = ("<ul class=\"facts\">" + "".join(f"<li><b>{l}:</b> {esc(v)}</li>" for l, v in price_bits) + "</ul>") if price_bits \
            else '<p class="mt2 mb0"><b>Hinta ei ilmoitettu – pyydä tarjous.</b></p>'
        rev = "<li><b>Arvostelut:</b> tietoa ei ole koottu luotettavasta riippumattomasta lähteestä.</li>"
        site_btn = (f'<a class="btn btn-secondary btn-sm" href="{esc(c["website"])}" rel="noopener nofollow" target="_blank" data-company="{c["id"]}">Katso yritys</a>'
                    if c["website"] else f'<a class="btn btn-secondary btn-sm" href="{esc(c["priceSource"])}" rel="noopener nofollow" target="_blank" data-company="{c["id"]}">Yrityksen tiedot</a>')
        out += f'''<article class="card co-card" data-cats="{"|".join(c["categories"])}">
<h3>{esc(c["name"])}</h3><p class="city">{icon("map",16).replace('aria-hidden="true"','aria-hidden="true" style="display:inline;vertical-align:-2px"')} {esc(c["city"])} · {esc(c["serviceArea"])}</p>
<div>{svc}</div>{prices}
<ul class="facts"><li><b>Huomio:</b> {esc(c["notes"])}</li>{rev}<li class="source">Lähde: <a href="{esc(c["priceSource"])}" rel="noopener nofollow" target="_blank">{_host(c["priceSource"])}</a>, tarkistettu {fdate(c["priceCheckedAt"])}</li></ul>
<div class="row">{site_btn}<a class="btn btn-primary btn-sm" href="/tarjouspyynto?yritys={c["id"]}">Pyydä tarjous</a></div></article>'''
    return out


def company_filters():
    cats = ["Kattohuolto", "Kattopesu", "Sammaleen poisto", "Kattoremontti", "Kattomaalaus", "Kuntotarkastus"]
    b = '<button type="button" class="btn btn-primary btn-sm" data-filter="all" aria-pressed="true">Kaikki</button>'
    b += "".join(f'<button type="button" class="btn btn-secondary btn-sm" data-filter="{c}" aria-pressed="false">{c}</button>' for c in cats)
    return f'<div class="filters" id="co-filters" role="group" aria-label="Suodata yrityksiä palvelun mukaan">{b}</div><p class="sr-only" id="co-count" aria-live="polite"></p>'


def order_steps():
    return '''<ol class="steps">
<li><h3>Tarkista katon perustiedot</h3><p>Selvitä ennen tarjouspyyntöä katon tyyppi, arvioitu pinta-ala, rakennuksen ja katon ikä sekä näkyvät ongelmat. Katon pinta-alan näet usein rakennuslupapiirustuksista; karkeasti se on noin 1,2–1,5 kertaa rakennuksen pohjapinta-ala harjakatolla. Ota kuvia katosta maasta käsin – ne nopeuttavat arviota.</p></li>
<li><h3>Pyydä vähintään 2–3 tarjousta</h3><p>Hinnat ja työtavat vaihtelevat yrityksittäin. Useampi tarjous auttaa hahmottamaan markkinahinnan ja huomaamaan, jos jokin tarjous poikkeaa selvästi muista.</p></li>
<li><h3>Varmista mitä tarjous sisältää</h3><p>Vertaile sisältöä, älä vain loppusummaa:</p>
<ul class="checklist"><li>Työ</li><li>Materiaalit</li><li>ALV</li><li>Jätteiden poisto</li><li>Telineet / nostimet</li><li>Suojaukset</li><li>Jälkikäsittely</li><li>Mahdolliset korjaukset</li><li>Takuu</li></ul></li>
<li><h3>Älä valitse automaattisesti halvinta</h3><p>Kokonaiskustannukseen vaikuttavat myös lisätyöt, telinekulut ja se, kuinka pitkään lopputulos kestää. Halvin tarjous voi tulla kalliiksi, jos siitä puuttuu suojakäsittely tai jos työ joudutaan tekemään pian uudelleen. Tarkista myös, että yritys kuuluu ennakkoperintärekisteriin – se on edellytys kotitalousvähennykselle.</p></li>
<li><h3>Pyydä kirjallinen tarjous</h3><p>Kirjallisesta tarjouksesta näkyvät hinta, sisältö, aikataulu, maksuehdot ja takuu. Pyydä työn osuus eriteltynä, jotta voit hakea kotitalousvähennystä. Kuluttajan ja yrityksen välisissä sopimuksissa voi hyödyntää Rakennustietosäätiön sopimuslomakkeita.</p></li>
</ol>'''


SERVICE_OPTS = ["Katon pesu", "Sammaleen poisto", "Pesu + suojakäsittely", "Rännien puhdistus", "Katon kuntotarkastus",
                "Katon maalaus tai pinnoitus", "Pieni kattokorjaus", "En tiedä vielä – tarvitsen arvion"]


def quote_form(heading="Pyydä tarjouksia kattohuollosta", hlevel="h2"):
    svc = "".join(f'<option value="{s}">{s}</option>' for s in SERVICE_OPTS)
    return f'''<section class="section" id="tarjous" aria-labelledby="form-h"><div class="wrap">
<div class="layout"><div class="form-card">
<{hlevel} id="form-h">{heading}</{hlevel}>
<p class="muted">Kerro kohteestasi, niin välitämme tarjouspyyntösi pääkaupunkiseudulla toimiville kattohuoltoyrityksille. Palvelu on sinulle maksuton eikä sido sinua mihinkään. Yritykset ottavat yhteyttä suoraan, ja sinä päätät, kenen tarjouksen hyväksyt.</p>
<p class="note" id="co-note" hidden>Toivoit tarjousta erityisesti yritykseltä <b></b>. Välitämme toiveen eteenpäin.</p>
<form id="quote-form" data-names="{esc(json.dumps({x["id"]: x["name"] for x in COMPANIES["companies"]}, ensure_ascii=False))}" name="tarjouspyynto" method="POST" action="/kiitos" data-netlify="true" netlify-honeypot="osoite2" enctype="multipart/form-data" novalidate>
<input type="hidden" name="form-name" value="tarjouspyynto"><input type="hidden" name="toivottu_yritys" value="">
<p class="hp"><label>Älä täytä tätä kenttää <input name="osoite2" tabindex="-1" autocomplete="off"></label></p>
<div class="fgrid">
<div class="field"><label for="f-nimi">Nimi *</label><input id="f-nimi" name="nimi" type="text" autocomplete="name" required></div>
<div class="field"><label for="f-puh">Puhelinnumero *</label><input id="f-puh" name="puhelin" type="tel" autocomplete="tel" inputmode="tel" required></div>
<div class="field"><label for="f-email">Sähköposti *</label><input id="f-email" name="sahkoposti" type="email" autocomplete="email" required></div>
<div class="field"><label for="f-pnro">Postinumero *</label><input id="f-pnro" name="postinumero" type="text" inputmode="numeric" autocomplete="postal-code" maxlength="5" pattern="[0-9]{{5}}" required><p class="hint">Esim. 00200</p></div>
<div class="field"><label for="f-tyyppi">Kattotyyppi *</label><select id="f-tyyppi" name="kattotyyppi" required><option value="">Valitse</option><option>Peltikatto</option><option>Tiilikatto (betoni)</option><option>Tiilikatto (savi)</option><option>Huopakatto</option><option>Bitumikermi / tasakatto</option><option>Muu / en tiedä</option></select></div>
<div class="field"><label for="f-koko">Arvioitu katon koko *</label><select id="f-koko" name="koko" required><option value="">Valitse</option><option>alle 80 m²</option><option>80–120 m²</option><option>120–180 m²</option><option>yli 180 m²</option><option>En tiedä</option></select></div>
<div class="field full"><label for="f-palvelu">Tarvittava palvelu *</label><select id="f-palvelu" name="palvelu" required><option value="">Valitse</option>{svc}</select></div>
<div class="field full"><label for="f-lisa">Lisätiedot</label><textarea id="f-lisa" name="lisatiedot" placeholder="Esim. rakennusvuosi, kerrosluku, havaitut ongelmat, toivottu ajankohta"></textarea></div>
<div class="field full"><label for="f-kuvat">Kuvat katosta (valinnainen)</label><input id="f-kuvat" name="kuvat" type="file" accept="image/*" multiple><p class="hint">Kuvat maasta käsin riittävät. Älä kiipeä katolle kuvaamaan.</p></div>
<div class="field full"><label class="consent"><input type="checkbox" name="suostumus" value="kyllä" required> <span>Hyväksyn, että tietojani voidaan käyttää tarjouspyyntöni käsittelyyn. Tiedot välitetään tarjouspyynnön käsittelyyn osallistuville kattohuoltoyrityksille <a href="/tietosuojaseloste">tietosuojaselosteen</a> mukaisesti. *</span></label></div>
</div>
<div class="btn-row mt2"><button class="btn btn-primary" type="submit">Pyydä tarjouksia</button></div>
<p id="form-status" class="form-status" role="status" aria-live="polite"></p>
</form></div>
<aside class="aside"><div class="card"><h3>Mitä tapahtuu seuraavaksi?</h3><ol class="mb0"><li>Käymme pyynnön läpi ja välitämme sen kohteeseen sopiville yrityksille.</li><li>Yritykset ottavat yhteyttä ja voivat pyytää lisätietoja tai sopia kohdekäynnin.</li><li>Vertailet tarjoukset rauhassa. Et ole velvollinen hyväksymään yhtäkään.</li></ol></div>
<div class="card"><h3>Vinkki</h3><p class="mb0">Vertaile tarjouksia <a href="/tarjousten-vertailu">tarkistuslistan</a> avulla ja varmista, että yritys kuuluu ennakkoperintärekisteriin.</p></div></aside>
</div></div></section>'''


ROOF_TYPES = [
    ("Peltikatto", "/peltikaton-huolto", ["Ruoste ja maalipinnan kuluminen", "Ruuvien ja kiinnikkeiden kunto", "Läpiviennit ja pellitykset", "Pesu tarvittaessa matalalla paineella", "Huoltomaalaus maalipinnan kuluttua"]),
    ("Tiilikatto", "/tiilikaton-huolto", ["Sammal ja jäkälä", "Rikkinäiset ja siirtyneet tiilet", "Aluskatteen kunto", "Harjatiivisteet ja -kiinnitykset", "Pesu ja pinnoitus (betonitiili)"]),
    ("Huopakatto", "/huopakaton-huolto", ["Pintasirotteen kuluminen", "Saumat ja halkeamat", "Läpivientien tiiveys", "Kasvusto ja roskat", "Vedenpoisto ja kaivot"]),
]


def roof_types():
    return '<div class="grid g3">' + "".join(
        f'<article class="card"><div class="icon">{icon("roof")}</div><h3>{t}</h3><ul>' + "".join(f"<li>{x}</li>" for x in li) +
        f'</ul><a class="more" href="{u}">{t[:-2]}ton huolto {ARROW}</a></article>' for t, u, li in ROOF_TYPES) + "</div>"


def areas():
    return f'''<ul class="pills"><li><a href="/kattohuolto-helsinki">Kattohuolto Helsinki</a></li><li><a href="/kattohuolto-espoo">Kattohuolto Espoo</a></li>
<li><a href="/kattohuolto-vantaa">Kattohuolto Vantaa</a></li><li><a href="/kattohuolto-kauniainen">Kattohuolto Kauniainen</a></li></ul>'''


def band(title="Haluatko tarjouksia omaan kohteeseesi?", text="Täytä tarjouspyyntö kerran ja vertaile vastauksia rauhassa. Maksuton ja sitoumukseton.",
         primary=("/tarjouspyynto", "Pyydä tarjouksia"), secondary=("/hinnat", "Vertaile hintoja")):
    return f'''<section class="section"><div class="wrap"><div class="band"><div><h2>{title}</h2><p>{text}</p></div>
<div class="btn-row"><a class="btn btn-primary" href="{primary[0]}">{primary[1]}</a><a class="btn btn-secondary" href="{secondary[0]}">{secondary[1]}</a></div></div></div></section>'''


def faq_section(items, title="Usein kysyttyä", ids=True):
    det = ""
    for q, a in items:
        slug = re.sub(r"[^a-z0-9]+", "-", q.lower().translate(str.maketrans("äöå", "aoa"))).strip("-")
        if "kotitalousv" in slug:
            slug = "kotitalousvahennys"
        det += f'<details id="{slug}"><summary>{q}</summary><div class="a">{a}</div></details>'
    return f'<section class="section" aria-labelledby="faq-h"><div class="wrap narrow"><h2 id="faq-h">{title}</h2><div class="faq">{det}</div></div></section>'


def related(links, title="Lue myös"):
    return f'<div class="card"><h3>{title}</h3><ul class="mb0">' + "".join(f'<li><a href="{u}">{t}</a></li>' for u, t in links) + "</ul></div>"


def aside_cta():
    return f'''<div class="card" style="background:var(--ink);color:#dfe5ee;border-color:var(--ink)"><h3 style="color:#fff">Pyydä tarjouksia</h3>
<p style="color:#c9d2df">Kerro kohteestasi kerran – vertaile tarjoukset rauhassa.</p><a class="btn btn-primary" href="/tarjouspyynto">Pyydä tarjouksia</a>
<p class="mb0 mt2"><a href="/hinnat#laskuri" style="color:#fff">Laske kustannusarvio {ARROW.replace('aria-hidden="true"','aria-hidden="true" style="display:inline;vertical-align:-3px"')}</a></p></div>'''


def prose_page(body, aside_links=None, article_id=None):
    aside = aside_cta() + (related(aside_links) if aside_links else "")
    art = f' data-article="{article_id}"' if article_id else ""
    return f'''<section class="section"><div class="wrap"><div class="layout"><article class="prose"{art}>{body}<span id="article-end"></span></article>
<aside class="aside">{aside}</aside></div></div></section>'''
