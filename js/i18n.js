// Static, locally served translations. No visitor content is sent to a translation service.
window.AlleyI18n = (() => {
  const supported = ['ko', 'en', 'ja', 'zh-CN'];
  const names = { ko: '한국어', en: 'English', ja: '日本語', 'zh-CN': '简体中文' };
  const url = new URL(location.href);
  let saved;
  try { saved = localStorage.getItem('alley-language'); } catch { /* Storage may be disabled. */ }
  let lang = supported.includes(url.searchParams.get('lang')) ? url.searchParams.get('lang') : supported.includes(saved) ? saved : 'ko';
  let catalog = {};
  const t = (key, values = {}) => {
    let template = String(catalog.ui?.[key] ?? key ?? '');
    if (lang === 'en' && key === '{count}가지 비교 · {places}곳' && values.count === 1) template = template.replace('comparisons', 'comparison');
    return template.replace(/\{(\w+)\}/g, (match, name) => values[name] ?? match);
  };
  const fields = ['name', 'category', 'visitWhen', 'cost', 'schedule', 'closure', 'description', 'address', 'hours', 'useMode', 'visitTip', 'accessSummary', 'access', 'unknown', 'checkLabel', 'photoLabel'];
  function translateStatic() {
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    const texts = [];
    while (walker.nextNode()) texts.push(walker.currentNode);
    texts.forEach(node => {
      if (node.parentElement.closest('script, style, [data-language-name]')) return;
      const key = node.textContent.trim();
      if (key && catalog.ui?.[key]) node.textContent = node.textContent.replace(key, t(key));
    });
    document.querySelectorAll('[aria-label], [title], [placeholder]').forEach(node => {
      ['aria-label', 'title', 'placeholder'].forEach(attr => { if (node.hasAttribute(attr)) node.setAttribute(attr, t(node.getAttribute(attr))); });
    });
    document.querySelectorAll('.language-select').forEach(select => {
      select.replaceChildren(...supported.map(code => {
        const option = document.createElement('option');
        option.value = code;
        option.lang = code;
        option.textContent = names[code];
        return option;
      }));
      select.value = lang;
      select.addEventListener('change', () => {
        if (!supported.includes(select.value) || select.value === lang) return;
        const target = new URL(location.href);
        target.searchParams.set('lang', select.value);
        try { localStorage.setItem('alley-language', select.value); } catch { /* URL still persists the choice. */ }
        window.dispatchEvent(new CustomEvent('alley:language-change', { detail: target.href }));
        location.replace(target.href);
      });
    });
  }
  const ready = (async () => {
    if (lang !== 'ko') {
      try {
        const [response, uiResponse] = await Promise.all([fetch(`js/locales/${lang}.json?v=26`), fetch('js/locales/ui.json?v=26')]);
        if (!response.ok || !uiResponse.ok) throw new Error('Translation unavailable');
        catalog = await response.json();
        const ui = await uiResponse.json();
        catalog.ui = Object.fromEntries(Object.entries(ui).map(([key, values]) => [key, values[supported.indexOf(lang) - 1]]));
        if (!window.ALLEY_PLACES.every(place => Array.isArray(catalog.places?.[place.id]) && catalog.places[place.id].length === fields.length) ||
            !window.BLIND_SPOT_PAIRS.every(pair => catalog.pairs?.[pair.id])) throw new Error('Translation catalog incomplete');
      } catch {
        lang = 'ko';
        catalog = {};
        document.getElementById('language-status').hidden = false;
      }
    }
    document.documentElement.lang = lang;
    // Keep language in shared links and same-origin navigation, including with storage disabled.
    if (url.searchParams.get('lang') !== lang) {
      url.searchParams.set('lang', lang);
      history.replaceState(history.state, '', url);
    }
    window.ALLEY_PLACES.forEach(place => {
      place.originalName = place.name;
      place.originalAddress = place.address;
      if (lang === 'ko') return;
      const row = catalog.places[place.id];
      fields.forEach((field, index) => { place[field] = row[index]; });
      place.mapName = catalog.mapNames?.[place.id] || place.name;
      place.hoursSummary = [place.schedule.replace(/\n/g, ' · '), place.closure].filter(Boolean).join(' · ');
      place.imageAlt = `${place.name} · ${place.photoLabel}`;
      place.sourceLabel = t(place.sourceLabel);
      place.locationSource = t(place.locationSource);
      place.photoAuthor = t(place.photoAuthor);
      place.photoDate = t(place.photoDate);
      place.review = { ...place.review, fields: t(place.review.fields), note: t(place.review.note) };
      if (place.notice) place.notice = { ...place.notice, ...catalog.notices?.[place.id] };
    });
    window.BLIND_SPOT_PAIRS.forEach(pair => {
      pair.regionLabel = t(pair.regionLabel);
      if (lang === 'ko') return;
      const originalChoices = pair.choices || {};
      const translation = catalog.pairs[pair.id];
      Object.assign(pair, translation);
      if (translation.choices) pair.choices = Object.fromEntries(Object.entries(translation.choices).map(([id, choice]) => {
        const merged = { ...originalChoices[id], ...choice };
        if (merged.review) merged.review = { ...merged.review, fields: t(merged.review.fields), note: t(merged.review.note) };
        return [id, merged];
      }));
    });
    window.ALLEY_CATEGORIES.forEach(category => { category.label = t(category.label); });
    translateStatic();
    document.querySelectorAll('.brand').forEach(link => { link.href = `./?lang=${lang}`; });
    document.title = t('AI 추천에 없는 안국·서촌');
    document.querySelector('meta[name="description"]').content = t('AI 추천에 없는 안국·서촌. 핫플과 골목의 다른 선택을 사진과 지도로 나란히 비교해 보세요.');
  })();
  return { t, ready, get lang() { return lang; }, get isKorean() { return lang === 'ko'; },
    mapStyle(style) {
      if (lang !== 'ko') style.layers.filter(layer => layer.type === 'symbol' && layer.layout?.['text-field']).forEach(layer => {
        layer.layout['text-field'] = ['coalesce', ['get', `name:${lang === 'zh-CN' ? 'zh' : lang}`], ['get', 'name:en'], ['get', 'name']];
      });
      Object.values(style.sources).forEach(source => { if (source.attribution) source.attribution = source.attribution.replace('스타일 출처', t('스타일 출처')); });
      return style;
    }
  };
})();
