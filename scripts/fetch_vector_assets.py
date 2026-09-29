"""Vendor the pinned MapLibre browser bundle from its npm distribution."""
from pathlib import Path
from urllib.request import Request, urlopen
import json
import tarfile
import io

root = Path(__file__).resolve().parents[1]
version = '5.24.0'
headers = {'User-Agent': 'AlleyGuide/1.0 (https://github.com/realbrsitol/ai-blindspot-explorer)'}
with urlopen(Request(f'https://registry.npmjs.org/maplibre-gl/{version}', headers=headers), timeout=30) as response:
    metadata = json.load(response)
with urlopen(Request(metadata['dist']['tarball'], headers=headers), timeout=60) as response:
    archive = tarfile.open(fileobj=io.BytesIO(response.read()), mode='r:gz')
vendor = root / 'vendor' / 'maplibre'
vendor.mkdir(parents=True, exist_ok=True)
for source, target in [('package/dist/maplibre-gl.js', 'maplibre-gl.js'),
                       ('package/dist/maplibre-gl.css', 'maplibre-gl.css'),
                       ('package/LICENSE.txt', 'LICENSE.txt')]:
    member = archive.extractfile(source)
    (vendor / target).write_bytes(member.read())
    print(target, (vendor / target).stat().st_size)
