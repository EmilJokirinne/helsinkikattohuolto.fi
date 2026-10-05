# helsinkikattohuolto.fi

Staattinen, tuotantovalmis sivusto (HTML + CSS + vanilla JS). Ei build-riippuvuuksia, ei kehyksiä, ei ulkoisia fontteja tai kirjastoja → erittäin nopea (Core Web Vitals).

## Julkaisu
Kaikki tiedostot ovat juuressa. Lataa sellaisenaan palvelimelle:

- **Netlify / Cloudflare Pages:** toimii suoraan. Siistit URL:t (`/hinnat` → `hinnat.html`) ja `404.html` hoituvat automaattisesti. `_headers` asettaa tietoturva- ja välimuistiotsakkeet. Netlifyssä tarjouspyyntölomake toimii Netlify Formsin kautta ilman lisäasetuksia.
- **Vercel:** `vercel.json` ottaa siistit URL:t käyttöön.
- **Apache / perinteinen webhotelli:** `.htaccess` hoitaa siistit URL:t, HTTPS-ohjauksen, www-ohjauksen ja 404-sivun.

## Asetukset – `config.js`
- `gaMeasurementId` – GA4-tunnus. Tyhjä = ei analytiikkaa. Analytiikka ladataan vain evästesuostumuksella.
- `formEndpoint` – lomakkeen vastaanottaja (esim. Formspree tai oma backend). Tyhjä = Netlify Forms.
- `contactEmail` – ylläpidon sähköposti.

Seuratut tapahtumat: `quote_request`, `price_calculator_used`, `company_clicked`, `phone_clicked`, `email_clicked`, `article_read`, `comparison_used` (dataLayer + gtag).

## Yritysten ja hintojen päivitys – `companies.json`
Lisää tai muokkaa yrityksiä tässä tiedostossa. `null` hintakentässä = "Ei julkaistu". Päivitä aina `priceSource`, `priceCheckedAt` ja ylätason `updatedAt`.
Sivu hakee tiedoston selaimessa ja päivittää vertailutaulukon heti. Aja lisäksi `python3 build.py`, niin myös hakukoneille näkyvä esirenderöity HTML päivittyy.

## Sisällön muokkaus
Sivut generoidaan Python-skriptillä (Python 3.9+, ei riippuvuuksia):

- `content_pages.py` – pääsivut, palvelut, alueet, hinnat, yritykset, juridiset sivut
- `content_articles.py` – Katto-opas ja artikkelit
- `content_faq.py` – usein kysytyt kysymykset (myös FAQPage-merkinnät)
- `components.py` – yhteiset osiot (laskuri, vertailu, lomake, taulukot)
- `build.py` – sivupohja, metatiedot, Schema.org, sitemap.xml, robots.txt

Aja muutosten jälkeen: `python3 build.py`

Hintalaskurin €/m²-tasot ovat `app.js`:n `CALC`-objektissa.

## Ennen julkaisua tarkista
1. **Liiketoimintamalli:** "Tietoa sivustosta" -sivulla on lause mahdollisesta korvauksesta tarjouspyyntöjen välittämisestä. Muokkaa sitä vastaamaan todellista mallia (`content_pages.py`, TIETOA).
2. **Rekisterinpitäjä:** lisää tietosuojaselosteeseen yrityksen virallinen nimi ja Y-tunnus.
3. **Kotitalousvähennys:** teksti perustuu hallituksen esitykseen HE 113/2026 (40 %, enintään 2 100 €, omavastuu 150 €). Tarkista, että laki on vahvistettu.
4. **Kuvat:** hero on kevyt SVG-kuvitus. Jos haluat valokuvan, käytä omaa tai lisensoitua kuvaa WebP/AVIF-muodossa.
