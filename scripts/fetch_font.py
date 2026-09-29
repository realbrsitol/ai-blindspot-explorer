"""Vendor Pretendard 1.3.9 and its SIL Open Font License from the upstream repo."""
from pathlib import Path
from urllib.request import Request, urlopen

root = Path(__file__).resolve().parents[1] / 'fonts'
root.mkdir(exist_ok=True)
base = 'https://raw.githubusercontent.com/orioncactus/pretendard/v1.3.9/'
for source, name in [
    ('packages/pretendard/dist/web/variable/woff2/PretendardVariable.woff2', 'PretendardVariable.woff2'),
    ('LICENSE', 'Pretendard-LICENSE.txt'),
]:
    with urlopen(Request(base + source, headers={'User-Agent': 'AlleyGuide/1.0'}), timeout=40) as response:
        data = response.read()
    (root / name).write_bytes(data)
    print(f'{name}: {len(data)} bytes')
