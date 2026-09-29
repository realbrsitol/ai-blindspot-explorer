"""Local reference photos from recorded official source pages (not open-license claims)."""
from pathlib import Path
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor
from html import unescape
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'research' / 'source-pages-v23'
PHOTO = ROOT / 'images' / 'places'
records = []
for key in ['tongin', 'tosokchon', 'hwangsaengga', 'changdeok', 'unhyeon', 'gogung', 'folk', 'mmca', 'gyeongbok']:
    html = (PAGES / f'{key}.html').read_text(encoding='utf-8')
    url = re.search(r'<meta property="og:image" content="([^"]+)"', html).group(1)
    coords = [float(v) for v in re.findall(r'"(?:latitude|longitude)"\s*:\s*"([0-9.]+)"', html)]
    records.append({'id': key, 'imageUrl': unescape(url), 'coords': coords})
records.extend([
    {'id': 'workshop', 'imageUrl': 'https://yeyak.seoul.go.kr/cmsdata/web_upload/svc/20240122/1705911054743XIUWJY3OQHE5U949ITJ2VDT25.JPG', 'coords': [37.58253, 126.98602]},
    {'id': 'bukchoncenter', 'imageUrl': 'https://english.visitseoul.net/comm/getImage?srvcId=MEDIA&parentSn=11859&fileTy=MEDIA&fileNo=1&thumbTy=L', 'coords': [37.57906987420643, 126.98642849263337]},
])

def fetch(record):
    target = PHOTO / f"{record['id']}.jpg"
    if not target.exists():
        with urlopen(Request(record['imageUrl'], headers={'User-Agent': 'Mozilla/5.0'}), timeout=30) as response:
            if not response.headers.get('Content-Type', '').startswith('image/'):
                raise ValueError(f"Not an image: {record['id']}")
            target.write_bytes(response.read())
    return f"{record['id']}: {target.stat().st_size} bytes"

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(fetch, records):
            print(result)
    (ROOT / 'research' / 'expansion_assets_v23.json').write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
