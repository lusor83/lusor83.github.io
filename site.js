(() => {
  'use strict';
  const UTM_KEYS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'];
  const STORAGE_KEY = 'dlf_campaign';
  const TTL_MS = 7 * 24 * 60 * 60 * 1000;
  const now = Date.now();
  const page = location.pathname;
  const pageSlug = (page.split('/').pop() || 'home').replace(/\.html$/, '');
  let consent = window.lusorAnalyticsConsent === true;

  // Campaign values are public slugs, never names, email addresses or full URLs.
  function sanitize(input) {
    const result = {};
    UTM_KEYS.forEach(key => {
      const value = input[key];
      if (typeof value === 'string' && /^[a-zA-Z0-9_-]{1,80}$/.test(value)) result[key] = value;
    });
    return result;
  }
  function clearStored() {
    try {
      localStorage.removeItem(STORAGE_KEY);
      localStorage.removeItem('dlf_last_play_click');
    } catch (_) {}
  }
  const current = sanitize(Object.fromEntries(new URLSearchParams(location.search)));
  let stored = {};
  if (consent) {
    try {
      const candidate = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
      const captured = Date.parse(candidate.captured_at);
      if (Number.isFinite(captured) && captured <= now && now - captured < TTL_MS) stored = sanitize(candidate);
      else clearStored();
    } catch (_) { clearStored(); }
  } else clearStored();
  const campaign = Object.keys(current).length ? current : stored;
  const capturedAt = Object.keys(current).length ? now : Date.parse((() => {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}').captured_at; } catch (_) { return ''; }
  })());

  function persist() {
    if (!consent || !Object.keys(campaign).length || !Number.isFinite(capturedAt)) return;
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify({...campaign, captured_at: new Date(capturedAt).toISOString()})); } catch (_) {}
  }
  persist();
  // An existing consent UI can call this after an explicit analytics choice.
  // No analytics SDK or remote endpoint is loaded by this script.
  window.lusorSetAnalyticsConsent = granted => {
    consent = granted === true;
    window.lusorAnalyticsConsent = consent;
    if (consent) persist(); else clearStored();
  };
  function track(eventName, extra = {}, attribution = campaign) {
    const payload = {page, ...attribution, ...extra};
    window.dispatchEvent(new CustomEvent('lusor:campaign-event', {detail: {event: eventName, ...payload}}));
    if (consent && typeof window.gtag === 'function') window.gtag('event', eventName, payload);
  }

  document.querySelectorAll('a[href]').forEach(link => {
    try {
      const url = new URL(link.href, location.href);
      if (url.protocol !== 'https:' && url.origin !== location.origin) return;
      if (url.hostname === 'play.google.com' && url.pathname === '/store/apps/details') {
        const appId = url.searchParams.get('id');
        if (!appId || !/^[a-zA-Z0-9_.]+$/.test(appId)) return;
        const referral = new URLSearchParams({
          utm_source: campaign.utm_source || 'dlf_website',
          utm_medium: campaign.utm_medium || 'website',
          utm_campaign: campaign.utm_campaign || 'organic_site',
          utm_content: campaign.utm_content || pageSlug
        });
        if (campaign.utm_term) referral.set('utm_term', campaign.utm_term);
        if (!url.searchParams.has('referrer')) url.searchParams.set('referrer', referral.toString());
        const actualReferral = sanitize(Object.fromEntries(new URLSearchParams(url.searchParams.get('referrer'))));
        link.href = url.toString();
        link.addEventListener('click', () => track('play_store_click', {app_id: appId}, actualReferral));
      } else if (url.origin === location.origin && /^\/press\/(?:[^/]+\.html)?$/.test(url.pathname)) {
        link.addEventListener('click', () => track('press_kit_click', {destination: url.pathname}));
      } else if (url.origin === location.origin && /^\/(?:nerelune|astral-fusion|life-unwritten|looktwist|my-finance-forecast|baggage-color-flow|ruinshot)\.html$/.test(url.pathname)) {
        link.addEventListener('click', () => track('game_page_click', {destination: url.pathname}));
      }
    } catch (_) {}
  });
})();

