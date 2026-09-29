"""Download reference photos, retaining credit and full composition."""
from pathlib import Path
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor
from html import unescape
import json
import re
from PIL import Image, ImageOps, ImageDraw
from collect_catalog_v26 import SOURCES, ROOT, DEST

PHOTO = ROOT / 'images' / 'places'
records = []
manifest_path = ROOT / 'research' / 'catalog_assets_v26.json'
previous = {row['id']: row for row in json.loads(manifest_path.read_text(encoding='utf-8'))} if manifest_path.exists() else {}
for key, source in SOURCES.items():
    if key.endswith('-location'):
        continue
    html = (DEST / f'{key}.html').read_text(encoding='utf-8')
    image_url = unescape(re.search(r'<meta property="og:image" content="([^"]+)"', html).group(1))
    if key == 'fritz':
        image_url = 'https://english.visitseoul.net/comm/getImage?srvcId=MEDIA&parentSn=23261&fileTy=MEDIA&fileNo=1'
    if key == 'park':
        image_url = 'https://english.visitseoul.net/comm/getImage?srvcId=MEDIA&parentSn=56153&fileTy=MEDIA&fileNo=1'
    if key == 'sangchon':
        image_url = 'https://english.visitseoul.net/comm/getImage?srvcId=MEDIA&parentSn=27460&fileTy=MEDIA&fileNo=1'
    coords_html = (DEST / 'sangchon-location.html').read_text(encoding='utf-8') if key == 'sangchon' else html
    coords = [float(v) for v in re.findall(r'"(?:latitude|longitude)"\s*:\s*"([0-9.]+)"', coords_html)]
    if not coords:
        coords = [float(v) for v in re.findall(r"var (?:lat|lng) = '([0-9.]+)'", coords_html)]
    if key == 'fritz':
        coords = [37.5777021, 126.9885964]
    if len(coords) != 2:
        raise ValueError(f'No unambiguous source coordinates: {key}')
    location_source = 'https://maps.app.goo.gl/ERXjkcyKVRqJkViFA' if key == 'fritz' else SOURCES['sangchon-location'] if key == 'sangchon' else source
    records.append({'id': key, 'source': source, 'imageUrl': image_url, 'coords': coords, 'locationSourceUrl': location_source, 'checkedAt': '2026-09-30', 'license': 'Reference photo; redistribution permission not established'})

def fetch(row):
    target = PHOTO / f"{row['id']}.jpg"
    if not target.exists() or previous.get(row['id'], {}).get('imageUrl') != row['imageUrl']:
        with urlopen(Request(row['imageUrl'], headers={'User-Agent': 'Mozilla/5.0'}), timeout=35) as response:
            if not response.headers.get('Content-Type', '').startswith('image/'):
                raise ValueError(f"Image unavailable: {row['id']}")
            target.write_bytes(response.read())
    return row['id']

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=4) as pool:
        for key in pool.map(fetch, records):
            print(key)
    (ROOT / 'research' / 'catalog_assets_v26.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    # Contact sheet for editorial photo identification; not a product asset.
    sheet = Image.new('RGB', (1000, 200 * ((len(records) + 3) // 4)), 'white')
    draw = ImageDraw.Draw(sheet)
    for index, row in enumerate(records):
        with Image.open(PHOTO / f"{row['id']}.jpg") as original:
            thumb = ImageOps.contain(original.convert('RGB'), (240, 165))
        x, y = index % 4 * 250, index // 4 * 200
        sheet.paste(thumb, (x, y + 20))
        draw.text((x + 4, y + 2), row['id'], fill='black')
    sheet.save(ROOT / 'research' / 'catalog-photos-v26.jpg')
