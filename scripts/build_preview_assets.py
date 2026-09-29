"""Build same-composition photo previews and a renamed OFL UI-font subset.

Run after editing visible Korean copy: python scripts/build_preview_assets.py
Requires Pillow, fontTools and brotli. Original source assets are never modified.
"""
from pathlib import Path
import json

from PIL import Image, ImageOps
from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
PHOTO_DIR = ROOT / 'images' / 'places'
OUTPUT = PHOTO_DIR / 'optimized'
OUTPUT.mkdir(exist_ok=True)
photos = []
for source in sorted(PHOTO_DIR.glob('*.jpg')):
    with Image.open(source) as original:
        normalized = ImageOps.exif_transpose(original).convert('RGB')
        item = {'id': source.stem, 'originalBytes': source.stat().st_size, 'previews': []}
        for limit in (480, 960):
            image = normalized.copy()
            image.thumbnail((limit, limit), Image.Resampling.LANCZOS)
            target = OUTPUT / f'{source.stem}-{limit}.webp'
            image.save(target, 'WEBP', quality=82, method=6)
            item['previews'].append({'file': target.relative_to(ROOT).as_posix(),
                                     'width': image.width, 'height': image.height,
                                     'bytes': target.stat().st_size})
        photos.append(item)

font_path = ROOT / 'fonts' / 'PretendardVariable.woff2'
font = TTFont(font_path, recalcTimestamp=False)
copy_files = [ROOT / 'index.html', *sorted((ROOT / 'js').glob('*.js')),
              *sorted((ROOT / 'css').glob('*.css'))]
characters = set(''.join(path.read_text(encoding='utf-8') for path in copy_files))
characters.update(chr(code) for code in range(0x20, 0x250))
characters.update(chr(code) for code in range(0x3131, 0x318F))
options = subset.Options()
options.flavor = 'woff2'
options.name_IDs = ['*']
options.name_legacy = True
options.name_languages = ['*']
subsetter = subset.Subsetter(options=options)
subsetter.populate(text=''.join(sorted(characters)))
subsetter.subset(font)
# The original's OFL reserves Pretendard. Name the derivative, preserving its license.
for record in font['name'].names:
    if record.nameID in (0, 13, 14):
        continue
    value = record.toUnicode().replace('Pretendard', 'Alley Sans').replace('Alley SansVariable', 'Alley Sans')
    if record.nameID in (6, 25):
        value = value.replace(' ', '')
    record.string = value.encode(record.getEncoding())
font.flavor = 'woff2'
font_output = ROOT / 'fonts' / 'AlleySans.woff2'
font.save(font_output)
manifest = {'font': {'originalBytes': font_path.stat().st_size,
                     'subsetBytes': font_output.stat().st_size,
                     'glyphs': len(font.getGlyphOrder())}, 'photos': photos}
(OUTPUT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(manifest, ensure_ascii=True))
