"""Katto-opas: artikkelit ja oppaan etusivu."""
import components as C
from content_faq import faq_by_ids

D = lambda: C.fdate(C.COMPANIES["updatedAt"])


def art(slug, title, desc, h1, lead, body, links, faq_ids=(), published="2026-10-05", read_min=5):
    return dict(slug=slug, title=title, desc=desc, h1=h1, lead=lead, crumbs=[("/katto-opas", "Katto-opas"), (slug, h1)],
                body=C.prose_page(body, links, article_id=slug.strip("/")) + C.band(), article={"published": published},
                faq=faq_by_ids(*faq_ids) if faq_ids else None, priority="0.7", nav="/katto-opas",
                meta_line=f"HelsinkiKattoHuolto.fi toimitus · Päivitetty {D()} · Lukuaika noin {read_min} min")


A1 = art("/katon-huolto-opas", "Katon huolto – täydellinen opas suomalaiselle omakotitalolle",
  "Kattava opas omakotitalon katon huoltoon: vuosirytmi, tarkistettavat kohdat, kattotyyppien erot, kustannukset ja milloin kannattaa kutsua ammattilainen.",
  "Katon huolto – täydellinen opas suomalaiselle omakotitalolle",
  "Katto on talon tärkein suoja säätä vastaan. Hyvin hoidettu katto kestää vuosikymmeniä, hoitamaton voi alkaa vuotaa paljon ennen aikojaan. Tämä opas kokoaa olennaisen yhteen.", f'''
<nav class="toc card" aria-label="Sisällys" style="box-shadow:none;margin-bottom:24px"><h2 class="h3" style="font-size:1.05rem">Sisällys</h2><ol>
<li><a href="#miksi">Miksi kattoa pitää huoltaa?</a></li><li><a href="#rytmi">Huollon vuosirytmi</a></li><li><a href="#tarkista">Mitä tarkistaa?</a></li><li><a href="#tyypit">Kattotyyppien erot</a></li><li><a href="#itse">Itse vai ammattilainen?</a></li><li><a href="#kulut">Paljonko huolto maksaa?</a></li></ol></nav>
<h2 id="miksi">Miksi kattoa pitää huoltaa?</h2>
<p>Suomalainen katto joutuu kovaan rasitukseen: lumikuorma, jäätyminen ja sulaminen, syyssateet, UV-säteily ja kasvusto kuluttavat katetta vuodesta toiseen. Huolto ei tee katosta uutta, mutta se hidastaa kulumista ja paljastaa pienet viat ennen kuin vesi pääsee rakenteisiin. Vesivahingon korjaus maksaa usein moninkertaisesti säännölliseen huoltoon verrattuna.</p>
<h2 id="rytmi">Huollon vuosirytmi</h2>
<ul><li><b>Keväällä:</b> tarkista talven jäljet, kuten irronneet osat, rikkoutuneet tiilet ja lumiesteet. Varmista, että sulamisvedet pääsevät ränneihin ja syöksytorviin. <a href="/kevaan-katon-tarkistuslista">Kevään tarkistuslista</a></li>
<li><b>Kesällä:</b> sopiva aika katon pesuun, sammalkäsittelyyn, pinnoitukseen ja korjauksiin.</li>
<li><b>Syksyllä:</b> puhdista rännit lehtien pudottua ja tarkista läpiviennit ennen talvea. <a href="/syksyn-katon-tarkistuslista">Syksyn tarkistuslista</a></li>
<li><b>Talvella:</b> seuraa lumikuormaa ja jään kertymistä räystäille. Pudota lunta vain turvallisesti.</li></ul>
<h2 id="tarkista">Mitä tarkistaa?</h2>
<p>Suurimman osan voi tarkistaa maasta käsin kiikareilla ja ullakolta taskulampulla:</p>
<ul class="checklist"><li>Kasvusto ja lika</li><li>Rikkinäiset tiilet</li><li>Ruoste ja maalipinta</li><li>Löysät ruuvit</li><li>Läpiviennit</li><li>Pellitykset</li><li>Rännit ja syöksytorvet</li><li>Lumiesteet ja tikkaat</li><li>Vuotojäljet ullakolla</li><li>Aluskatteen kunto</li></ul>
<p>Oireiden tulkintaan löydät apua <a href="/kattohuolto#oireet">oiretaulukosta</a>.</p>
<h2 id="tyypit">Kattotyyppien erot</h2>
<p><a href="/peltikaton-huolto">Peltikatossa</a> tärkeintä on maalipinta, kiinnikkeet ja läpiviennit. <a href="/tiilikaton-huolto">Tiilikatossa</a> korostuvat kasvusto, rikkinäiset tiilet ja aluskate. <a href="/huopakaton-huolto">Huopakatossa</a> tarkistetaan saumat, pintasirote ja vedenpoisto, eikä sitä pestä kovalla paineella.</p>
<h2 id="itse">Itse vai ammattilainen?</h2>
<p>Silmämääräiset tarkistukset ja matalan talon rännien puhdistus onnistuvat itse. Katolle nouseminen on aina putoamisriski. Pesu, sammalkäsittely, korjaukset ja maalaus kannattaa yleensä teettää ammattilaisella, jolla on oikeat välineet ja menetelmät. Edellytä aina, että kattoturvatuotteet ovat kunnossa – myös nuohoojan ja huoltohenkilöstön vuoksi.</p>
<h2 id="kulut">Paljonko huolto maksaa?</h2>
<p>Pääkaupunkiseudun julkaistujen hinnastojen perusteella pesu maksaa noin 5–10 €/m², rännien puhdistus noin 150–400 € ja kuntotarkastus noin 250–500 € (tarkistettu {D()}). Katso <a href="/hinnat">kaikki hinnat ja hintalaskuri</a>. Kunnossapitotyöstä voi saada kotitalousvähennystä työn osuudesta.</p>''',
  [("/kattohuolto", "Kattohuolto"), ("/hinnat", "Hinnat"), ("/katon-kuntotarkastus", "Katon kuntotarkastus")], ("usein", "kotitalousvahennys"), read_min=6)

A2 = art("/katon-pesu-hinta", "Paljonko katon pesu maksaa? Hinnat ja esimerkit 2026",
  "Paljonko katon pesu maksaa? Neliöhinnat, kokonaishinnat eri kattokoille, mitä hintaan sisältyy ja miten kotitalousvähennys vaikuttaa.",
  "Paljonko katon pesu maksaa?", "Katon pesun hinta muodostuu katon koosta, materiaalista, jyrkkyydestä ja kasvuston määrästä. Näin hinta rakentuu ja mitä tavallisen omakotitalon katon pesu maksaa.", f'''
<h2>Lyhyt vastaus</h2>
<p>Pääkaupunkiseudulla julkaistujen hinnastojen perusteella katon pesu maksaa noin <b>5–10 €/m²</b>. Tavallisen omakotitalon katolle (80–150 m²) kokonaishinta on usein noin <b>700–1 200 €</b> suojakäsittelyineen (tarkistettu {D()}).</p>
<h2>Miten hinta muodostuu?</h2>
<ul><li><b>Pinta-ala:</b> isompi katto maksaa enemmän, mutta neliöhinta yleensä laskee koon kasvaessa.</li>
<li><b>Minimiveloitus:</b> pienille katoille on usein vähimmäishinta, koska kaluston kuljetus ja turvajärjestelyt maksavat saman verran katon koosta riippumatta. Esimerkiksi Kotikatto.fi ilmoittaa minimiveloitukseksi 990 €.</li>
<li><b>Jyrkkyys ja korkeus:</b> jyrkällä tai korkealla katolla työ on hitaampaa ja voi vaatia nostimen.</li>
<li><b>Kasvusto:</b> paksu sammal vaatii mekaanista poistoa tai kaksivaiheista käsittelyä.</li>
<li><b>Sisältö:</b> suojakäsittely, rännien tyhjennys ja jätteiden poisto voivat sisältyä hintaan tai olla lisäpalveluita.</li></ul>
<h2>Esimerkkihinnat</h2>
<div class="table-wrap"><table class="stack"><thead><tr><th scope="col">Katto</th><th scope="col">Arvio</th></tr></thead><tbody>
<tr><th scope="row">Pieni katto, alle 80 m²</th><td data-label="Arvio">noin 490–990 €</td></tr>
<tr><th scope="row">Keskikokoinen katto, 80–150 m²</th><td data-label="Arvio">noin 700–1 350 €</td></tr>
<tr><th scope="row">Suuri katto, 150–250 m²</th><td data-label="Arvio">noin 1 200–2 250 €</td></tr></tbody></table></div>
<p class="source">Haarukat perustuvat Ulkopesun julkaisemiin kokoluokkahintoihin ja Kotikatto.fi:n julkaisemaan 9 €/m² neliöhintaan, tarkistettu {D()}.</p>
<h2>Kotitalousvähennys</h2>
<p>Katon pesu on kunnossapitotyötä. Hallituksen esityksen mukaan vuonna 2026 voit vähentää 40 % työn osuudesta (omavastuu 150 €, enintään 2 100 €/hlö). Esimerkiksi 1 000 euron pesussa, jossa työn osuus on 800 €, vähennys on noin 170 €. <a href="/usein-kysyttya#kotitalousvahennys">Lue ehdot</a>.</p>
<h2>Halpa vai hyvä?</h2>
<p>Vertaa tarjousten sisältöä, älä pelkkää hintaa. Pesu ilman suojakäsittelyä voi olla halvempi, mutta kasvusto palaa nopeammin. Kysy myös menetelmästä: väärä paine voi vaurioittaa katetta. <a href="/tarjousten-vertailu">Näin vertailet tarjouksia</a>.</p>''',
  [("/katon-pesu", "Katon pesu"), ("/katon-pesu-helsinki", "Kattopesun hinta Helsingissä"), ("/hinnat#laskuri", "Hintalaskuri")], ("pesu_hinta", "kesto"))

A3 = art("/kattohuolto-hinta-helsinki", "Paljonko kattohuolto maksaa Helsingissä? Vuosibudjetti omakotitalolle",
  "Paljonko kattohuolto maksaa Helsingissä vuodessa ja kymmenessä vuodessa? Esimerkkibudjetti omakotitalolle julkaistujen hintojen perusteella.",
  "Paljonko kattohuolto maksaa Helsingissä?", "Yksittäisten palveluiden hinnat ovat yksi asia, kokonaiskustannus toinen. Laskimme, mitä katon säännöllinen huolto maksaa tavalliselle helsinkiläiselle omakotitalolle vuodessa ja kymmenessä vuodessa.", f'''
<h2>Esimerkkikohde</h2>
<p>Helsinkiläinen omakotitalo, jossa on 130 m² betonitiilikatto, tontilla on puita ja kasvustoa on kohtalaisesti. Laskelma perustuu pääkaupunkiseudun yritysten julkaisemiin hintoihin (tarkistettu {D()}). Se on suuntaa-antava, eikä se ole tarjous.</p>
<h2>Kymmenen vuoden huoltosuunnitelma</h2>
<div class="table-wrap"><table class="stack"><thead><tr><th scope="col">Toimenpide</th><th scope="col">Kertoja 10 v</th><th scope="col">Hinta / kerta</th><th scope="col">Yhteensä</th></tr></thead><tbody>
<tr><th scope="row">Rännien puhdistus</th><td data-label="Kertoja">10 (1×/v)</td><td data-label="Hinta / kerta">noin 150–370 €</td><td data-label="Yhteensä">1 500–3 700 €</td></tr>
<tr><th scope="row">Pesu ja suojakäsittely</th><td data-label="Kertoja">2–3</td><td data-label="Hinta / kerta">noin 700–1 300 €</td><td data-label="Yhteensä">1 400–3 900 €</td></tr>
<tr><th scope="row">Kuntotarkastus</th><td data-label="Kertoja">2</td><td data-label="Hinta / kerta">noin 290–390 €</td><td data-label="Yhteensä">580–780 €</td></tr>
<tr><th scope="row">Pienet korjaukset</th><td data-label="Kertoja">tarpeen mukaan</td><td data-label="Hinta / kerta">tarjouskohtainen</td><td data-label="Yhteensä">varaa esim. 500–1 000 €</td></tr>
</tbody></table></div>
<p><b>Yhteensä noin 4 000–9 400 € kymmenessä vuodessa eli noin 400–940 € vuodessa ennen kotitalousvähennystä.</b> Rännit voi puhdistaa itse matalasta talosta, mikä pienentää kustannuksia selvästi.</p>
<h2>Mihin vertaan?</h2>
<p>Kotikatto.fi:n julkaiseman hinnaston mukaan tiilikattoremontti maksaa 70–100 €/m² eli 130 m² katolle karkeasti 9 100–13 000 € ({D()}). Jos säännöllinen huolto lisää katteen käyttöikää useilla vuosilla, se maksaa itsensä usein takaisin. Tarkkaa hyötyä on kuitenkin vaikea luvata, koska käyttöikään vaikuttavat myös asennuksen laatu ja olosuhteet.</p>
<h2>Miten säästää?</h2>
<ul><li>Yhdistä palvelut: pesu, rännit ja tarkastus samalla käynnillä.</li><li>Hae kotitalousvähennys työn osuudesta.</li><li>Karsi kattoa varjostavat oksat, jotta katto pysyy puhtaana pidempään.</li><li>Pyydä 2–3 tarjousta samoilla tiedoilla.</li></ul>''',
  [("/hinnat", "Kattohuollon hinnat"), ("/kattohuolto-helsinki", "Kattohuolto Helsingissä"), ("/pinnoitus-vai-kattoremontti", "Pinnoitus vai kattoremontti?")], ("kotitalousvahennys",))

A4 = art("/milloin-katto-kannattaa-pesta", "Milloin katto kannattaa pestä? Merkit ja paras ajankohta",
  "Milloin katto kannattaa pestä? Tunnista pesun tarve, valitse oikea vuodenaika ja sää ja tiedä, kuinka usein eri katot pestään.",
  "Milloin katto kannattaa pestä?", "Pesu kannattaa ajoittaa sekä katon kunnon että sään mukaan. Näin tunnistat oikean hetken.", '''
<h2>Merkit pesun tarpeesta</h2>
<ul><li>katolla näkyy vihreää sammalta, harmaata jäkälää tai tummia levälaikkuja</li><li>tiilet ovat tummuneet tai vihertyneet erityisesti pohjoislappeella</li><li>rännit tukkeutuvat toistuvasti sammaleesta ja roskista</li><li>edellisestä pesusta on yli 3–5 vuotta</li><li>talo on metsän tai suurten puiden lähellä</li><li>suunnittelet huoltomaalausta tai pinnoitusta, sillä pesu on aina sen ensimmäinen vaihe</li></ul>
<h2>Paras vuodenaika</h2>
<p>Pesu tehdään kuivalla säällä ja plussakeleillä. Etelä-Suomessa otollisinta aikaa ovat yleensä <b>touko–kesäkuu</b> ja <b>elo–syyskuu</b>. Keväällä pesu poistaa talven aikana kertyneen lian ja kasvuston ennen kasvukauden huippua. Syksyllä katto saadaan puhtaaksi ennen talvea.</p>
<h2>Milloin ei kannata pestä?</h2>
<ul><li><b>Pakkasella:</b> vesi jäätyy, katto muuttuu liukkaaksi, ja jäätyvä vesi voi vaurioittaa katetta.</li><li><b>Sateella:</b> pesu- ja suoja-aineet huuhtoutuvat pois ennen kuin ne ehtivät vaikuttaa.</li><li><b>Helteellä:</b> kuuma kattopinta kuivattaa pesuaineen liian nopeasti.</li></ul>
<h2>Kuinka usein?</h2>
<p>Nyrkkisääntönä 3–5 vuoden välein. Varjoisilla ja kosteilla tonteilla väli voi olla 2–3 vuotta. Peltikatto tarvitsee pesua yleensä harvemmin kuin betonitiilikatto. Suojakäsittely pesun jälkeen pidentää väliä.</p>
<h2>Varaa ajoissa</h2>
<p>Kattopesun sesonki on lyhyt, ja suosituimmat ajat täyttyvät keväällä nopeasti. Pyydä tarjoukset hyvissä ajoin, esimerkiksi maalis–huhtikuussa kesäkuun pesua varten.</p>''',
  [("/katon-pesu", "Katon pesu"), ("/katon-pesu-hinta", "Paljonko katon pesu maksaa?"), ("/kevaan-katon-tarkistuslista", "Kevään tarkistuslista")], ("milloin_pesta", "kesto"), read_min=4)

A5 = art("/sammal-katolla", "Sammal katolla – pitääkö olla huolissaan?",
  "Onko sammal katolla vaarallista? Milloin sammal on vain kauneusvirhe ja milloin se alkaa vaurioittaa kattoa, ja mitä asialle kannattaa tehdä.",
  "Sammal katolla – pitääkö olla huolissaan?", "Ohut sammalkerros ei ole hätätilanne, mutta sitä ei kannata jättää kasvamaan vuosiksi. Näin arvioit, milloin on aika toimia.", '''
<h2>Lyhyt vastaus</h2>
<p>Vähäinen sammal ei yleensä vaurioita kattoa heti. Ajan mittaan se kuitenkin pitää katteen kosteana, tukkii rännejä ja voi pakkasen kanssa rapauttaa tiiliä ja haurastuttaa huopaa. Mitä aiemmin kasvuston poistaa, sitä helpompaa ja edullisempaa se on.</p>
<h2>Miksi sammal on haitallinen?</h2>
<ul><li><b>Kosteus:</b> sammal imee vettä, jolloin katto ei pääse kuivumaan.</li><li><b>Jäätyminen:</b> kosteus laajenee pakkasella ja rapauttaa tiilen pintaa.</li><li><b>Vedenohjaus:</b> tiilten saumoissa kasvava sammal voi padota vettä ja ohjata sitä tiilien alle.</li><li><b>Rännit:</b> irtoava sammal tukkii rännit ja syöksytorvet.</li><li><b>Huopa:</b> juurtuva kasvusto voi aiheuttaa halkeamia ja epätiiviitä kohtia.</li></ul>
<h2>Milloin toimia?</h2>
<div class="table-wrap"><table class="stack"><thead><tr><th scope="col">Tilanne</th><th scope="col">Suositus</th></tr></thead><tbody>
<tr><th scope="row">Yksittäisiä sammaltyynyjä</th><td data-label="Suositus">Seuraa tilannetta ja suunnittele pesu seuraavalle kesälle.</td></tr>
<tr><th scope="row">Sammalta laajasti pohjoislappeella</th><td data-label="Suositus">Pesu ja suojakäsittely kuluvalla tai seuraavalla kaudella.</td></tr>
<tr><th scope="row">Paksu, yli sentin kerros tai sammalta tiilten alla</th><td data-label="Suositus">Sammaleen poisto (tarvittaessa kaksivaiheinen) ja kuntotarkastus.</td></tr>
<tr><th scope="row">Sammalta ja vuotojälkiä ullakolla</th><td data-label="Suositus">Kuntotarkastus pikaisesti.</td></tr></tbody></table></div>
<h2>Entä jäkälä ja levä?</h2>
<p>Jäkälä kasvaa hitaammin ja kiinnittyy tiukasti. Se on usein merkki pitkään jatkuneesta kosteudesta. Levä näkyy tummina raitoina tai laikkuina. Molemmat poistetaan pesulla ja kasvustoa tuhoavalla aineella, ja suojakäsittely hidastaa niiden paluuta.</p>
<h2>Kannattaako sammal raapia itse?</h2>
<p>Kova kaapiminen tai painepesu voi vahingoittaa erityisesti vanhoja tiiliä ja huopakattoa. Lisäksi katolla työskentely on vaarallista. Pieni määrä sammalta matalalta katolta onnistuu varovasti harjalla, mutta laajemmat kasvustot kannattaa jättää ammattilaiselle. <a href="/sammaleen-poisto">Lue sammaleen poiston menetelmistä ja hinnoista</a>.</p>''',
  [("/sammaleen-poisto", "Sammaleen poisto"), ("/tiilikaton-huolto", "Tiilikaton huolto"), ("/huopakaton-huolto", "Huopakaton huolto")], ("sammal",), read_min=4)

A9 = art("/kuntotarkastus-mita-tarkastetaan", "Katon kuntotarkastus – mitä tarkastuksessa katsotaan?",
  "Katon kuntotarkastuksen tarkistuslista: katemateriaali, läpiviennit, pellitykset, kiinnitykset, aluskate, ullakko, kattoturvatuotteet ja sadevesijärjestelmä.",
  "Katon kuntotarkastus – mitä tarkastuksessa katsotaan?", "Hyvä kuntotarkastus on järjestelmällinen ja dokumentoitu. Tällä listalla tiedät, mitä tarkastajalta kannattaa odottaa ja mitä raportista pitäisi löytyä.", '''
<h2>1. Katemateriaali</h2><ul><li>kulumisaste ja pinnoitteen kunto</li><li>halkeamat, rapautuminen ja rikkinäiset tiilet</li><li>ruoste ja maalipinnan vauriot</li><li>huopakatteen saumat, kuplat ja pintasirote</li><li>kasvuston määrä ja sijainti</li></ul>
<h2>2. Läpiviennit ja piippu</h2><ul><li>tiivisteiden ja kumien kunto</li><li>piipun pellitys ja pinnoite</li><li>ilmanvaihtoputkien, antennien ja aurinkopaneelien kiinnitykset</li></ul>
<h2>3. Pellitykset ja kiinnitykset</h2><ul><li>räystäs-, harja-, otsa- ja jiiripellitykset</li><li>ruuvien ja kiinnikkeiden kunto ja tiiviys</li><li>harjatiilien kiinnitys ja harjatiivisteet</li></ul>
<h2>4. Ullakko ja aluskate</h2><ul><li>kosteus- ja vuotojäljet ruoteissa ja vasoissa</li><li>aluskatteen repeämät ja haurastuminen</li><li>tuuletusraot ja ilman kulku</li><li>huurre talvella ja mikrobikasvuston merkit</li></ul>
<h2>5. Kattoturvatuotteet</h2><ul><li>lumiesteet, lapetikkaat, kattosillat ja seinätikkaat</li><li>kiinnitysten lujuus ja niiden alla olevan katteen kunto</li></ul>
<h2>6. Sadevesijärjestelmä</h2><ul><li>rännien kaadot, kiinnikkeet ja vuotokohdat</li><li>syöksytorvien toiminta ja vedenohjaus pois sokkelilta</li></ul>
<h2>Mitä raportista pitäisi löytyä?</h2>
<ul class="checklist"><li>Kuvat havainnoista</li><li>Kiireellisyysluokitus</li><li>Arvio jäljellä olevasta käyttöiästä</li><li>Suositellut toimenpiteet</li><li>Tarkastuksen rajaukset</li></ul>
<p>Rajaukset ovat tärkeitä: jos ullakolle ei päästy tai katolle ei noustu, raportin pitää kertoa se. Lue lisää palvelusta ja hinnoista <a href="/katon-kuntotarkastus">kuntotarkastussivulta</a>.</p>''',
  [("/katon-kuntotarkastus", "Katon kuntotarkastus"), ("/pinnoitus-vai-kattoremontti", "Pinnoitus vai kattoremontti?")], ("remontti",), read_min=4)

A10 = art("/pinnoitus-vai-kattoremontti", "Katon pinnoitus vai kattoremontti? Näin päätät",
  "Katon pinnoitus vai kattoremontti? Vertailu kustannuksista, käyttöiästä ja edellytyksistä sekä päätöstaulukko, jonka avulla valitset oikean ratkaisun.",
  "Katon pinnoitus vai kattoremontti?", "Pinnoitus maksaa murto-osan remontista, mutta se ei aina ole oikea ratkaisu. Ratkaisevaa on katon rakenteiden kunto.", f'''
<h2>Perusero</h2>
<p><b>Pinnoitus tai huoltomaalaus</b> uusii katteen pintakerroksen. Se suojaa ja parantaa ulkonäköä, mutta ei korjaa rakenteita. <b>Kattoremontissa</b> vanha kate puretaan ja uusitaan, usein myös aluskate ja tarvittaessa ruoteet sekä pellitykset.</p>
<h2>Kustannukset</h2>
<div class="table-wrap"><table class="stack"><thead><tr><th scope="col">Työ</th><th scope="col">Julkaistu hinta</th><th scope="col">130 m² katto</th></tr></thead><tbody>
<tr><th scope="row">Pinnoitus (pesu + käsittely)</th><td data-label="Julkaistu hinta">29 €/m²</td><td data-label="130 m²">noin 3 800 €</td></tr>
<tr><th scope="row">Peltikattoremontti</th><td data-label="Julkaistu hinta">50–70 €/m²</td><td data-label="130 m²">noin 6 500–9 100 €</td></tr>
<tr><th scope="row">Tiilikattoremontti</th><td data-label="Julkaistu hinta">70–100 €/m²</td><td data-label="130 m²">noin 9 100–13 000 €</td></tr></tbody></table></div>
<p class="source">Lähde: <a href="https://www.kotikatto.fi/hinta" rel="noopener nofollow" target="_blank">Kotikatto.fi:n hinnasto</a>, tarkistettu {D()}. Laskelmat ovat suuntaa-antavia. Remonttihinnat vaihtelevat paljon kohteen mukaan.</p>
<h2>Päätöstaulukko</h2>
<div class="table-wrap"><table class="stack"><thead><tr><th scope="col">Havainto</th><th scope="col">Suunta</th></tr></thead><tbody>
<tr><th scope="row">Pinta haalistunut, ei vuotoja</th><td data-label="Suunta">Pinnoitus tai maalaus</td></tr>
<tr><th scope="row">Pistemäistä pintaruostetta peltikatossa</th><td data-label="Suunta">Ruosteenpoisto ja huoltomaalaus</td></tr>
<tr><th scope="row">Betonitiilet ehjiä mutta huokoisia</th><td data-label="Suunta">Pesu ja pinnoitus</td></tr>
<tr><th scope="row">Aluskate haurastunut tai puuttuu</th><td data-label="Suunta">Kattoremontti</td></tr>
<tr><th scope="row">Toistuvia vuotoja useasta kohdasta</th><td data-label="Suunta">Kuntotarkastus, todennäköisesti remontti</td></tr>
<tr><th scope="row">Läpiruostunut pelti tai laajasti rapautuneet tiilet</th><td data-label="Suunta">Kattoremontti</td></tr>
<tr><th scope="row">Kate lähellä tavanomaisen käyttöikänsä loppua</th><td data-label="Suunta">Harkitse remonttia, pinnoitus voi olla huono sijoitus</td></tr></tbody></table></div>
<h2>Varo myyntipuhetta</h2>
<p>Pinnoitusta myydään joskus katteille, joiden aluskate on jo käyttöikänsä päässä. Remonttia taas voidaan tarjota katolle, jolle riittäisi huolto. Pyydä kuntotarkastus ja kirjallinen perustelu ehdotetulle ratkaisulle, ja kysy tarvittaessa toinen mielipide.</p>''',
  [("/katon-pinnoitus", "Katon maalaus ja pinnoitus"), ("/katon-kuntotarkastus", "Katon kuntotarkastus")], ("pinnoitus", "remontti"))

A11 = art("/rannien-puhdistus-kuinka-usein", "Rännien puhdistus – kuinka usein se kannattaa tehdä?",
  "Kuinka usein rännit pitää puhdistaa? Suositus tontin puuston mukaan, merkit tukkeutumisesta ja mitä laiminlyönti voi maksaa.",
  "Rännien puhdistus – kuinka usein se kannattaa tehdä?", "Rännien puhdistus on halpaa verrattuna siihen, mitä tukkeutunut sadevesijärjestelmä voi pahimmillaan aiheuttaa. Oikea väli riippuu ennen kaikkea tontin puustosta.", '''
<h2>Suositus tontin mukaan</h2>
<div class="table-wrap"><table class="stack"><thead><tr><th scope="col">Tontti</th><th scope="col">Puhdistusväli</th></tr></thead><tbody>
<tr><th scope="row">Avoin, ei puita lähellä</th><td data-label="Puhdistusväli">1 kerta vuodessa (syksy)</td></tr>
<tr><th scope="row">Lehtipuita lähellä</th><td data-label="Puhdistusväli">1–2 kertaa vuodessa, viimeistään lehtien pudottua</td></tr>
<tr><th scope="row">Havupuita tai paljon puustoa</th><td data-label="Puhdistusväli">2 kertaa vuodessa (kevät ja syksy)</td></tr></tbody></table></div>
<h2>Merkit tukoksesta</h2>
<ul><li>vesi valuu sateella rännin reunan yli</li><li>rännissä kasvaa sammalta tai heinää</li><li>syöksytorvesta ei tule vettä sateella</li><li>sokkelissa tai julkisivun alaosassa on roiskejälkiä tai kosteutta</li><li>räystäille muodostuu talvella paksuja jääpuikkoja</li></ul>
<h2>Mitä laiminlyönti voi aiheuttaa?</h2>
<p>Tukkeutunut ränni ohjaa veden julkisivulle ja sokkelin viereen. Seurauksena voi olla julkisivun kastumista, sokkelin ja perustusten kosteusrasitusta sekä talvella jäätymisen aiheuttamia vaurioita ränneille ja räystäille. Painava, jäätynyt ränni voi myös irrota kiinnikkeistään.</p>
<h2>Itse vai ammattilainen?</h2>
<p>Matalan talon rännit voi puhdistaa itse tukevilta tikkailta. Kaksikerroksisessa talossa ja jyrkällä katolla ammattilainen on turvallisempi valinta. Pääkaupunkiseudulla puhdistus maksaa julkaistujen hinnastojen perusteella noin 150–400 €. <a href="/rannien-puhdistus">Katso hinnat ja palvelun sisältö</a>.</p>''',
  [("/rannien-puhdistus", "Rännien puhdistus"), ("/syksyn-katon-tarkistuslista", "Syksyn tarkistuslista")], ("rannit_hinta",), read_min=3)

A12 = art("/kevaan-katon-tarkistuslista", "Kevään katon tarkistuslista – 10 kohtaa talven jälkeen",
  "Kevään katon tarkistuslista: tarkista talven jäljet, lumiesteet, rännit, läpiviennit ja ullakko. Tulostettava lista omakotitalon omistajalle.",
  "Kevään katon tarkistuslista", "Kun lumet ovat sulaneet, on hyvä hetki katsoa, miten katto selvisi talvesta. Suurimman osan tarkistuksista voit tehdä maasta käsin ja ullakolta.", '''
<p class="note" style="margin-top:0">Turvallisuus ensin: älä nouse liukkaalle katolle. Käytä kiikareita ja ota kuvia. Jos katolle on pakko nousta, käytä kattoturvatuotteita ja turvavaljaita.</p>
<h2>Tarkistuslista</h2>
<ol>
<li><b>Irronneet osat:</b> onko pihalla tiilenpaloja, ruuveja, pellinkappaleita tai pintasirotetta?</li>
<li><b>Tiilet ja kate:</b> näkyykö rikkinäisiä, siirtyneitä tai puuttuvia tiiliä, halkeamia tai painumia?</li>
<li><b>Peltikatto:</b> onko maalipinnassa kolhuja tai lumen ja jään aiheuttamia naarmuja? Onko ruuveja löystynyt?</li>
<li><b>Lumiesteet ja tikkaat:</b> ovatko lumiesteet, kattotikkaat ja kulkusillat suorassa ja tukevasti kiinni?</li>
<li><b>Läpiviennit:</b> näyttävätkö piipun ja ilmanvaihdon läpivientien tiivisteet ehjiltä?</li>
<li><b>Pellitykset:</b> ovatko räystäs- ja harjapellit paikallaan, vai onko tuuli taivuttanut niitä?</li>
<li><b>Rännit:</b> ovatko rännit suorassa? Lumikuorma voi vääntää rännejä ja kiinnikkeitä.</li>
<li><b>Syöksytorvet:</b> pääsevätkö sulamisvedet vapaasti alas ja pois sokkelilta?</li>
<li><b>Ullakko:</b> näkyykö kosteusjälkiä, valumia tai tummuneita kohtia ruoteissa?</li>
<li><b>Kasvusto:</b> paljastuiko lumen alta sammalta? Merkitse muistiin, milloin pesu kannattaa tehdä.</li></ol>
<h2>Mitä seuraavaksi?</h2>
<p>Kirjaa havainnot ja ota kuvat talteen. Pienet asiat, kuten rännin kiinnikkeen kiristyksen, voi hoitaa itse. Vuotojäljet, irronneet pellitykset ja rikkinäiset tiilet kannattaa korjauttaa ennen kesän sateita. Jos havaintoja on useita, tilaa <a href="/katon-kuntotarkastus">kuntotarkastus</a>.</p>''',
  [("/syksyn-katon-tarkistuslista", "Syksyn tarkistuslista"), ("/katon-huolto-opas", "Katon huolto – täydellinen opas")], (), read_min=3)

A13 = art("/syksyn-katon-tarkistuslista", "Syksyn katon tarkistuslista – valmistele katto talveen",
  "Syksyn katon tarkistuslista: rännien puhdistus, läpiviennit, lumiesteet, ullakon tuuletus ja muut toimet ennen talvea.",
  "Syksyn katon tarkistuslista", "Syksy on katon tärkein huoltohetki. Kun rännit ovat auki ja liitokset tiiviitä, katto kestää talven sateet, lumen ja jäätymisen paremmin.", '''
<h2>Tarkistuslista</h2>
<ol>
<li><b>Rännit ja syöksytorvet:</b> puhdista viimeisten lehtien pudottua ja testaa vedenkulku.</li>
<li><b>Roskat katolla:</b> poista lehdet ja oksat taitteista, piipun takaa ja läpivientien ympäriltä.</li>
<li><b>Läpiviennit:</b> tarkista tiivisteet ennen pakkasia, sillä sulavat ja jäätyvät vedet etsivät heikot kohdat.</li>
<li><b>Lumiesteet:</b> varmista kiinnitykset ennen ensimmäistä lunta.</li>
<li><b>Kattotikkaat ja kulkusillat:</b> nuohoojan ja lumenpudotuksen pitää päästä katolle turvallisesti.</li>
<li><b>Myrskyvauriot:</b> tarkista syysmyrskyjen jälkeen pellitykset ja harjat.</li>
<li><b>Oksat:</b> karsi katolle ulottuvat oksat, jotka hankaavat katetta tai pudottavat lunta.</li>
<li><b>Ullakon tuuletus:</b> varmista, etteivät tuuletusaukot ole tukossa. Huono tuuletus voi aiheuttaa huurretta ja kosteutta talvella.</li>
<li><b>Lumityövälineet:</b> hanki turvallinen lumenpudotusväline, jos katolta pitää pudottaa lunta.</li></ol>
<h2>Talven aikana</h2>
<p>Seuraa lumikuormaa erityisesti suojasäiden jälkeen, kun märkä lumi on raskasta. Pudota lunta vain turvallisesti ja kattoturvatuotteita käyttäen. Isoilla tai korkeilla katoilla lumenpudotus kannattaa tilata ammattilaiselta. Jääpuikot räystäillä voivat kertoa lämpövuodoista tai tukkeutuneista ränneistä.</p>''',
  [("/rannien-puhdistus", "Rännien puhdistus"), ("/kevaan-katon-tarkistuslista", "Kevään tarkistuslista")], ("usein",), read_min=3)

A15 = art("/tarjousten-vertailu", "Näin vertailet kattohuollon tarjouksia – tarkistuslista",
  "Näin vertailet kattohuollon tarjouksia: mitä tarjouksessa pitää lukea, mitkä kulut usein puuttuvat, miten tarkistat yrityksen ja mitä sopimukseen kirjataan.",
  "Näin vertailet kattohuollon tarjouksia", "Kaksi saman hintaista tarjousta voi sisältää aivan eri asiat. Tällä tarkistuslistalla teet tarjouksista vertailukelpoisia.", '''
<h2>1. Pyydä tarjoukset samoilla tiedoilla</h2>
<p>Anna kaikille yrityksille samat tiedot: kattotyyppi, pinta-ala, kerrosluku, rakennusvuosi, havaitut ongelmat ja kuvat. Silloin erot johtuvat yrityksistä eivätkä lähtötiedoista.</p>
<h2>2. Vertaa sisältöä rivi riviltä</h2>
<div class="table-wrap"><table class="stack"><thead><tr><th scope="col">Tarkista</th><th scope="col">Miksi?</th></tr></thead><tbody>
<tr><th scope="row">Työ ja menetelmä</th><td data-label="Miksi?">Väärä paine tai aine voi vaurioittaa katetta.</td></tr>
<tr><th scope="row">Materiaalit ja aineet</th><td data-label="Miksi?">Suoja-aineen laatu vaikuttaa lopputuloksen kestoon.</td></tr>
<tr><th scope="row">ALV</th><td data-label="Miksi?">Kuluttajahinnoissa pitää näkyä verollinen hinta.</td></tr>
<tr><th scope="row">Jätteiden poisto</th><td data-label="Miksi?">Sammal ja roskat voivat jäädä pihalle, jos poisto ei kuulu hintaan.</td></tr>
<tr><th scope="row">Telineet / nostimet</th><td data-label="Miksi?">Voivat olla merkittävä lisäkulu korkeissa kohteissa.</td></tr>
<tr><th scope="row">Suojaukset</th><td data-label="Miksi?">Ikkunat, julkisivu ja istutukset.</td></tr>
<tr><th scope="row">Jälkikäsittely</th><td data-label="Miksi?">Ilman suojakäsittelyä kasvusto palaa nopeammin.</td></tr>
<tr><th scope="row">Mahdolliset korjaukset</th><td data-label="Miksi?">Sovi etukäteen lisätöiden hinnoittelu ja hyväksyntä.</td></tr>
<tr><th scope="row">Takuu</th><td data-label="Miksi?">Mitä takuu kattaa ja kuinka kauan?</td></tr></tbody></table></div>
<h2>3. Tarkista yritys</h2>
<ul><li>Y-tunnus ja ennakkoperintärekisteri <a href="https://www.ytj.fi/" rel="noopener" target="_blank">YTJ:stä</a></li><li>vastuuvakuutus</li><li>kokemus juuri sinun kattotyypistäsi</li><li>kirjallinen tarjous ja selkeät maksuehdot</li></ul>
<h2>4. Laske kokonaiskustannus</h2>
<p>Halvin tarjous ei aina ole edullisin. Laske mukaan mahdolliset lisätyöt, telinekulut ja lopputuloksen kesto. Jos yksi tarjous on selvästi muita halvempi, selvitä, mitä siitä puuttuu.</p>
<h2>5. Kirjaa sopimukseen</h2>
<ul><li>työn sisältö ja menetelmät</li><li>aikataulu ja sääolosuhteiden vaikutus</li><li>hinta, maksuerät ja työn osuus eriteltynä kotitalousvähennystä varten</li><li>lisätöiden hinnoittelu</li><li>takuu ja reklamaatiomenettely</li></ul>
<p>Kuluttajan oikeuksista kerrotaan tarkemmin <a href="https://www.kkv.fi/kuluttaja-asiat/" rel="noopener" target="_blank">Kilpailu- ja kuluttajaviraston</a> sivuilla.</p>''',
  [("/yritykset", "Yritysvertailu"), ("/hinnat", "Hinnat")], ("tarjoukset", "kysy"))

ARTICLES = [A1, A2, A3, A4, A5, A9, A10, A11, A12, A13, A15]

INDEX = [
    ("/katon-huolto-opas", "Katon huolto – täydellinen opas suomalaiselle omakotitalolle", "Vuosirytmi, tarkistuskohteet ja kustannukset yhdessä paikassa."),
    ("/katon-pesu-hinta", "Paljonko katon pesu maksaa?", "Neliöhinnat, esimerkit ja kotitalousvähennys."),
    ("/kattohuolto-hinta-helsinki", "Paljonko kattohuolto maksaa Helsingissä?", "Kymmenen vuoden huoltobudjetti omakotitalolle."),
    ("/milloin-katto-kannattaa-pesta", "Milloin katto kannattaa pestä?", "Merkit pesun tarpeesta ja paras ajankohta."),
    ("/sammal-katolla", "Sammal katolla – pitääkö olla huolissaan?", "Milloin sammal on riski ja mitä tehdä."),
    ("/peltikaton-huolto", "Peltikaton huolto", "Ruoste, maalipinta, kiinnikkeet ja huoltomaalaus."),
    ("/tiilikaton-huolto", "Tiilikaton huolto", "Sammal, rikkinäiset tiilet, aluskate ja pinnoitus."),
    ("/huopakaton-huolto", "Huopakaton huolto", "Saumat, pintasirote ja vedenpoisto."),
    ("/kuntotarkastus-mita-tarkastetaan", "Katon kuntotarkastus – mitä tarkastuksessa katsotaan?", "Tarkistuslista ja hyvän raportin sisältö."),
    ("/pinnoitus-vai-kattoremontti", "Katon pinnoitus vai kattoremontti?", "Kustannukset ja päätöstaulukko."),
    ("/rannien-puhdistus-kuinka-usein", "Rännien puhdistus – kuinka usein se kannattaa tehdä?", "Suositukset tontin puuston mukaan."),
    ("/kevaan-katon-tarkistuslista", "Kevään katon tarkistuslista", "10 kohtaa talven jälkeen."),
    ("/syksyn-katon-tarkistuslista", "Syksyn katon tarkistuslista", "Valmistele katto talveen."),
    ("/katon-pesu-helsinki", "Kattopesun hinta Helsingissä", "Julkaistut hinnat ja esimerkkilaskelmat."),
    ("/tarjousten-vertailu", "Näin vertailet kattohuollon tarjouksia", "Tarkistuslista tarjousten vertailuun."),
]


def articles_index_page():
    cards = "".join(f'<a class="card" href="{u}"><h3>{t}</h3><p class="mb0">{d}</p></a>' for u, t, d in INDEX)
    return dict(slug="/katto-opas", title="Katto-opas – oppaat katon huoltoon ja kustannuksiin",
                desc="Katto-opas: käytännön oppaat katon pesuun, sammaleen poistoon, kuntotarkastukseen, pinnoitukseen, rännien puhdistukseen ja tarjousten vertailuun.",
                h1="Katto-opas", lead="Käytännönläheiset oppaat katon huoltoon, kustannuksiin ja tarjousten vertailuun – ilman myyntipuhetta.",
                crumbs=[("/katto-opas", "Katto-opas")], priority="0.8",
                body=f'<section class="section"><div class="wrap"><div class="grid g3">{cards}</div></div></section>' + C.band())
