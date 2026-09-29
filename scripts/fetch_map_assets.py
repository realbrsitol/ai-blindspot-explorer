"""Vendor Leaflet and cache a small, rate-limited public place lookup."""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import json
import time

root = Path(__file__).resolve().parents[1]
vendor = root / 'vendor' / 'leaflet'
vendor.mkdir(parents=True, exist_ok=True)
headers = {'User-Agent': 'AlleyGuide/1.0 (https://github.com/realbrsitol/ai-blindspot-explorer)'}
for name in ['leaflet.js', 'leaflet.css', 'images/layers.png', 'images/layers-2x.png', 'images/marker-icon.png', 'images/marker-icon-2x.png', 'images/marker-shadow.png', 'LICENSE']:
    target = vendor / name
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        continue
    path = name if name == 'LICENSE' else 'dist/' + name
    with urlopen(Request('https://unpkg.com/leaflet@1.9.4/' + path, headers=headers), timeout=30) as response:
        target.write_bytes(response.read())
print('Leaflet 1.9.4 downloaded', flush=True)

cache = root / 'scripts' / 'place_coordinates.json'
results = json.loads(cache.read_text(encoding='utf-8')) if cache.exists() else {}
queries = ['어니언 안국', '정독도서관', '스태픽스', '수성동 계곡', '런던베이글뮤지엄 안국', '배렴 가옥', '대오서점', '이상의 집']
for query in queries:
    if query in results:
        continue
    url = 'https://nominatim.openstreetmap.org/search?' + urlencode({'q': query, 'format': 'jsonv2', 'limit': 1, 'countrycodes': 'kr', 'viewbox': '126.94,37.60,127.01,37.56', 'bounded': 1})
    try:
        with urlopen(Request(url, headers=headers), timeout=15) as response:
            results[query] = json.load(response)
    except Exception as error:
        print(f'{query}: {error}', flush=True)
        results[query] = []
    cache.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    time.sleep(1.2)
for query, matches in results.items():
    for match in matches:
        print(query, match['lat'], match['lon'], match['display_name'], flush=True)
