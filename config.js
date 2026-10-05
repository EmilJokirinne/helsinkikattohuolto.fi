/* Sivuston asetukset – muokkaa tätä tiedostoa, ei app.js:ää.
 *
 * gaMeasurementId:  Google Analytics 4 -mittaustunnus (esim. "G-XXXXXXX").
 *                   Tyhjä = analytiikkaa ei ladata lainkaan. GA ladataan vain,
 *                   jos käyttäjä hyväksyy analytiikkaevästeet.
 * formEndpoint:     Osoite, johon tarjouspyyntölomake lähetetään (esim. Formspree,
 *                   oma backend tai Make/Zapier-webhook). Tyhjä = lomake lähetetään
 *                   Netlify Forms -palveluun (toimii, kun sivusto on Netlifyssä).
 * contactEmail:     Ylläpidon yhteysosoite.
 */
window.HKH_CONFIG = {
  gaMeasurementId: "",
  formEndpoint: "",
  contactEmail: "info@helsinkikattohuolto.fi"
};
