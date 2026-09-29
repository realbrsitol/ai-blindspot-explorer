window.createAlleyMap = () => {
  const { t } = window.AlleyI18n;
  const places = window.ALLEY_PLACES;
  const host = document.getElementById('map');
  const status = document.getElementById('map-status');
  const selection = document.getElementById('map-selection');
  const announcement = document.getElementById('map-announcement');
  const title = document.getElementById('map-title');
  const retry = document.getElementById('map-retry');
  const markers = new Map();
  let map;
  let visible = [];
  let focusedPair = '';
  let selectedId = '';
  let browsing = false;
  let comparing = false;
  let cameraPlaceId = '';
  let failed = false;
  let slow = false;
  let statusMessage = '';
  let libraryPromise;
  let initialization;
  let loadTimer;
  let resizeFrame;
  const lngLat = place => [place.coords[1], place.coords[0]];
  const emit = (name, id) => window.dispatchEvent(new CustomEvent(name, { detail: id }));
  const activePairs = () => focusedPair ? visible.filter(pair => pair.id === focusedPair) : visible;
  const activePlaces = () => [...new Set(activePairs().flatMap(pair => pair.placeIds))].map(id => places.find(place => place.id === id));
  const mapName = place => place.mapName || place.name;
  const overview = () => !focusedPair && new Set(visible.map(pair => pair.region)).size > 1;
  function node(tag, className, text) {
    const result = document.createElement(tag);
    if (className) result.className = className;
    if (text) result.textContent = t(text);
    return result;
  }
  function button(text, action, className = '') {
    const result = node('button', className, text);
    result.type = 'button';
    result.addEventListener('click', action);
    return result;
  }
  function fit(items = activePlaces(), maxZoom = 17) {
    if (!map || !items.length || !host.clientWidth || !host.clientHeight) return;
    const bounds = new maplibregl.LngLatBounds();
    items.forEach(place => bounds.extend(lngLat(place)));
    // The card has its own layout space. Padding protects name labels and controls.
    const side = Math.min(72, Math.floor(host.clientWidth * .21));
    const vertical = Math.min(58, Math.floor(host.clientHeight * .23));
    map.fitBounds(bounds, { padding: { top: vertical, bottom: vertical + 8, left: side, right: side }, maxZoom: Math.min(maxZoom, 16.5), duration: 0 });
  }
  function photo(place) {
    const image = window.AlleyMedia.create(place, { eager: true, onError: () => { image.hidden = true; } });
    image.className = 'map-card-photo';
    return image;
  }
  function updateChooserHint() {
    const hint = selection.querySelector('.map-scroll-hint');
    if (hint) {
      const hintHeight = hint.hidden ? 0 : hint.getBoundingClientRect().height + 8;
      hint.hidden = selection.scrollHeight - hintHeight <= selection.clientHeight + 1;
    }
  }
  function choosePlace(place) {
    browsing = false;
    comparing = false;
    if (overview()) { emit('alley:region', place.region); }
    cameraPlaceId = place.id;
    emit('alley:select', place.id);
    requestAnimationFrame(() => {
      if (map && !focusedPair) focusCameraPlace();
      selection.querySelector('.map-primary-action')?.focus({ preventScroll: true });
    });
  }
  function focusCameraPlace() {
    const place = activePlaces().find(item => item.id === cameraPlaceId);
    if (!map || !place || focusedPair) return false;
    map.easeTo({ center: lngLat(place), zoom: Math.max(map.getZoom(), 16), duration: 0 });
    return true;
  }
  function renderSelection() {
    // Preserve focus when a keyboard user changes the place using this dock.
    const focusKey = selection.contains(document.activeElement) ? document.activeElement.dataset.focusKey : '';
    selection.replaceChildren();
    const items = activePlaces();
    const place = items.find(item => item.id === selectedId);
    const pair = activePairs().find(item => item.placeIds.includes(selectedId));
    const matchingPairs = activePairs().filter(item => item.placeIds.includes(selectedId));
    const region = visible.length && visible.every(item => item.region === visible[0].region) ? visible[0].region : '';
    const regionName = t(region === 'anguk' ? '안국' : region === 'seochon' ? '서촌' : '안국 · 서촌');
    title.textContent = focusedPair ? t('두 곳의 위치 비교') : t('{region} 지도', { region: regionName });
    document.getElementById('map-reset').textContent = region ? t('{region} 전체', { region: regionName }) : t('전체 위치');
    selection.dataset.state = !place || browsing ? 'choices' : 'selected';
    if (!items.length) {
      selection.append(node('p', 'map-card-hours', '이 동네에는 선택한 목적의 비교가 아직 없어요. 위에서 목적을 바꾸거나 ‘전체’ 동네를 선택해 주세요.'));
      return;
    }
    if (place && comparing && !focusedPair) {
      const heading = node('div', 'map-chooser-heading');
      heading.append(node('h3', '', `${place.name} · ${t('비교 고르기')}`), button('돌아가기', () => { comparing = false; renderSelection(); }, 'map-text-button'));
      const list = node('div', 'map-comparison-options');
      matchingPairs.forEach(item => list.append(button(item.title, () => { comparing = false; emit('alley:focus-pair', item.id); }, 'map-place-option')));
      selection.append(heading, list);
      selection.querySelector('.map-place-option')?.focus({ preventScroll: true });
      return;
    }
    if (!place || browsing) {
      const heading = node('div', 'map-chooser-heading');
      heading.append(node('h3', '', focusedPair ? '어느 곳을 살펴볼까요?' : '장소 선택'), node('span', 'map-place-count', t('{count}곳', { count: items.length })));
      if (place) heading.append(button('선택한 장소', () => {
        browsing = false;
        renderSelection();
        selection.querySelector('.map-primary-action')?.focus({ preventScroll: true });
      }, 'map-text-button'));
      const list = node('div', 'map-place-options');
      const placeOption = item => {
        const option = button(item.name, () => choosePlace(item), 'map-place-option');
        option.dataset.focusKey = `choose-${item.id}`;
        option.setAttribute('aria-pressed', String(item.id === selectedId));
        return option;
      };
      if (overview()) {
        ['seochon', 'anguk'].forEach(regionId => {
          const group = node('div', 'map-neighborhood-options');
          const heading = node('h4', '', regionId === 'anguk' ? '안국' : '서촌');
          heading.id = `map-options-${regionId}`;
          group.setAttribute('role', 'group');
          group.setAttribute('aria-labelledby', heading.id);
          group.append(heading, ...items.filter(item => item.region === regionId).map(placeOption));
          list.append(group);
        });
      } else list.append(...items.map(placeOption));
      const scrollHint = node('p', 'map-scroll-hint', '목록을 위아래로 밀어 더 볼 수 있어요');
      scrollHint.hidden = true;
      selection.append(heading, list, scrollHint);
      requestAnimationFrame(updateChooserHint);
      if (focusKey) [...selection.querySelectorAll('[data-focus-key]')].find(item => item.dataset.focusKey === focusKey)?.focus({ preventScroll: true });
      return;
    }
    if (focusedPair) {
      const tabs = node('div', 'map-pair-switcher');
      tabs.setAttribute('role', 'group');
      tabs.setAttribute('aria-label', t('비교 중인 두 장소'));
      items.forEach(item => {
        const option = button(item.name, () => emit('alley:select', item.id));
        option.dataset.focusKey = item.id;
        option.setAttribute('aria-pressed', String(item.id === selectedId));
        tabs.append(option);
      });
      selection.append(tabs);
    }
    if (pair) {
      const choice = focusedPair ? window.ALLEY_CHOICE(place, pair) : place;
      const summary = node('div', 'map-card-summary');
      const copy = node('div', 'map-card-copy');
      copy.append(node('h3', '', place.name), node('p', 'map-card-facts', choice.cost));
      summary.append(photo(place), copy);
      if (!focusedPair) summary.append(button('변경', () => {
        browsing = true;
        renderSelection();
        selection.querySelector('.map-place-option')?.focus({ preventScroll: true });
      }, 'map-change-place'));
      const hours = node('p', 'map-card-hours', `${choice.schedule.replace(/\n/g, ' · ')}${choice.closure ? ` · ${choice.closure}` : ''}`);
      const actions = node('div', 'map-selection-actions');
      const primary = button('자세히 보기', () => emit('alley:detail', { id: place.id, pairId: focusedPair || (matchingPairs.length === 1 ? pair.id : '') }), 'map-primary-action');
      primary.dataset.focusKey = 'detail';
      const compare = button(focusedPair ? '비교 내용 보기' : matchingPairs.length > 1 ? '비교 고르기' : '두 곳 비교', () => {
        if (!focusedPair && matchingPairs.length > 1) { comparing = true; renderSelection(); }
        else emit(focusedPair ? 'alley:compare' : 'alley:focus-pair', pair.id);
      });
      compare.dataset.focusKey = 'compare';
      actions.append(primary, compare);
      selection.append(summary, hours);
      if (place.locationSource === 'legacy') selection.append(node('p', 'map-location-note', '대략적 위치 · 정확한 입구는 별도 확인'));
      selection.append(actions);
    }
    if (focusKey) [...selection.querySelectorAll('[data-focus-key]')].find(item => item.dataset.focusKey === focusKey)?.focus({ preventScroll: true });
  }
  function groupPosition(items) {
    const points = items.map(place => map.project(lngLat(place)));
    return { x: points.reduce((sum, point) => sum + point.x, 0) / points.length,
      y: points.reduce((sum, point) => sum + point.y, 0) / points.length };
  }
  function groupLabel(items) {
    if (items.length === 1) return mapName(items[0]);
    const region = t(items.every(item => item.region === items[0].region) ? (items[0].region === 'anguk' ? '안국' : '서촌') : '주변');
    return `${region} · ${window.AlleyI18n.lang === 'en' ? items.length : t('{count}곳', { count: items.length })}`;
  }
  function markerGroups(items) {
    // Overview groups are intentional navigation to a neighborhood. Within a
    // neighborhood, each real place owns exactly one geographic point.
    if (overview()) return ['seochon', 'anguk'].map(region => items.filter(place => place.region === region)).filter(group => group.length);
    return items.map(place => [place]);
  }
  function placeLabels(groups) {
    const placed = [];
    const positions = new Map();
    const points = groups.filter(items => items.length === 1).map(items => ({ place: items[0], point: groupPosition(items) }));
    points.sort((a, b) => Number(b.place.id === selectedId) - Number(a.place.id === selectedId));
    points.forEach(({ place, point }) => {
      const width = Math.min(250, Math.ceil([...mapName(place)].reduce((sum, char) => sum + (/[^\u0000-\u00ff]/.test(char) ? 14 : 8), 14)));
      const height = 28;
      const candidates = [
        { x: point.x - width / 2, y: point.y - height - 11 },
        { x: point.x - width / 2, y: point.y + 11 },
        { x: point.x + 13, y: point.y - height / 2 },
        { x: point.x - width - 13, y: point.y - height / 2 }
      ].map(box => ({ ...box, width, height }));
      const area = (a, b) => Math.max(0, Math.min(a.x + a.width, b.x + b.width) - Math.max(a.x, b.x)) *
        Math.max(0, Math.min(a.y + a.height, b.y + b.height) - Math.max(a.y, b.y));
      const score = box => {
        const inside = area(box, { x: 6, y: 6, width: host.clientWidth - 12, height: host.clientHeight - 36 });
        const collisions = placed.reduce((sum, other) => sum + area(box, other), 0);
        const pins = points.filter(other => other.place.id !== place.id).reduce((sum, other) => sum + area(box,
          { x: other.point.x - 12, y: other.point.y - 12, width: 24, height: 24 }), 0);
        return (width * height - inside) * 5 + collisions * 4 + pins * 4;
      };
      candidates.sort((a, b) => score(a) - score(b));
      const best = candidates[0];
      const colliding = points.length > 4 && place.id !== selectedId && score(best) > 100;
      if (!colliding) placed.push(best);
      positions.set(place.id, { ...best, colliding });
    });
    return positions;
  }
  function refreshPins() {
    markers.forEach(({ element, items }) => {
      const selected = items.some(place => place.id === selectedId);
      element.classList.toggle('is-selected', selected);
      element.style.zIndex = selected ? '3' : '2';
      const control = element.querySelector('button');
      if (items.length === 1) control.setAttribute('aria-pressed', String(selected));
    });
  }
  function drawMarkers() {
    if (!map) return;
    const groups = markerGroups(activePlaces());
    const labels = placeLabels(groups);
    const next = new Set();
    let lostFocus = false;
    groups.forEach(items => {
      const key = items.map(item => item.id).sort().join('|');
      next.add(key);
      const position = groupPosition(items);
      const coords = items.length === 1 ? lngLat(items[0]) : map.unproject([position.x, position.y]);
      let record = markers.get(key);
      if (!record) {
        const element = node('div', 'alley-marker');
        const control = button('', () => {
          if (items.length === 1) { browsing = false; comparing = false; emit('alley:select', items[0].id); }
          else emit('alley:region', items[0].region);
        }, 'map-pin');
        const label = node('span', 'map-pin-label', groupLabel(items));
        const dot = node('span', 'map-pin-dot');
        dot.setAttribute('aria-hidden', 'true');
        control.append(dot, label);
        control.setAttribute('aria-label', items.length > 1 ? t('{region} {count}곳 지도 열기', { region: t(items[0].region === 'anguk' ? '안국' : '서촌'), count: items.length }) : items[0].name + (items[0].locationSource === 'legacy' ? ` · ${t('대략적 위치')}` : ''));
        control.addEventListener('click', event => event.stopPropagation());
        control.addEventListener('keydown', event => event.stopPropagation());
        element.classList.toggle('is-cluster', items.length > 1);
        element.classList.toggle('is-approximate', items.length === 1 && items[0].locationSource === 'legacy');
        element.append(control);
        const marker = new maplibregl.Marker({ element, anchor: 'center' }).setLngLat(coords).addTo(map);
        // MapLibre supplies a generic button role; the nested native button owns interaction.
        element.removeAttribute('role');
        element.removeAttribute('aria-label');
        record = { marker, element, items };
        markers.set(key, record);
      } else record.marker.setLngLat(coords);
      if (items.length === 1) {
        const box = labels.get(items[0].id);
        const label = record.element.querySelector('.map-pin-label');
        label.style.left = `${box.x - position.x + 22}px`;
        label.style.top = `${box.y - position.y + 22}px`;
        label.style.width = `${box.width}px`;
        label.classList.toggle('is-colliding', box.colliding);
      }
      const inView = position.x >= 0 && position.x <= host.clientWidth && position.y >= 0 && position.y <= host.clientHeight;
      record.element.style.visibility = inView ? '' : 'hidden';
      record.element.querySelector('button').tabIndex = inView ? 0 : -1;
    });
    markers.forEach((record, key) => {
      if (!next.has(key)) {
        lostFocus ||= record.element.contains(document.activeElement);
        record.marker.remove();
        markers.delete(key);
      }
    });
    refreshPins();
    if (lostFocus && !selection.contains(document.activeElement)) {
      (selection.querySelector('button') || map.getCanvas()).focus({ preventScroll: true });
    }
  }
  function updateStatus(message = statusMessage) {
    statusMessage = message;
    status.textContent = t(!navigator.onLine ? '인터넷 연결이 끊겼어요. 장소 정보의 주소를 이용해 주세요.' : message);
    retry.hidden = !failed && !(slow && map);
  }
  function loadLibrary() {
    if (libraryPromise) return libraryPromise;
    const asset = (id, tag, url) => new Promise((resolve, reject) => {
      const existing = document.getElementById(id);
      if (existing?.dataset.loaded === 'true') { resolve(); return; }
      const resource = document.createElement(tag);
      resource.id = id;
      if (tag === 'link') { resource.rel = 'stylesheet'; resource.href = url; }
      else { resource.src = url; resource.async = true; }
      resource.onload = () => { resource.dataset.loaded = 'true'; resolve(); };
      resource.onerror = () => { resource.remove(); reject(new Error('Map asset unavailable')); };
      document.head.append(resource);
    });
    libraryPromise = Promise.allSettled([
      asset('map-library-style', 'link', 'vendor/maplibre/maplibre-gl.css'),
      window.maplibregl ? Promise.resolve() : asset('map-library-script', 'script', 'vendor/maplibre/maplibre-gl.js')
    ]).then(results => {
      if (results.some(result => result.status === 'rejected')) {
        libraryPromise = undefined;
        throw new Error('Map library unavailable');
      }
    });
    return libraryPromise;
  }
  function startLoading() {
    slow = false;
    clearTimeout(loadTimer);
    updateStatus('지도 불러오는 중…');
    loadTimer = setTimeout(() => {
      if (!map?.loaded()) {
        slow = true;
        updateStatus('지도를 불러오는 데 시간이 걸려요. 아래 장소 목록은 계속 이용할 수 있어요.');
      }
    }, 15000);
  }
  async function ensure() {
    if (!host.clientWidth || !host.clientHeight) return false;
    if (map) return true;
    if (initialization) return initialization;
    initialization = initialize().finally(() => { initialization = undefined; });
    return initialization;
  }
  async function initialize() {
    startLoading();
    try {
      await loadLibrary();
      // A user may return to the list while the assets are downloading.
      if (!host.clientWidth || !host.clientHeight) { clearTimeout(loadTimer); return false; }
      const response = await fetch('maps/alley-style.json?v=22');
      if (!response.ok) throw new Error('Map style unavailable');
      const style = window.AlleyI18n.mapStyle(await response.json());
      if (!host.clientWidth || !host.clientHeight) { clearTimeout(loadTimer); return false; }
      map = new maplibregl.Map({ container: host, style, center: [126.975, 37.579],
        zoom: 14, minZoom: 11, maxZoom: 19, maxPitch: 0, dragRotate: false, pitchWithRotate: false,
        touchPitch: false, attributionControl: false, localIdeographFontFamily: 'Yu Gothic, Microsoft YaHei, Malgun Gothic, sans-serif',
        locale: { 'NavigationControl.ZoomIn': t('확대'), 'NavigationControl.ZoomOut': t('축소'),
          'AttributionControl.ToggleAttribution': t('지도 데이터 출처'), 'Map.Title': t('안국·서촌 장소 지도') } });
      map.touchZoomRotate.disableRotation();
      map.scrollZoom.disable();
      map.keyboard.disableRotation();
      map.addControl(new maplibregl.ScaleControl({ maxWidth: 80, unit: 'metric' }), 'bottom-left');
      map.addControl(new maplibregl.AttributionControl({ compact: true }), 'bottom-right');
      map.on('moveend', drawMarkers);
      map.on('dragstart', () => { cameraPlaceId = ''; });
      map.on('zoomstart', event => { if (event.originalEvent) cameraPlaceId = ''; });
      map.on('error', () => {
        failed = true;
        clearTimeout(loadTimer);
        updateStatus('배경 지도 일부를 불러오지 못했어요. 장소 정보와 주소는 볼 수 있어요.');
      });
      map.on('load', () => {
        clearTimeout(loadTimer);
        slow = false;
        if (!failed) updateStatus('');
        drawMarkers();
      });
      map.on('webglcontextlost', () => {
        failed = true;
        updateStatus('지도 표시가 중단됐어요. 다시 불러오거나 장소 주소를 확인해 주세요.');
      });
      return true;
    } catch {
      clearTimeout(loadTimer);
      map?.remove();
      map = undefined;
      failed = true;
      updateStatus('지도를 표시하지 못했어요. 다시 불러오거나 아래에서 장소를 골라 주소를 확인해 주세요.');
      return false;
    }
  }
  async function showMap() {
    renderSelection();
    if (await ensure() && host.clientWidth && host.clientHeight) {
      map.resize();
      if (!focusCameraPlace()) fit();
      drawMarkers();
    }
  }
  retry.addEventListener('click', () => {
    if (initialization) return;
    clearTimeout(loadTimer);
    markers.forEach(record => record.marker.remove());
    markers.clear();
    map?.remove();
    map = undefined;
    failed = false;
    slow = false;
    showMap();
  });
  document.getElementById('map-zoom-in').addEventListener('click', () => { cameraPlaceId = ''; map?.zoomIn({ duration: 0 }); });
  document.getElementById('map-zoom-out').addEventListener('click', () => { cameraPlaceId = ''; map?.zoomOut({ duration: 0 }); });
  window.addEventListener('offline', () => updateStatus());
  window.addEventListener('online', () => {
    if (map?.loaded() && !failed) { slow = false; updateStatus(''); return; }
    failed = true;
    updateStatus('인터넷에 다시 연결됐어요. 지도를 다시 불러와 주세요.');
  });
  document.getElementById('map-reset').addEventListener('click', () => {
    focusedPair = '';
    selectedId = '';
    browsing = false;
    cameraPlaceId = '';
    emit('alley:select', '');
    emit('alley:reset-map');
    showMap();
  });
  new ResizeObserver(() => {
    cancelAnimationFrame(resizeFrame);
    resizeFrame = requestAnimationFrame(async () => {
      if (!host.clientWidth || !host.clientHeight) return;
      const existing = Boolean(map);
      if (await ensure() && host.clientWidth && host.clientHeight) {
        map.resize();
        if ((!existing || focusedPair) && !focusCameraPlace()) fit();
        drawMarkers();
      }
    });
  }).observe(host);
  new ResizeObserver(updateChooserHint).observe(selection);
  return {
    render(items) {
      visible = items;
      focusedPair = '';
      cameraPlaceId = '';
      browsing = false;
      comparing = false;
      if (!activePlaces().some(place => place.id === selectedId)) selectedId = '';
      showMap();
    },
    show(pairId) {
      cameraPlaceId = '';
      focusedPair = visible.some(pair => pair.id === pairId) ? pairId : '';
      browsing = false;
      comparing = false;
      if (!activePlaces().some(place => place.id === selectedId)) selectedId = '';
      showMap();
    },
    select(id) {
      if (id !== cameraPlaceId) cameraPlaceId = '';
      selectedId = id;
      browsing = false;
      comparing = false;
      drawMarkers();
      renderSelection();
      const place = places.find(item => item.id === id);
      announcement.textContent = place ? t('{name} 선택. 지도 아래에 장소 정보가 표시됩니다.', { name: place.name }) : '';
    }
  };
};
