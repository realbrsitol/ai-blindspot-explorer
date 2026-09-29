"""Save public place source pages and metadata for local editorial work."""
from pathlib import Path
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor
from html import unescape
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'research' / 'source-pages-v26'
KTO = 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId='
SOURCES = {
    'chebu': 'https://french.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=60424',
    'jalppajin': KTO + '60129',
    'gippen': 'https://english.visitseoul.net/restaurants/GIPPEN/ENPl3xyt0',
    'sujebi': 'https://english.visitseoul.net/area/Samcheong-dongSujebi/ENPqgbap0',
    'london': KTO + '191147',
    'osulloc': KTO + '1573739',
    'chatteul': 'https://english.visitseoul.net/PalaceArea/Cha-teul/ENP139gfg',
    'fritz': 'https://english.visitseoul.net/hallyu/Walking-Through-Wonseo-dong-Alleyways/30586',
    'teatherapy': KTO + '188076',
    'park': 'https://english.visitseoul.net/museum/ParkNoSoo-Museum/ENP042350',
    'daelim': KTO + '89412',
    'hakgojae': 'https://english.visitseoul.net/attractions/hakgojae-gallery/ENP001871',
    'boan': KTO + '175341',
    'baekinje': KTO + '64978',
    'sangchon': 'https://english.visitseoul.net/editorspicks/Sangchonjae-Cultural-Space/ENN037775',
    'sajik': KTO + '86285',
    'donglim': KTO + '97767',
    'sangchon-location': 'https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=175347',
}

def fetch(item):
    key, url = item
    file = DEST / f'{key}.html'
    try:
        if not file.exists():
            with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=35) as response:
                file.write_text(response.read().decode('utf-8', errors='replace'), encoding='utf-8')
        html = file.read_text(encoding='utf-8')
        metadata = [line.strip()[:1500] for line in html.splitlines() if re.search(r'og:image|latitude|longitude|LatLng|mapx|mapy|mapX|mapY|mapLat|mapLng|lat:|lng:|getImage|imgSrc', line)]
        return {'id': key, 'source': url, 'metadata': metadata[:45]}
    except Exception as error:
        return {'id': key, 'source': url, 'error': str(error)}

if __name__ == '__main__':
    DEST.mkdir(exist_ok=True)
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(fetch, SOURCES.items()))
    (ROOT / 'research' / 'catalog_source_metadata_v26.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for row in rows:
        print(row['id'], row['error'] if 'error' in row else f"{len(row['metadata'])} metadata lines")
