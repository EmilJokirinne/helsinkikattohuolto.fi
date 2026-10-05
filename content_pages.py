"""Pääsivujen sisältö."""
import components as C
from content_faq import FAQ_ALL, FAQ_ORDER, faq_by_ids

A = C.ARROW


def sec(inner, white=False, id=None, label=None):
    i = f' id="{id}"' if id else ""
    l = f' aria-labelledby="{label}"' if label else ""
    return f'<section class="section{" white" if white else ""}"{i}{l}><div class="wrap">{inner}</div></section>'


def head(eyebrow, h2, text="", id=None):
    i = f' id="{id}"' if id else ""
    return f'<div class="section-head"><p class="eyebrow">{eyebrow}</p><h2{i}>{h2}</h2>{f"<p>{text}</p>" if text else ""}</div>'


# =====================================================================
# ETUSIVU
# =====================================================================
HOME_HERO = f'''<section class="hero"><div class="wrap hero-grid">
<div><p class="eyebrow">Kattohuollon tietopalvelu · Helsinki ja pääkaupunkiseutu</p>
<h1>Kattohuolto Helsingissä – hinnat, palvelut ja yritykset vertailussa</h1>
<p class="lead">Milloin katto kannattaa pestä, huoltaa tai korjata? HelsinkiKattoHuolto.fi kokoaa yhteen tietoa katon huollosta, kustannuksista ja Helsingin alueella toimivista palveluntarjoajista.</p>
<div class="btn-row"><a class="btn btn-primary" href="#hinnat">Vertaile kattohuollon hintoja</a><a class="btn btn-secondary" href="/kevaan-katon-tarkistuslista">Katso huollon tarkistuslista</a></div>
<p class="meta-line">Emme tee kattotöitä itse. Autamme ymmärtämään katon huoltoa, kustannuksia ja vaihtoehtoja ennen kuin tilaat työn.</p></div>
<div class="hero-art">{C.hero_svg()}</div></div></section>''' + C.trust_bar()

HOME_QUICK = sec(f'''<div class="grid g4">
<a class="card" href="/kattohuolto"><div class="icon">{C.icon("book")}</div><h3>Mitä kattohuolto on?</h3><p class="mb0">Pesu, sammaleen poisto, rännit, tarkastus ja pienet korjaukset – katon käyttöikää pidentävät toimet.</p></a>
<a class="card" href="#palvelut"><div class="icon">{C.icon("list")}</div><h3>Mitä palveluita on?</h3><p class="mb0">Kuusi yleisintä kattohuollon palvelua ja milloin kukin on ajankohtainen.</p></a>
<a class="card" href="#hinnat"><div class="icon">{C.icon("euro")}</div><h3>Paljonko maksaa?</h3><p class="mb0">Suuntaa-antavat hinnat julkaistuista hinnastoista ja hintalaskuri.</p></a>
<a class="card" href="#yritykset"><div class="icon">{C.icon("scale")}</div><h3>Miten vertailen?</h3><p class="mb0">Yritysten julkaisemat hinnat rinnakkain ja ohje tarjousten vertailuun.</p></a>
</div>''', label=None)

HOME_WHEN = sec(head("Tunnista huollon tarve", "Milloin katto tarvitsee huoltoa?",
  "Useimmat katto-ongelmat alkavat pienistä merkeistä, jotka näkee maasta käsin tai ullakolta. Kun ne huomaa ajoissa, korjaus on yleensä edullinen.", "when-h") + '''
<div class="grid g2" style="margin-bottom:28px">
<div class="card"><h3>Katon pinnalla</h3><p><b>Sammal ja jäkälä</b> pidättävät kosteutta, joka pakkasella laajenee ja rapauttaa pintaa. <b>Lika, lehdet ja havunneulaset</b> kerääntyvät erityisesti kattolappeiden taitteisiin ja läpivientien taakse. <b>Ruoste</b> peltikatolla on merkki maalipinnan kulumisesta. <b>Rikkinäiset tai siirtyneet tiilet</b> ja <b>löystyneet ruuvit</b> avaavat reitin vedelle.</p><p class="mb0">Katso myös <b>läpivientien</b> (piippu, ilmanvaihto, antennit) tiivisteitä sekä <b>lumiesteitä, kattotikkaita ja kulkusiltoja</b>: niiden pitää olla tukevasti kiinni.</p></div>
<div class="card"><h3>Räystäillä ja sisällä</h3><p><b>Rännit</b>, joista vesi valuu yli tai joissa kasvaa sammalta, ovat tukossa. Tukkeutunut sadevesijärjestelmä kastelee julkisivua ja sokkelia ja voi aiheuttaa jäätymisvaurioita.</p><p class="mb0">Sisäpuolella tärkeimmät merkit ovat <b>vuotojäljet</b> katossa tai seinien yläosissa sekä <b>kosteus, huurre tai tunkkainen haju ullakolla</b>. Ne voivat viitata läpivientiin, pellitykseen tai aluskatteeseen, ja ne kannattaa tarkastuttaa pian.</p></div>
</div>''' + C.symptoms_table(5) + '<p class="mt2"><a href="/kattohuolto#oireet">Katso koko oiretaulukko (11 yleistä havaintoa) ' + A.replace('aria-hidden="true"', 'aria-hidden="true" style="display:inline;vertical-align:-3px"') + '</a></p>', white=True, label="when-h")

HOME_SERVICES = sec(head("Palvelut", "Kattohuollon palvelut", "Kattohuolto koostuu muutamasta selkeästä palvelusta. Näin ne eroavat toisistaan.", "svc-h") + C.service_cards(), id="palvelut", label="svc-h")

HOME_PRICES = sec(head("Hinnat", "Paljonko kattohuolto maksaa Helsingissä?",
  "Kattohuollon hinta riippuu useasta tekijästä. Siksi luotettavin hinta saadaan aina kohteen perusteella. Alla olevat haarukat auttavat arvioimaan, onko saamasi tarjous kohtuullinen.", "price-h") + '''
<div class="grid g2" style="align-items:start"><div>''' + C.price_table() + '''</div>
<div class="card"><h3>Hintaan vaikuttavat</h3>''' + C.price_factors() + '''<p class="mb0 muted" style="font-size:.95rem">Esimerkiksi jyrkkä, kaksikerroksisen talon katto voi vaatia nostimen, mikä nostaa hintaa samankokoiseen matalaan kattoon verrattuna.</p></div></div>''', white=True, id="hinnat", label="price-h")

HOME_COMPARE = sec(head("Hintavertailu", "Kattohuollon hinnat – mitä eri yritykset veloittavat?",
  "Vertailussa on vain yritysten itse julkaisemia hintoja. Jokaisen hinnan kohdalla näkyy lähde ja tarkistuspäivä.", "cmp-h") + C.comparison() +
  f'<div class="btn-row mt2"><a class="btn btn-secondary" href="/yritykset">Etsi kattohuoltoyritys</a><a class="btn btn-ghost" href="/hinnat">Kaikki hintatiedot</a></div>', id="yritykset", label="cmp-h")

HOME_ORDER = sec(head("Opas", "Näin tilaat kattohuollon Helsingissä", "Viisi vaihetta, joilla saat vertailukelpoiset tarjoukset ja vältät yleisimmät sudenkuopat.", "ord-h") + C.order_steps(), white=True, label="ord-h")

HOME_TYPES = sec(head("Kattotyypit", "Katon huolto kattotyypeittäin", "Pelti-, tiili- ja huopakatto vanhenevat eri tavoin, joten myös huolto on erilaista.", "types-h") + C.roof_types(), label="types-h")

HOME_HKI = sec('''<div class="grid g2" style="align-items:start"><div>''' + head("Paikallisesti", "Kattohuolto Helsingissä", "", "hki-h") + '''
<p>Helsingin rannikkoilmasto on kostea, ja talvisin lämpötila vaihtelee usein nollan molemmin puolin. Toistuva sulaminen ja jäätyminen rasittavat katteita, läpivientejä ja rännejä enemmän kuin tasainen pakkastalvi. Lumikuorma ja jää kertyvät erityisesti räystäille ja kattolappeiden taitteisiin.</p>
<p>Syksyn lehdet ja havunneulaset tukkivat rännejä erityisesti puistomaisilla pientaloalueilla, kuten Oulunkylässä, Pakilassa, Kulosaaressa ja Laajasalossa. Kevään sulamisvedet paljastavat, toimiiko sadevesijärjestelmä.</p>
<p>Helsingissä on paljon vanhaa pientalokantaa, jonka katoissa on jo useampi huolto- tai korjauskierros takana. Vanhoissa taloissa kannattaa kiinnittää huomiota erityisesti aluskatteeseen ja läpivientien tiivistyksiin. Pesua tarvitaan useammin varjoisilla, puiden ympäröimillä tonteilla, kuten monilla meren läheisillä alueilla.</p>
<p><a href="/kattohuolto-helsinki">Lue lisää kattohuollosta Helsingissä ''' + A.replace('aria-hidden="true"', 'aria-hidden="true" style="display:inline;vertical-align:-3px"') + '''</a></p></div>
<div class="card"><h3>Kattohuolto pääkaupunkiseudulla</h3><p>Samat yritykset palvelevat usein koko pääkaupunkiseutua. Paikallisilla sivuilla kerromme alueen erityispiirteistä ja vertailussa olevista yrityksistä, jotka ilmoittavat palvelevansa aluetta.</p>''' + C.areas() + '''</div></div>''', white=True, label="hki-h")

HOME_GUIDE = sec(head("Katto-opas", "Uusimmat oppaat", "Käytännönläheisiä ohjeita katon huoltoon ilman myyntipuhetta.", "guide-h") + f'''<div class="grid g3">
<a class="card" href="/katon-huolto-opas"><h3>Katon huolto – täydellinen opas suomalaiselle omakotitalolle</h3><p class="mb0">Kaikki olennainen katon huollosta yhdessä paikassa.</p></a>
<a class="card" href="/sammal-katolla"><h3>Sammal katolla – pitääkö olla huolissaan?</h3><p class="mb0">Milloin sammal on kosmeettinen haitta ja milloin riski.</p></a>
<a class="card" href="/pinnoitus-vai-kattoremontti"><h3>Katon pinnoitus vai kattoremontti?</h3><p class="mb0">Näin arvioit, kumpi on järkevämpi sijoitus.</p></a>
</div><p class="mt2"><a class="btn btn-secondary" href="/katto-opas">Kaikki artikkelit</a></p>''', label="guide-h")

HOME = dict(slug="/", title="Kattohuolto Helsinki – hinnat, palvelut ja yritysten vertailu",
    desc="Kattohuolto Helsingissä: vertaa katon pesun, sammaleen poiston, kuntotarkastuksen ja muiden kattopalveluiden hintoja sekä löydä sopiva palveluntarjoaja.",
    h1="Kattohuolto Helsingissä – hinnat, palvelut ja yritykset vertailussa", hero_html=HOME_HERO, priority="1.0",
    body=HOME_QUICK + HOME_WHEN + HOME_SERVICES + HOME_PRICES + C.calculator() + HOME_COMPARE + HOME_ORDER + C.quote_form() + HOME_TYPES + HOME_HKI + HOME_GUIDE,
    faq=faq_by_ids("usein", "pesu_hinta", "milloin_pesta", "painepesuri", "kotitalousvahennys", "tarjoukset"),
    faq_title="Usein kysyttyä kattohuollosta")


# =====================================================================
# PALVELUSIVUT
# =====================================================================
def svc_page(slug, title, desc, h1, lead, crumbs, body, faq_ids=(), links=None, priority="0.8", calc=False, article=None, modified=None):
    content = C.prose_page(body, links)
    if calc:
        content += C.calculator()
    content += C.band()
    p = dict(slug=slug, title=title, desc=desc, h1=h1, lead=lead, crumbs=crumbs, body=content, priority=priority,
             faq=faq_by_ids(*faq_ids) if faq_ids else None, meta_line=f"Päivitetty {C.fdate(C.COMPANIES['updatedAt'])} · Hintatiedot tarkistettu {C.fdate(C.COMPANIES['updatedAt'])}")
    if article:
        p["article"] = {"published": article}
    return p


KATTOHUOLTO = svc_page("/kattohuolto", "Kattohuolto – mitä se sisältää ja milloin sitä tarvitaan",
  "Mitä kattohuolto sisältää? Katon pesu, sammaleen poisto, rännien puhdistus, kuntotarkastus ja pienet korjaukset selkeästi selitettynä sekä suuntaa-antavat hinnat.",
  "Kattohuolto – mitä se sisältää ja milloin sitä tarvitaan",
  "Kattohuolto on katon säännöllistä kunnossapitoa, jolla pidennetään katteen käyttöikää ja ehkäistään vesivahinkoja. Tällä sivulla käymme läpi, mistä huolto koostuu ja miten tunnistat tarpeen.",
  [("/kattohuolto", "Kattohuolto")], f'''
<h2>Mitä kattohuolto tarkoittaa?</h2>
<p>Kattohuollolla tarkoitetaan toimenpiteitä, joilla katto pidetään toimintakuntoisena ennen kuin ongelmat ehtivät rakenteisiin. Kattoremontti uusii katteen, kun taas huolto pitää olemassa olevan katon kunnossa mahdollisimman pitkään. Tyypillinen kattohuolto sisältää yhden tai useamman seuraavista:</p>
<ul><li><a href="/katon-pesu">katon pesu</a> ja roskien poisto</li><li><a href="/sammaleen-poisto">sammaleen ja jäkälän poisto</a> sekä suojakäsittely</li><li><a href="/rannien-puhdistus">rännien ja syöksytorvien puhdistus</a></li><li><a href="/katon-kuntotarkastus">katon kuntotarkastus</a></li><li><a href="/katon-pinnoitus">huoltomaalaus tai pinnoitus</a></li><li>pienet korjaukset, kuten tiilien vaihto ja läpivientien tiivistys</li></ul>
<h2 id="oireet">Milloin katto tarvitsee huoltoa?</h2>
<p>Alla olevaan taulukkoon on koottu yleisimmät havainnot, niiden tavalliset syyt ja suositeltu jatkotoimi. Taulukko on suuntaa antava: varma syy selviää vasta tarkastuksessa.</p>
{C.symptoms_table()}
<h2>Huollon vuosirytmi</h2>
<div class="table-wrap"><table class="stack"><thead><tr><th scope="col">Toimenpide</th><th scope="col">Tyypillinen väli</th></tr></thead><tbody>
<tr><th scope="row">Silmämääräinen tarkistus maasta ja ullakolta</th><td data-label="Tyypillinen väli">2 kertaa vuodessa (kevät ja syksy)</td></tr>
<tr><th scope="row">Rännien puhdistus</th><td data-label="Tyypillinen väli">1–2 kertaa vuodessa</td></tr>
<tr><th scope="row">Katon pesu ja suojakäsittely</th><td data-label="Tyypillinen väli">3–5 vuoden välein, varjoisalla tontilla useammin</td></tr>
<tr><th scope="row">Ammattilaisen kuntotarkastus</th><td data-label="Tyypillinen väli">noin 5 vuoden välein ja aina vuotoepäilyssä</td></tr>
<tr><th scope="row">Huoltomaalaus (peltikatto)</th><td data-label="Tyypillinen väli">kun maalipinta on kulunut, usein 15–25 vuoden välein</td></tr>
</tbody></table></div>
<p>Välit ovat yleisiä nyrkkisääntöjä. Valmistajan ohjeet ja katon todellinen kunto ratkaisevat.</p>
<h2 id="korjaukset">Pienet kattokorjaukset</h2>
<p>Moni vesivahinko alkaa yksittäisestä vauriosta, jonka korjaaminen olisi ollut nopeaa. Tyypillisiä pieniä korjauksia ovat:</p>
<ul><li><b>Tiilien vaihto:</b> haljenneet, rapautuneet tai siirtyneet tiilet vaihdetaan tai asetetaan paikalleen. Varatiilet kannattaa säilyttää.</li>
<li><b>Ruuvien ja kiinnikkeiden tarkistus:</b> peltikaton ruuvien tiivisteet vanhenevat, ja ruuvit voivat löystyä lämpöliikkeen takia.</li>
<li><b>Tiivistykset:</b> läpivientien kumit ja massat haurastuvat ajan myötä. Vanhentunut tiiviste on yleinen vuotokohta.</li>
<li><b>Pellitykset:</b> piipun, räystään ja taitteiden pellitysten kiinnitykset ja saumat tarkistetaan ja korjataan.</li>
<li><b>Läpiviennit:</b> ilmanvaihtoputkien, antennien ja muiden läpivientien liitokset tarkistetaan.</li></ul>
<p>Pienet korjaukset hinnoitellaan yleensä tarjouksen perusteella. Esimerkiksi Kotikatto.fi ilmoittaa läpivientien tiivistyksille kiinteät pakettihinnat <a href="https://www.kotikatto.fi/hinta" rel="noopener nofollow" target="_blank">hinnastossaan</a>.</p>
<h2>Kuka huollon tekee?</h2>
<p>Kevyitä toimia, kuten roskien poiston rännistä matalalta katolta, voi tehdä itse, kun kattoturvatuotteet ovat kunnossa. Pesu, sammalkäsittely, korjaukset ja tarkastukset kannattaa yleensä teettää ammattilaisella sekä työturvallisuuden että lopputuloksen vuoksi. Vertailemme pääkaupunkiseudulla toimivia yrityksiä <a href="/yritykset">yrityssivulla</a>.</p>
<h2>Kattohuollon hinnat lyhyesti</h2>
{C.price_table()}''', faq_ids=("usein", "kotitalousvahennys", "remontti"),
  links=[("/hinnat", "Kattohuollon hinnat"), ("/katon-huolto-opas", "Katon huolto – täydellinen opas"), ("/kevaan-katon-tarkistuslista", "Kevään tarkistuslista"), ("/syksyn-katon-tarkistuslista", "Syksyn tarkistuslista")], priority="0.9")


KATON_PESU = svc_page("/katon-pesu", "Katon pesu – menetelmät, hinta ja ajankohta",
  "Katon pesu selkeästi: miten pesu tehdään eri kattomateriaaleille, mitä jälkikäsittely tarkoittaa, paljonko pesu maksaa ja milloin se kannattaa tehdä.",
  "Katon pesu", "Katon pesu poistaa lian, roskat ja kasvuston alut sekä hidastaa katteen kulumista. Tärkeintä on valita menetelmä kattomateriaalin mukaan.",
  [("/katon-pesu", "Katon pesu")], f'''
<h2>Mitä katon pesu sisältää?</h2>
<p>Ammattimainen katon pesu etenee yleensä seuraavasti:</p>
<ol><li><b>Tarkastus:</b> kattomateriaali, kunto ja kasvuston määrä arvioidaan. Samalla nähdään, onko katolla korjattavaa.</li>
<li><b>Suojaus:</b> ikkunat, julkisivu ja istutukset suojataan pesuvedeltä.</li>
<li><b>Lian ja kasvuston poisto:</b> irtoroskat, lehdet ja paksu sammal poistetaan mekaanisesti.</li>
<li><b>Pesu:</b> katto pestään materiaalille sopivalla paineella ja pesuaineella ylhäältä alaspäin.</li>
<li><b>Jälkikäsittely:</b> pinnalle levitetään suoja-aine, joka hidastaa sammaleen, jäkälän ja levän uudelleenkasvua.</li>
<li><b>Viimeistely:</b> rännit tyhjennetään pesussa irronneesta aineksesta, ja pihapiiri siivotaan.</li></ol>
<h2>Pesu kattomateriaalin mukaan</h2>
<div class="table-wrap"><table class="stack"><thead><tr><th scope="col">Kattotyyppi</th><th scope="col">Pesutapa</th><th scope="col">Huomioitavaa</th></tr></thead><tbody>
<tr><th scope="row">Peltikatto</th><td data-label="Pesutapa">Matala paine, usein pelkkä vesi tai mieto pesuaine</td><td data-label="Huomioitavaa">Maalipintaa ei saa kuluttaa. Pesu tehdään usein ennen huoltomaalausta.</td></tr>
<tr><th scope="row">Betonitiilikatto</th><td data-label="Pesutapa">Mekaaninen poisto ja painepesu sopivalla paineella</td><td data-label="Huomioitavaa">Huokoinen pinta sammaloituu nopeasti. Suojakäsittely tai pinnoitus on tärkeä.</td></tr>
<tr><th scope="row">Savitiilikatto</th><td data-label="Pesutapa">Varovainen pesu ja kasvustonpoistoaine</td><td data-label="Huomioitavaa">Vettä ei saa painaa tiilien alle. Valmistajan ohjeet kannattaa tarkistaa.</td></tr>
<tr><th scope="row">Huopakatto</th><td data-label="Pesutapa">Harjaus, matala paine ja pesuaine</td><td data-label="Huomioitavaa">Kova paine irrottaa pintasirotetta. Ei korkeapainepesua.</td></tr>
</tbody></table></div>
<h2>Paljonko katon pesu maksaa?</h2>
<p>Pääkaupunkiseudulla julkaistujen hinnastojen perusteella katon pesu maksaa noin <b>5–10 €/m²</b>. Esimerkkejä yritysten julkaisemista hinnoista:</p>
<ul><li>Kotikatto.fi: katon pesu 9 €/m², minimiveloitus 990 € (<a href="https://www.kotikatto.fi/hinta" rel="noopener nofollow" target="_blank">lähde</a>, tarkistettu {C.fdate(C.COMPANIES["updatedAt"])})</li>
<li>Ulkopesu: kattopesu suojakäsittelyineen 490–700 € (alle 80 m²), 700–1 200 € (80–150 m²) ja 1 200–1 800 € (150–250 m²) (<a href="https://www.ulkopesu.fi/palvelut/kattopesu" rel="noopener nofollow" target="_blank">lähde</a>, tarkistettu {C.fdate(C.COMPANIES["updatedAt"])})</li></ul>
<p>Hinnoittelutavat eroavat, joten vertaa tarjousten sisältöä: sisältyykö suojakäsittely, rännien tyhjennys ja mahdolliset nostimet. <a href="/katon-pesu-hinta">Lue tarkempi hintaopas</a>.</p>
<h2>Milloin pesu kannattaa tehdä?</h2>
<p>Pesu tehdään kuivalla säällä, kun lämpötila pysyy plussalla myös öisin. Käytännössä parasta aikaa ovat touko–kesäkuu ja elo–syyskuu. Pakkasella pesua ei tehdä, ja helteellä pesuaineet kuivuvat liian nopeasti. <a href="/milloin-katto-kannattaa-pesta">Milloin katto kannattaa pestä?</a></p>
<h2>Kannattaako pestä itse?</h2>
<p>Katolla työskentely on putoamisvaaran vuoksi vaarallista, ja märkä, pesuaineella käsitelty pinta on liukas. Jos pesee itse, katolla on oltava kunnolliset kattoturvatuotteet ja käytössä turvavaljaat. Painepesurin väärä käyttö voi myös vaurioittaa katetta. Jyrkille ja korkeille katoille suosittelemme ammattilaista.</p>''',
  faq_ids=("pesu_hinta", "milloin_pesta", "painepesuri", "kesto"),
  links=[("/katon-pesu-helsinki", "Kattopesun hinta Helsingissä"), ("/sammaleen-poisto", "Sammaleen poisto"), ("/katon-pesu-hinta", "Paljonko katon pesu maksaa?")], calc=True, priority="0.9")


KATON_PESU_HKI = svc_page("/katon-pesu-helsinki", "Kattopesun hinta Helsingissä – vertailu ja esimerkit",
  "Kattopesu Helsingissä: julkaistut hinnat, esimerkkilaskelmat eri kokoisille katoille, kotitalousvähennyksen vaikutus ja vinkit tarjousten vertailuun.",
  "Kattopesun hinta Helsingissä", "Paljonko katon pesu maksaa helsinkiläiselle omakotitalolle? Kokosimme yritysten julkaisemat hinnat ja laskimme esimerkit tavallisille kattokoille.",
  [("/katon-pesu", "Katon pesu"), ("/katon-pesu-helsinki", "Helsinki")], f'''
<h2>Kattopesun hinnat Helsingissä</h2>
<p>Helsingissä toimivien yritysten julkaisemien hinnastojen perusteella katon pesu maksaa noin <b>5–10 €/m²</b>. Neliöhinta laskee yleensä katon koon kasvaessa, ja pienille katoille on usein minimiveloitus.</p>
<div class="table-wrap"><table class="stack"><thead><tr><th scope="col">Katon koko</th><th scope="col">Ulkopesu (sis. suojakäsittely)</th><th scope="col">Kotikatto.fi (9 €/m², min. 990 €)</th></tr></thead><tbody>
<tr><th scope="row">alle 80 m²</th><td data-label="Ulkopesu">490–700 €</td><td data-label="Kotikatto.fi">990 € (minimiveloitus)</td></tr>
<tr><th scope="row">120 m²</th><td data-label="Ulkopesu">700–1 200 € (80–150 m²)</td><td data-label="Kotikatto.fi">1 080 € (laskettu)</td></tr>
<tr><th scope="row">200 m²</th><td data-label="Ulkopesu">1 200–1 800 € (150–250 m²)</td><td data-label="Kotikatto.fi">1 800 € (laskettu)</td></tr>
</tbody></table></div>
<p class="source">Lähteet: <a href="https://www.ulkopesu.fi/palvelut/kattopesu" rel="noopener nofollow" target="_blank">ulkopesu.fi</a> ja <a href="https://www.kotikatto.fi/hinta" rel="noopener nofollow" target="_blank">kotikatto.fi</a>, tarkistettu {C.fdate(C.COMPANIES["updatedAt"])}. Kotikatto.fi:n rivit on laskettu yrityksen ilmoittamasta neliöhinnasta. Ne eivät ole yrityksen antamia tarjouksia.</p>
<h2>Kotitalousvähennyksen vaikutus</h2>
<p>Kattopesu on kunnossapitotyötä, josta voi saada kotitalousvähennystä työn osuudesta. Hallituksen esityksen mukaan vuonna 2026 vähennys on 40 % työn osuudesta, ja omavastuu on 150 €. Esimerkki: jos 1 000 euron laskussa työn osuus on 800 €, vähennys on 800 € × 40 % − 150 € = <b>170 €</b>. Todellinen työn osuus näkyy yrityksen laskusta. <a href="/usein-kysyttya#kotitalousvahennys">Lue ehdot</a>.</p>
<h2>Miksi hinnat vaihtelevat Helsingissä?</h2>
<ul><li><b>Rakennuksen korkeus ja jyrkkyys:</b> kaksikerroksisissa ja jyrkkäkattoisissa taloissa voidaan tarvita nostinta.</li>
<li><b>Saavutettavuus:</b> ahtaat tontit ja pysäköinti kantakaupungin lähellä voivat vaikuttaa työn järjestelyihin.</li>
<li><b>Kasvuston määrä:</b> meren ja puiston läheisillä, varjoisilla tonteilla kasvustoa on usein enemmän.</li>
<li><b>Sisältö:</b> osa hinnoista sisältää suojakäsittelyn ja rännien tyhjennyksen, osa ei.</li></ul>
<h2>Näin saat parhaan hinta-laatusuhteen</h2>
<p>Pyydä 2–3 tarjousta samoilla tiedoilla: katon tyyppi, pinta-ala, kerrosluku ja kuvat. Varmista, että tarjouksissa on sama sisältö, ja kysy suojakäsittelyn vaikutusajasta. <a href="/tarjousten-vertailu">Katso tarjousten vertailun tarkistuslista</a>.</p>''',
  faq_ids=("pesu_hinta", "kotitalousvahennys"), links=[("/katon-pesu", "Katon pesu"), ("/kattohuolto-helsinki", "Kattohuolto Helsingissä"), ("/yritykset", "Yritysvertailu")], calc=True, article="2026-10-05")


SAMMAL = svc_page("/sammaleen-poisto", "Sammaleen poisto katolta – menetelmät ja hinta",
  "Sammaleen poisto katolta: miksi sammal kannattaa poistaa, miten menetelmä riippuu kattomateriaalista, paljonko poisto maksaa ja miten uudelleenkasvua hidastetaan.",
  "Sammaleen poisto katolta", "Sammal ei ole vain ulkonäköasia. Se sitoo kosteutta ja voi ajan myötä vaurioittaa katetta. Kerromme, miten sammal poistetaan oikein eri kattotyypeiltä.",
  [("/sammaleen-poisto", "Sammaleen poisto")], f'''
<h2>Miksi sammal kannattaa poistaa?</h2>
<p>Sammal ja jäkälä pidättävät vettä kuin sieni. Katon pinta pysyy kosteana pitkään, ja pakkasella jäätyvä vesi laajenee ja rapauttaa tiilen pintaa. Huopakatolla juurtuva kasvusto voi muodostaa halkeamia ja epätiiviitä kohtia, ja peltikatolla kosteus ja orgaaninen aines kuluttavat maalipintaa. Sammal myös tukkii rännejä ja voi padota vettä tiilien väliin.</p>
<p>Sammal ilmestyy tavallisesti ensin pohjoisen ja idän puoleisille lappeille sekä puiden varjostamiin kohtiin.</p>
<h2>Menetelmä riippuu kattomateriaalista</h2>
<ul><li><b>Betonitiilikatto:</b> paksu sammal poistetaan mekaanisesti, ja katto pestään ja käsitellään sammalta tuhoavalla aineella. Suojakäsittely tai pinnoitus hidastaa uudelleenkasvua.</li>
<li><b>Savitiilikatto:</b> käsittely tehdään varovasti, jotta lasite tai pinta ei vaurioidu eikä vesi pääse tiilien alle.</li>
<li><b>Huopakatto:</b> sammal irrotetaan varovasti harjaamalla ja kemiallisella käsittelyllä. Kova painepesu tai kaapiminen voi irrottaa pintasirotteen.</li>
<li><b>Peltikatto:</b> kasvustoa on yleensä vähemmän. Se poistetaan pesuaineella ja matalalla paineella maalipintaa kuluttamatta.</li></ul>
<h2>Kaksivaiheinen käsittely paksulle sammaleelle</h2>
<p>Kun sammalkerros on paksu, tehokas tapa on käsitellä katto ensin kasvustoa tuhoavalla aineella ja antaa sen vaikuttaa. Kuollut sammal irtoaa helpommin, ja se poistetaan harjaamalla tai pesemällä muutaman viikon tai kuukauden kuluttua. Näin vältetään liiallinen mekaaninen rasitus.</p>
<h2>Paljonko sammaleen poisto maksaa?</h2>
<p>Hinnat vaihtelevat sen mukaan, myydäänkö sammaleen poisto osana kattopesua vai erillisenä syväpuhdistuksena. Julkaistuja esimerkkejä:</p>
<ul><li>Kotikatto.fi: normaali sammaleen poisto 12 €/m², vaativa (paljon sammalta) 15 €/m² (<a href="https://www.kotikatto.fi/hinta" rel="noopener nofollow" target="_blank">lähde</a>)</li>
<li>Ulkopesu: sammaleen poisto sisältyy kattopesuun (esim. 700–1 200 € katolle 80–150 m²) (<a href="https://www.ulkopesu.fi/palvelut/kattopesu" rel="noopener nofollow" target="_blank">lähde</a>)</li></ul>
<p>Hinnat tarkistettu {C.fdate(C.COMPANIES["updatedAt"])}. Kokonaishinta selviää kohdekäynnillä.</p>
<h2>Miten estän sammaleen paluun?</h2>
<ul><li>Pidä katto ja rännit puhtaina lehdistä ja neulasista.</li><li>Karsi katon ylle kurottuvia oksia, jotta katto kuivuu nopeammin.</li><li>Teetä pesun jälkeen suojakäsittely ja uusi se valmistajan suosituksen mukaan.</li><li>Betonitiilikatolla pinnoitus voi tiivistää pintaa ja hidastaa kasvustoa.</li></ul>''',
  faq_ids=("sammal", "painepesuri"), links=[("/sammal-katolla", "Sammal katolla – pitääkö olla huolissaan?"), ("/katon-pesu", "Katon pesu"), ("/tiilikaton-huolto", "Tiilikaton huolto")], calc=True, priority="0.9")


TARKASTUS = svc_page("/katon-kuntotarkastus", "Katon kuntotarkastus Helsinki – sisältö ja hinta",
  "Katon kuntotarkastus: mitä tarkastuksessa katsotaan, milloin se kannattaa tilata, paljonko se maksaa pääkaupunkiseudulla ja miten raporttia luetaan.",
  "Katon kuntotarkastus", "Kuntotarkastus kertoo, missä kunnossa katto oikeasti on ja paljonko käyttöikää sillä on jäljellä. Se auttaa ajoittamaan huollon tai remontin oikein ja välttämään turhia kuluja.",
  [("/katon-kuntotarkastus", "Katon kuntotarkastus")], f'''
<h2>Mitä tarkastuksessa katsotaan?</h2>
<ul><li><b>Katon yleiskunto:</b> katemateriaalin kuluminen, pinnoitteen kunto, kasvusto ja mahdolliset vauriot.</li>
<li><b>Läpiviennit:</b> piipun, ilmanvaihtoputkien, antennien ja muiden läpivientien tiivistykset.</li>
<li><b>Pellitykset:</b> räystäs-, harja-, otsa- ja piippupellitykset sekä saumat ja kiinnitykset.</li>
<li><b>Kiinnitykset:</b> ruuvit, naulat, tiilien kiinnikkeet ja harjatiivisteet.</li>
<li><b>Aluskate:</b> mahdollisuuksien mukaan ullakolta käsin – repeämät, kosteusjäljet ja tuuletus.</li>
<li><b>Kattoturvatuotteet:</b> lumiesteet, kattotikkaat, kulkusillat ja niiden kiinnitykset.</li>
<li><b>Sadevesijärjestelmä:</b> rännien kaadot, kiinnikkeet ja syöksytorvien toiminta.</li></ul>
<p>Osa yrityksistä käyttää tarkastuksessa dronekuvausta, jolloin koko katto voidaan dokumentoida ilman katolle nousua. Kysy aina, saatko kirjallisen raportin ja kuvat. <a href="/kuntotarkastus-mita-tarkastetaan">Lue tarkempi tarkastuslista</a>.</p>
<h2>Milloin kuntotarkastus kannattaa?</h2>
<ul><li>kun huomaat vuotojälkiä tai kosteutta ullakolla</li><li>ennen asuntokauppaa tai sen jälkeen</li><li>kun harkitset pinnoitusta tai kattoremonttia</li><li>myrskyn tai poikkeuksellisen lumitalven jälkeen</li><li>säännöllisesti noin viiden vuoden välein</li></ul>
<h2>Paljonko kuntotarkastus maksaa?</h2>
<p>Pääkaupunkiseudulla tarkastus maksaa omakotitalolle noin <b>250–500 €</b> laajuudesta riippuen. Esimerkiksi Kotikatto.fi ilmoittaa kuntoarvion hinnaksi 290 € omakotitalolle ja 390 € paritalolle tai isolle kohteelle (<a href="https://www.kotikatto.fi/hinta" rel="noopener nofollow" target="_blank">lähde</a>, tarkistettu {C.fdate(C.COMPANIES["updatedAt"])}). Huomaa, että osa yrityksistä tekee maksuttoman arvion tarjouksen yhteydessä. Se on kuitenkin eri asia kuin puolueeton kuntotarkastus.</p>
<h2>Puolueeton tarkastaja vai urakoitsija?</h2>
<p>Urakoitsijan tekemä arvio on usein maksuton tai edullinen, mutta urakoitsijalla on intressi myydä työtä. Jos edessä on suuri päätös, kuten kattoremontti, voit harkita tarkastusta myös sellaiselta toimijalta, joka ei itse tee korjaustyötä. Molemmissa tapauksissa pyydä kirjallinen raportti, jossa havainnot ja kiireellisyys on eritelty.</p>''',
  faq_ids=("usein", "remontti"), links=[("/kuntotarkastus-mita-tarkastetaan", "Kuntotarkastus – mitä tarkastetaan?"), ("/pinnoitus-vai-kattoremontti", "Pinnoitus vai kattoremontti?")], calc=True, priority="0.9")


PINNOITUS = svc_page("/katon-pinnoitus", "Katon pinnoitus ja maalaus Helsinki – milloin se kannattaa",
  "Katon pinnoitus ja huoltomaalaus: milloin se on järkevä vaihtoehto kattoremontille, mitä työ sisältää ja paljonko se maksaa pääkaupunkiseudulla.",
  "Katon maalaus ja pinnoitus", "Pinnoitus tai huoltomaalaus voi lisätä katolle vuosia käyttöikää, kun rakenne on vielä kunnossa. Kerromme, milloin se on hyvä sijoitus ja milloin rahat kannattaa käyttää kattoremonttiin.",
  [("/katon-pinnoitus", "Katon pinnoitus")], f'''
<h2>Maalaus vai pinnoitus?</h2>
<p>Termejä käytetään osin päällekkäin. <b>Huoltomaalaus</b> tarkoittaa yleensä peltikaton tai betonitiilikaton maalaamista kattomaalilla, kun alkuperäinen pinta on kulunut. <b>Pinnoitus</b> voi tarkoittaa maalausta, mutta myös esimerkiksi betonitiilikaton impregnointia, jossa pintaan imeytetään vettä ja likaa hylkivä aine. Molemmissa esikäsittely eli pesu, kasvuston poisto ja ruosteenpoisto on työn tärkein vaihe.</p>
<h2>Milloin pinnoitus on järkevä?</h2>
<ul><li>peltikaton maalipinta on haalistunut, liituuntunut tai siinä on pistemäistä pintaruostetta</li>
<li>betonitiilikaton pinta on huokoistunut ja sammaloituu nopeasti</li>
<li>katto ei vuoda, ja aluskate, ruoteet ja kiinnitykset ovat kunnossa</li>
<li>katteella on vielä teknistä käyttöikää jäljellä</li></ul>
<h2>Milloin kattoremontti on parempi?</h2>
<ul><li>katto vuotaa useasta kohdasta tai aluskate on haurastunut</li>
<li>pellissä on läpiruostumista tai tiilissä laajaa rapautumista</li>
<li>huopakaton pinta ja saumat ovat laajasti haljenneet</li>
<li>katteen tavanomainen käyttöikä on lopuillaan</li></ul>
<p>Pinnoitus ei korjaa rakenteellisia vikoja. Jos vuotoja on, kuntotarkastus kannattaa tehdä ennen päätöstä. <a href="/pinnoitus-vai-kattoremontti">Lue vertailu: pinnoitus vai kattoremontti</a>.</p>
<h2>Paljonko pinnoitus maksaa?</h2>
<p>Julkaistujen hinnastojen perusteella pinnoitus ja maalaus maksavat pääkaupunkiseudulla noin <b>20–30 €/m²</b>. Esimerkiksi Kotikatto.fi ilmoittaa pinnoitukselle (pesu ja käsittely) 29 €/m² sekä maalaukselle 22 €/m² peltikatolle ja 28 €/m² tiilikatolle, minimiveloitus 2 200 € (<a href="https://www.kotikatto.fi/hinta" rel="noopener nofollow" target="_blank">lähde</a>, tarkistettu {C.fdate(C.COMPANIES["updatedAt"])}). 120 m² katolle tämä tarkoittaa karkeasti 2 600–3 500 € ennen kotitalousvähennystä.</p>
<h2>Sää ja ajoitus</h2>
<p>Kattomaalaus vaatii kuivan sään ja riittävän lämmön myös öisin. Maalivalmistajat ja K-Raudan ammattilaisohje mainitsevat esimerkiksi yli viiden asteen lämpötilan läpi vuorokauden ja alle 80 prosentin suhteellisen kosteuden. Siksi sesonki on Etelä-Suomessa tyypillisesti touko–elokuu. Varaa työ ajoissa, sillä sesonki on lyhyt.</p>''',
  faq_ids=("pinnoitus", "remontti"), links=[("/pinnoitus-vai-kattoremontti", "Pinnoitus vai kattoremontti?"), ("/peltikaton-huolto", "Peltikaton huolto"), ("/tiilikaton-huolto", "Tiilikaton huolto")], calc=True, priority="0.8")


RANNIT = svc_page("/rannien-puhdistus", "Rännien puhdistus Helsinki – hinta ja ohjeet",
  "Rännien puhdistus: miksi sadevesijärjestelmä kannattaa puhdistaa, kuinka usein, mitä työ sisältää ja paljonko se maksaa Helsingissä ja pääkaupunkiseudulla.",
  "Rännien puhdistus", "Tukkeutunut ränni on yksi yleisimmistä ja helpoimmin ehkäistävistä katto-ongelmista. Toimiva sadevesijärjestelmä suojaa julkisivua, sokkelia ja perustuksia.",
  [("/rannien-puhdistus", "Rännien puhdistus")], f'''
<h2>Mitä rännien puhdistus sisältää?</h2>
<ul><li><b>Sadevesijärjestelmän puhdistus:</b> räystäskouruista poistetaan lehdet, neulaset, sammal ja kattopinnalta valunut hiekka.</li>
<li><b>Roskien poisto:</b> roskat kerätään ja viedään pois, eikä niitä huuhdella syöksytorviin.</li>
<li><b>Syöksytorvien tarkistus:</b> vedenkulku testataan ja tukokset avataan. Samalla tarkistetaan, ohjautuuko vesi sadevesikaivoon tai kauas sokkelista.</li>
<li><b>Kiinnikkeet ja kaadot:</b> löystyneet kiinnikkeet ja painuneet kourut havaitaan. Seisova vesi kertoo väärästä kaadosta.</li></ul>
<h2>Kuinka usein rännit puhdistetaan?</h2>
<p>Yleensä 1–2 kertaa vuodessa: syksyllä lehtien pudottua ja tarvittaessa keväällä. Jos tontilla on paljon puita, erityisesti mäntyjä tai koivuja, puhdistusta voidaan tarvita useammin. <a href="/rannien-puhdistus-kuinka-usein">Lue lisää ajoituksesta</a>.</p>
<h2>Paljonko rännien puhdistus maksaa?</h2>
<p>Pääkaupunkiseudulla rännien puhdistus maksaa julkaistujen hinnastojen perusteella noin <b>150–400 €</b>:</p>
<ul><li>Kotikatto.fi: 270 € (katto 0–100 m²), 320 € (100–200 m²), 370 € (yli 200 m²) (<a href="https://www.kotikatto.fi/hinta" rel="noopener nofollow" target="_blank">lähde</a>)</li>
<li>Ulkopesu: alkaen 149 € kattopesun lisänä (<a href="https://www.ulkopesu.fi/palvelut/kattopesu" rel="noopener nofollow" target="_blank">lähde</a>)</li></ul>
<p>Hinnat tarkistettu {C.fdate(C.COMPANIES["updatedAt"])}. Puhdistus on usein edullisinta yhdistää kattopesuun tai syyshuoltoon.</p>
<h2>Voiko rännit puhdistaa itse?</h2>
<p>Yksikerroksisen talon rännit voi puhdistaa itse tukevilta tikkailta, kun tikkaat on varmistettu liukumista vastaan ja työtä ei tehdä yksin. Älä kurottele, vaan siirrä tikkaita. Kaksikerroksisen talon ja jyrkän katon kohdalla ammattilainen on turvallisempi valinta.</p>''',
  faq_ids=("rannit_hinta", "usein"), links=[("/rannien-puhdistus-kuinka-usein", "Rännien puhdistus – kuinka usein?"), ("/syksyn-katon-tarkistuslista", "Syksyn tarkistuslista")], calc=True, priority="0.8")


# =====================================================================
# KATTOTYYPIT
# =====================================================================
KATTOTYYPIT = dict(slug="/kattotyypit", title="Katon huolto kattotyypeittäin – pelti, tiili ja huopa",
  desc="Katon huolto kattotyypeittäin: peltikaton, tiilikaton ja huopakaton tyypilliset ongelmat, huoltotoimet ja tarkistettavat kohdat.",
  h1="Katon huolto kattotyypeittäin", lead="Pelti-, tiili- ja huopakatto vanhenevat eri tavoin. Valitse kattotyyppisi ja katso, mihin huollossa kannattaa kiinnittää huomiota.",
  crumbs=[("/kattotyypit", "Kattotyypit")], priority="0.8",
  body=sec(C.roof_types()) + sec(head("Vertailu", "Kattotyypit lyhyesti", "", "kt-h") + '''<div class="table-wrap"><table class="stack"><thead><tr><th scope="col">Kattotyyppi</th><th scope="col">Yleisin huoltotarve</th><th scope="col">Pesu</th><th scope="col">Pinnoitus / maalaus</th></tr></thead><tbody>
<tr><th scope="row"><a href="/peltikaton-huolto">Peltikatto</a></th><td data-label="Yleisin huoltotarve">Maalipinnan kuluminen, ruuvien tiivisteet, läpiviennit</td><td data-label="Pesu">Matala paine tai vesi</td><td data-label="Pinnoitus / maalaus">Huoltomaalaus pinnan kuluttua</td></tr>
<tr><th scope="row"><a href="/tiilikaton-huolto">Tiilikatto</a></th><td data-label="Yleisin huoltotarve">Sammal ja jäkälä, rikkinäiset tiilet, harjat</td><td data-label="Pesu">Mekaaninen poisto ja pesu</td><td data-label="Pinnoitus / maalaus">Betonitiilen pinnoitus tai maalaus</td></tr>
<tr><th scope="row"><a href="/huopakaton-huolto">Huopakatto</a></th><td data-label="Yleisin huoltotarve">Saumat, halkeamat, pintasirote, vedenpoisto</td><td data-label="Pesu">Harjaus ja matala paine</td><td data-label="Pinnoitus / maalaus">Huopakattomaali tai uusi kermi</td></tr>
</tbody></table></div>
<p class="mt2">Etkö tiedä, mikä kattosi on? Kattotyyppi näkyy usein rakennuslupapiirustuksista tai talon myyntiasiakirjoista. Myös kuva katosta riittää useimmiten yritykselle tunnistukseen.</p>''', white=True, label="kt-h") + C.band())


def roof_page(slug, name, desc, lead, body, faq_ids, links):
    return svc_page(slug, f"{name}n huolto – ohjeet, ongelmat ja hinnat",
      desc, f"{name}n huolto", lead, [("/kattotyypit", "Kattotyypit"), (slug, f"{name}n huolto")], body, faq_ids=faq_ids, links=links, article="2026-10-05", priority="0.8")


PELTI = roof_page("/peltikaton-huolto", "Peltikato",
  "Peltikaton huolto: ruoste, maalipinnan kuluminen, ruuvit ja kiinnikkeet, läpiviennit, pesu ja huoltomaalaus. Käytännön ohjeet ja suuntaa-antavat hinnat.",
  "Peltikatto on Suomen yleisin kattotyyppi. Se on kestävä ja vähähuoltoinen, mutta maalipinta, kiinnitykset ja läpiviennit tarvitsevat säännöllistä tarkistusta.", f'''
<h2>Peltikaton yleisimmät ongelmat</h2>
<h3>Ruoste</h3><p>Ruoste alkaa yleensä kohdista, joissa maalipinta on vaurioitunut: leikkausreunoista, ruuvien ympäriltä, kolhuista ja paikoista, joihin vesi tai roskat jäävät seisomaan. Pistemäinen pintaruoste on merkki huoltomaalauksen tarpeesta. Läpiruostunut pelti vaatii korjauksen tai uusimisen.</p>
<h3>Maalipinnan kuluminen</h3><p>UV-säteily ja sää haalistavat ja liituuttavat maalipintaa. Kun sormeen jää väriä pintaa pyyhkäistessä tai sävy on selvästi vaalentunut, suojaava kerros on ohentunut.</p>
<h3>Kiinnikkeet</h3><p>Profiilipeltikaton ruuvien kumitiivisteet vanhenevat, ja ruuvit voivat löystyä lämpöliikkeen vuoksi. Löysä ruuvi on mahdollinen vuotokohta. Konesaumakatoissa kiinnitykset ovat piilossa, mutta saumat ja pellitykset tarkistetaan.</p>
<h3>Läpiviennit ja pellitykset</h3><p>Piipun, ilmanvaihdon ja antennien läpivientien tiivisteet ovat peltikaton yleisimpiä vuotokohtia. Myös harja-, räystäs- ja otsapellitysten kiinnitykset tarkistetaan.</p>
<h2>Pesu</h2><p>Peltikaton pesuun riittää usein vesi ja harja tai matala paine. Voimakasta painetta ja hankaavia aineita vältetään, jotta maalipinta ei kulu. Pesu tehdään aina ennen huoltomaalausta.</p>
<h2>Huoltomaalaus</h2><p>Kun maalipinta on kulunut mutta pelti on ehjää, huoltomaalaus voi lisätä katolle vuosia käyttöikää. Työ vaatii huolellisen esikäsittelyn: pesun, ruosteenpoiston ja vanhan maalin tartunnan tarkistuksen. Julkaistuissa hinnastoissa peltikaton maalaus maksaa esimerkiksi 22 €/m² (Kotikatto.fi, <a href="https://www.kotikatto.fi/hinta" rel="noopener nofollow" target="_blank">lähde</a>, tarkistettu {C.fdate(C.COMPANIES["updatedAt"])}).</p>
<h2>Lumiesteet ja kattoturva</h2><p>Peltikatolta lumi liukuu helposti, joten lumiesteet ovat tärkeä turvallisuustekijä. Tarkista vuosittain, että lumiesteet, kattotikkaat ja kulkusillat ovat tukevasti kiinni.</p>
<h2>Peltikaton huollon tarkistuslista</h2>
<ul class="checklist"><li>Maalipinnan kunto</li><li>Pintaruoste</li><li>Ruuvit ja tiivisteet</li><li>Läpiviennit</li><li>Pellitykset</li><li>Lumiesteet</li><li>Rännit</li><li>Roskat taitteissa</li></ul>''',
  ("painepesuri", "pinnoitus"), [("/katon-pinnoitus", "Katon maalaus ja pinnoitus"), ("/pinnoitus-vai-kattoremontti", "Pinnoitus vai kattoremontti?")])

TIILI = roof_page("/tiilikaton-huolto", "Tiilikato",
  "Tiilikaton huolto: sammal ja jäkälä, rikkinäiset tiilet, aluskate, harjatiivisteet, pesu ja pinnoitus. Ohjeet betoni- ja savitiilikatoille.",
  "Tiilikatto on pitkäikäinen, mutta sen huokoinen pinta kerää kasvustoa. Säännöllinen pesu, suojakäsittely ja yksittäisten tiilien vaihto pitävät katon kunnossa.", '''
<h2>Betonitiili vai savitiili?</h2><p>Suomessa yleisin on betonitiilikatto. Betonitiilen pinnoite kuluu ajan myötä, jolloin pinta muuttuu huokoisemmaksi ja kerää kosteutta ja kasvustoa. Savitiili on luonnostaan kestävämpi, mutta sekin voi rapautua pakkasen vaikutuksesta. Huoltotapa valitaan tiilityypin ja valmistajan ohjeiden mukaan.</p>
<h2>Sammal ja jäkälä</h2><p>Tiilikatto on altis sammaleelle ja jäkälälle erityisesti pohjoislappeella ja puiden varjossa. Kasvusto pitää tiilen kosteana, ja jäätyvä vesi voi rapauttaa sitä. <a href="/sammaleen-poisto">Lue sammaleen poistosta</a>.</p>
<h2>Rikkinäiset tiilet</h2><p>Haljennut tai siirtynyt tiili päästää veden aluskatteelle. Yksittäiset tiilet voi vaihtaa, kun samaa mallia on saatavilla. Säilytä siksi mahdolliset varatiilet. Tarkista tiilet erityisesti talven ja myrskyjen jälkeen.</p>
<h2>Aluskate</h2><p>Tiilikatossa aluskate on toinen vedeneristyskerros. Vanhoissa taloissa aluskate voi olla haurastunut, mikä näkyy ullakolla kosteusjälkinä tai valona katteen läpi. Aluskatteen uusiminen tarkoittaa käytännössä katteen purkamista, joten sen kunto ratkaisee usein, kannattaako pinnoittaa vai remontoida.</p>
<h2>Harjatiivisteet ja -kiinnitykset</h2><p>Harjatiilien tiivisteet ja kiinnitykset tarkistetaan, koska harja on alttiina tuulelle. Irronneet harjatiilet ja vanhentuneet tiivisteet ovat tavallisia korjauskohteita.</p>
<h2>Pesu ja pinnoitus</h2><p>Betonitiilikatto pestään mekaanisen kasvustonpoiston jälkeen sopivalla paineella ylhäältä alaspäin, jotta vettä ei pääse tiilien alle. Pesun jälkeen tehdään suojakäsittely tai pinnoitus, joka hidastaa uudelleenkasvua. Pinnoitus kannattaa, kun tiilet ovat ehjiä ja aluskate kunnossa.</p>
<h2>Tiilikaton huollon tarkistuslista</h2>
<ul class="checklist"><li>Sammal ja jäkälä</li><li>Rikkinäiset tiilet</li><li>Siirtyneet tiilet</li><li>Harjatiivisteet</li><li>Läpiviennit</li><li>Aluskate ullakolta</li><li>Lumiesteet</li><li>Rännit</li></ul>''',
  ("sammal", "pinnoitus"), [("/sammaleen-poisto", "Sammaleen poisto"), ("/sammal-katolla", "Sammal katolla – pitääkö olla huolissaan?")])

HUOPA = roof_page("/huopakaton-huolto", "Huopakato",
  "Huopakaton huolto: pintasirote, saumat, läpiviennit, halkeamat, kasvusto ja vedenpoisto. Ohjeet huopakaton pesuun ja kunnon arviointiin.",
  "Huopakatto on yleinen loivissa katoissa ja pientaloissa. Se vaatii hellävaraista käsittelyä ja säännöllistä saumojen ja vedenpoiston tarkistusta.", '''
<h2>Pintasirote</h2><p>Huopakatteen pinnalla oleva kivirouhe eli pintasirote suojaa bitumia UV-säteilyltä. Kun sirotetta irtoaa ja sitä kertyy ränneihin, katteen pinta alkaa vanhentua nopeammin. Siksi huopakattoa ei pestä korkeapaineella.</p>
<h2>Saumat ja halkeamat</h2><p>Saumojen auki repeäminen ja halkeamat ovat huopakaton tavallisimpia vuotokohtia. Pienet vauriot voidaan paikata bitumikermillä ja -liimalla. Paikkauksen päälle voi sirotella katon väristä rouhetta. Laaja halkeilu on merkki katteen uusimisen tarpeesta.</p>
<h2>Läpiviennit</h2><p>Läpivientien liitokset tarkistetaan erityisen huolella, koska loivalla katolla vesi viipyy pinnalla pidempään.</p>
<h2>Kasvusto</h2><p>Huopakattoon tarttuu helposti sammalta ja roskia, jotka kuluttavat ja haurastuttavat pintaa. Puhdistus tehdään harjaamalla, pesuaineella ja matalalla paineella. Kasvustoa ei kaavita voimakkaasti.</p>
<h2>Vedenpoisto</h2><p>Loivilla huopakatoilla ja tasakatoilla vedenpoiston toimivuus on ratkaisevaa. Kattokaivojen, räystäskourujen ja syöksytorvien pitää olla auki, eikä katolle saa jäädä lammikoita. Seisova vesi kertoo painumasta tai tukoksesta.</p>
<h2>Käyttöikä</h2><p>Huopakatteen käyttöikä on lyhyempi kuin pelti- tai tiilikatteen. Kun pinta on laajasti haljennut ja sirote kulunut, uusi kermi on usein järkevämpi kuin jatkuva paikkaus. Kuntotarkastus auttaa ajoittamaan uusimisen.</p>
<h2>Huopakaton huollon tarkistuslista</h2>
<ul class="checklist"><li>Pintasirote</li><li>Saumat</li><li>Halkeamat ja kuplat</li><li>Läpiviennit</li><li>Kasvusto</li><li>Kattokaivot</li><li>Lammikoituminen</li><li>Rännit</li></ul>''',
  ("painepesuri", "remontti"), [("/katon-kuntotarkastus", "Katon kuntotarkastus"), ("/rannien-puhdistus", "Rännien puhdistus")])


# =====================================================================
# HINNAT, YRITYKSET
# =====================================================================
HINNAT = dict(slug="/hinnat", title="Kattohuollon hinnat 2026 – katon pesu, sammal, rännit ja tarkastus",
  desc="Kattohuollon hinnat Helsingissä ja pääkaupunkiseudulla: suuntaa-antavat hinnat, yritysten julkaisemat hinnastot rinnakkain ja hintalaskuri.",
  h1="Kattohuollon hinnat Helsingissä", lead="Kokosimme yritysten julkaisemat hinnat ja muutimme ne helposti vertailtaviksi hintahaarukoiksi. Jokaisen hinnan kohdalla näkyy lähde ja tarkistuspäivä.",
  crumbs=[("/hinnat", "Hinnat")], priority="0.9", meta_line=f"Hintatiedot tarkistettu {C.fdate(C.COMPANIES['updatedAt'])}",
  body=sec('<div class="grid g2" style="align-items:start"><div>' + head("Yhteenveto", "Paljonko kattohuolto maksaa Helsingissä?", "", "hp-h") + C.price_table() +
    '</div><div class="card"><h3>Hintaan vaikuttavat</h3>' + C.price_factors() + '</div></div>', label="hp-h") +
    C.calculator() +
    sec(head("Hintavertailu", "Kattohuollon hinnat – mitä eri yritykset veloittavat?", "Vain julkisesti saatavilla olevia hinnastoja. Puuttuvia tietoja ei ole arvioitu.", "cmp2-h") + C.comparison(), white=True, label="cmp2-h") +
    sec(head("Kotitalousvähennys", "Kotitalousvähennys pienentää kustannusta", "", "kv-h") + '<div class="narrow">' + FAQ_ALL["kotitalousvahennys"][1] +
        '<p><b>Esimerkki:</b> katon pesu ja suojakäsittely maksaa 1 000 €, josta työn osuus on 800 €. Vähennys on 800 € × 40 % − 150 € = 170 €, eli kustannukseksi jää noin 830 €. Puolisot voivat hakea vähennystä kumpikin, mutta omavastuu vähennetään molemmilta.</p></div>', label="kv-h") +
    sec(head("Esimerkit", "Esimerkkilaskelmia", "Esimerkit on laskettu julkaistujen hintojen keskitasolla. Ne eivät ole tarjouksia.", "ex-h") + '''<div class="grid g3">
<div class="card"><h3>Pieni peltikatto, 70 m²</h3><p>Pesu: noin 490–700 €<br>Rännien puhdistus: noin 150–300 €</p><p class="kpi mb0">≈ 650–1 000 €</p></div>
<div class="card"><h3>Tiilikatto, 130 m², paljon sammalta</h3><p>Sammaleen poisto ja pesu: noin 1 200–2 000 €<br>Suojakäsittely: usein mukana</p><p class="kpi mb0">≈ 1 200–2 000 €</p></div>
<div class="card"><h3>Peltikaton huoltomaalaus, 150 m²</h3><p>Pesu, esikäsittely ja maalaus: noin 22–30 €/m²</p><p class="kpi mb0">≈ 3 300–4 500 €</p></div></div>''', white=True, label="ex-h") +
    C.band("Sopiiko hinta-arvio kohteeseesi?", "Tarkka hinta selviää vain kohteen perusteella. Pyydä 2–3 tarjousta ja vertaa niiden sisältöä."),
  faq=faq_by_ids("pesu_hinta", "rannit_hinta", "tarjoukset", "kysy"))

YRITYKSET = dict(slug="/yritykset", title="Kattohuoltoyritykset Helsingissä – vertailu ja hinnat",
  desc="Kattohuoltoyritykset Helsingissä ja pääkaupunkiseudulla: palvelut, julkaistut hinnat ja lähteet. Vertaile yrityksiä ja pyydä tarjous.",
  h1="Kattohuoltoyritykset Helsingissä", lead="Helsingissä toimii useita kattohuoltoon, kattopesuihin, kattokorjauksiin ja kattoremontteihin erikoistuneita yrityksiä. Alla oleva vertailu auttaa hahmottamaan, millaisia palveluita markkinoilta löytyy.",
  crumbs=[("/yritykset", "Palveluntarjoajat")], priority="0.9", nav="/yritykset",
  meta_line=f"Tiedot tarkistettu {C.fdate(C.COMPANIES['updatedAt'])} · Tiedot perustuvat yritysten omiin julkaisuihin",
  body=sec(C.company_filters() + '<div class="grid g2">' + C.company_cards() + '</div>' +
    '''<div class="note"><p><b>Näin yritykset on valittu:</b> vertailussa on yrityksiä, jotka ilmoittavat palvelevansa Helsingissä tai pääkaupunkiseudulla ja joiden palvelut voi todentaa yrityksen omasta lähteestä. Palvelut ja hinnat on poimittu yrityksen omilta sivuilta tai yrityksen itse julkaisemista kuvauksista. Arvosteluja ei näytetä, koska niitä ei ole koottu luotettavasta ja riippumattomasta lähteestä. Lista ei ole kattava. Jos edustat yritystä ja haluat korjata tietoja tai tulla mukaan vertailuun, <a href="/yhteystiedot">ota yhteyttä</a>.</p></div>''') +
    sec(head("Hinnat rinnakkain", "Julkaistut hinnat rinnakkain", "", "cmp3-h") + C.comparison(), white=True, label="cmp3-h") +
    sec(head("Ennen kuin valitset", "Mitä tarkistaa yrityksestä?", "", "chk-h") + '''<div class="grid g3">
<div class="card"><h3>Ennakkoperintärekisteri</h3><p class="mb0">Tarkista Y-tunnus ja rekisteröinti <a href="https://www.ytj.fi/" rel="noopener" target="_blank">YTJ:stä</a>. Ilman rekisteröintiä et saa kotitalousvähennystä.</p></div>
<div class="card"><h3>Vastuuvakuutus</h3><p class="mb0">Kysy, onko yrityksellä vastuuvakuutus, joka kattaa mahdolliset vahingot katolle ja pihapiirille.</p></div>
<div class="card"><h3>Kirjallinen tarjous ja takuu</h3><p class="mb0">Pyydä tarjous kirjallisena, ja tarkista sisältö, aikataulu, maksuehdot ja takuu.</p></div></div>''', label="chk-h") + C.band(),
  faq=faq_by_ids("tarjoukset", "kysy"))


# =====================================================================
# ALUESIVUT
# =====================================================================
def companies_serving(city):
    out = []
    for c in C.COMPANIES["companies"]:
        if city in c["serviceArea"] or city in c["city"] or (city == "Helsinki" and "Helsingin seutu" in c["serviceArea"]):
            out.append(f'<li><b>{C.esc(c["name"])}</b> ({C.esc(c["city"])}) – {", ".join(C.esc(s) for s in c["services"][:3]).lower()}</li>')
    return "<ul>" + "".join(out) + "</ul>" if out else "<p>Vertailussa ei vielä ole yrityksiä, jotka mainitsevat alueen erikseen. Useimmat pääkaupunkiseudun yritykset palvelevat kuitenkin koko seutua.</p>"


def area_page(slug, city, desc, lead, local, prio="0.7"):
    other = [(u, t) for u, t in [("/kattohuolto-helsinki", "Kattohuolto Helsinki"), ("/kattohuolto-espoo", "Kattohuolto Espoo"),
             ("/kattohuolto-vantaa", "Kattohuolto Vantaa"), ("/kattohuolto-kauniainen", "Kattohuolto Kauniainen")] if u != slug]
    body = local + f'''
<h2>Kattohuollon hinnat: {city}</h2>
<p>Pääkaupunkiseudun yritykset hinnoittelevat yleensä samalla tavalla koko seudulla. Suuntaa-antavat hinnat:</p>{C.price_table()}
<h2>Vertailussa olevat yritykset, jotka ilmoittavat palvelevansa: {city}</h2>
<p>Alla ovat yritykset, joiden oma kuvaus mainitsee alueen tai jotka toimivat alueella. Tiedot on poimittu yritysten omista lähteistä.</p>
{companies_serving(city)}
<p><a href="/yritykset">Katso kaikki yritykset ja julkaistut hinnat</a></p>
<h2>Näin pääset alkuun</h2>
<p>Selvitä katon tyyppi ja pinta-ala, ota muutama kuva maasta käsin ja pyydä 2–3 tarjousta. <a href="/tarjousten-vertailu">Tarjousten vertailun tarkistuslista</a> auttaa vertaamaan tarjouksia oikein.</p>'''
    return svc_page(slug, f"Kattohuolto {city} – hinnat, yritykset ja paikalliset vinkit",
        desc, f"Kattohuolto {city}", lead, [("/kattohuolto", "Kattohuolto"), (slug, city)], body,
        faq_ids=("usein", "kotitalousvahennys"), links=other, priority=prio)


HKI = area_page("/kattohuolto-helsinki", "Helsinki",
  "Kattohuolto Helsingissä: miten rannikkoilmasto, lumi, jää ja vanha rakennuskanta vaikuttavat katon huoltoon. Hinnat ja alueella toimivat yritykset.",
  "Helsingin sää ja rakennuskanta asettavat katoille omat vaatimuksensa. Tällä sivulla kerromme, mihin helsinkiläisen kannattaa kiinnittää huomiota.", '''
<h2>Helsingin sääolosuhteet ja katto</h2>
<p>Helsingissä ilmasto on rannikon vuoksi kosteampi ja talvet leudompia kuin sisämaassa. Leutous ei kuitenkaan tarkoita kevyempää rasitusta katolle. Lämpötila vaihtelee talvella usein nollan molemmin puolin, jolloin lumi sulaa päivällä ja jäätyy yöllä. Tämä kerää jäätä räystäille ja ränneihin, ja jäätyvä vesi rasittaa tiiviitä liitoksia.</p>
<p><b>Lumi ja jää:</b> runsaslumisina talvina lumikuorma kasaantuu kattolappeiden taitteisiin ja piippujen taakse. Lumiesteiden ja kattoturvatuotteiden on oltava kunnossa, jotta lumen voi pudottaa turvallisesti.</p>
<p><b>Sade ja kosteus:</b> syksyn pitkät sadejaksot paljastavat tukkeutuneet rännit ja heikot läpiviennit. Merellinen, kostea ilma myös pitää katon pinnan kosteana pidempään, mikä edistää levän ja jäkälän kasvua erityisesti varjoisilla lappeilla.</p>
<p><b>Syksyn lehdet ja kevään sulamisvedet:</b> monilla puistomaisilla pientaloalueilla, kuten Oulunkylässä, Pakilassa, Tapanilassa, Kulosaaressa ja Laajasalossa, lehdet ja havut tukkivat rännejä nopeasti. Keväällä sulamisvesien pitää päästä vapaasti syöksytorviin.</p>
<h2>Vanha rakennuskanta</h2>
<p>Helsingissä on paljon sotien jälkeen rakennettuja rintamamiestaloja ja 1960–1980-lukujen pientaloja, joiden katot ovat jo useamman huolto- tai uusimiskierroksen kohteena. Vanhoissa taloissa aluskate voi olla haurastunut tai puuttua kokonaan, ja läpivientien tiivisteet on usein uusittu vaihtelevasti. Ennen pinnoitusta kannattaa siksi tarkastuttaa katon kunto. Suojeltujen tai arvokkaiden rakennusten kohdalla katemateriaalin muutoksista kannattaa kysyä rakennusvalvonnasta.</p>
<h2>Kaupunginosittaiset erot</h2>
<p>Huollon tarve riippuu enemmän tontista kuin osoitteesta: varjoisuus, puusto ja tuulisuus ratkaisevat. Meren läheisillä tuulisilla alueilla, kuten Lauttasaaressa ja Vuosaaressa, kannattaa tarkistaa pellitysten ja harjojen kiinnitykset myrskyjen jälkeen. Metsäisillä pientaloalueilla, kuten Malmilla, Kontulassa ja Herttoniemen pientaloalueilla, sammal ja rännien tukkeutuminen ovat tavallisempia.</p>''', prio="0.9")

ESPOO = area_page("/kattohuolto-espoo", "Espoo",
  "Kattohuolto Espoossa: pientaloalueiden tyypilliset kattotarpeet, suuntaa-antavat hinnat ja Espoossa palvelevat kattohuoltoyritykset.",
  "Espoossa on paljon omakoti- ja rivitaloalueita, joissa katot ovat usein puuston ympäröimiä. Tämä näkyy sammaleen ja rännien huollon tarpeena.", '''
<h2>Mitä espoolaisen kannattaa huomioida?</h2>
<p>Espoon pientaloalueet ovat usein väljiä ja metsäisiä. Puusto suojaa tuulelta, mutta varjostaa kattoja ja pudottaa niille lehtiä ja neulasia. Varjoisilla, pohjoiseen viettävillä lappeilla sammal ja jäkälä kasvavat nopeammin, joten pesu ja suojakäsittely voivat olla tarpeen useammin kuin avoimilla tonteilla.</p>
<p>Rännit kannattaa tarkistaa syksyllä viimeisten lehtien pudottua. Rannikon läheisillä alueilla, kuten Espoonlahden ja Westendin suunnalla, tuulisuus korostaa pellitysten ja kattoturvatuotteiden kiinnitysten merkitystä.</p>
<p>Monet Espoon pientalot on rakennettu 1970–1990-luvuilla, joten niissä alkuperäinen katemateriaali lähestyy elinkaarensa loppua tai on jo uusittu. Jos katto on alkuperäinen, kuntotarkastus kertoo, riittääkö huolto vai onko edessä remontti.</p>''')

VANTAA = area_page("/kattohuolto-vantaa", "Vantaa",
  "Kattohuolto Vantaalla: katon huollon erityispiirteet, suuntaa-antavat hinnat ja Vantaalla palvelevat kattohuoltoyritykset.",
  "Vantaalla on monipuolinen pientalokanta rintamamiestaloista uusiin asuntoalueisiin. Huollon tarve vaihtelee talon iän ja tontin mukaan.", '''
<h2>Mitä vantaalaisen kannattaa huomioida?</h2>
<p>Vantaan vanhemmilla pientaloalueilla, kuten Tikkurilan, Korson, Hakunilan ja Myyrmäen ympäristöissä, on paljon rintamamiestaloja ja 1960–1980-lukujen omakotitaloja. Näissä katoissa aluskatteen kunto ja läpivientien tiivisteet ovat tärkeimpiä tarkistuskohteita. Uudemmilla alueilla, kuten Kivistössä, katot ovat nuoria, ja huolto keskittyy rännien puhdistukseen ja kattoturvatuotteiden tarkistukseen.</p>
<p>Sisämaata kohti talvet voivat olla hieman lumisempia kuin rannikolla, joten lumiesteiden ja kattotikkaiden kunto sekä lumikuorman seuraaminen korostuvat. Avoimilla peltoalueiden reunoilla tuuli rasittaa harjoja ja pellityksiä.</p>''')

KAUNIAINEN = area_page("/kattohuolto-kauniainen", "Kauniainen",
  "Kattohuolto Kauniaisissa: vanhan ja puustoisen pientaloalueen kattohuollon erityispiirteet, hinnat ja alueella palvelevat yritykset.",
  "Kauniainen on pieni ja puistomainen pientalokaupunki, jossa on paljon vanhaa ja arvokasta rakennuskantaa. Se näkyy myös katon huollossa.", '''
<h2>Mitä kauniaislaisen kannattaa huomioida?</h2>
<p>Kauniaisten vehreys tarkoittaa, että monet katot ovat isojen puiden varjossa. Lehdet, neulaset ja varjo lisäävät sammaleen ja jäkälän kasvua sekä rännien tukkeutumista, joten rännien puhdistus kahdesti vuodessa on monelle tontille perusteltu.</p>
<p>Kaupungissa on paljon vanhoja huviloita ja pientaloja, joiden katoissa voi olla perinteisiä materiaaleja, kuten konesaumattua peltiä tai savitiiltä. Niiden huolto vaatii materiaalin tuntemusta: pesussa käytetään varovaisia menetelmiä, ja korjauksissa pyritään säilyttämään alkuperäinen ilme. Jos rakennus on suojeltu tai asemakaavassa on määräyksiä katteesta, tarkista muutoksista ennen työtä Kauniaisten rakennusvalvonnasta.</p>''', prio="0.6")


# =====================================================================
# FAQ, LOMAKE, TIETOA, YHTEYS, JURIDIIKKA
# =====================================================================
FAQ_PAGE = dict(slug="/usein-kysyttya", title="Usein kysyttyä kattohuollosta – vastaukset yleisimpiin kysymyksiin",
  desc="Vastaukset yleisimpiin kattohuollon kysymyksiin: kuinka usein katto huolletaan, paljonko pesu maksaa, painepesuri, sammal, kotitalousvähennys ja tarjoukset.",
  h1="Usein kysyttyä kattohuollosta", lead="Kokosimme vastaukset kysymyksiin, joita kattohuoltoa suunnittelevat useimmin pohtivat.",
  crumbs=[("/usein-kysyttya", "Usein kysyttyä")], priority="0.8",
  faq=[FAQ_ALL[k] for k in FAQ_ORDER], faq_title="Kysymykset ja vastaukset",
  body="")
FAQ_PAGE["body"] = ""  # FAQ-osio lisätään renderöinnissä
FAQ_PAGE["after_faq"] = C.band("Etkö löytänyt vastausta?", "Kysy suoraan yrityksiltä tarjouspyynnön yhteydessä tai lue lisää katto-oppaasta.", ("/tarjouspyynto", "Pyydä tarjouksia"), ("/katto-opas", "Katto-opas"))

TARJOUS = dict(slug="/tarjouspyynto", title="Pyydä tarjouksia kattohuollosta – maksuton tarjouspyyntö",
  desc="Pyydä tarjouksia katon pesusta, sammaleen poistosta, rännien puhdistuksesta, kuntotarkastuksesta tai pinnoituksesta Helsingissä ja pääkaupunkiseudulla.",
  h1="Pyydä tarjouksia kattohuollosta", lead="Täytä tiedot kerran. Välitämme pyyntösi kohteeseesi sopiville kattohuoltoyrityksille, ja sinä vertailet tarjoukset rauhassa.",
  crumbs=[("/tarjouspyynto", "Tarjouspyyntö")], priority="0.7", nav="",
  body=C.quote_form("Tarjouspyyntö", "h2"))

TIETOA = svc_page("/tietoa-sivustosta", "Tietoa sivustosta – miten HelsinkiKattoHuolto.fi toimii",
  "Kuka ylläpitää HelsinkiKattoHuolto.fi:tä, miten yritykset valitaan vertailuun, miten hintatiedot kerätään ja miten yhteistyöt ilmoitetaan.",
  "Tietoa sivustosta", "Läpinäkyvyys on meille tärkeää. Tällä sivulla kerromme, miten sivusto toimii ja miten tiedot kerätään.",
  [("/tietoa-sivustosta", "Tietoa sivustosta")], f'''
<h2>Mikä HelsinkiKattoHuolto.fi on?</h2>
<p>HelsinkiKattoHuolto.fi on kattohuollon tietopalvelu Helsingin ja pääkaupunkiseudun kiinteistönomistajille. Tavoitteemme on auttaa ymmärtämään katon huoltoa, kustannuksia ja vaihtoehtoja ennen kuin tilaat työn.</p>
<p><b>Emme tee kattotöitä itse.</b> Emme ole kattohuoltoyritys, emmekä myy kattopalveluita. Kattotyöt tekevät itsenäiset yritykset, joiden kanssa teet sopimuksen suoraan.</p>
<h2>Kuka sivustoa ylläpitää?</h2>
<p>Sivustoa ylläpitää HelsinkiKattoHuolto.fi:n toimitus. Voit ottaa yhteyttä <a href="/yhteystiedot">yhteystiedot-sivun</a> kautta.</p>
<h2>Miten yritykset valitaan vertailuun?</h2>
<ul><li>Yritys ilmoittaa palvelevansa Helsingissä tai pääkaupunkiseudulla.</li>
<li>Yrityksen palvelut voidaan todentaa yrityksen omasta lähteestä, kuten verkkosivuilta tai yrityksen itse julkaisemasta kuvauksesta.</li>
<li>Emme lisää palveluita, hintoja, arvosteluja, takuita tai sertifikaatteja, joita ei voi todentaa.</li>
<li>Vertailussa ei ole maksettuja sijoituksia. Järjestys perustuu julkaistujen hintatietojen määrään.</li></ul>
<p>Lista ei ole kattava. Yritykset voivat pyytää tietojensa korjaamista tai lisäämistä.</p>
<h2>Miten hintatiedot kerätään?</h2>
<p>Hinnat poimitaan yritysten julkisista hinnastoista. Jokaisen hinnan yhteydessä näkyy lähde ja tarkistuspäivä. Yleiset hintahaarukat on muodostettu näiden julkaistujen hintojen perusteella. Kaikki hinnat ovat suuntaa-antavia, eivätkä ne ole tarjouksia. Todellinen hinta määräytyy kohteen, katon koon, kunnon ja työn laajuuden perusteella.</p>
<p><b>Hinnat on viimeksi tarkistettu {C.fdate(C.COMPANIES["updatedAt"])}.</b> Tarkistamme hinnat säännöllisesti, ja muutokset päivitetään vertailuun.</p>
<h2>Miten sivusto rahoitetaan ja miten yhteistyöt ilmoitetaan?</h2>
<p>Saatamme saada yhteistyökumppaneilta korvauksen tarjouspyyntöjen välittämisestä. Tämä ei vaikuta siihen, miten hintatiedot esitetään. Mahdolliset kaupalliset yhteistyöt merkitään selvästi sivuilla, joilla ne näkyvät, eikä yhteistyö vaikuta yritysten järjestykseen tai hintatietojen esittämiseen.</p>
<h2>Sisällön periaatteet</h2>
<ul><li>Kerromme ensisijaisesti tietoa, emme myy.</li><li>Merkitsemme arviot ja hinnat suuntaa-antaviksi.</li><li>Viittaamme lähteisiin, kuten yritysten hinnastoihin ja Verohallinnon ohjeisiin.</li><li>Korjaamme virheet nopeasti. Ilmoita virheestä <a href="/yhteystiedot">yhteystiedot-sivun</a> kautta.</li></ul>''',
  links=[("/yritykset", "Yritysvertailu"), ("/hinnat", "Hinnat"), ("/tietosuojaseloste", "Tietosuojaseloste")], priority="0.5")

YHTEYS = dict(slug="/yhteystiedot", title="Yhteystiedot – HelsinkiKattoHuolto.fi",
  desc="Ota yhteyttä HelsinkiKattoHuolto.fi:n toimitukseen: palaute, tietojen korjaukset ja yritysten tietopyynnöt.",
  h1="Yhteystiedot", lead="Palaute, korjaukset ja yritysten tietopyynnöt. Huomaathan, ettemme tee kattotöitä itse.",
  crumbs=[("/yhteystiedot", "Yhteystiedot")], priority="0.4",
  body=sec('''<div class="grid g3">
<div class="card"><div class="icon">''' + C.icon("drop") + '''</div><h3>Tarvitsetko kattohuoltoa?</h3><p>Täytä tarjouspyyntö, niin välitämme sen kohteeseesi sopiville yrityksille.</p><a class="btn btn-primary" href="/tarjouspyynto">Pyydä tarjouksia</a></div>
<div class="card"><div class="icon">''' + C.icon("book") + '''</div><h3>Palaute ja korjaukset</h3><p>Huomasitko virheen tai vanhentuneen hinnan? Kerro meille, niin tarkistamme tiedon.</p><p class="mb0"><a href="mailto:info@helsinkikattohuolto.fi" data-email>info@helsinkikattohuolto.fi</a></p></div>
<div class="card"><div class="icon">''' + C.icon("scale") + '''</div><h3>Yrityksille</h3><p>Haluatko korjata yrityksesi tiedot tai tulla mukaan vertailuun? Lähetä linkki julkiseen hinnastoon tai palvelukuvaukseen.</p><p class="mb0"><a href="mailto:info@helsinkikattohuolto.fi?subject=Yrityksen%20tiedot">Lähetä tiedot</a></p></div></div>'''))

TIETOSUOJA = svc_page("/tietosuojaseloste", "Tietosuojaseloste – HelsinkiKattoHuolto.fi",
  "HelsinkiKattoHuolto.fi:n tietosuojaseloste: mitä henkilötietoja keräämme tarjouspyynnöistä, miksi, kenelle niitä luovutetaan ja mitkä ovat oikeutesi.",
  "Tietosuojaseloste", "Tässä selosteessa kerromme, miten käsittelemme henkilötietoja EU:n yleisen tietosuoja-asetuksen (GDPR) mukaisesti.",
  [("/tietosuojaseloste", "Tietosuojaseloste")], '''
<h2>1. Rekisterinpitäjä</h2><p>HelsinkiKattoHuolto.fi<br>Sähköposti: <a href="mailto:info@helsinkikattohuolto.fi">info@helsinkikattohuolto.fi</a></p>
<h2>2. Käsiteltävät henkilötiedot</h2><p>Tarjouspyyntölomakkeella keräämme nimen, puhelinnumeron, sähköpostiosoitteen, postinumeron, katon tiedot (kattotyyppi, arvioitu koko, tarvittava palvelu), lisätiedot ja lähettämäsi kuvat. Yhteydenotoista tallennamme viestin sisällön ja yhteystiedot.</p>
<h2>3. Käsittelyn tarkoitus ja oikeusperuste</h2><p>Käsittelemme tietoja tarjouspyyntösi välittämiseen ja siihen liittyvään yhteydenpitoon. Oikeusperusteena on suostumuksesi, jonka annat lomakkeella. Analytiikkaa käytämme vain, jos hyväksyt sen evästeasetuksissa.</p>
<h2>4. Tietojen luovutus</h2><p>Välitämme tarjouspyyntösi tiedot niille kattohuoltoyrityksille, jotka voivat tehdä tarjouksen kohteeseesi. Yritykset käsittelevät tietoja omina rekisterinpitäjinään. Lisäksi tietoja voivat käsitellä palveluntarjoajamme, kuten lomake-, sähköposti- ja palvelinpalvelut, sopimustemme mukaisesti. Emme myy henkilötietoja.</p>
<h2>5. Siirrot EU:n ulkopuolelle</h2><p>Jos käyttämämme palveluntarjoaja käsittelee tietoja EU:n tai ETA:n ulkopuolella, huolehdimme siirtojen lainmukaisuudesta esimerkiksi Euroopan komission vakiosopimuslausekkeilla.</p>
<h2>6. Säilytysaika</h2><p>Säilytämme tarjouspyynnön tietoja enintään 12 kuukautta pyynnön lähettämisestä, ellei pidempi säilytys ole lain vuoksi tarpeen.</p>
<h2>7. Oikeutesi</h2><p>Sinulla on oikeus tarkastaa tietosi, pyytää niiden oikaisemista tai poistamista, rajoittaa käsittelyä, vastustaa käsittelyä sekä peruuttaa suostumuksesi milloin tahansa. Pyynnöt voit lähettää yllä olevaan sähköpostiosoitteeseen. Sinulla on myös oikeus tehdä valitus tietosuojavaltuutetun toimistolle (<a href="https://tietosuoja.fi" rel="noopener" target="_blank">tietosuoja.fi</a>).</p>
<h2>8. Tietoturva</h2><p>Tiedot siirretään salattuna (HTTPS), ja pääsy niihin on rajattu henkilöihin, jotka tarvitsevat niitä tarjouspyyntöjen käsittelyyn.</p>
<p class="muted">Päivitetty 5.10.2026.</p>''', priority="0.2")

EVASTEET = svc_page("/evastekaytannot", "Evästekäytännöt – HelsinkiKattoHuolto.fi",
  "HelsinkiKattoHuolto.fi:n evästekäytännöt: mitä evästeitä käytämme, mihin ja miten voit muuttaa evästeasetuksiasi.",
  "Evästekäytännöt", "Käytämme evästeitä ja vastaavia tekniikoita vain siinä laajuudessa kuin on tarpeen. Analytiikka otetaan käyttöön vain suostumuksellasi.",
  [("/evastekaytannot", "Evästekäytännöt")], '''
<h2>Välttämättömät</h2><p>Tallennamme selaimesi paikalliseen muistiin (localStorage) evästevalintasi, jotta emme kysy sitä joka käynnillä. Tämä ei sisällä henkilötietoja.</p>
<h2>Analytiikka (vain suostumuksella)</h2><p>Jos hyväksyt analytiikan, käytämme Google Analytics 4 -palvelua ymmärtääksemme, mitä sisältöjä luetaan ja toimiiko hintalaskuri. Google Analytics asettaa evästeitä, kuten _ga ja _ga_*, joiden säilytysaika on enintään 2 vuotta. IP-osoitteet anonymisoidaan. Seuraamme esimerkiksi seuraavia tapahtumia: tarjouspyynnön lähetys, hintalaskurin käyttö, yritysten verkkosivulinkkien klikkaukset ja artikkelien lukeminen.</p>
<h2>Markkinointievästeet</h2><p>Emme käytä markkinointi- tai uudelleenmarkkinointievästeitä.</p>
<h2>Miten muutan valintaani?</h2><p>Voit muuttaa valintaa milloin tahansa sivun alareunan <b>Evästeasetukset</b>-linkistä tai tyhjentämällä selaimesi sivustotiedot.</p>
<p class="muted">Päivitetty 5.10.2026.</p>''', priority="0.2")

KIITOS = dict(slug="/kiitos", title="Kiitos tarjouspyynnöstä – HelsinkiKattoHuolto.fi", desc="Tarjouspyyntösi on vastaanotettu.",
  h1="Kiitos – tarjouspyyntösi on vastaanotettu", lead="Käymme pyynnön läpi ja välitämme sen kohteeseesi sopiville yrityksille. Yritykset ottavat yhteyttä suoraan sinuun.",
  noindex=True, crumbs=None, nav="",
  body=sec('''<div class="grid g3"><a class="card" href="/tarjousten-vertailu"><h3>Vertaile tarjoukset oikein</h3><p class="mb0">Tarkistuslista tarjousten vertailuun.</p></a>
<a class="card" href="/hinnat"><h3>Tarkista hintataso</h3><p class="mb0">Julkaistut hinnat ja hintalaskuri.</p></a>
<a class="card" href="/usein-kysyttya#kotitalousvahennys"><h3>Kotitalousvähennys</h3><p class="mb0">Näin haet vähennystä työn osuudesta.</p></a></div>'''))

NOT_FOUND = dict(slug="/404", title="Sivua ei löytynyt – HelsinkiKattoHuolto.fi", desc="Etsimääsi sivua ei löytynyt.",
  h1="Sivua ei löytynyt", lead="Sivu on voinut siirtyä tai osoitteessa on kirjoitusvirhe. Tästä pääset alkuun:", noindex=True, nav="",
  body=sec('<ul class="pills"><li><a href="/">Etusivu</a></li><li><a href="/hinnat">Hinnat</a></li><li><a href="/yritykset">Yritykset</a></li><li><a href="/katto-opas">Katto-opas</a></li><li><a href="/usein-kysyttya">Usein kysyttyä</a></li></ul>'))

PAGES = [HOME, KATTOHUOLTO, HKI, ESPOO, VANTAA, KAUNIAINEN, KATON_PESU, KATON_PESU_HKI, SAMMAL, TARKASTUS, PINNOITUS, RANNIT,
         KATTOTYYPIT, PELTI, TIILI, HUOPA, HINNAT, YRITYKSET, FAQ_PAGE, TARJOUS, TIETOA, YHTEYS, TIETOSUOJA, EVASTEET, KIITOS, NOT_FOUND]
