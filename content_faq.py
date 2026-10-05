"""Usein kysytyt kysymykset. Vastaukset HTML:nä. Käytetään FAQ-sivulla ja FAQPage-merkinnöissä."""

KV = ('<p>Kyllä, useimmiten. Katon pesu, sammaleen poisto, rännien puhdistus, huolto ja korjaukset ovat kunnossapitotyötä, '
      'josta voi saada kotitalousvähennystä <b>työn osuudesta</b> – ei materiaaleista eikä matkakuluista. Hallituksen esityksen '
      '(HE 113/2026) mukaan vuosina 2026–2027 vähennys on 40 % yritykseltä ostetun työn osuudesta, enintään 2 100 € henkilöä kohden, '
      'ja omavastuu on 150 € vuodessa. Muutos on tarkoitus soveltaa takautuvasti vuoden 2026 alusta.</p>'
      '<p>Edellytyksenä on, että yritys kuuluu ennakkoperintärekisteriin sopimuksen tekohetkellä ja että laskussa on eritelty työn osuus. '
      'Tarkista voimassa olevat ehdot aina <a href="https://www.vero.fi/henkiloasiakkaat/verokortti-ja-veroilmoitus/tulot-ja-vahennykset/kotitalousvahennys/" rel="noopener" target="_blank">Verohallinnon sivuilta</a>. '
      'Asunto-osakeyhtiö ei voi saada kotitalousvähennystä.</p>')

FAQ_ALL = {
    "usein": ("Kuinka usein katto kannattaa huoltaa?",
              "<p>Katto kannattaa tarkistaa silmämääräisesti maasta käsin kahdesti vuodessa, keväällä lumien sulettua ja syksyllä lehtien pudottua. "
              "Rännit puhdistetaan tyypillisesti 1–2 kertaa vuodessa. Pesua tarvitaan yleensä 3–5 vuoden välein ja varjoisilla, puiden ympäröimillä tonteilla useammin. "
              "Ammattilaisen kuntotarkastus on järkevä noin 5 vuoden välein ja aina, jos huomaat vuotojälkiä, kosteutta ullakolla tai irronneita osia.</p>"),
    "pesu_hinta": ("Paljonko katon pesu maksaa?",
                   "<p>Pääkaupunkiseudulla julkaistujen hinnastojen perusteella katon pesu maksaa noin 5–10 €/m². Omakotitalon katolle (80–150 m²) "
                   "kokonaishinta on usein noin 700–1 200 € suojakäsittelyn kanssa. Pienille katoille on yleensä minimiveloitus. "
                   "Hintaan vaikuttavat katon koko, jyrkkyys, korkeus, kasvuston määrä ja se, sisältyykö suojakäsittely. "
                   "<a href=\"/hinnat\">Katso hintavertailu</a>.</p>"),
    "milloin_pesta": ("Milloin katto kannattaa pestä?",
                      "<p>Paras aika on loppukevät–alkukesä tai loppukesä–alkusyksy, kun sää on kuiva ja lämpötila pysyy plussalla myös öisin. "
                      "Pakkasella pesua ei tehdä, ja helteellä pesuaine kuivuu liian nopeasti. Katto kannattaa pestä, kun pinnalla näkyy sammalta, jäkälää tai "
                      "tummumista tai kun edellisestä pesusta on kulunut 3–5 vuotta.</p>"),
    "painepesuri": ("Voiko katon pestä painepesurilla?",
                    "<p>Riippuu kattomateriaalista. Peltikaton voi pestä varovasti matalalla paineella, ja betonitiilikatto kestää painepesua ammattilaisen säätämällä paineella. "
                    "Huopakattoa ei pidä pestä kovalla paineella, koska se irrottaa pintasirotetta ja kuluttaa huopaa. Väärä paine tai suuttimen kulma voi myös painaa vettä "
                    "tiilien saumoista aluskatteelle. Ota huomioon myös työturvallisuus: katolla työskentely vaatii asianmukaiset kattoturvatuotteet ja turvavaljaat.</p>"),
    "sammal": ("Miten sammal poistetaan katolta?",
               "<p>Paksu sammal poistetaan ensin mekaanisesti esimerkiksi harjaamalla tai kaapimalla kattoa vahingoittamatta. Sen jälkeen katto pestään ja käsitellään "
               "sammaleen ja jäkälän tuhoavalla aineella. Hyvin paksun kasvuston kohdalla voidaan käyttää kaksivaiheista käsittelyä: ensin aine tappaa kasvuston, "
               "ja kuollut sammal poistetaan muutaman viikon tai kuukauden kuluttua. Menetelmä valitaan aina kattomateriaalin mukaan. "
               "<a href=\"/sammaleen-poisto\">Lue lisää sammaleen poistosta</a>.</p>"),
    "rannit_hinta": ("Paljonko rännien puhdistus maksaa?",
                     "<p>Julkaistujen hinnastojen perusteella rännien puhdistus maksaa pääkaupunkiseudulla noin 150–400 €. Kattopesun yhteydessä tehtynä hinta on usein edullisempi, "
                     "esimerkiksi alkaen 149 €. Erillisenä palveluna hinta voi olla noin 270–370 € katon koon mukaan.</p>"),
    "pinnoitus": ("Milloin katto kannattaa pinnoittaa?",
                  "<p>Pinnoitus tai huoltomaalaus on järkevä, kun katon pinta on kulunut mutta rakenne, kiinnitykset ja aluskate ovat vielä hyvässä kunnossa. "
                  "Peltikaton maalipinnan haalistuminen ja pistemäinen pintaruoste sekä betonitiilikaton pinnan huokoistuminen ovat tyypillisiä merkkejä. "
                  "Pinnoitus ei korjaa vuotavaa kattoa tai vaurioitunutta aluskatetta. <a href=\"/pinnoitus-vai-kattoremontti\">Pinnoitus vai kattoremontti?</a></p>"),
    "remontti": ("Milloin tarvitaan kattoremontti?",
                 "<p>Kattoremonttia kannattaa harkita, kun katto vuotaa toistuvasti useasta kohdasta, aluskate on haurastunut, ruodelaudoitus on kostunut tai lahonnut, "
                 "peltikaton ruoste on syövyttänyt peltiä läpi tai huopakaton saumat ja pinta ovat laajasti haljenneet. Myös katteen ikä vaikuttaa: kun katemateriaalin "
                 "tavanomainen käyttöikä lähestyy loppuaan, pinnoitukseen sijoittaminen ei välttämättä enää kannata. Kuntotarkastus auttaa arvioimaan tilanteen.</p>"),
    "tarjoukset": ("Kannattaako pyytää useampi tarjous?",
                   "<p>Kyllä. Suosittelemme vähintään 2–3 tarjousta. Kattotöiden hinnoittelu vaihtelee, ja tarjouksia vertaamalla näet sekä markkinahinnan että sen, mitä eri yritykset "
                   "sisällyttävät hintaan, kuten suojakäsittelyn, rännien puhdistuksen tai telineet. <a href=\"/tarjousten-vertailu\">Näin vertailet tarjouksia</a>.</p>"),
    "kotitalousvahennys": ("Voiko kattohuollosta saada kotitalousvähennystä?", KV),
    "kesto": ("Kuinka kauan katon pesu kestää?",
              "<p>Omakotitalon katon pesu kestää tyypillisesti yhden työpäivän, suuremmilla tai jyrkillä katoilla 1–2 päivää. Jos katolle tehdään kaksivaiheinen sammalkäsittely, "
              "lopullinen tulos näkyy vasta viikkojen tai kuukausien kuluttua, kun kuollut kasvusto irtoaa. Sää voi siirtää työtä, sillä pesua ei tehdä sateella eikä pakkasella.</p>"),
    "kysy": ("Mitä tarjouspyynnössä kannattaa kysyä?",
             "<ul><li>Mitä hinta sisältää: työ, materiaalit, ALV, suojaukset, jätteiden poisto, nostimet tai telineet?</li>"
             "<li>Millä menetelmällä ja aineella katto käsitellään, ja sopiiko se kattomateriaalille?</li>"
             "<li>Sisältyykö suojakäsittely, ja kuinka kauan sen vaikutus yrityksen mukaan kestää?</li>"
             "<li>Miten mahdolliset lisätyöt hinnoitellaan, jos katolta löytyy korjattavaa?</li>"
             "<li>Mikä on työn takuu ja miten reklamaatiot hoidetaan?</li>"
             "<li>Onko yritys ennakkoperintärekisterissä ja onko sillä vastuuvakuutus?</li>"
             "<li>Erotellaanko laskussa työn osuus kotitalousvähennystä varten?</li></ul>"),
    "itse": ("Voinko pestä katon itse?",
             "<p>Matalan ja loivan katon voi huoltaa itse, jos käytössä on asianmukaiset kattoturvatuotteet, turvavaljaat ja kattoa vahingoittamattomat menetelmät. "
             "Katolla työskentely on kuitenkin putoamisvaaran vuoksi riskialtista, ja märkä, pesuaineella käsitelty katto on liukas. "
             "Jyrkille ja korkeille katoille suosittelemme ammattilaista.</p>"),
    "taloyhtio": ("Koskeeko sivusto myös taloyhtiöitä?",
                  "<p>Sivuston hinnat ja ohjeet on kirjoitettu ensisijaisesti omakoti-, pari- ja rivitaloille. Taloyhtiöiden kattohuolto hinnoitellaan yleensä kohdekohtaisesti, "
                  "ja huolto kannattaa sisällyttää kunnossapitosuunnitelmaan. Huomaa, ettei asunto-osakeyhtiö voi saada kotitalousvähennystä.</p>"),
}

FAQ_ORDER = ["usein", "pesu_hinta", "milloin_pesta", "painepesuri", "sammal", "rannit_hinta", "pinnoitus", "remontti",
             "tarjoukset", "kotitalousvahennys", "kesto", "kysy", "itse", "taloyhtio"]


def faq_by_ids(*ids):
    return [FAQ_ALL[i] for i in ids]
