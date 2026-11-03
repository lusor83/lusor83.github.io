# Release readiness — 2 November 2026

PR #2 prepares CTA measurement and the verified RuinShot launch. No remote analytics SDK or property is enabled.

Validated: 10 Node tests cover consent grant/revocation, seven-day storage expiry, invalid/personal UTM values, explicit Play referrers, blocked storage, and Play/press/game CTA events. An Install click remains a click, never an installation.

RuinShot production 14 / 0.3.0-rc.5 was observed active in 178 countries/regions; the public US listing exposed Install in an anonymous browser. The signed-in listing reports device availability. A fresh installation on a second device was not performed. Launch pages, metadata, product facts and creator ZIP are updated together. Existing screenshots retain desktop provenance.

The central web integration is blocked on a verified web stream/measurement ID and consent UI configuration. The Astral Android stream 15466639305 is not a website stream. Until configured, only local campaign events exist; website traffic and conversion totals are unavailable. No measurement ID has been guessed.

Deployment requires owner production approval. Review this PR and preview the pages first. After deployment, verify the public CTA, official package ID and canonical URLs; confirm no Analytics requests/storage before opt-in and no further sends/storage after revocation. Then validate actual first-open attribution separately from click events.

App telemetry coverage: Astral has Firebase/GA4 gameplay events and automatic SDK events, with exact-build Android 10 evidence; its developer filter is still Test and commercial cohorts are not certified clean. LookTwist has bounded local diagnostics, not a verified remote funnel. Baggage and Life app-specific remote progression/retention are not verified. Nerelune uses its existing Android bridge; central GA4 coverage is unverified. RuinShot has Play and AdMob reports, with no verified GA4 gameplay funnel. My Finance Forecast app-level GA4 coverage is unverified. Play store visitors/Install clicks, Play acquisitions and AdMob requests/impressions/revenue must retain separate definitions and periods for every product.

# Campaign 3.0 — 3 November 2026

Three English Android gameplay pilots are public on RacingHub and verified anonymously through YouTube oEmbed with matching titles and author. The three press kits, product JSON, README and creator ZIP include those links and truthful outcome context. The partner page gives these games priority without removing RuinShot or Baggage materials. No private Drive assets, metrics or QA logs are included in the public site.

Life: https://youtube.com/shorts/3eyEgai7CKE
Astral: https://youtube.com/shorts/2BT2FnKZrm4
Nerelune: https://youtube.com/shorts/xStyPXXzKns

Deployment remains gated on owner approval; publishing a Short does not deploy this PR or change any game release. Central analytics remains unconfigured.
