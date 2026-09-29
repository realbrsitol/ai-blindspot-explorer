"""Download the two verified, openly licensed reference photographs."""
from pathlib import Path
from urllib.request import Request, urlopen
import hashlib

ROOT = Path(__file__).resolve().parents[1] / 'images' / 'places'
ROOT.mkdir(parents=True, exist_ok=True)

for filename, local_name in [('Jeongdok_Library.jpg', 'jeongdok.jpg'), ('Giringyo.jpg', 'suseongdong.jpg')]:
    digest = hashlib.md5(filename.encode()).hexdigest()
    url = f'https://upload.wikimedia.org/wikipedia/commons/thumb/{digest[0]}/{digest[:2]}/{filename}/1280px-{filename}'
    request = Request(url, headers={'User-Agent': 'AlleyGuide/1.0 (place photo attribution in images/places/README.md)'})
    try:
        with urlopen(request, timeout=40) as response:
            data = response.read()
        (ROOT / local_name).write_bytes(data)
        print(f'{local_name}: {len(data)} bytes')
    except Exception as error:
        print(f'{local_name}: {error}')
