"""Editorial copy: Korean / English / Japanese / Simplified Chinese.

Facts derive from research/catalog_assets_v26.json and CATEGORY_EXPANSION_V26.md.
Translations are authored locally; no visitor data or remote translation API.
"""
def L(text):
    values = [value.strip() for value in text.split('|')]
    if len(values) != 4:
        raise ValueError('Copy requires four languages: ' + text)
    return values

PROFILES = {
    'food': {
        'useMode': L('메뉴별 주문·결제 | Order and pay by dish | メニューごとに注文・会計 | 按菜品点单付款'),
        'accessSummary': L('좌석·출입구 단차는 매장에 확인 | Ask about seating and entrance steps | 座席と入口の段差は店舗へ確認 | 请向店家确认座位和入口台阶'),
        'access': L('휠체어·유모차 진입과 화장실 동선은 현장 확인이 필요합니다. | Ask the restaurant about wheelchair, stroller and restroom access. | 車いす・ベビーカーの入店とトイレへの経路は店舗へご確認ください。 | 轮椅、婴儿车及洗手间通行路线需向店家确认。'),
        'unknown': L('당일 대기·가격, 재료와 알레르기 대응, 휴식시간, 무단차 좌석 | Same-day queues, prices, ingredients, dietary accommodation, breaks and step-free seating | 当日の待ち時間・価格・食材・アレルギー対応・休憩時間・段差のない座席 | 当日排队、价格、食材、过敏需求、午休及无台阶座位'),
        'checkLabel': L('메뉴·운영 안내 | Menu & opening information | メニュー・営業案内 | 菜单及营业信息'),
    },
    'cafe': {
        'useMode': L('음료·디저트 주문 · 좌석 이용 조건 확인 | Order drinks or sweets; check seating rules | 飲み物・お菓子を注文。座席利用条件を確認 | 点饮品或甜点，确认座位使用规则'),
        'accessSummary': L('좌식·의자석과 출입구 단차 확인 | Check floor/table seating and entrance steps | 座敷・椅子席と入口の段差を確認 | 确认地席、椅子座位及入口台阶'),
        'access': L('좌석과 층별 이동 경로는 매장마다 다릅니다. 필요한 좌석·무단차 경로를 방문 전에 문의하세요. | Seating and floor access differ. Ask about the seat and step-free route you need. | 座席や階ごとの経路は異なります。必要な席と段差のない経路を事前にお問い合わせください。 | 座位和楼层通行情况各异，请提前确认所需座位及无台阶路线。'),
        'unknown': L('현재 가격·좌석·대기, 카페인·알레르기, 계단 없는 이용, 상품 재고 | Current prices, seats, queues, caffeine, allergens, step-free access and stock | 現在の価格・空席・待ち時間・カフェイン・アレルギー・段差のない利用・在庫 | 当前价格、座位、排队、咖啡因、过敏原、无台阶通行及库存'),
        'checkLabel': L('매장 방문 안내 | Café visitor information | 店舗の利用案内 | 咖啡馆到访信息'),
    },
    'exhibit': {
        'useMode': L('전시 일정·관람권·입장 마감 확인 후 관람 | Check exhibition dates, tickets and last entry | 展示日程・チケット・最終入場を確認して鑑賞 | 确认展期、门票和最晚入场时间后参观'),
        'accessSummary': L('전시실별 계단·엘리베이터 동선 확인 | Check stairs and lift access by gallery | 展示室ごとの階段・エレベーター経路を確認 | 确认各展厅的楼梯及电梯路线'),
        'access': L('전시실과 건물에 따라 단차·계단이 있을 수 있습니다. 필요한 이동 지원을 운영기관에 문의하세요. | Routes depend on the gallery and building. Ask the operator about steps and mobility assistance. | 建物や展示室によって段差・階段があります。必要な移動支援は運営者へご相談ください。 | 不同展厅及建筑可能有台阶或楼梯，所需通行协助请向运营方确认。'),
        'unknown': L('현재 전시·요금·휴관, 촬영 규칙, 연령 제한, 무단차 경로 | Current exhibition, admission, closures, photo rules, age limits and step-free routes | 現在の展示・料金・休館・撮影規則・年齢制限・段差のない経路 | 当前展览、票价、休馆、拍摄规则、年龄限制及无台阶路线'),
        'checkLabel': L('전시·관람 안내 | Exhibitions & visiting | 展示・観覧案内 | 展览及参观信息'),
    },
    'hanok': {
        'useMode': L('일반 개방 구역 관람 · 해설·체험은 별도 조건 | Visit open areas; tours and activities have separate rules | 一般公開エリアを見学。解説・体験は別条件 | 参观开放区域，导览和体验另有规定'),
        'accessSummary': L('한옥 문턱·마당과 개방 구역 확인 | Check hanok thresholds, courtyards and open areas | 韓屋の敷居・庭と公開範囲を確認 | 确认韩屋门槛、庭院及开放区域'),
        'access': L('마당과 실내의 단차가 다릅니다. 유모차·휠체어로 방문할 경우 이용 가능한 구역을 문의하세요. | Indoor and courtyard thresholds differ. Ask which areas accommodate strollers or wheelchairs. | 庭と室内では段差が異なります。ベビーカー・車いすで利用できる範囲をご確認ください。 | 庭院和室内门槛情况不同，婴儿车或轮椅可进入的区域请提前确认。'),
        'unknown': L('당일 개방 구역·해설 잔여석, 프로그램 비용·언어, 무단차 경로 | Open areas, tour availability, activity fees, languages and step-free routes | 当日の公開範囲・解説空席・体験料金・言語・段差のない経路 | 当日开放范围、导览名额、活动费用、语言及无台阶路线'),
        'checkLabel': L('관람·프로그램 안내 | Visits & programs | 見学・プログラム案内 | 参观及活动信息'),
    },
    'park': {
        'useMode': L('공원 개방 구간 산책 · 문화유산 내부는 별도 | Walk in open park areas; heritage interiors are separate | 公園の公開区間を散策。文化遺産内部は別条件 | 在公园开放区域散步，文化遗产内部另有规定'),
        'accessSummary': L('야외 경사·보행로와 현장 통제 확인 | Check outdoor slopes, paths and restrictions | 屋外の坂・歩道と現地規制を確認 | 确认室外坡度、步道及现场限制'),
        'access': L('공원 안에서도 경사·단차와 개방 구간이 다릅니다. 우천·공사·행사 시 현장 안내를 따르세요. | Slopes, steps and open paths vary. Follow notices for rain, works or events. | 園内でも坂・段差・公開区間が異なります。雨・工事・行事の際は現地案内に従ってください。 | 园内坡度、台阶和开放路线不同，雨天、施工或活动时请遵从现场提示。'),
        'unknown': L('당일 통제·행사, 화장실 개방, 무단차 산책 구간 | Same-day restrictions, events, restroom access and step-free paths | 当日の規制・行事・トイレ開放・段差のない散策区間 | 当日限制、活动、洗手间开放及无台阶步道'),
        'checkLabel': L('공원 이용 안내 | Park visitor information | 公園の利用案内 | 公园使用信息'),
    },
}

PLACES = []
def place(id, region, profile, name, category, visit, cost, schedule, closure, description, address, tip, photo, **extra):
    row = dict(PROFILES[profile])
    row.update(name=L(name), category=L(category), visitWhen=L(visit), cost=L(cost), schedule=L(schedule), closure=L(closure), description=L(description), address=[address[0], address[1], address[1], address[1]], visitTip=L(tip), photoLabel=L(photo))
    row['hours'] = [f"{row['schedule'][i]}. {row['closure'][i]}." for i in range(4)]
    PLACES.append({'id': id, 'region': region, 'copy': row, **extra})

place('chebu', 'seochon', 'food',
      '체부동잔치집돼지갈비 | Chebudong Janchijip Dwaejigalbi | チェブドンジャンチジプ・テジカルビ | 体府洞宴会猪排骨',
      '식당 · 돼지갈비 | Restaurant · grilled pork | 食堂・豚カルビ | 餐厅·烤猪排骨',
      '양념갈비를 구워 함께 먹기 | Share grilled marinated ribs | 味付けカルビを焼いて分け合う | 分享现烤腌制排骨',
      '메뉴별 결제 · 주문 단위 확인 | Pay by dish · check minimum order | メニュー別会計・注文単位を確認 | 按菜品付款，确认起订份数',
      '10시 개점 안내 · 종료 재확인 | Listed opening 10:00 · confirm closing | 10時開店の案内・閉店時刻は要確認 | 公示10时开门，关门时间需确认',
      '휴무·주문 마감 매장 확인 | Confirm closures and last orders | 休業・最終注文は店舗へ確認 | 向店家确认休息日及最后点单',
      '세종마을 음식문화거리의 양념갈비 식당입니다. 메밀국수 한 그릇과, 테이블에서 고기를 구워 나누는 식사를 비교해 보세요. | A marinated-rib restaurant on Sejong Village Food Street. Compare a shared grill meal with a bowl of buckwheat noodles. | 世宗マウル飲食店街の味付けカルビ店。焼肉を分け合う食事と、そば一杯の食事を比較できます。 | 位于世宗村美食街的腌排骨店，可与一碗荞麦面的用餐方式作比较。',
      ('서울 종로구 자하문로1길 24', '24 Jahamun-ro 1-gil, Jongno-gu, Seoul'),
      '이름이 비슷한 국수집과 구분해 주소를 확인하세요. 공식 관광 자료의 마감시간이 달라 늦은 방문은 전화 확인이 필요합니다. | Check the address: a similarly named noodle restaurant is different. Tourism listings disagree on closing times; call for late visits. | 同名に近い麺料理店とは別店舗です。観光資料で閉店時刻が異なるため、遅い時間は電話確認を。 | 请核对地址，勿与名称相近的面馆混淆。官方旅游资料的关门时间不一致，较晚到访请先致电。',
      '식당 외관과 간판 | Restaurant exterior and sign | 店舗外観と看板 | 餐厅外观及招牌', phone='02-722-3555')

place('jalppajin', 'seochon', 'food',
      '잘빠진메밀 서촌 | Jalppajin Memil Seochon | ジャルパジンメミル西村 | Jalppajin荞麦面西村',
      '식당 · 메밀국수 | Restaurant · buckwheat noodles | 食堂・そば | 餐厅·荞麦面',
      '메밀국수와 수육으로 식사하기 | Eat buckwheat noodles and sliced pork | そばとゆで豚で食事 | 荞麦面配白切肉',
      '메뉴별 결제 · 현재 가격 확인 | Pay by dish · confirm current prices | メニュー別会計・現在価格を確認 | 按菜品付款，确认当前价格',
      '월–토 11–21:30 · 일 21시 종료 | Mon–Sat 11:00–21:30 · Sun until 21:00 | 月～土11～21:30・日曜21時まで | 周一至六11–21:30，周日至21时',
      '휴식시간·주문 마감 별도 확인 | Confirm breaks and last orders | 休憩時間・最終注文は別途確認 | 午休及最后点单需另行确认',
      '메밀국수와 수육 등을 내는 서촌 본점입니다. 양념을 비비거나 국물과 먹는 면 요리를 고를 수 있습니다. | The Seochon main branch serves buckwheat noodles and sliced pork, with seasoned or broth-based noodle options. | 西村本店ではそばやゆで豚を提供。タレで和える麺と、スープで食べる麺を選べます。 | 西村本店供应荞麦面及白切肉，可选择拌面或汤面。',
      ('서울 종로구 자하문로 41-1', '41-1 Jahamun-ro, Jongno-gu, Seoul'),
      '관광공사 한글 주소와 영문 주소가 다릅니다. 서촌 본점의 최신 입구를 매장에 확인하세요. 메밀면도 육수·양념의 채식·알레르기 대응은 별도 확인입니다. | The KTO Korean and English addresses differ. Confirm the Seochon entrance with the shop. Buckwheat noodles do not establish vegetarian or allergen-free broth and sauces. | 観光公社の韓英住所表記が異なります。西村本店の入口を確認し、だし・タレの菜食やアレルギー対応もお問い合わせください。 | 旅游公社的韩英地址不一致，请向西村本店核实入口；荞麦面不代表汤底及酱料符合素食或过敏需求。',
      '공식 안내의 매장 외관 · 현재 입구 확인 | Listed exterior · confirm current entrance | 掲載の外観・現在の入口を確認 | 官方所载外观，当前入口需确认', phone='0507-1403-1214', extraSource='https://www.instagram.com/jalppajin_seochon')

place('gippen', 'anguk', 'food',
      '깊은 | GIPPEN | GIPPEN（キプン） | GIPPEN',
      '식당 · 국밥·숯불 요리 | Restaurant · soup & charcoal grill | 食堂・スープご飯・炭火料理 | 餐厅·汤饭及炭烤',
      '엉겅퀴 해장국과 숯불 요리 고르기 | Choose thistle soup or charcoal dishes | アザミのスープや炭火料理を選ぶ | 选择蓟菜汤或炭烤菜品',
      '메뉴별 결제 · 현재 메뉴 확인 | Pay by dish · check the current menu | メニュー別会計・最新メニュー確認 | 按菜品付款，查看当前菜单',
      '관광 안내 11:30–22시 | Listed hours 11:30–22:00 | 観光案内11:30～22時 | 旅游资料11:30–22时',
      '휴식시간·예약 가능 여부 확인 | Check breaks and reservations | 休憩時間・予約可否を確認 | 确认午休及预约情况',
      '안국역 남쪽 인사동16길의 국밥·숯불 요리 식당입니다. 관광재단은 영어 메뉴와 비건 선택지를 안내하지만, 가능한 메뉴는 주문 전에 확인하세요. | A soup and charcoal-grill restaurant south of Anguk Station. Seoul Tourism lists English menus and vegan options; confirm the available dishes before ordering. | 安国駅南側のスープご飯・炭火料理店。観光財団は英語メニューとヴィーガンの選択肢を紹介していますが、注文前に内容を確認してください。 | 位于安国站南侧的汤饭及炭烤餐厅。首尔旅游财团介绍其有英文菜单和纯素选项，请点单前确认具体菜品。',
      ('서울 종로구 인사동16길 6', '6 Insadong 16-gil, Jongno-gu, Seoul'),
      '안국역 남측 권역입니다. 비건 메뉴 유무와 별개로 알레르기·교차 접촉 대응, 예약 좌석은 매장에 확인하세요. | This is south of Anguk Station. Confirm allergens, cross-contact handling and reservations separately from vegan menu availability. | 安国駅南側です。ヴィーガンメニューの有無とは別に、アレルギー・調理時の接触・予約席をご確認ください。 | 地处安国站南侧。纯素选项不等于满足过敏需求，请另行确认交叉接触及预约座位。',
      '요리 참고 사진 · 메뉴 구성은 확인 | Reference dish photo · confirm menu | 料理の参考写真・メニューは要確認 | 菜品参考照片，实际菜单需确认')

place('sujebi', 'anguk', 'food',
      '삼청동수제비 | Samcheong-dong Sujebi | 三清洞スジェビ | 三清洞面片汤',
      '식당 · 수제비 | Restaurant · hand-torn dough soup | 食堂・すいとん | 餐厅·面片汤',
      '수제비와 감자전으로 식사하기 | Eat dough soup and potato pancakes | すいとんとじゃがいもチヂミ | 面片汤配土豆煎饼',
      '메뉴별 결제 · 현재 가격 확인 | Pay by dish · confirm prices | メニュー別会計・価格確認 | 按菜品付款，确认价格',
      '11시 개점 · 종료시간 확인 | Opens 11:00 · confirm closing | 11時開店・閉店時刻は要確認 | 11时开门，关门时间需确认',
      '임시 휴무·주문 마감 확인 | Confirm temporary closures and last orders | 臨時休業・最終注文を確認 | 确认临时休息及最后点单',
      '삼청로 북쪽의 수제비 식당입니다. 안국역 바로 앞은 아니므로 지도에서 위치를 보고, 면 요리와 국밥 중 원하는 한 끼를 고르세요. | A dough-soup restaurant farther north on Samcheong-ro. Check its location before choosing between dough soup and rice soup near Anguk Station. | 三清路北側のすいとん店。安国駅前ではないため、地図で位置を確認してスープご飯と比べましょう。 | 位于三清路北段的面片汤店，并非安国站门口，先查看地图再与汤饭作比较。',
      ('서울 종로구 삼청로 101-1', '101-1 Samcheong-ro, Jongno-gu, Seoul'),
      '서울관광재단은 20시, 다른 관광 안내는 21시 종료로 기재합니다. 늦게 방문한다면 확인하고, 밀·조개류 등 재료도 주문 전 문의하세요. | Seoul Tourism lists closing at 20:00, another tourism listing at 21:00. Confirm late visits and ingredients such as wheat or shellfish. | 観光財団は20時、別の観光資料は21時閉店と記載。遅い時間と小麦・貝類などの食材は事前確認を。 | 首尔旅游财团记载20时结束，其他资料记载21时。较晚到访及小麦、贝类等食材请先确认。',
      '식당 외관 | Restaurant exterior | 店舗外観 | 餐厅外观', phone='02-735-2965')

place('london', 'anguk', 'cafe',
      '런던베이글뮤지엄 안국점 | London Bagel Museum Anguk | ロンドンベーグルミュージアム安国店 | 伦敦贝果博物馆安国店',
      '베이커리 · 베이글 | Bakery · bagels | ベーカリー・ベーグル | 烘焙店·贝果',
      '베이글을 골라 먹거나 포장하기 | Choose bagels to eat or take away | ベーグルを選んで店内・持ち帰り | 选购贝果堂食或打包',
      '베이글·음료별 결제 | Bagels and drinks priced separately | ベーグル・飲み物は別料金 | 贝果及饮品分别计价',
      '기본 08–18시 | Usually 08:00–18:00 | 基本08～18時 | 通常08–18时',
      '대기 접수·품절·마감 확인 | Check queue registration, stock and cutoff | 待機受付・売切れ・締切を確認 | 确认排队登记、售罄及截止时间',
      '안국의 베이글 전문점입니다. 원하는 메뉴를 사는 것이 목적인지, 차를 마시며 머무는 것이 목적인지 비교해 선택하세요. | A bagel specialist in Anguk. Decide whether your priority is a particular baked item or spending time over tea. | 安国のベーグル専門店。目当てのパンを買うことと、お茶を飲んで過ごすことを比べて選べます。 | 安国的贝果专门店，可比较购买心仪面包与坐下喝茶两种目的。',
      ('서울 종로구 북촌로4길 20', '20 Bukchon-ro 4-gil, Jongno-gu, Seoul'),
      '현장·원격 대기 방식과 포장 가능 여부는 매장 안내를 확인하세요. 이 앱은 실시간 대기 순번이나 재고를 제공하지 않습니다. | Check current waitlist and takeaway rules. This app does not show live queue numbers or stock. | 店頭・遠隔の待機受付と持ち帰り条件を確認。このアプリはリアルタイムの順番・在庫を提供しません。 | 请查看现场或远程排队及打包规定。本应用不提供实时排队号码或库存。',
      '베이글 진열 · 현재 재고 아님 | Bagel display · not live stock | ベーグル陳列・現在の在庫ではありません | 贝果陈列，并非实时库存')

place('osulloc', 'anguk', 'cafe',
      '오설록 티하우스 북촌점 | Osulloc Tea House Bukchon | オソルロック・ティーハウス北村店 | OSULLOC北村茶屋',
      '티하우스 · 차·디저트 | Tea house · tea & sweets | ティーハウス・茶・お菓子 | 茶屋·茶及甜点',
      '차와 차를 활용한 디저트 즐기기 | Enjoy tea and tea-based sweets | お茶と茶のスイーツを楽しむ | 品茶及茶味甜点',
      '음료·디저트·상품별 결제 | Drinks, sweets and products priced separately | 飲み物・お菓子・商品は別料金 | 饮品、甜点及商品分别计价',
      '관광 안내 11–20시 | Listed hours 11:00–20:00 | 観光案内11～20時 | 旅游资料11–20时',
      '층별 운영·주문 마감 확인 | Check hours by floor and last orders | 階別の営業時間・最終注文を確認 | 确认各楼层营业及最后点单',
      '북촌로의 티하우스로 차 음료, 디저트와 차 상품을 만날 수 있습니다. 카페 이용과 여행 선물 구매는 각각의 비용을 확인하세요. | A Bukchon-ro tea house with drinks, sweets and tea products. Café orders and gifts have separate costs. | 北村路のティーハウス。茶の飲み物・お菓子・商品があり、飲食とお土産の料金は別です。 | 位于北村路的茶屋，提供茶饮、甜点及茶产品，堂食与购买伴手礼费用不同。',
      ('서울 종로구 북촌로 45', '45 Bukchon-ro, Jongno-gu, Seoul'),
      '체험·티코스는 일반 음료 주문과 다를 수 있습니다. 예약, 카페인과 선물 포장·재고를 확인하세요. | Tea courses may differ from ordinary drink orders. Check bookings, caffeine, gift packaging and stock. | ティーコースは通常の飲み物注文と別条件の場合があります。予約・カフェイン・包装・在庫を確認。 | 茶席或体验可能与普通点单规则不同，请确认预约、咖啡因、礼品包装及库存。',
      '티하우스 건물 외관 | Tea-house exterior | ティーハウス外観 | 茶屋建筑外观', phone='070-4121-2019', extraSource='https://access.visitkorea.or.kr/food/detail.do?cotId=2f8ed3f7-9ab0-489e-a03c-20a9d5700bdc')

place('chatteul', 'anguk', 'cafe',
      '차마시는뜰 | Chamasineun Tteul | チャマシヌントゥル | 喝茶的庭院',
      '찻집 · 한옥·전통차 | Tea house · hanok & traditional tea | 茶屋・韓屋・伝統茶 | 茶馆·韩屋及传统茶',
      '한옥에서 전통차와 다과 즐기기 | Have traditional tea and sweets in a hanok | 韓屋で伝統茶とお菓子 | 在韩屋品尝传统茶及茶点',
      '차·다과별 결제 | Tea and sweets priced separately | 茶・お菓子は別料金 | 茶及茶点分别计价',
      '10–19시 · 주문 마감 18:10 안내 | 10:00–19:00 · listed last order 18:10 | 10～19時・最終注文18:10の案内 | 10–19时，公示最后点单18:10',
      '화요일 휴무 · 명절 확인 | Closed Tuesdays · check holidays | 火曜休業・祝祭期は確認 | 周二休息，节假日需确认',
      '한옥의 낮은 상에서 전통차와 다과를 즐기는 찻집입니다. 좌식이 편한지, 의자석이 필요한지 먼저 생각해 보세요. | A hanok tea house with low-table seating and traditional tea. Consider whether floor seating suits you or you need a chair. | 韓屋の低いテーブルで伝統茶を楽しむ茶屋。座敷が快適か、椅子席が必要かを考えて選びましょう。 | 在韩屋低桌席品尝传统茶的茶馆，请先考虑地席是否合适或是否需要椅子座位。',
      ('서울 종로구 북촌로11나길 26', '26 Bukchon-ro 11na-gil, Jongno-gu, Seoul'),
      '북촌 주거 골목의 관광 방문시간·현장 표지를 먼저 확인하세요. 매장 영업시간이 골목 출입 가능 시간을 뜻하지는 않습니다. | Check residential-lane visiting restrictions and signs first. Shop hours do not establish when tourists may enter nearby lanes. | 北村住宅路地の観光訪問時間と標識を確認。店舗の営業時間と路地への訪問可能時間は異なります。 | 请先查看北村住宅巷道的游客到访限制和标志。商店营业时间不等于巷道可通行时间。',
      '한옥 입구 · 야간 참고 사진 | Hanok entrance · evening reference photo | 韓屋入口・夜の参考写真 | 韩屋入口，夜间参考照片', phone='0507-1304-7029')

place('fritz', 'anguk', 'cafe',
      '프릳츠 원서 | Fritz Coffee Wonseo | フリッツ・コーヒー苑西店 | Fritz Coffee苑西店',
      '카페 · 커피·빵 | Café · coffee & bread | カフェ・コーヒー・パン | 咖啡馆·咖啡及面包',
      '원서동에서 커피와 빵 즐기기 | Have coffee and bread in Wonseo-dong | 苑西洞でコーヒーとパン | 在苑西洞喝咖啡吃面包',
      '음료·빵·상품별 결제 | Drinks, bread and products priced separately | 飲み物・パン・商品は別料金 | 饮品、面包及商品分别计价',
      '관광 안내 10–21시 · 매장 재확인 | Tourism listing 10:00–21:00 · confirm with café | 観光案内10～21時・店舗へ再確認 | 旅游资料10–21时，请向店家核实',
      '임시 휴무·주문 마감 확인 | Confirm closures and last orders | 臨時休業・最終注文を確認 | 确认临时休息及最后点单',
      '아라리오뮤지엄 옆 원서점에서 커피와 빵을 주문할 수 있습니다. 미술관 관람과 카페 이용은 별개의 선택입니다. | Order coffee and bread at the Wonseo branch beside Arario Museum. Museum admission and café use are separate. | アラリオミュージアム横の苑西店でコーヒーとパンを注文できます。美術館鑑賞とカフェ利用は別です。 | 位于Arario博物馆旁的苑西店供应咖啡及面包，博物馆门票与咖啡馆消费相互独立。',
      ('서울 종로구 율곡로 83', '83 Yulgok-ro, Jongno-gu, Seoul'),
      '공식 매장 안내에서 원서점을 선택하세요. 선물용 원두·드립백은 해당 지점 재고를 확인하고, 미술관 개관시간을 카페 시간으로 적용하지 마세요. | Select Wonseo on the official store page. Confirm beans and drip-bag stock at this branch; museum hours do not establish café hours. | 公式店舗案内で苑西店を選択。豆・ドリップバッグの在庫を確認し、美術館の時間をカフェに当てはめないでください。 | 官方门店页请选择苑西店，确认本店咖啡豆及挂耳包库存，勿以博物馆开放时间作为咖啡馆时间。',
      '한옥 공간 외관 | Hanok-space exterior | 韓屋スペース外観 | 韩屋空间外观', phone='02-747-8101', extraSource='https://fritz.co.kr/store.html')

place('teatherapy', 'anguk', 'cafe',
      '티테라피 | Tea Therapy | ティーテラピー | Tea Therapy茶疗',
      '찻집 · 블렌딩 차 | Tea house · blended tea | 茶屋・ブレンド茶 | 茶馆·调配茶',
      '허브·과일차를 취향대로 고르기 | Choose herbal or fruit tea by taste | 好みでハーブ・果実茶を選ぶ | 按口味挑选草本茶或果茶',
      '차·상품 유료 · 체험 별도 확인 | Tea and products charged · check activities separately | 茶・商品は有料・体験は別途確認 | 茶及商品收费，体验需另行确认',
      '월–토 10–21시 · 일 20시 종료 | Mon–Sat 10:00–21:00 · Sun until 20:00 | 月～土10～21時・日曜20時まで | 周一至六10–21时，周日至20时',
      '계절별 변경·체험 일정 확인 | Check seasonal changes and activity dates | 季節変更・体験日程を確認 | 确认季节变化及体验日程',
      '윤보선길의 찻집으로 허브·과일을 활용한 차와 차 상품을 소개합니다. 맛과 향을 중심으로 고르고, 원데이 차 프로그램은 별도 문의하세요. | A Yunboseon-gil tea house offering herbal and fruit teas and tea products. Choose by flavour; ask separately about one-day tea programs. | 尹潽善通りの茶屋でハーブ・果実茶と茶商品を紹介。味や香りで選び、一日体験は別途お問い合わせください。 | 尹潽善路的茶馆供应草本及果茶、茶产品，按口味和香气选择，单日茶体验请另行咨询。',
      ('서울 종로구 윤보선길 74', '74 Yunboseon-gil, Jongno-gu, Seoul'),
      '차 수업·족욕의 당일 운영, 비용과 예약을 문의하세요. 차의 건강 효과를 이 앱에서 판단하거나 보장하지 않습니다. | Ask about tea classes, foot-bath availability, fees and reservations. This app does not assess or guarantee health effects of tea. | 茶の講座・足湯の開催、料金、予約を確認。このアプリは茶の健康効果を判断・保証しません。 | 请确认茶课、足浴当日开放、费用及预约，本应用不判断或保证茶的健康效果。',
      '찻집 외관 | Tea-house exterior | 茶屋外観 | 茶馆外观', phone='02-730-7507', extraSource='https://english.visitseoul.net/restaurants/Four-wellness-cafes-in-Seoul/ENN032527')

place('park', 'seochon', 'exhibit',
      '종로구립 박노수미술관 | Park No-soo Museum | 朴魯寿美術館 | 朴鲁寿美术馆',
      '미술관 · 작가의 집 | Art museum · artist home | 美術館・画家の家 | 美术馆·画家故居',
      '작가의 집과 한국화 살펴보기 | Explore an artist home and Korean painting | 画家の家と韓国画を見る | 参观画家故居及韩国画',
      '성인 3,000원 안내 · 감면 확인 | Listed adult admission ₩3,000 · check concessions | 大人3,000ウォンの案内・割引確認 | 公示成人3,000韩元，优惠需确认',
      '기본 10–18시 | Usually 10:00–18:00 | 基本10～18時 | 通常10–18时',
      '월요일·1월 1일·설·추석 휴관 안내 | Closed Mondays, Jan 1, Seollal and Chuseok | 月曜・1月1日・旧正月・秋夕休館の案内 | 公示周一、1月1日、春节及中秋休馆',
      '화가 박노수가 살던 집에서 작품과 정원을 함께 보는 미술관입니다. 여러 층의 기획전시를 보는 일정과 작은 작가의 집을 둘러보는 일정을 비교하세요. | An art museum in painter Park No-soo’s former home, with works and a garden. Compare an artist-house visit with a multi-floor temporary exhibition. | 画家・朴魯寿の旧宅で作品と庭を見学する美術館。企画展を巡る鑑賞と作家の家の見学を比べましょう。 | 在画家朴鲁寿故居欣赏作品及庭院的美术馆，可与多层临时展览的参观方式比较。',
      ('서울 종로구 옥인1길 34', '34 Ogin 1-gil, Jongno-gu, Seoul'),
      '외관 사진에 계단이 보입니다. 내부 진입, 정원 이용과 전시 교체 기간을 확인하세요. | The exterior photo shows steps. Confirm interior access, garden use and exhibition-change closures. | 外観写真には階段があります。内部への経路、庭の利用、展示替え休館を確認してください。 | 外观照片可见台阶，请确认室内入口、庭院使用及换展休馆。',
      '작가의 집 외관 · 계단 있는 진입부 | Artist-home exterior · stepped approach | 作家の家の外観・階段のある入口 | 画家故居外观，入口有台阶', phone='02-2148-4171')

place('daelim', 'seochon', 'exhibit',
      '대림미술관 | Daelim Museum | 大林美術館 | 大林美术馆',
      '미술관 · 기획전시 | Art museum · temporary exhibitions | 美術館・企画展 | 美术馆·临时展览',
      '사진·디자인 등 기획전시 고르기 | Choose a photography or design exhibition | 写真・デザインなどの企画展を選ぶ | 选择摄影、设计等临时展览',
      '전시별 요금·예매 확인 | Fees and booking depend on exhibition | 展示別の料金・予約確認 | 票价及预约依展览而定',
      '현재 전시의 관람시간 확인 | Check current exhibition hours | 現在の展示の観覧時間を確認 | 查看当前展览开放时间',
      '월요일 등 휴관·전시 교체 확인 | Check Monday and exhibition-change closures | 月曜などの休館・展示替えを確認 | 确认周一等休馆日及换展安排',
      '통의동의 기획전 중심 미술관입니다. 전시마다 주제, 관람료와 운영시간이 바뀔 수 있어 현재 열리는 전시부터 살펴보세요. | A museum in Tongui-dong focused on temporary exhibitions. Themes, admission and hours can change, so start with the current exhibition. | 通義洞の企画展中心の美術館。テーマ・料金・時間が変わるため、開催中の展示から確認しましょう。 | 通义洞以临时展览为主的美术馆，主题、票价及开放时间可能变化，请先查看当前展览。',
      ('서울 종로구 자하문로4길 21', '21 Jahamun-ro 4-gil, Jongno-gu, Seoul'),
      '서울숲의 디뮤지엄과 다른 장소입니다. 이전 관광자료의 관람료 대신 대림미술관의 현재 전시 예매 조건을 확인하세요. | This is not D Museum in Seoul Forest. Use current Daelim exhibition ticket rules rather than older tourism prices. | ソウルの森のDミュージアムとは別館です。古い観光資料の料金ではなく、現在の企画展の予約条件を確認。 | 此处不同于首尔林的D Museum，请以大林美术馆当前展览售票规则为准，勿套用旧旅游票价。',
      '미술관 외관 · 현재 전시 사진 아님 | Museum exterior · not the current exhibition | 美術館外観・現在の展示写真ではありません | 美术馆外观，并非当前展览', phone='02-720-0667', extraSource='https://www.daelimmuseum.org/')

place('hakgojae', 'anguk', 'exhibit',
      '학고재 | Hakgojae Gallery | 学古斎ギャラリー | 学古斋画廊',
      '갤러리 · 현대미술 | Gallery · contemporary art | ギャラリー・現代美術 | 画廊·当代艺术',
      '한옥과 현대 전시실에서 작품 보기 | See art in hanok and modern galleries | 韓屋と現代的な展示室で鑑賞 | 在韩屋及现代展厅欣赏作品',
      '일반 전시 무료 안내 · 현재 전시 확인 | General exhibitions listed free · check current show | 一般展示無料の案内・開催展を確認 | 一般展览公示免费，请确认当前展览',
      '기본 10–18시 | Usually 10:00–18:00 | 基本10～18時 | 通常10–18时',
      '일·월요일 휴관 안내 · 전시 교체 확인 | Listed closed Sun & Mon · check changeovers | 日・月曜休館の案内・展示替え確認 | 公示周日、周一休馆，请确认换展',
      '삼청로의 한옥 본관과 현대식 전시 공간을 가진 갤러리입니다. 큰 미술관의 여러 전시와, 갤러리의 현재 전시를 비교해 보세요. | A Samcheong-ro gallery with hanok and contemporary spaces. Compare one gallery show with the multiple exhibitions of a large museum. | 三清路に韓屋の本館と現代的な空間を持つギャラリー。大きな美術館の複数展と、一つの画廊の展示を比較できます。 | 三清路上拥有韩屋主馆和现代空间的画廊，可与大型美术馆的多项展览比较。',
      ('서울 종로구 삼청로 50', '50 Samcheong-ro, Jongno-gu, Seoul'),
      '같은 갤러리도 전시 교체일에는 닫을 수 있습니다. 촬영·큰 가방·단체 방문 조건을 확인하세요. | Galleries may close between shows. Check photography, large-bag and group-visit rules. | 展示替えには閉まる場合があります。撮影・大きな荷物・団体訪問の条件を確認してください。 | 换展期间可能关闭，请确认拍摄、大件行李及团体到访规则。',
      '한옥 갤러리 외관 | Hanok-gallery exterior | 韓屋ギャラリー外観 | 韩屋画廊外观', phone='02-720-1524', extraSource='https://www.hakgojae.com/')

place('boan', 'seochon', 'exhibit',
      '보안1942 | Boan1942 | 保安1942 | 保安1942',
      '예술공간 · 옛 여관 | Art space · former inn | アート空間・旧旅館 | 艺术空间·旧旅馆',
      '옛 여관의 공간과 전시 살펴보기 | Explore a former inn and its exhibitions | 旧旅館の空間と展示を見る | 参观旧旅馆空间及展览',
      '전시별 확인 · 책·음료 별도 구매 | Check each exhibition · books and drinks extra | 展示別確認・本と飲み物は別料金 | 各展费用需确认，书籍及饮品另付',
      '전시장 기본 화–일 12–18시 | Galleries usually Tue–Sun 12:00–18:00 | 展示室基本火～日12～18時 | 展厅通常周二至日12–18时',
      '월요일 휴관 · 공간별 시간 상이 | Closed Mondays · hours vary by space | 月曜休館・空間により時間が異なる | 周一休息，不同空间时间有别',
      '옛 보안여관을 활용한 전시공간과 책방 등이 함께 있는 문화공간입니다. 작품뿐 아니라 건물에 남은 흔적을 보는 방문을 제안합니다. | A cultural space with exhibitions and a bookshop around the former Boan Inn. Explore both the artwork and traces of the old building. | 旧保安旅館を活用した展示室と書店などの文化空間。作品と建物に残る痕跡を見て過ごせます。 | 利用旧保安旅馆设有展厅、书店等的文化空间，可同时欣赏作品与旧建筑痕迹。',
      ('서울 종로구 효자로 33', '33 Hyoja-ro, Jongno-gu, Seoul'),
      '전시장·책방·카페·숙박은 시간과 이용 조건이 다릅니다. 옛 건물의 층간 계단, 전시 공백기와 개방 구역을 확인하세요. | Gallery, bookshop, café and lodging have different rules. Check stairs, gaps between exhibitions and open areas. | 展示室・書店・カフェ・宿泊は別条件です。旧館の階段、展示の空白期間、公開範囲を確認。 | 展厅、书店、咖啡馆及住宿规则不同，请确认旧楼层间楼梯、展览空档及开放范围。',
      '과거 전시가 보이는 실내 · 현재 전시 아님 | Interior with a past exhibition · not current | 過去の展示が写る室内・現在の展示ではありません | 含过往展览的室内照片，并非当前展览', phone='02-720-8409', extraSource='https://b1942.com/')

place('baekinje', 'anguk', 'hanok',
      '백인제가옥 | Baek In-je House | 白麟済家屋 | 白麟济故居',
      '한옥 · 근대 주거 | Hanok · modern-era home | 韓屋・近代の住宅 | 韩屋·近代住宅',
      '큰 한옥의 마당과 생활 공간 살펴보기 | Explore a large hanok and courtyard | 大きな韓屋の庭と住まいを見る | 参观大型韩屋庭院及生活空间',
      '일반 관람 무료 · 내부 해설 별도 예약 | General admission free · book interior tours | 一般見学無料・内部解説は別途予約 | 一般参观免费，室内导览需另预约',
      '09–18시 · 입장 마감 17:30 | 09:00–18:00 · last entry 17:30 | 09～18時・最終入場17:30 | 09–18时，最晚入场17:30',
      '월요일·1월 1일 휴관 안내 | Listed closed Mondays and Jan 1 | 月曜・1月1日休館の案内 | 公示周一及1月1日休馆',
      '근대 한옥의 구조와 정원을 살펴볼 수 있는 가옥입니다. 일반 방문은 외부 개방 구역을 중심으로 하며, 일부 실내는 해설 예약이 필요합니다. | A historic house for exploring modern-era hanok architecture and its garden. General visits focus on outdoor open areas; some interiors require a guided-tour booking. | 近代韓屋の構造と庭を見られる家屋。一般見学は屋外公開区間が中心で、一部内部は解説予約が必要です。 | 可了解近代韩屋结构和庭园的故居，一般到访以室外开放区域为主，部分室内需预约导览。',
      ('서울 종로구 북촌로7길 16', '16 Bukchon-ro 7-gil, Jongno-gu, Seoul'),
      '예약 없이 모든 실내에 들어갈 수 있는 곳은 아닙니다. 원하는 관람 구역, 해설 언어·시간과 어린이 동반 조건을 확인하세요. | Not all interiors are open without booking. Check desired areas, tour language, timing and child-accompaniment rules. | 予約なしですべての室内に入れるわけではありません。見学範囲・解説言語・時間・子どもの同行条件を確認。 | 未预约不可进入所有室内，请确认所需区域、导览语言、时间及儿童陪同规定。',
      '가옥 입구 · 계단 있는 진입부 | House entrance · stepped approach | 家屋入口・階段のある進入部 | 故居入口，有台阶', extraSource='https://english.visitseoul.net/attractions/Baek-Injes-House/ENP021128')

place('sangchon', 'seochon', 'hanok',
      '상촌재 | Sangchonjae | 上村斎 | 上村斋',
      '한옥 · 온돌 문화 | Hanok · ondol culture | 韓屋・オンドル文化 | 韩屋·温突文化',
      '한옥과 온돌의 구조 살펴보기 | Discover hanok and floor-heating design | 韓屋とオンドルの構造を見る | 了解韩屋及地暖结构',
      '일반 관람 무료 · 프로그램 별도 | General admission free · programs separate | 一般見学無料・プログラムは別途 | 一般参观免费，活动另计',
      '기본 09–18시 | Usually 09:00–18:00 | 基本09～18時 | 通常09–18时',
      '월요일·1월 1일·설·추석 휴관 확인 | Check Monday, Jan 1, Seollal and Chuseok closures | 月曜・1月1日・旧正月・秋夕の休館確認 | 确认周一、1月1日、春节及中秋休馆',
      '서촌의 한옥 문화공간으로 온돌과 전통 생활문화를 소개합니다. 계절 행사와 교육은 매일 열리는 프로그램이 아니므로 따로 확인하세요. | A Seochon hanok cultural space introducing ondol heating and traditional life. Seasonal events and classes are not daily; check the schedule separately. | 西村でオンドルと伝統生活を紹介する韓屋文化空間。季節行事・教育は毎日開催ではないため、別途日程を確認してください。 | 西村介绍温突地暖及传统生活的韩屋文化空间，季节活动和课程并非每天举办，需另查日程。',
      ('서울 종로구 자하문로17길 12-11', '12-11 Jahamun-ro 17-gil, Jongno-gu, Seoul'),
      '관람 무료와 체험 무료는 다릅니다. 프로그램 신청·재료비·진행 언어와 마당 개방 범위를 확인하세요. | Free admission does not make all activities free. Check registration, materials fees, language and courtyard access. | 入場無料でも体験は有料の場合があります。申込・材料費・言語・庭の開放範囲を確認。 | 免费入场不代表所有体验免费，请确认报名、材料费、语言及庭院开放范围。',
      '한옥 문화공간 참고 사진 | Hanok cultural-space reference photo | 韓屋文化空間の参考写真 | 韩屋文化空间参考照片', phone='02-6013-1142', extraSource='https://www.jfac.or.kr/site/main/content/sangchj01')

place('sajik', 'seochon', 'park',
      '사직공원 | Sajik Park Seoul | 社稷公園（ソウル） | 社稷公园（首尔）',
      '공원 · 야외 산책 | Park · outdoor walk | 公園・屋外散策 | 公园·户外散步',
      '공원 길을 따라 쉬엄쉬엄 걷기 | Take a gentle park walk | 公園の道をゆっくり歩く | 沿公园步道慢慢走',
      '공원 산책 무료 · 시설별 조건 별도 | Park walks free · facility rules separate | 公園散策無料・施設条件は別 | 公园散步免费，各设施规定不同',
      '공원 상시 개방 안내 | Park listed open 24 hours | 公園は常時開放の案内 | 公园公示全天开放',
      '사직단·시설 내부와 행사 통제 별도 | Altar/interior access and event restrictions separate | 社稷壇・施設内部・行事規制は別 | 社稷坛、设施内部及活动限制另计',
      '사직단 주변의 공원 구역입니다. 산자락 계곡까지 오르기보다 공원에서 걷고 싶을 때 비교하세요. 사직단 내부를 자유롭게 이용한다는 뜻은 아닙니다. | Park areas around Sajik Altar. Compare a park stroll with walking farther up to a valley; this does not imply unrestricted altar access. | 社稷壇周辺の公園。山裾の渓谷へ向かう散歩と比較できます。社稷壇内部の自由利用を意味しません。 | 社稷坛周围的公园区域，可与前往山麓溪谷散步比较，并不表示社稷坛内部可自由进入。',
      ('서울 종로구 사직로 89', '89 Sajik-ro, Jongno-gu, Seoul'),
      '아이와 함께라면 문화유산 구역과 일반 산책 구간을 구분하고, 비·더위에는 실내 비교를 선택하세요. | With children, distinguish heritage areas from walking paths. Choose an indoor comparison in rain or heat. | 子ども連れでは文化遺産区間と散策区間を区別。雨や暑い日は室内の比較を選びましょう。 | 带孩子时请区分文化遗产区域与散步路线，雨天或炎热时可选择室内对比。',
      '사직단 풍경 · 자유 출입 보장 아님 | Sajik Altar view · access is not guaranteed | 社稷壇の風景・自由入場を保証しません | 社稷坛景观，不保证自由进入')

place('donglim', 'anguk', 'hanok',
      '동림매듭공방 | Donglim Knot Workshop | 東琳組紐工房 | 东琳绳结工坊',
      '공방 · 전통 매듭 | Workshop · Korean knots | 工房・伝統の結び | 工坊·传统绳结',
      '매듭 장식을 보고 직접 만들기 | See and make decorative knots | 飾り結びを見て作る | 观赏并制作装饰绳结',
      '체험·작품별 유료 · 현재 비용 확인 | Activities and works charged · confirm fees | 体験・作品は有料・現在料金確認 | 体验及作品收费，请确认当前费用',
      '기본 10–18시 | Usually 10:00–18:00 | 基本10～18時 | 通常10–18时',
      '월요일·명절 휴무 안내 | Listed closed Mondays and major holidays | 月曜・旧正月等休業の案内 | 公示周一及主要节日休息',
      '전통 매듭 작품을 전시하고 팔찌·장식 등을 만드는 체험을 운영하는 한옥 공방입니다. 체험 종류와 재료비는 선택한 작업에 따라 다릅니다. | A hanok workshop displaying traditional knots and offering bracelet or ornament making. Activities and material costs depend on the piece. | 伝統の飾り結びを展示し、ブレスレットや装飾品づくりを行う韓屋工房。内容と材料費は作品により異なります。 | 展示传统绳结并提供手链、装饰品制作的韩屋工坊，体验及材料费用依作品而异。',
      ('서울 종로구 북촌로12길 10', '10 Bukchon-ro 12-gil, Jongno-gu, Seoul'),
      '예약 가능 시간, 소요시간, 설명 언어와 어린이 참여 가능 연령을 문의하세요. 전시 관람과 만들기를 구분해 신청하세요. | Ask about booking times, duration, teaching language and minimum age. Distinguish viewing the display from joining a workshop. | 予約時間・所要時間・説明言語・子どもの対象年齢を確認。展示を見ることと制作への参加は別です。 | 请询问可预约时间、时长、授课语言及儿童参与年龄，观展与制作体验需区分。',
      '매듭 공방 한옥 외관 | Hanok knot-workshop exterior | 結び工房の韓屋外観 | 绳结工坊韩屋外观', phone='02-3673-2778', extraSource='https://english.visitseoul.net/attractions/donglim-knot-workshop_/18964')

CATEGORIES = [
    ('all', L('모두 | All | すべて | 全部')),
    ('food', L('먹거리 | Food | 食事 | 美食')),
    ('cafe', L('카페·차 | Cafés & tea | カフェ・茶 | 咖啡·茶')),
    ('rest', L('쉬기·산책 | Rest & walks | 休憩・散策 | 休息·散步')),
    ('culture', L('문화·역사 | Culture | 文化・歴史 | 文化·历史')),
    ('art', L('미술·전시 | Art & exhibits | 美術・展示 | 艺术·展览')),
    ('make', L('체험·선물 | Crafts & gifts | 体験・お土産 | 体验·伴手礼')),
    ('weather', L('비·더위 | Rain & heat | 雨・暑い日 | 雨天·避暑')),
    ('family', L('아이와 | With kids | 子どもと | 亲子')),
    ('free', L('무료 관람 | Free visits | 無料見学 | 免费参观')),
]

PAIRS = []
def pair(id, region, category, ids, title, reason, notice=None, choices=None):
    copy = {'title': L(title), 'reason': L(reason)}
    if notice:
        copy['notice'] = L(notice)
    PAIRS.append({'id': id, 'region': region, 'category': category, 'placeIds': ids.split(), 'copy': copy, 'choices': choices or {}})

pair('soup-choice', 'anguk', 'food', 'sujebi gippen',
     '수제비 한 그릇, 국밥 한 그릇 | Dough soup or rice soup? | すいとん、それともスープご飯？ | 面片汤，还是汤饭？',
     '삼청로의 수제비와 안국역 남측의 국밥·숯불 요리를 비교해요. | Compare sujebi on Samcheong-ro with rice soup and charcoal dishes south of Anguk Station. | 三清路のすいとんと安国駅南側のスープご飯・炭火料理を比較。 | 比较三清路面片汤与安国站南侧的汤饭、炭烤料理。',
     '두 곳은 안국 권역의 서로 다른 쪽에 있어요. 현재 위치에서 갈 곳을 지도로 확인하세요. | These places are on different sides of the Anguk area. Check the map before choosing. | 安国エリアの異なる側にあります。現在地からの位置を地図で確認。 | 两处位于安国片区不同方向，请先查看地图。')
pair('seochon-noodle-grill', 'seochon', 'food', 'chebu jalppajin',
     '갈비를 나눠 먹을까, 메밀국수를 먹을까? | Shared ribs or buckwheat noodles? | カルビを分け合う？そばを食べる？ | 分享烤排骨，还是吃荞麦面？',
     '테이블에서 굽는 고기와 면·수육 중심 식사의 차이를 살펴요. | Compare tabletop grilled meat with noodles and sliced pork. | 卓上で焼く肉と、麺・ゆで豚中心の食事を比較。 | 比较桌边烤肉与面条、白切肉为主的用餐方式。',
     '현재 메뉴·주문 인원·휴식시간을 확인하세요. 메밀면만으로 채식·알레르기 대응을 판단하지 마세요. | Check menus, minimum orders and breaks; buckwheat noodles do not establish dietary suitability. | メニュー・注文単位・休憩時間を確認。そばだけで菜食・アレルギー対応を判断しないでください。 | 请确认菜单、起订份数及午休；不能仅凭荞麦面判断素食或过敏适用性。')
pair('bagel-tea', 'anguk', 'cafe', 'london chatteul',
     '베이글을 고르거나, 차 한 잔에 머물거나 | Pick a bagel or settle in for tea | ベーグルを選ぶ？お茶でひと息？ | 挑贝果，还是坐下喝茶？',
     '베이글 구매와 한옥에서 전통차를 마시는 시간을 비교해요. | Compare a bagel stop with traditional tea in a hanok. | ベーグルを買う時間と韓屋で伝統茶を飲む時間を比較。 | 比较买贝果与在韩屋品传统茶两种停留方式。',
     '차마시는뜰은 주거 골목 안에 있어요. 매장 시간과 별개로 관광 방문시간·현장 안내를 확인하세요. | The tea house is in residential lanes. Check visitor restrictions separately from shop hours. | 茶屋は住宅路地内。営業時間とは別に観光訪問時間・現地案内を確認。 | 茶馆位于住宅巷内，请另外核对游客到访时间及现场提示。')
pair('coffee-tea-hanok', 'anguk', 'cafe', 'onion osulloc',
     '빵과 커피, 차와 디저트 | Bread and coffee, tea and sweets | パンとコーヒー、茶とスイーツ | 面包咖啡，茶与甜点',
     '어니언의 빵·커피와 오설록의 차 메뉴를 비교해요. | Compare Onion bread and coffee with Osulloc tea menus. | オニオンのパン・コーヒーとオソルロックのお茶を比較。 | 比较Onion面包咖啡与OSULLOC茶品。')
pair('roasted-blended', 'anguk', 'cafe', 'fritz teatherapy',
     '로스팅 커피와 블렌딩 차 | Roasted coffee or blended tea | 焙煎コーヒーとブレンド茶 | 烘焙咖啡与调配茶',
     '원서동의 커피·빵과 윤보선길의 허브·과일차 중 골라요. | Choose coffee and bread in Wonseo-dong or herbal and fruit tea on Yunboseon-gil. | 苑西洞のコーヒー・パンと尹潽善通りのハーブ・果実茶から選ぶ。 | 选择苑西洞的咖啡面包，或尹潽善路的草本果茶。')
pair('seochon-cafe', 'seochon', 'cafe', 'staffpicks daeo',
     '테라스 카페, 오래된 서점 카페 | Terrace café or old-bookshop café | テラスカフェ、古い書店カフェ | 露台咖啡馆，旧书店咖啡馆',
     '바깥 좌석의 풍경과 오래된 책·마당이 남은 공간을 비교해요. | Compare outdoor seating with a space retaining old books and a courtyard. | 屋外席の風景と古い本・庭が残る空間を比較。 | 比较室外座位景观与保留旧书、庭院的空间。',
     '두 곳 모두 구매·좌석 이용 조건이 있어요. 대오서점은 일반 도서관이 아닙니다. | Both have purchase and seating conditions. Daeo is not a public library. | 両店とも購入・座席条件があります。大悟書店は公共図書館ではありません。 | 两处均有消费和座位条件，大悟书店并非公共图书馆。')
pair('hanok-courtyards', 'anguk', 'rest', 'baeryeom baekinje',
     '작은 한옥, 넓은 가옥의 마당 | A small hanok or a larger house courtyard | 小さな韓屋、大きな家屋の庭 | 小韩屋，大家宅的庭院',
     '배렴 가옥의 작은 공간과 백인제가옥의 정원·건축을 비교해요. | Compare Baeryeom’s small house with Baek In-je House’s garden and architecture. | 裵濂家屋の小空間と白麟済家屋の庭・建築を比較。 | 比较裵濂故居的小空间与白麟济故居的庭园、建筑。',
     '관람 공간입니다. 피크닉·장시간 좌석 이용과 내부 출입은 현장 규칙을 따라주세요. | These are visitor sites. Follow rules on picnics, extended seating and interior access. | 見学施設です。ピクニック・長時間着席・内部立入りは現地規則に従ってください。 | 两处均为参观空间，野餐、长时间占座及室内进入请遵从现场规定。')
pair('park-hanok', 'seochon', 'rest', 'sajik sangchon',
     '공원 길을 걷거나, 한옥을 둘러보거나 | Park paths or a hanok visit | 公園を歩く？韓屋を見学する？ | 走公园步道，还是参观韩屋？',
     '사직공원의 야외 산책과 상촌재의 마당·온돌 관람을 비교해요. | Compare a Sajik Park walk with Sangchonjae’s courtyard and ondol displays. | 社稷公園の散策と上村斎の庭・オンドル見学を比較。 | 比较社稷公园散步与上村斋庭院、温突展示。')
pair('hanok-life', 'anguk', 'culture', 'baekinje bukchoncenter',
     '근대 한옥의 생활, 북촌의 한옥문화 | Historic home life or Bukchon hanok culture | 近代韓屋の暮らし、北村の韓屋文化 | 近代韩屋生活，北村韩屋文化',
     '백인제가옥의 주거 구조와 북촌문화센터의 한옥·문화 안내를 비교해요. | Compare Baek In-je House architecture with the hanok and cultural information at Bukchon Culture Center. | 白麟済家屋の住居構造と北村文化センターの韓屋・文化案内を比較。 | 比较白麟济故居的住宅结构与北村文化中心的韩屋、文化介绍。',
     '가옥 내부 해설과 문화센터 프로그램은 각각 예약·일정을 확인하세요. | Check house-tour bookings and culture-center program dates separately. | 家屋内部の解説と文化センターの講座は別々に予約・日程を確認。 | 故居室内导览与文化中心活动的预约、日程需分别确认。')
pair('museum-gallery', 'anguk', 'art', 'mmca hakgojae',
     '여러 전시를 넓게, 갤러리 한 곳을 가깝게 | A large museum or a focused gallery visit | 大きな美術館、ひとつのギャラリー | 大型美术馆，专注一间画廊',
     '국립현대미술관의 여러 전시와 학고재의 현재 전시를 비교해요. | Compare MMCA’s multiple exhibitions with Hakgojae’s current show. | 国立現代美術館の複数展と学古斎の開催展を比較。 | 比较国立现代美术馆的多项展览与学古斋当前展览。')
pair('artist-writer', 'seochon', 'art', 'park yisang',
     '화가의 작품, 작가의 기록 | A painter’s work or a writer’s records | 画家の作品、作家の記録 | 画家的作品，作家的记录',
     '박노수미술관의 회화와 이상의 집의 문학 전시를 비교해요. | Compare paintings at Park No-soo Museum with literary displays at Yi Sang’s House. | 朴魯寿美術館の絵画と李箱の家の文学展示を比較。 | 比较朴鲁寿美术馆的绘画与李箱故居的文学展示。')
pair('seochon-art', 'seochon', 'art', 'daelim boan',
     '기획전 미술관, 옛 여관의 예술공간 | Temporary-show museum or former-inn art space | 企画展の美術館、旧旅館のアート空間 | 临展美术馆，旧旅馆艺术空间',
     '대림미술관의 기획전과 보안1942의 건물·전시를 비교해요. | Compare Daelim’s temporary exhibitions with Boan1942’s building and shows. | 大林美術館の企画展と保安1942の建物・展示を比較。 | 比较大林美术馆的临展与保安1942的建筑、展览。',
     '전시 공백기에는 방문할 전시가 없을 수 있어요. 현재 전시와 요금을 먼저 확인하세요. | There may be no exhibition between shows. Check current dates and fees first. | 展示の空白期間には鑑賞できない場合があります。開催日と料金を先に確認。 | 换展空档可能没有可看展览，请先核实当前展期及费用。')
pair('knot-tea', 'anguk', 'make', 'donglim teatherapy',
     '매듭으로 남길까, 차의 향으로 남길까? | A knot to keep or a tea to remember? | 結びを持ち帰る？お茶を選ぶ？ | 留下绳结，还是茶香？',
     '전통 매듭 만들기와 취향에 맞는 차·차 프로그램을 비교해요. | Compare traditional knot making with tea selection and tea programs. | 伝統の結びづくりと好みの茶・茶の体験を比較。 | 比较传统绳结制作与选茶、茶体验。',
     '공방·차 수업은 당일 참여를 보장하지 않아요. 예약·비용·언어·완성품 수령을 확인하세요. | Walk-in workshops are not guaranteed. Confirm booking, fees, language and when items can be taken home. | 当日参加は保証されません。予約・料金・言語・完成品の受取時期を確認。 | 不保证当天可参加，请确认预约、费用、语言及成品领取时间。',
     choices={'teatherapy': {'visitWhen': L('차를 고르거나 예약한 차 프로그램 참여 | Choose tea or join a booked tea program | 茶を選ぶ・予約した茶の体験に参加 | 选茶或参加已预约的茶体验'), 'useMode': L('차·상품 구매 · 차 수업은 별도 예약·비용 확인 | Buy tea products; classes require separate booking and fee checks | 茶・商品購入。講座は別途予約・料金確認 | 购买茶品，茶课预约及费用另行确认')}})
pair('tea-coffee-gifts', 'anguk', 'make', 'osulloc fritz',
     '차 선물, 커피 선물 | Tea gifts or coffee gifts | お茶のお土産、コーヒーのお土産 | 茶伴手礼，咖啡伴手礼',
     '찻잎·차 상품과 원두·드립백을 비교해요. 카페 메뉴 가격과 상품 가격은 달라요. | Compare tea products with beans and drip bags. Café menus and gift prices differ. | 茶葉・茶商品と豆・ドリップバッグを比較。飲食と商品の価格は別です。 | 比较茶叶、茶品与咖啡豆、挂耳包；堂食菜单和商品价格不同。',
     '두 지점의 현재 상품·재고·포장과 가져갈 나라의 반입 조건을 확인하세요. | Confirm branch stock, packaging and your destination’s import rules. | 店舗在庫・包装と持ち帰る国の持込条件を確認。 | 请确认分店库存、包装及目的地入境携带规定。')
pair('rain-royal-art', 'seochon', 'weather', 'gogung daelim',
     '비 오는 서촌, 왕실 유물이나 기획전 | Rain in Seochon: royal objects or an art show | 雨の西村、王室の遺物か企画展か | 雨中的西村：王室文物或艺术展',
     '고궁박물관의 실내 전시와 대림미술관의 기획전을 비교해요. | Compare indoor royal exhibits with Daelim’s temporary show. | 古宮博物館の屋内展示と大林美術館の企画展を比較。 | 比较古宫博物馆室内展览与大林美术馆临展。')
pair('rain-reading-culture', 'anguk', 'weather', 'folk jeongdok',
     '생활문화 전시, 조용한 자료실 | Everyday-culture exhibits or a quiet reading room | 生活文化の展示、静かな閲覧室 | 生活文化展览，安静阅览室',
     '민속박물관의 일반 전시와 정독도서관 자료 열람을 비교해요. | Compare the Folk Museum’s general galleries with reading at Jeongdok Library. | 民俗博物館の一般展示と正読図書館の閲覧を比較。 | 比较民俗博物馆一般展厅与正读图书馆阅览。',
     '도서관은 조용히 이용하는 공간이에요. 좌석을 보장하지 않으며 건물까지의 이동은 야외입니다. | Library use must be quiet; seats are not guaranteed and access to buildings is outdoors. | 図書館では静かに。座席保証はなく、建物までの移動は屋外です。 | 图书馆需安静使用，不保证座位，前往建筑仍需走室外。')
pair('rain-artist-spaces', 'seochon', 'weather', 'park boan',
     '작은 미술관에서 비를 피해 관람하기 | Small art spaces on a rainy day | 雨の日に小さな美術空間へ | 雨天走进小型艺术空间',
     '박노수미술관과 보안1942의 실내 전시를 비교해요. | Compare indoor exhibitions at Park No-soo Museum and Boan1942. | 朴魯寿美術館と保安1942の屋内展示を比較。 | 比较朴鲁寿美术馆与保安1942的室内展览。',
     '입구·정원·건물 간 이동에는 비를 맞을 수 있어요. 젖은 계단과 전시 운영 여부를 확인하세요. | Entrances, gardens or between-building routes may be exposed. Check wet steps and exhibition opening. | 入口・庭・棟間は雨に濡れる場合があります。濡れた階段と展示開催を確認。 | 入口、庭院及楼间路线可能淋雨，请留意湿滑台阶并确认展览开放。')
pair('family-royal', 'seochon', 'family', 'gyeongbok gogung',
     '궁궐을 직접 걷거나, 왕실 물건을 보거나 | Walk a palace or see royal objects | 宮殿を歩く？王室の品を見る？ | 亲自走宫殿，还是看王室文物？',
     '야외 건축 중심 경복궁과 실내 유물 중심 고궁박물관을 아이의 관심에 맞춰 골라요. | Match your child’s interests: outdoor palace architecture or indoor royal objects. | 子どもの興味に合わせ、屋外の宮殿建築か室内の王室遺物かを選ぶ。 | 按孩子兴趣选择室外宫殿建筑或室内王室文物。',
     '어린이 전용 체험 예약이 포함된 비교는 아닙니다. 유모차 동선·가족 감면·교육 일정은 별도 확인하세요. | This does not include booked children’s activities. Check stroller routes, concessions and education schedules. | 子ども専用体験の予約を含みません。ベビーカー経路・割引・教育日程は別途確認。 | 此对比不包含儿童专属体验预约，请另查婴儿车路线、优惠及教育日程。')
pair('family-break', 'seochon', 'family', 'tongin sajik',
     '아이의 다음 쉼표, 간식일까 산책일까? | The next family break: a snack or a walk? | 次の家族の休憩、おやつ？散歩？ | 孩子的下一站：小吃还是散步？',
     '시장에서 음식을 고르는 시간과 공원에서 걷는 시간을 비교해요. | Compare choosing market food with a park walk. | 市場で食べ物を選ぶ時間と公園を歩く時間を比較。 | 比较市场挑选食物与公园散步两种活动。',
     '시장 통로·뜨거운 음식과 공원 경사에 주의하세요. 도시락 식사 공간의 유모차 접근은 먼저 확인하세요. | Watch for narrow lanes, hot food and slopes. Ask about stroller access to the lunchbox dining area. | 市場の通路・熱い料理・公園の坂に注意。弁当の飲食スペースへのベビーカー進入は事前確認を。 | 留意市场通道、热食及公园坡道，先确认婴儿车能否进入便当用餐区。')
pair('family-hanok', 'anguk', 'family', 'workshop baekinje',
     '손으로 만들까, 한옥 구조를 살펴볼까? | Make something or discover a hanok? | 手で作る？韓屋の構造を見る？ | 动手制作，还是观察韩屋结构？',
     '전통공예 만들기와 가옥·정원 관람을 비교해요. | Compare a craft activity with a house and garden visit. | 伝統工芸づくりと家屋・庭の見学を比較。 | 比较传统工艺制作与故居、庭园参观。',
     '아이의 연령·작업 도구·보호자 조건은 체험별로 확인하세요. 백인제가옥 일부 실내는 해설 예약이 필요합니다. | Check age, tools and guardian rules for each activity. Some Baek In-je interiors require a guided-tour booking. | 体験ごとに年齢・道具・保護者条件を確認。白麟済家屋の一部内部は解説予約が必要です。 | 各体验的年龄、工具及监护人条件需确认，白麟济故居部分室内需预约导览。')
pair('free-craft-house', 'anguk', 'free', 'craft baekinje',
     '관람료 없이 공예 전시나 한옥 보기 | Free craft exhibits or a hanok visit | 無料で工芸展示か韓屋を見学 | 免费看工艺展或参观韩屋',
     '공예박물관 일반 전시와 백인제가옥 일반 개방 구역을 비교해요. | Compare general craft galleries with Baek In-je House’s public areas. | 工芸博物館の一般展示と白麟済家屋の一般公開範囲を比較。 | 比较工艺博物馆一般展览与白麟济故居公开区域。',
     '무료 관람에도 휴관일·예약 조건이 있습니다. 어린이관·특별 프로그램·상품은 별도 확인하세요. | Free visits can still have closures or booking rules. Check children’s galleries, programs and purchases separately. | 無料でも休館・予約条件があります。子ども館・特別講座・商品は別途確認。 | 免费参观仍有休馆及预约条件，儿童馆、特别活动及商品需另外确认。')
pair('free-life-hanok', 'anguk', 'free', 'folk bukchoncenter',
     '생활문화 전시, 북촌의 한옥 구경 | Everyday culture or a Bukchon hanok | 生活文化の展示、北村の韓屋 | 生活文化展览，北村韩屋',
     '민속박물관 일반 전시와 북촌문화센터 일반 공간을 비교해요. | Compare Folk Museum general exhibits with Bukchon Culture Center’s public space. | 民俗博物館の一般展示と北村文化センターの一般空間を比較。 | 比较民俗博物馆一般展览与北村文化中心公共空间。',
     '어린이관 예약과 문화센터의 유료·신청 프로그램은 무료 일반 관람과 다릅니다. | Children’s bookings and paid or bookable programs are separate from free general admission. | 子ども館予約と有料・申込プログラムは無料一般見学と別です。 | 儿童馆预约及收费、报名活动与免费一般参观不同。',
     choices={'bukchoncenter': {'cost': L('일반 공간 무료 · 프로그램 별도 | Public areas free · programs separate | 一般空間無料・プログラムは別途 | 公共区域免费，活动另计'), 'useMode': L('일반 한옥 공간 관람 · 강좌·체험은 별도 신청 | Visit public hanok areas; classes and activities require separate applications | 一般韓屋空間を見学。講座・体験は別途申込 | 参观公共韩屋空间，课程及体验需另报名')}})
pair('free-royal-ondol', 'seochon', 'free', 'gogung sangchon',
     '왕실의 물건, 한옥의 온돌 | Royal objects or hanok floor heating | 王室の品、韓屋のオンドル | 王室物品，韩屋地暖',
     '무료 일반 전시로 왕실 생활과 한옥 주거의 차이를 살펴요. | Compare royal life with hanok living through free general exhibitions. | 無料一般展示で王室の生活と韓屋の住まいを比べる。 | 通过免费一般展览比较王室生活与韩屋居住方式。')
pair('free-outdoor', 'seochon', 'free', 'sajik suseongdong',
     '입장료 없이 공원이나 계곡 산책 | A free park or valley walk | 入場料なしで公園か渓谷へ | 免费逛公园或溪谷',
     '사직공원의 길과 수성동 계곡의 바위·산자락 풍경을 비교해요. | Compare Sajik Park paths with Suseongdong Valley’s rocks and foothill scenery. | 社稷公園の道と水声洞渓谷の岩・山裾の風景を比較。 | 比较社稷公园步道与水声洞溪谷的岩石、山麓景观。',
     '무료여도 모든 구간이 평탄하거나 항상 열려 있지는 않아요. 기상·현장 통제를 확인하세요. | Free does not mean flat or always open. Check weather and local restrictions. | 無料でも全区間が平坦・常時開放とは限りません。天候と現地規制を確認。 | 免费不代表所有路线平坦或始终开放，请核实天气及现场限制。')
