"""Compile the v26 editorial catalog and merge its local translations.

Run after editing catalog_v26_content.py; then rebuild preview assets/font.
This is a content compiler, not an application test runner.
"""
import json
from pathlib import Path
from catalog_v26_content import L, PLACES, PAIRS, CATEGORIES

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ['name', 'category', 'visitWhen', 'cost', 'schedule', 'closure', 'description', 'address', 'hours', 'useMode', 'visitTip', 'accessSummary', 'access', 'unknown', 'checkLabel', 'photoLabel']
assets = {row['id']: row for row in json.loads((ROOT / 'research/catalog_assets_v26.json').read_text(encoding='utf-8'))}
locales = {code: json.loads((ROOT / f'js/locales/{code}.json').read_text(encoding='utf-8')) for code in ['en', 'ja', 'zh-CN']}
ui = json.loads((ROOT / 'js/locales/ui.json').read_text(encoding='utf-8'))

def ui_copy(value):
    ui[value[0]] = value[1:]
    return value[0]

source_labels = {
    'kto': ui_copy(L('한국관광공사 장소 안내 | Korea Tourism Organization place guide | 韓国観光公社スポット案内 | 韩国旅游公社地点信息')),
    'sto': ui_copy(L('서울관광재단 장소 안내 | Seoul Tourism Organization place guide | ソウル観光財団スポット案内 | 首尔旅游财团地点信息')),
}
location_labels = {
    'kto': ui_copy(L('한국관광공사 장소 좌표 | KTO place coordinates | 韓国観光公社の地点座標 | 韩国旅游公社地点坐标')),
    'sto': ui_copy(L('서울관광재단 장소 좌표 | Seoul Tourism place coordinates | ソウル観光財団の地点座標 | 首尔旅游财团地点坐标')),
    'operator': ui_copy(L('운영자 연결 지도 | Map linked by the operator | 運営者が案内する地図 | 运营方链接地图')),
}
photo_labels = {
    'kto': ui_copy(L('한국관광공사 게시 · 원본 표기 유지 | Published by KTO · original markings retained | 韓国観光公社掲載・原本の表記を維持 | 韩国旅游公社刊载，保留原图标识')),
    'sto': ui_copy(L('서울관광재단 게시 · 원본 표기 유지 | Published by Seoul Tourism · original markings retained | ソウル観光財団掲載・原本の表記を維持 | 首尔旅游财团刊载，保留原图标识')),
}
review_fields = ui_copy(L('공개 방문 안내·주소·대표 위치 | Published visitor guide, address and representative location | 公開利用案内・住所・代表位置 | 公开到访信息、地址及代表位置'))
review_note = ui_copy(L('자료 열람일 기준 · 당일 운영·가격·예약은 방문 전 확인 | Sources read on the stated date; confirm same-day operation, prices and bookings | 記載日に資料を閲覧。当日の営業・価格・予約は訪問前に確認 | 以资料查阅日期为准，到访前确认当日营业、价格及预约'))

compiled_places = []
for item in PLACES:
    asset = assets[item['id']]
    kind = 'sto' if 'visitseoul.net' in asset['source'] else 'kto'
    row = {key: value[0] for key, value in item['copy'].items()}
    row.update({key: value for key, value in item.items() if key != 'copy'})
    row.update(englishName=item['copy']['name'][1], source=asset['source'], sourceLabel=source_labels[kind],
               coords=asset['coords'], locationSource=location_labels['operator' if item['id'] == 'fritz' else 'kto' if item['id'] == 'sangchon' else kind],
               locationSourceUrl=asset['locationSourceUrl'], photoSource=asset['source'],
               photoAuthor=photo_labels[kind], photoDate='촬영일 미상',
               image=f"images/places/{item['id']}.jpg", preview=f"images/places/optimized/{item['id']}-480.webp",
               largePreview=f"images/places/optimized/{item['id']}-960.webp",
               imageAlt=f"{row['name']} · {row['photoLabel']}", hoursSummary=f"{row['schedule']} · {row['closure']}",
               checkUrl=row.get('extraSource', asset['source']),
               review={'checkedAt': '2026-09-30', 'fields': review_fields, 'note': review_note})
    if asset['source'].startswith('https://english.'):
        row['englishSource'] = asset['source']
    if item['id'] == 'jalppajin':
        # Source address variants differ. Use the existing approximate-pin presentation.
        row['locationSource'] = 'legacy'
    compiled_places.append(row)
    for index, (code, locale) in enumerate(locales.items(), 1):
        locale['places'][item['id']] = [item['copy'][field][index] for field in FIELDS]

gift = next(pair for pair in PAIRS if pair['id'] == 'tea-coffee-gifts')
for id, visit in [
    ('osulloc', L('찻잎·차 상품 고르기 | Choose packaged tea products | 茶葉・茶商品を選ぶ | 挑选茶叶及茶商品')),
    ('fritz', L('원두·드립백 선물 고르기 | Choose beans and drip-bag gifts | 豆・ドリップバッグを選ぶ | 挑选咖啡豆及挂耳礼品')),
]:
    gift['choices'][id] = {
        'visitWhen': visit,
        'cost': L('선물 상품별 유료 · 재고 확인 | Gifts priced per product · confirm stock | 商品別有料・在庫確認 | 礼品按商品计价，请确认库存'),
        'useMode': L('상품 구매 · 매장 재고·포장 확인 | Buy products; confirm branch stock and packaging | 商品購入・店舗在庫と包装を確認 | 购买商品，确认门店库存及包装'),
    }
compiled_pairs = []
for item in PAIRS:
    row = {key: value for key, value in item.items() if key not in ['copy', 'choices']}
    row.update({key: value[0] for key, value in item['copy'].items()})
    row['shortTitle'] = row['title']
    row['regionLabel'] = '안국' if row['region'] == 'anguk' else '서촌'
    row['choices'] = {id: {key: value[0] for key, value in choice.items()} for id, choice in item['choices'].items()}
    if item['id'] == 'free-life-hanok':
        row['choices']['bukchoncenter']['checkUrl'] = 'https://english.visitseoul.net/tours/Bukchon_/872'
    compiled_pairs.append(row)
    for index, (code, locale) in enumerate(locales.items(), 1):
        copy = {key: value[index] for key, value in item['copy'].items()}
        copy['shortTitle'] = copy['title']
        if item['choices']:
            copy['choices'] = {id: {key: value[index] for key, value in choice.items()} for id, choice in item['choices'].items()}
        locale['pairs'][row['id']] = copy

categories = [{'id': id, 'label': ui_copy(label)} for id, label in CATEGORIES]
for copy in [
    L('관심 있는 목적을 골라보세요. 각 목적마다 4가지 비교·8곳을 담았어요. | Choose a purpose: each has 4 comparisons and 8 distinct places. | 目的を選ぶと、それぞれ4組・8か所を比較できます。 | 选择出游目的，每类有4组对比、8个不同地点。'),
    L('모든 카테고리 | All categories | すべてのカテゴリー | 所有分类'),
    L('카테고리 접기 | Show fewer categories | カテゴリーを閉じる | 收起分类'),
    L('일반 관람 기준이에요. 유료 체험·상품과 예약 조건은 별도로 확인하세요. | Free refers to general visits. Check paid activities, purchases and booking rules separately. | 無料は一般見学が対象。有料体験・商品・予約条件は別途確認。 | 免费指一般参观，收费体验、商品及预约规则需另查。'),
    L('어린이 전용 체험과 일반 동반 방문을 구분했어요. 연령·보호자 조건을 확인하세요. | Dedicated children’s activities and general family visits differ. Check age and guardian rules. | 子ども専用体験と一般の同伴見学を区別しています。年齢・保護者条件を確認。 | 已区分儿童专属体验与一般亲子参观，请确认年龄和监护人条件。'),
    L('실내 관람 중심이에요. 입구·건물 사이 이동과 휴관일도 확인하세요. | Mainly indoor visits. Check outdoor access routes and closure days too. | 屋内鑑賞が中心。入口・棟間の移動と休館日も確認。 | 以室内参观为主，也请确认入口、楼间路线及休馆日。'),
    L('서로 다른 카테고리에 같은 장소가 포함될 수 있어요. | A place may appear in more than one category. | 同じ場所が複数のカテゴリーに含まれる場合があります。 | 同一地点可能出现在不同分类中。'),
]:
    ui_copy(copy)

data = {'places': compiled_places, 'categories': categories, 'pairs': compiled_pairs}
script = '// Generated by scripts/build_catalog_v26.py. Edit scripts/catalog_v26_content.py.\n(() => {\n  const catalog = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n'
script += """  window.ALLEY_PLACES.push(...catalog.places);
  window.ALLEY_CATEGORIES = catalog.categories;
  // Preserve existing shared comparison IDs while giving exhibitions a clear home.
  window.BLIND_SPOT_PAIRS.find(pair => pair.id === 'baeryeom').category = 'art';
  window.BLIND_SPOT_PAIRS.push(...catalog.pairs);
  // The overview samples different purposes before showing second pairs.
  const categoryOrder = new Map(catalog.categories.map((category, index) => [category.id, index]));
  const withinCategory = new Map();
  const order = new Map(window.BLIND_SPOT_PAIRS.map(pair => {
    const rank = withinCategory.get(pair.category) || 0;
    withinCategory.set(pair.category, rank + 1);
    return [pair.id, rank * catalog.categories.length + categoryOrder.get(pair.category)];
  }));
  window.BLIND_SPOT_PAIRS.sort((a, b) => order.get(a.id) - order.get(b.id));
})();
"""
(ROOT / 'js/catalog.js').write_text(script, encoding='utf-8')
for code, locale in locales.items():
    (ROOT / f'js/locales/{code}.json').write_text(json.dumps(locale, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
(ROOT / 'js/locales/ui.json').write_text(json.dumps(ui, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Compiled {len(compiled_places)} new places, {len(compiled_pairs)} new comparisons, {len(categories)-1} categories in four languages.')
