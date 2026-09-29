"""Fetch documentary images from the source pages recorded in js/data.js.

These are source-attributed reference assets, not a claim of an open license.
Existing Commons images retain their separate license records.
"""
from pathlib import Path
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor

ROOT = Path(__file__).resolve().parents[1] / 'images' / 'places'
ASSETS = {
    'onion.jpg': 'https://tong.visitkorea.or.kr/cms/resource/83/3079683_image2_1.jpg',
    'staffpicks.jpg': 'https://access.visitkorea.or.kr/bfvk_img/call?cmd=VIEW&id=b7370692-0db0-4cbb-a4a2-fa4aee7fe5bf&',
    'craft.jpg': 'https://tong.visitkorea.or.kr/cms/resource/28/2738528_image2_1.jpg',
    'baeryeom.jpg': 'https://www.heritage.go.kr/unisearch/images/register/thumb/1666942.jpg',
    'daeo.jpg': 'https://tong.visitkorea.or.kr/cms/resource/75/2947175_image2_1.jpg',
    'yisang.jpg': 'https://nationaltrustkorea.org/views/_layout/modified/img/own_1_01.jpg',
}

def fetch(item):
    name, url = item
    request = Request(url, headers={'User-Agent': 'AlleyGuide/1.0'})
    with urlopen(request, timeout=40) as response:
        if not response.headers.get('Content-Type', '').startswith('image/'):
            raise ValueError(f'{name}: response is not an image')
        content = response.read()
    (ROOT / name).write_bytes(content)
    return f'{name}: {len(content)} bytes'

if __name__ == '__main__':
    ROOT.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=3) as pool:
        for result in pool.map(fetch, ASSETS.items()):
            print(result)
