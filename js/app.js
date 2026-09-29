(async () => {
await window.AlleyI18n.ready;
const { t } = window.AlleyI18n;
window.AlleyMap = window.createAlleyMap();
const places = window.ALLEY_PLACES;
const pairs = window.BLIND_SPOT_PAIRS;
const grid = document.getElementById('place-grid');
const resultCount = document.getElementById('result-count');
const regionButtons = [...document.querySelectorAll('.region-button')];
const detail = document.getElementById('place-detail');
const viewToggle = document.getElementById('view-toggle');
let currentRegion = '';
let currentCategory = '';
let currentContext = '';
let filteredPairs = [];
let listLimit = 4;
let currentPlace = '';
let selectedPlace = '';
let returnFocus = null;
let mapView = false;
let listScroll = 0;
let mapPair = '';
let mapReturnFocus = null;
let locationReady = false;
const categories = window.ALLEY_CATEGORIES;
const moreComparisons = document.getElementById('more-comparisons');
const mapCategory = document.getElementById('map-category');
categories.forEach(category => {
  const option = document.createElement('option');
  option.value = category.id;
  option.textContent = category.label;
  mapCategory.append(option);
});

// Remove only the legacy app's worker and caches.
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.getRegistrations().then(registrations => {
    registrations.filter(registration => registration.active?.scriptURL.endsWith('/sw.js'))
      .forEach(registration => registration.unregister());
  }).catch(() => {});
}
if ('caches' in window) {
  caches.keys().then(keys => keys.filter(key => key.startsWith('blindspot-cache-'))
    .forEach(key => caches.delete(key))).catch(() => {});
}

function element(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text) node.textContent = t(text);
  return node;
}
function externalLink(text, url) {
  const link = element('a', '', text);
  link.href = url;
  link.target = '_blank';
  link.rel = 'noopener noreferrer';
  return link;
}
function makePhoto(place, eager = false, detailPhoto = false) {
  const media = element('div', 'place-media');
  const loading = element('span', 'loading-note', '사진 불러오는 중');
  const image = window.AlleyMedia.create(place, { eager, detail: detailPhoto,
    onLoad: () => loading.remove(),
    onError: () => {
      media.classList.add('photo-placeholder');
      media.replaceChildren(element('span', 'cover-note', '사진을 불러오지 못했어요'));
    }
  });
  media.append(image, loading);
  return media;
}
function selectPlace(id) {
  selectedPlace = id;
  document.querySelectorAll('.place-choice').forEach(link => {
    const selected = link.dataset.place === id;
    link.classList.toggle('is-selected', selected);
    if (selected) link.setAttribute('aria-current', 'true');
    else link.removeAttribute('aria-current');
  });
  window.AlleyMap?.select(id);
}
function detailUrl(place, pairId = '') {
  const url = new URL(location.href);
  url.hash = `place/${place.id}`;
  if (pairId) url.searchParams.set('context', pairId);
  else url.searchParams.delete('context');
  return url;
}
function showDetails(place, opener, pairId = '') {
  returnFocus = opener || document.activeElement;
  history.pushState({ detailFromApp: true }, '', detailUrl(place, pairId));
  syncLocation();
}
function renderCard(pair) {
  const items = pair.placeIds.map(id => window.ALLEY_CHOICE(places.find(place => place.id === id), pair));
  const card = element('article', 'comparison-card');
  card.id = `comparison-${pair.id}`;
  card.tabIndex = -1;
  const heading = element('h2', 'comparison-heading', pair.title);
  heading.id = `pair-${pair.id}`;
  card.setAttribute('aria-labelledby', heading.id);
  const header = element('header', 'comparison-header');
  header.append(element('span', 'comparison-region', `${pair.regionLabel} · ${categories.find(item => item.id === pair.category).label}`), heading,
    element('p', 'comparison-reason', pair.reason));
  const columns = element('div', 'comparison-columns');
  items.forEach(place => {
    const link = element('a', 'place-choice');
    link.href = detailUrl(place, pair.id);
    link.dataset.place = place.id;
    link.dataset.pair = pair.id;
    link.setAttribute('aria-label', t('{name} 장소 정보 보기', { name: place.name }));
    link.addEventListener('click', event => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.button !== 0) return;
      event.preventDefault();
      showDetails(places.find(item => item.id === place.id), link, pair.id);
    });
    const name = element('h3', 'comparison-name', place.name);
    name.id = `name-${pair.id}-${place.id}`;
    link.append(makePhoto(place, pair === pairs[0]), name, element('p', 'comparison-value', place.visitWhen),
      element('span', 'choice-action', '자세히 보기 ›'));
    columns.append(link);
  });
  const facts = element('table', 'comparison-facts');
  facts.append(element('caption', 'sr-only', t('{names} 비교', { names: items.map(item => item.name).join(' · ') })));
  const head = element('thead', 'sr-only');
  const names = element('tr');
  items.forEach(place => { const th = element('th', '', place.name); th.scope = 'col'; names.append(th); });
  head.append(names);
  const body = element('tbody');
  [['비용', 'cost'], ['기본 운영', 'schedule']].forEach(([label, key]) => {
    const row = element('tr');
    items.forEach(place => {
      const cell = element('td');
      cell.append(element('span', 'fact-label', label), element('span', 'fact-value', place[key]));
      if (key === 'schedule') {
        if (place.closure) cell.append(element('span', 'fact-closure', place.closure));
        const check = externalLink(`${place.checkLabel} ↗`, place.checkUrl);
        check.className = 'fact-check';
        check.setAttribute('aria-label', t('{name} {label} (새 창)', { name: place.name, label: place.checkLabel }));
        cell.append(check);
      }
      row.append(cell);
    });
    body.append(row);
  });
  facts.append(head, body);
  const mapButton = element('button', 'pair-map-button', '두 곳의 위치 비교');
  mapButton.type = 'button';
  mapButton.setAttribute('aria-label', t('{names} 지도에서 비교', { names: items.map(item => item.name).join(', ') }));
  mapButton.addEventListener('click', () => navigateView(true, pair.id));
  const actions = element('div', 'pair-actions');
  const shareButton = element('button', 'pair-share-button', '비교 링크');
  shareButton.type = 'button';
  shareButton.setAttribute('aria-label', t('{title} 두 장소 비교 링크 복사', { title: pair.title }));
  const shareStatus = element('p', 'copy-status');
  shareStatus.setAttribute('role', 'status');
  const shareFallback = element('input', 'copy-fallback');
  shareFallback.readOnly = true;
  shareFallback.hidden = true;
  shareFallback.setAttribute('aria-label', t('복사할 두 장소 비교 링크'));
  shareButton.addEventListener('click', async () => {
    const url = new URL(location.href);
    url.hash = '';
    url.searchParams.delete('context');
    url.searchParams.set('category', pair.category);
    url.searchParams.set('region', pair.region);
    url.searchParams.set('view', 'map');
    url.searchParams.set('pair', pair.id);
    await copyUrl(url, shareStatus, shareFallback, '두 장소의 비교 링크를 복사했어요.');
  });
  actions.append(mapButton, shareButton);
  const alternatives = element('details', 'pair-alternatives');
  alternatives.append(element('summary', '', '두 곳 모두 어렵다면'));
  const otherSituations = element('div', 'alternative-options');
  pairs.filter(item => item.id !== pair.id).sort((a, b) =>
    Number(b.region === pair.region) - Number(a.region === pair.region) ||
    Number(b.category === pair.category) - Number(a.category === pair.category)).slice(0, 3).forEach(item => {
    const button = element('button', 'situation-link', `${item.shortTitle} · ${item.regionLabel}`);
    button.type = 'button';
    button.addEventListener('click', () => jumpToPair(item.id));
    otherSituations.append(button);
  });
  alternatives.append(element('p', '', '다른 상황을 골라 비교해 보세요. 각 장소의 운영 안내를 확인해 주세요.'), otherSituations);
  card.append(header, columns, facts);
  if (pair.id === 'baeryeom') card.append(element('p', 'pair-notice', '두 곳 모두 기본 월요일 휴관입니다. 공예박물관은 공휴일 예외가 있어요.'));
  if (pair.notice) card.append(element('p', 'pair-notice', pair.notice));
  card.append(actions, shareStatus, shareFallback, alternatives);
  return card;
}

async function copyUrl(url, status, fallback, message) {
  status.textContent = '';
  fallback.hidden = true;
  try {
    await navigator.clipboard.writeText(url.href);
    if (status.isConnected) status.textContent = t(message);
  } catch {
    if (!fallback.isConnected) return;
    fallback.hidden = false;
    fallback.value = url.href;
    fallback.focus();
    fallback.select();
    status.textContent = t('아래 링크를 길게 누르거나 복사해 주세요.');
  }
}

function openPlace(place) {
  const url = new URL(location.href);
  const contextId = url.searchParams.get('context') || url.searchParams.get('pair');
  const contextPair = pairs.find(item => item.id === contextId && item.placeIds.includes(place.id));
  const pair = contextPair ||
    filteredPairs.find(item => item.placeIds.includes(place.id)) || pairs.find(item => item.placeIds.includes(place.id));
  if (currentPlace === place.id && currentContext === (contextPair?.id || '') && detail.open) return;
  currentPlace = place.id;
  currentContext = contextPair?.id || '';
  const choice = window.ALLEY_CHOICE(place, contextPair);
  selectPlace(place.id);
  detail.querySelector('.place-story').open = false;
  detail.querySelector('.operating-details').open = false;
  document.getElementById('copy-status').textContent = '';
  document.getElementById('copy-fallback').hidden = true;
  const closeButton = document.getElementById('close-detail');
  closeButton.setAttribute('aria-label', t(mapView ? '지도로 돌아가기' : '목록으로 돌아가기'));
  closeButton.lastChild.textContent = ` ${t(mapView ? '지도' : '목록')}`;
  document.getElementById('detail-photo').replaceChildren(makePhoto(place, true, true));
  const fields = { category: `${t(place.region === 'anguk' ? '안국' : '서촌')} · ${place.category}`, title: place.name,
    description: choice.description, address: place.address, tip: choice.visitTip, hours: choice.hours,
    cost: choice.cost, access: choice.access, use: choice.useMode, unknown: choice.unknown, 'hours-summary': contextPair?.choices?.[place.id]?.schedule ? `${choice.schedule} · ${choice.closure}` : place.hoursSummary,
    'access-summary': choice.accessSummary, 'photo-label': place.photoLabel };
  Object.entries(fields).forEach(([key, value]) => { document.getElementById(`detail-${key}`).textContent = value; });
  document.getElementById('detail-original').textContent = place.originalName;
  document.getElementById('detail-original').hidden = window.AlleyI18n.isKorean;
  document.getElementById('korean-address-block').hidden = window.AlleyI18n.isKorean;
  document.getElementById('korean-address').textContent = `${place.originalName} · ${place.originalAddress}`;
  document.getElementById('address-copy-status').textContent = '';
  document.getElementById('address-copy-fallback').hidden = true;
  const englishName = document.getElementById('detail-english');
  englishName.textContent = place.englishName || '';
  englishName.hidden = !place.englishName || !window.AlleyI18n.isKorean;
  const context = document.getElementById('detail-context');
  context.textContent = `${pair.shortTitle} · ${choice.visitWhen}`;
  context.hidden = !contextPair;
  const quickCheck = document.getElementById('detail-check');
  quickCheck.replaceChildren(externalLink(`${choice.checkLabel} ↗`, choice.checkUrl));
  if (place.englishSource) quickCheck.append(externalLink('English info ↗', place.englishSource));
  if (place.phone) {
    const phone = element('a', '', '전화로 문의');
    phone.href = `tel:${window.AlleyI18n.isKorean ? place.phone : place.phone.replace(/^0/, '+82')}`;
    phone.setAttribute('aria-label', t('{name} {phone} 전화로 문의', { name: place.name, phone: place.phone }));
    quickCheck.append(phone);
  }
  const notice = document.getElementById('detail-notice');
  notice.textContent = window.ALLEY_VISIT.notice(choice);
  notice.hidden = !notice.textContent;
  document.getElementById('detail-location').textContent = place.locationSource === 'legacy'
    ? t('앱 지도는 대략적인 위치입니다. 정확한 입구는 외부 지도와 운영자 안내에서 확인해 주세요.')
    : t('앱 지도는 장소의 대표 위치입니다({source}). 실제 입구와 도보 경로는 외부 지도에서 확인해 주세요.', { source: place.locationSource });
  const other = places.find(item => item.id === pair.placeIds.find(id => id !== place.id));
  const otherLink = document.getElementById('detail-other');
  otherLink.hidden = !contextPair && pairs.filter(item => item.placeIds.includes(place.id)).length > 1;
  otherLink.textContent = t('↔ {name}도 살펴보기', { name: other.name });
  otherLink.href = detailUrl(other, pair.id);
  otherLink.onclick = event => {
    if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.button !== 0) return;
    event.preventDefault();
    history.replaceState(history.state, '', detailUrl(other, pair.id));
    syncLocation();
    document.getElementById('detail-title').focus({ preventScroll: true });
  };
  const sources = document.getElementById('detail-source');
  sources.replaceChildren(externalLink(`${place.sourceLabel} ↗`, place.source));
  if (place.extraSource) {
    const labels = { jeongdok: '시설 안내', staffpicks: '매장 소식', baeryeom: '전시·프로그램', yisang: '운영기관 소식' };
    sources.append(' · ', externalLink(`${t(labels[place.id] || '추가 방문 안내')} ↗`, place.extraSource));
  }
  document.getElementById('detail-reviewed').textContent = `${window.ALLEY_VISIT.review(choice)}. ${t('실시간 운영 상태가 아닙니다.')}`;
  const credit = document.getElementById('detail-credit');
  credit.replaceChildren(`${t('사진')}: ${place.photoAuthor} · ${place.photoDate} · `,
    externalLink('사진 출처', place.photoSource || place.source));
  if (place.photoLicense) credit.append(' · ', externalLink(place.photoLicense, place.photoLicenseUrl));
  credit.append(` / ${t('원본 비율 유지 · 크기 조정·WebP 변환')}`);
  const mapLink = document.getElementById('detail-map');
  mapLink.href = `https://map.naver.com/p/search/${encodeURIComponent(`${place.originalName} ${place.originalAddress}`)}`;
  mapLink.setAttribute('aria-label', t('{name} 네이버 지도에서 보기 (새 창)', { name: place.name }));
  document.body.classList.add('detail-open');
  if (!detail.open) detail.showModal();
  document.getElementById('detail-scroll').scrollTop = 0;
  document.title = `${place.name} | ${t('AI 추천에 없는 안국·서촌')}`;
}
function closePlace() {
  if (history.state?.detailFromApp) history.back();
  else {
    const url = new URL(location.href);
    url.hash = '';
    history.replaceState(null, '', url);
    syncLocation();
  }
}
function navigateView(show, pairId = '') {
  const url = new URL(location.href);
  if (show) {
    if (!mapView) listScroll = window.scrollY;
    url.searchParams.set('view', 'map');
    if (pairId) {
      url.searchParams.set('pair', pairId);
      const pair = pairs.find(item => item.id === pairId);
      if (currentCategory !== 'all' && pair.category !== currentCategory) url.searchParams.set('category', pair.category);
    }
    else url.searchParams.delete('pair');
  } else {
    url.searchParams.delete('view');
    url.searchParams.delete('pair');
  }
  history.pushState(null, '', url);
  syncLocation();
  if (show) document.getElementById('places').scrollIntoView({ block: 'start' });
}
function jumpToPair(id) {
  const pair = pairs.find(item => item.id === id);
  if (!pair) return;
  const url = new URL(location.href);
  if (currentRegion !== 'all' && currentRegion !== pair.region) url.searchParams.set('region', pair.region);
  if (currentCategory !== 'all' && currentCategory !== pair.category) url.searchParams.set('category', pair.category);
  url.searchParams.delete('view');
  url.searchParams.delete('pair');
  history.pushState(null, '', url);
  syncLocation();
  const index = filteredPairs.findIndex(item => item.id === id);
  if (index >= listLimit) { listLimit = index + 1; renderList(); }
  requestAnimationFrame(() => {
    const card = document.getElementById(`comparison-${id}`);
    card?.scrollIntoView({ block: 'start' });
    card?.focus({ preventScroll: true });
  });
}
let categoriesExpanded = false;
function chooseCategory(id) {
  const url = new URL(location.href);
  url.searchParams.set('category', id);
  url.searchParams.delete('pair');
  url.searchParams.delete('context');
  history.pushState(null, '', url);
  syncLocation();
}
function renderSituationNav() {
  const primary = ['all', 'food', 'cafe', 'rest'];
  const visibleCategories = categories.filter(category => categoriesExpanded || primary.includes(category.id) || category.id === currentCategory);
  const nav = document.getElementById('situation-nav');
  const buttons = visibleCategories.map(category => {
    const button = element('button', 'situation-link', category.label);
    button.type = 'button';
    button.dataset.category = category.id;
    button.setAttribute('aria-controls', 'place-grid');
    button.setAttribute('aria-pressed', String(category.id === currentCategory));
    button.addEventListener('click', () => {
      chooseCategory(category.id);
      document.querySelector(`[data-category="${category.id}"]`)?.focus({ preventScroll: true });
    });
    return button;
  });
  const expand = element('button', 'situation-link category-expand', categoriesExpanded ? '카테고리 접기' : '모든 카테고리');
  expand.type = 'button';
  expand.dataset.expandCategories = '';
  expand.setAttribute('aria-expanded', String(categoriesExpanded));
  expand.setAttribute('aria-controls', 'situation-nav');
  expand.addEventListener('click', () => {
    categoriesExpanded = !categoriesExpanded;
    renderSituationNav();
    nav.querySelector('[data-expand-categories]')?.focus({ preventScroll: true });
  });
  nav.replaceChildren(...buttons, expand);
  const notes = {
    all: '관심 있는 목적을 골라보세요. 각 목적마다 4가지 비교·8곳을 담았어요.',
    free: '일반 관람 기준이에요. 유료 체험·상품과 예약 조건은 별도로 확인하세요.',
    family: '어린이 전용 체험과 일반 동반 방문을 구분했어요. 연령·보호자 조건을 확인하세요.',
    weather: '실내 관람 중심이에요. 입구·건물 사이 이동과 휴관일도 확인하세요.'
  };
  const note = document.getElementById('category-note');
  const noteText = notes[currentCategory] || '';
  note.textContent = t(noteText);
  note.hidden = !noteText || (currentCategory === 'all' && currentRegion !== 'all');
  mapCategory.value = currentCategory;
}
function renderList() {
  grid.replaceChildren(...filteredPairs.slice(0, listLimit).map(renderCard));
  const remaining = filteredPairs.length - listLimit;
  moreComparisons.hidden = remaining <= 0;
  moreComparisons.textContent = t('비교 {count}개 더 보기 · {remaining}개 남음', { count: Math.max(0, Math.min(4, remaining)), remaining: Math.max(0, remaining) });
  if (!filteredPairs.length) {
    const empty = element('div', 'empty-results');
    const category = categories.find(item => item.id === currentCategory);
    empty.append(element('h2', '', t('이 동네에는 ‘{category}’ 비교가 아직 없어요.', { category: category.label })));
    const reset = element('button', 'situation-link', '두 동네에서 찾기');
    reset.type = 'button';
    reset.addEventListener('click', () => {
      const url = new URL(location.href);
      url.searchParams.set('region', 'all');
      history.pushState(null, '', url);
      syncLocation();
    });
    empty.append(reset);
    grid.append(empty);
  }
  selectPlace(selectedPlace);
}
moreComparisons.addEventListener('click', () => {
  const next = filteredPairs[listLimit];
  listLimit += 4;
  renderList();
  if (next) document.getElementById(`comparison-${next.id}`)?.focus({ preventScroll: true });
});
mapCategory.addEventListener('change', () => chooseCategory(mapCategory.value));
function syncLocation() {
  const initialLocation = !locationReady;
  locationReady = true;
  const url = new URL(location.href);
  const requestedRegion = url.searchParams.get('region');
  const place = places.find(item => location.hash === `#place/${item.id}`);
  let region = ['anguk', 'seochon'].includes(requestedRegion) ? requestedRegion : 'all';
  let category = categories.some(item => item.id === url.searchParams.get('category')) ? url.searchParams.get('category') : 'all';
  const linkPair = pairs.find(item => item.id === url.searchParams.get('pair'));
  if (linkPair && category !== 'all' && linkPair.category !== category) {
    category = linkPair.category;
    url.searchParams.set('category', category);
    history.replaceState(history.state, '', url);
  }
  if (place && region !== 'all' && place.region !== region) {
    region = place.region;
    url.searchParams.set('region', region);
    history.replaceState(history.state, '', url);
  }
  if (currentRegion !== region || currentCategory !== category) {
    currentRegion = region;
    currentCategory = category;
    listLimit = 4;
    regionButtons.forEach(button => {
      const selected = button.dataset.region === region;
      button.classList.toggle('is-active', selected);
      button.setAttribute('aria-pressed', String(selected));
    });
    const visible = pairs.filter(pair => (region === 'all' || pair.region === region) && (category === 'all' || pair.category === category));
    filteredPairs = visible;
    if (!visible.some(pair => pair.placeIds.includes(selectedPlace))) selectedPlace = '';
    renderList();
    renderSituationNav();
    resultCount.textContent = t('{count}가지 비교 · {places}곳', { count: visible.length, places: new Set(visible.flatMap(pair => pair.placeIds)).size });
    window.AlleyMap?.render(visible);
    selectPlace(selectedPlace);
  }
  const showMap = url.searchParams.get('view') === 'map';
  const requestedPair = filteredPairs.find(pair => pair.id === url.searchParams.get('pair'));
  const pairId = requestedPair?.id || '';
  const wasMap = mapView;
  if (!wasMap && showMap) {
    listScroll = window.scrollY;
    mapReturnFocus = document.activeElement === document.body ? viewToggle : document.activeElement;
  }
  document.body.classList.toggle('is-map-view', showMap);
  viewToggle.textContent = t(showMap ? '비교 보기' : '지도 보기');
  viewToggle.setAttribute('aria-pressed', String(showMap));
  if (showMap && (!wasMap || pairId !== mapPair)) {
    if (requestedPair && !requestedPair.placeIds.includes(selectedPlace)) selectPlace('');
    window.AlleyMap?.show(pairId);
  }
  mapView = showMap;
  mapPair = pairId;
  if (wasMap && !showMap) window.AlleyMap?.show('');
  document.querySelectorAll('.place-choice').forEach(link => {
    const linkedPlace = places.find(item => item.id === link.dataset.place);
    link.href = detailUrl(linkedPlace, link.dataset.pair);
  });
  if (!initialLocation && wasMap !== showMap) requestAnimationFrame(() => {
    if (detail.open) return;
    if (showMap) document.getElementById('map-title').focus({ preventScroll: true });
    else {
      window.scrollTo({ top: listScroll, behavior: 'instant' });
      const target = mapReturnFocus?.isConnected && mapReturnFocus.getClientRects().length ? mapReturnFocus : viewToggle;
      target.focus({ preventScroll: true });
    }
  });
  if (place) openPlace(place);
  else {
    const wasOpen = detail.open;
    if (wasOpen) detail.close();
    document.body.classList.remove('detail-open');
    currentPlace = '';
    currentContext = '';
    document.title = t('AI 추천에 없는 안국·서촌');
    if (wasOpen) {
      const target = returnFocus?.isConnected ? returnFocus : document.querySelector('.map-selection-actions button');
      target?.focus({ preventScroll: true });
    }
    returnFocus = null;
  }
}

regionButtons.forEach(button => button.addEventListener('click', () => {
  const url = new URL(location.href);
  url.searchParams.set('region', button.dataset.region);
  url.searchParams.delete('pair');
  history.replaceState(null, '', url);
  mapPair = '';
  syncLocation();
}));
document.getElementById('close-detail').addEventListener('click', closePlace);
detail.addEventListener('cancel', event => { event.preventDefault(); closePlace(); });
window.addEventListener('popstate', syncLocation);
window.addEventListener('hashchange', syncLocation);
viewToggle.addEventListener('click', () => navigateView(!mapView));
window.addEventListener('alley:select', event => selectPlace(event.detail));
window.addEventListener('alley:detail', event => {
  const id = typeof event.detail === 'string' ? event.detail : event.detail.id;
  const place = places.find(item => item.id === id);
  if (place) showDetails(place, undefined, event.detail.pairId || mapPair);
});
window.addEventListener('alley:reset-map', () => {
  const url = new URL(location.href);
  url.searchParams.delete('pair');
  history.replaceState(history.state, '', url);
  mapPair = '';
});
window.addEventListener('alley:compare', event => jumpToPair(event.detail));
window.addEventListener('alley:focus-pair', event => navigateView(true, event.detail));
window.addEventListener('alley:region', event => {
  if (!['anguk', 'seochon'].includes(event.detail)) return;
  const url = new URL(location.href);
  url.searchParams.set('region', event.detail);
  url.searchParams.set('view', 'map');
  url.searchParams.delete('pair');
  history.pushState(null, '', url);
  syncLocation();
  document.getElementById('map-title').focus({ preventScroll: true });
});
document.getElementById('copy-link').addEventListener('click', async () => {
  const copiedId = currentPlace;
  const url = new URL(location.href);
  url.searchParams.delete('view');
  url.searchParams.delete('pair');
  try {
    await navigator.clipboard.writeText(url.href);
    if (currentPlace === copiedId) document.getElementById('copy-status').textContent = t('장소 링크를 복사했어요.');
  } catch {
    if (currentPlace !== copiedId) return;
    const input = document.getElementById('copy-fallback');
    input.hidden = false;
    input.value = url.href;
    input.focus();
    input.select();
    document.getElementById('copy-status').textContent = t('아래 링크를 길게 누르거나 복사해 주세요.');
  }
});
document.getElementById('copy-address').addEventListener('click', async () => {
  const text = document.getElementById('korean-address').textContent;
  const status = document.getElementById('address-copy-status');
  const fallback = document.getElementById('address-copy-fallback');
  fallback.hidden = true;
  try { await navigator.clipboard.writeText(text); status.textContent = t('한국어 주소를 복사했어요.'); }
  catch { fallback.hidden = false; fallback.value = text; fallback.focus(); fallback.select(); status.textContent = t('아래 주소를 길게 누르거나 복사해 주세요.'); }
});
window.addEventListener('alley:language-change', event => {
  // After a document reload, the close control should keep the newly chosen language.
  if (detail.open) history.replaceState({ ...history.state, detailFromApp: false }, '', location.href);
  try { sessionStorage.setItem('alley-language-view', JSON.stringify({ url: event.detail, selectedPlace, listLimit, listScroll, scrollY: window.scrollY })); } catch { /* URL preserves the current route. */ }
});
syncLocation();
try {
  const saved = JSON.parse(sessionStorage.getItem('alley-language-view') || 'null');
  sessionStorage.removeItem('alley-language-view');
  if (saved?.url === location.href) {
    listLimit = Math.max(4, Math.min(pairs.length, Number(saved.listLimit) || 4));
    listScroll = Number(saved.listScroll) || 0;
    renderList();
    if (filteredPairs.some(pair => pair.placeIds.includes(saved.selectedPlace))) selectPlace(saved.selectedPlace);
    if (!mapView && !detail.open) window.scrollTo({ top: Number(saved.scrollY) || 0, behavior: 'instant' });
  }
} catch { /* Storage is optional. */ }
})();
