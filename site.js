(() => {
  const UTM_KEYS = ['utm_source','utm_medium','utm_campaign','utm_content','utm_term'];
  const params = new URLSearchParams(window.location.search);
  const current = {};
  UTM_KEYS.forEach((key) => {
    const value = params.get(key);
    if (value) current[key] = value;
  });

  if (Object.keys(current).length) {
    try {
      localStorage.setItem('dlf_campaign', JSON.stringify({ ...current, landing_page: location.pathname, captured_at: new Date().toISOString() }));
    } catch (_) {}
  }

  let stored = {};
  try { stored = JSON.parse(localStorage.getItem('dlf_campaign') || '{}'); } catch (_) {}

  const campaign = Object.keys(current).length ? current : stored;
  const pageSlug = (location.pathname.split('/').pop() || 'home').replace('.html','');

  document.querySelectorAll('a[href*="play.google.com/store/apps/details"]').forEach((link) => {
    try {
      const url = new URL(link.href);
      const referral = new URLSearchParams();
      referral.set('utm_source', campaign.utm_source || 'dlf_website');
      referral.set('utm_medium', campaign.utm_medium || 'website');
      referral.set('utm_campaign', campaign.utm_campaign || 'organic_site');
      referral.set('utm_content', campaign.utm_content || pageSlug);
      if (campaign.utm_term) referral.set('utm_term', campaign.utm_term);
      if (!url.searchParams.get('referrer')) url.searchParams.set('referrer', referral.toString());
      link.href = url.toString();

      link.addEventListener('click', () => {
        const appId = url.searchParams.get('id') || '';
        const payload = { event: 'play_store_click', app_id: appId, page: pageSlug, ...Object.fromEntries(referral.entries()) };
        try { localStorage.setItem('dlf_last_play_click', JSON.stringify({ ...payload, clicked_at: new Date().toISOString() })); } catch (_) {}
        if (typeof window.gtag === 'function') {
          window.gtag('event', 'play_store_click', payload);
        }
      });
    } catch (_) {}
  });
})();
