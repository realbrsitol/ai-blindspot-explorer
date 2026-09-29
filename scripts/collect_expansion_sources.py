"""Collect public source HTML for editorial review, never user data.

Downloads are confined to research/source-pages-v23. This does not publish assets.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'research' / 'source-pages-v23'
SOURCES = {
    'tongin': 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=79811',
    'tosokchon': 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=97919',
    'hwangsaengga': 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=86236',
    'changdeok': 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=94399',
    'unhyeon': 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=111253',
    'gogung': 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=106970',
    'folk': 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=110875',
    'mmca': 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=76101',
    'gyeongbok': 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=87740',
    'hanok': 'https://hanok.seoul.go.kr/front/util/bcgTour03.do?lang=KOR',
    'workshop': 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S240122144020674558',
    'bukchoncenter': 'https://english.visitseoul.net/PalaceArea/Bukchon-Traditional-Culture-Center-k/ENP018916',
    'unhyeon-notice': 'https://www.unhyeongung.or.kr/sub/notice_guide/notice.php?abmode=view&bfsort=ino&bsort=desc&code=B10&group=basic&no=1974',
}

def fetch(item):
    key, url = item
    try:
        if (DEST / f'{key}.html').exists():
            html = (DEST / f'{key}.html').read_text(encoding='utf-8')
        else:
            with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=30) as response:
                html = response.read().decode('utf-8', errors='replace')
            (DEST / f'{key}.html').write_text(html, encoding='utf-8')
        facts = [line.strip()[:500] for line in html.splitlines()
                 if re.search(r'latitude|longitude|mapx|mapy|image2_1|LatLng|coord', line, re.I)]
        return {'id': key, 'source': url, 'metadata': facts[:20]}
    except Exception as error:
        return {'id': key, 'source': url, 'error': str(error)}

if __name__ == '__main__':
    DEST.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(fetch, SOURCES.items()))
    (ROOT / 'research' / 'expansion_source_metadata.json').write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(records, ensure_ascii=True, indent=2))
