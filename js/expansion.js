// v23 editorial expansion. Sources checked 2026-09-29; never live availability.
(() => {
  const kto = id => `https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=${id}`;
  const hanok = 'https://hanok.seoul.go.kr/front/util/bcgTour03.do?lang=KOR';
  const craftBooking = 'https://craftmuseum.seoul.go.kr/chimsm/exhibit/plan/list/1';
  const folkChildren = 'https://nfm.go.kr/home/subIndex/1186.do';
  const additions = [
    {
      id: 'tongin', name: '통인시장', englishName: 'Tongin Market', region: 'seochon', category: '시장 · 도시락',
      visitWhen: '여러 가게에서 골라 도시락 만들기', cost: '음식별 결제 · 엽전 구매 조건 확인',
      description: '시장 가맹점을 돌며 음식을 골라 담는 엽전 도시락이 특징입니다. 한 식당에 앉아 먹기보다 여러 음식을 조금씩 고르는 식사를 원할 때 살펴보세요.',
      schedule: '도시락 기본 11–15시', closure: '시장 점포·도시락 휴무 별도 확인',
      hoursSummary: '도시락 기본 11–15시 · 시장 점포 시간은 별도',
      hours: '관광공사 장소 안내: 시장 07:00–21:00, 도시락카페 11:00–15:00. 점포별 시간·휴무가 다릅니다. 주말 도시락 종료시간과 월요일·셋째 일요일 휴무 안내는 자료마다 달라 시장에 재확인해 주세요.',
      useMode: '엽전 구매 → 가맹점에서 음식 선택 → 도시락카페 이용 · 모든 가게가 엽전을 받지는 않음',
      visitTip: '늦은 점심이라면 도시락 운영 종료부터 확인하세요. 엽전 최소 구매액, 남은 엽전 환불 조건과 메뉴 번역 QR 안내는 현장에서 확인할 수 있습니다.',
      accessSummary: '시장 통로 이동 · 도시락카페는 위층',
      access: '도시락카페는 고객만족센터 위층에 있습니다. 유모차·휠체어의 식사 공간 접근 경로는 사전 문의가 필요합니다.',
      unknown: '엽전 최소 구매액, 당일 참여 점포·잔여 음식, 알레르기·채식 대응, 무단차 식사 공간',
      address: '서울 종로구 자하문로15길 18', coords: [37.5807670044059, 126.969947621917],
      source: kto(79811), extraSource: 'https://www.instagram.com/tongin_official/',
      checkLabel: '시장·도시락 안내', photoLabel: '시장 입구 · 도시락카페 입구 아님', imageAlt: '통인시장 입구의 간판과 아치',
      reviewNote: '도시락 주말 시간·휴무·구매액은 공식 자료 간 차이가 있어 재확인 필요'
    },
    {
      id: 'tosokchon', name: '토속촌삼계탕', englishName: 'Tosokchon Samgyetang', region: 'seochon', category: '식당 · 삼계탕',
      visitWhen: '한옥 식당에서 따뜻한 한 끼 먹기', cost: '메뉴별 결제 · 현재 가격 확인',
      description: '한옥 건물에서 삼계탕과 닭 요리를 먹는 식당입니다. 시장을 돌아다니며 음식을 고르기보다 자리에 앉아 한 끼를 먹고 싶을 때 비교해 보세요.',
      schedule: '기본 10–22시', closure: '주문 마감 21시 · 임시 휴무 확인',
      hoursSummary: '기본 10–22시 · 주문 마감 21시', hours: '관광공사 안내 10:00–22:00, 마지막 주문 21:00. 연중무휴 안내이나 당일 운영은 매장 확인.',
      useMode: '메뉴를 주문해 식사하는 한옥 식당',
      visitTip: '삼계탕에는 닭·인삼·견과류 등이 들어갑니다. 식재료 제한이나 알레르기가 있으면 주문 전 매장에 알려 주세요. 대기 시간은 실시간으로 제공하지 않습니다.',
      accessSummary: '좌석 형태와 계단 없는 진입은 매장 문의',
      access: '공식 관광 페이지마다 출입구 단차 안내가 다릅니다. 필요한 진입 경로와 좌석을 매장에 확인해 주세요.',
      unknown: '현재 메뉴 가격·대기, 식재료 제외 가능 여부, 무단차 진입·좌석',
      address: '서울 종로구 자하문로5길 5', coords: [37.5775621208271, 126.971577362193],
      source: kto(97919), phone: '02-737-7444', checkLabel: '메뉴·이용 안내', photoLabel: '삼계탕 · 메뉴 참고 사진', imageAlt: '토속촌삼계탕의 뚝배기에 담긴 삼계탕',
      photoAuthor: '한국관광공사 게시 · 원본 저작자 표기 유지', reviewNote: '가격·대기와 접근 경로는 매장 재확인'
    },
    {
      id: 'hwangsaengga', name: '황생가칼국수', englishName: 'Hwangsaengga Kalguksu', region: 'anguk', category: '식당 · 칼국수',
      visitWhen: '사골 칼국수와 만두로 식사하기', cost: '메뉴별 결제 · 현재 가격 확인',
      description: '사골 칼국수와 왕만두 등을 내는 식당입니다. 빵과 커피 대신 따뜻한 국물과 면 요리로 식사하고 싶을 때 살펴보세요.',
      schedule: '기본 11–21:30', closure: '임시 휴무·주문 마감 매장 확인',
      hoursSummary: '관광공사 안내 11–21:30 · 당일 운영 확인', hours: '관광공사 안내 11:00–21:30, 연중무휴. 마지막 주문과 임시 휴무는 매장에 확인해 주세요.',
      useMode: '사골 칼국수·만두 등 메뉴 주문 후 식사',
      visitTip: '사골 육수와 밀가루 면을 쓰는 메뉴가 있습니다. 채식·알레르기 대응과 재료 변경 가능 여부는 주문 전에 확인하세요.',
      accessSummary: '출입구 단차 안내 · 필요한 동선 확인', access: '관광공사에 출입구 단차 안내가 있습니다. 계단 없는 진입과 좌석 이용은 매장 문의가 필요합니다.',
      unknown: '메뉴 가격·대기, 주문 마감, 채식·알레르기 대응, 무단차 좌석',
      address: '서울 종로구 북촌로5길 78', coords: [37.5800369825294, 126.98062085353],
      source: kto(86236), phone: '02-739-6334', checkLabel: '식당 이용 안내', photoLabel: '칼국수 · 메뉴 참고 사진', imageAlt: '황생가칼국수의 국물과 면이 담긴 칼국수',
      photoAuthor: '네이버블로그 이용 · 한국관광공사 게시'
    },
    {
      id: 'changdeok', name: '창덕궁', englishName: 'Changdeokgung Palace', region: 'anguk', category: '궁궐 · 역사',
      visitWhen: '여러 전각을 따라 궁궐 둘러보기', cost: '전각 일반 3,000원 · 후원 별도',
      description: '궁궐의 전각과 왕실 공간을 둘러보는 곳입니다. 전각 관람과 후원 관람은 이용 조건이 다르므로, 보고 싶은 구역을 먼저 정하세요.',
      schedule: '09시 개장\n계절별 17:30–18:30 종료', closure: '월요일 휴궁 · 공휴일 예외',
      hoursSummary: '09시 개장 · 계절별 종료 · 월요일 휴궁',
      hours: '전각: 2–5월·9–10월 09:00–18:00, 6–8월 09:00–18:30, 11–1월 09:00–17:30. 입장 마감 1시간 전. 월요일이 공휴일이면 다음 비공휴일 휴궁. 후원 회차는 별도 안내.',
      useMode: '전각 자유관람 · 후원은 별도 요금·회차·예약 조건 확인',
      visitTip: '후원을 포함한 사진이지만 전각 관람권만으로 후원에 입장할 수는 없습니다. 해설 언어·시간과 할인·면제 조건은 공식 안내를 확인하세요.',
      accessSummary: '야외 이동·돌바닥 · 후원 경사와 관람 구간 확인', access: '야외 구역과 경사·단차가 있는 동선입니다. 이동 지원이 필요하면 가능한 구역을 관리소에 문의해 주세요.',
      unknown: '후원 잔여석·당일 회차, 이동 지원, 특별 관람 일정',
      address: '서울 종로구 율곡로 99', coords: [37.57765074254216, 126.99023063100555],
      source: kto(94399), extraSource: 'https://royal.khs.go.kr/ROYAL/contents/R404000000.do?schGroupCode=cdg',
      checkLabel: '전각·후원 조건', checkSource: 'extraSource', phone: '02-3668-2300',
      photoLabel: '후원 풍경 · 별도 관람 구역', imageAlt: '창덕궁 후원 연못가의 정자와 나무'
    },
    {
      id: 'unhyeon', name: '운현궁', englishName: 'Unhyeongung Royal Residence', region: 'anguk', category: '왕실 가옥 · 역사',
      visitWhen: '왕실 가옥과 마당을 둘러보기', cost: '일반 관람 무료 · 체험 별도',
      description: '흥선대원군의 사저였던 왕실 가옥입니다. 여러 전각을 넓게 도는 궁궐 일정과, 가옥과 마당 중심의 관람을 비교해 보세요.',
      schedule: '기본 09–19시\n11–3월 18시 종료', closure: '월요일 휴궁 · 야간 운영 별도',
      hoursSummary: '기본 계절별 09–18/19시 · 야간 운영 공지 확인',
      hours: '기본 안내: 4–10월 09:00–19:00, 11–3월 09:00–18:00. 입장 마감 30분 전. 월요일 휴궁(공휴일 예외). 2026년 가을 야간 시범 운영은 별도 공지를 확인하세요.',
      useMode: '일반 공간 자유관람 · 문화체험·혼례 등은 일정과 이용 조건 별도',
      visitTip: '창덕궁과 별개의 장소입니다. 야간 개방은 한시 운영이며 목요일 등 요일별 종료시간을 확인하고 방문하세요.',
      accessSummary: '마당·한옥 단차 · 개방 구역 확인', access: '마당과 한옥 내부의 단차·개방 범위가 다릅니다. 필요한 이동 동선은 관리사무소에 문의해 주세요.',
      unknown: '날짜별 야간 개방 범위, 체험 비용·잔여석, 무단차 관람 동선',
      address: '서울 종로구 삼일대로 464', coords: [37.5764042098735, 126.987125878091],
      source: 'https://www.unhyeongung.or.kr/', sourceLabel: '운현궁 운영 안내', englishSource: kto(111253),
      extraSource: 'https://www.unhyeongung.or.kr/sub/notice_guide/notice.php?abmode=view&bfsort=ino&bsort=desc&code=B10&group=basic&no=1974',
      phone: '02-766-9090', checkLabel: '관람·야간 공지', photoSource: kto(111253),
      photoLabel: '운현궁 가옥과 마당', imageAlt: '운현궁의 한옥과 마당',
      notice: { from: '2026-09-01', through: '2026-11-29', text: '11월 29일까지 야간 개방 확대 시범 운영. 홈페이지는 목요일 18시, 다른 운영일 21시 종료로 안내합니다. 방문일 공지를 확인해 주세요.', expiredText: '가을 야간 시범 운영 기간이 끝났습니다. 최신 관람시간을 확인해 주세요.' }
    },
    {
      id: 'gogung', name: '국립고궁박물관', englishName: 'National Palace Museum of Korea', region: 'seochon', category: '박물관 · 왕실 문화',
      visitWhen: '실내에서 조선 왕실 유물 살펴보기', cost: '무료',
      description: '왕실의 생활과 문화를 유물로 살펴보는 박물관입니다. 궁궐의 건물과 야외 공간을 걷는 일정 대신 실내 전시를 보고 싶을 때 선택하세요.',
      schedule: '기본 09:30–17:30\n토요일 21시 종료', closure: '매월 마지막 월요일 휴관 · 예외 확인',
      hoursSummary: '기본 09:30–17:30 · 토요일 21시까지',
      hours: '운영기관 안내: 월–금·일 09:30–17:30, 토요일과 매월 마지막 수요일 21:00까지. 입장 마감 30분 전. 매월 마지막 월요일 휴관(공휴일이면 공휴일 다음날), 1월 1일·설·추석 당일 휴관.',
      useMode: '일반 전시 관람 · 교육·단체 프로그램은 별도 신청 확인',
      visitTip: '경복궁과 박물관의 관람료·휴관일은 다릅니다. 경복궁 화요일 휴궁을 박물관 휴관으로 생각하지 않도록 각각 확인하세요.',
      accessSummary: '실내 전시 · 계단 없는 출입구는 시설 안내 확인', access: '사진은 계단이 있는 정면입니다. 무단차 출입구와 이용 가능한 엘리베이터 동선은 박물관에 확인해 주세요.',
      unknown: '기획전 교체·부분 폐실, 필요한 이동 지원, 단체 예약 조건',
      address: '서울 종로구 효자로 12', coords: [37.57659156422034, 126.97497486352258],
      source: 'https://gogung.go.kr/gogung/main/contents.do?menuNo=800011', sourceLabel: '국립고궁박물관 관람안내', englishSource: kto(106970),
      phone: '02-3701-7500', checkLabel: '시간·휴관 확인', photoSource: kto(106970), photoLabel: '박물관 정면 · 계단 있는 출입구', imageAlt: '국립고궁박물관 정면과 계단',
      reviewNote: '관광공사에 남은 이전 시간보다 운영기관의 09:30 개장 안내를 우선'
    },
    {
      id: 'gyeongbok', name: '경복궁', englishName: 'Gyeongbokgung Palace', region: 'seochon', category: '궁궐 · 야외 관람',
      visitWhen: '궁궐 건물과 마당을 직접 걷기', cost: '일반 3,000원 · 감면 조건 확인',
      description: '궁궐 건물과 넓은 마당, 연못 풍경을 걸으며 둘러보는 곳입니다. 서촌에서 이어지는 경복궁역 권역으로 묶었습니다.',
      schedule: '09시 개장\n계절별 17–18:30 종료', closure: '화요일 휴궁 · 공휴일 예외',
      hoursSummary: '09시 개장 · 계절별 종료 · 화요일 휴궁',
      hours: '11–2월 09:00–17:00, 3–5월·9–10월 09:00–18:00, 6–8월 09:00–18:30. 입장 마감 1시간 전. 화요일이 공휴일이면 다음 비공휴일 휴궁. 야간·특별관람은 별도.',
      useMode: '주간 궁궐 관람권 이용 · 한복·연령 등에 따른 감면 조건은 공식 확인',
      visitTip: '야외 이동이 많습니다. 비·더위를 피하고 싶다면 가까운 고궁박물관과 비교하세요. 특별관람과 경회루 내부 관람은 일반 관람과 조건이 다릅니다.',
      accessSummary: '넓은 야외 동선 · 돌바닥과 문턱', access: '돌바닥·문턱이 있는 구간이 있습니다. 휠체어·유모차로 가능한 관람 구역은 관리소에 확인해 주세요.',
      unknown: '당일 행사·통제, 특별관람 잔여석, 이동 지원 구역',
      address: '서울 종로구 사직로 161', coords: [37.576030700049394, 126.97672186606306],
      source: kto(87740), phone: '02-3700-3900', checkLabel: '궁궐 이용 안내', photoLabel: '경회루 외부 풍경 · 입구 사진 아님', imageAlt: '경복궁 경회루와 연못'
    },
    {
      id: 'folk', name: '국립민속박물관', englishName: 'National Folk Museum of Korea', region: 'anguk', category: '박물관 · 생활문화',
      visitWhen: '한국의 생활문화와 옛 물건 살펴보기', cost: '무료 · 경복궁 입장과 별도',
      description: '일상에서 쓰던 물건과 생활문화를 살펴보는 박물관입니다. 일반 전시, 예약형 어린이박물관, 박물관 가게의 이용 조건을 구분해 계획하세요.',
      schedule: '3–10월 09–18시\n11–2월 17시 종료', closure: '설·추석 당일·1월 1일 및 임시 휴관',
      hoursSummary: '본관 계절별 09–17/18시 · 어린이관 별도',
      hours: '본관 3–10월 09:00–18:00, 11–2월 09:00–17:00. 입장 마감 1시간 전. 3–10월 수요일 20시까지. 어린이박물관은 09:30–16:50 예약 회차제, 야간 미운영. 1월 1일·설·추석 당일 및 임시 휴관일 확인.',
      useMode: '본관 일반 관람은 예약 없이 이용 · 어린이박물관은 사전 예약 후 보호자와 관람',
      visitTip: '삼청로 쪽 박물관 출입구를 확인하세요. 경복궁 관람권과 별개이며, 어린이박물관의 잔여 회차는 예약 페이지에서 확인해야 합니다.',
      accessSummary: '유아차·휠체어 대여 안내 · 재고 확인 필요', access: '공식 안내에 생후 24개월 이하 유아차와 휠체어 대여가 있습니다. 대여 재고·보관 공간·필요 동선은 방문 전에 문의해 주세요.',
      unknown: '어린이관 잔여석·대상 연령별 프로그램, 유아차 대여 재고, 당일 부분 폐실',
      address: '서울 종로구 삼청로 37', coords: [37.5819228315018, 126.978843195373],
      source: 'https://nfm.go.kr/home/subIndex/1239.do', sourceLabel: '국립민속박물관 본관 안내', extraSource: folkChildren, englishSource: kto(110875),
      phone: '02-3704-3114', checkLabel: '본관·시설 안내', photoSource: kto(110875), photoLabel: '박물관 외관 · 어린이 전시실 사진 아님', imageAlt: '국립민속박물관 외관과 앞마당',
      notice: { from: '2026-09-30', through: '2026-12-21', text: '상설전시관 1은 9월 30일–12월 21일 휴관 예정입니다. 다른 전시실과 어린이박물관의 운영은 각각 확인해 주세요.', expiredText: '상설전시관 1의 안내된 휴관 기간이 지났습니다. 재개관 여부는 공식 공지를 확인해 주세요.' }
    },
    {
      id: 'mmca', name: '국립현대미술관 서울', mapName: '현대미술관 서울', englishName: 'MMCA Seoul', region: 'anguk', category: '미술관 · 현대미술',
      visitWhen: '실내에서 현대미술 전시 관람하기', cost: '전시별 요금 · 무료 대상 확인',
      description: '여러 전시실에서 현대미술을 만나는 미술관입니다. 관람할 전시를 골라 요금을 확인하고, 작품과 관련된 책·상품은 아트존과 아트북에서 살펴볼 수 있습니다.',
      schedule: '기본 10–18시\n수·토 21시 종료', closure: '설·추석 당일·1월 1일 및 임시 휴관',
      hoursSummary: '기본 10–18시 · 수·토요일 21시까지',
      hours: '월·화·목·금·일 10:00–18:00, 수·토 10:00–21:00. 1월 1일·설·추석 당일 휴관. 2026년 임시 휴관 안내에는 12월 1일이 포함되어 있으므로 방문일 공지를 확인하세요.',
      useMode: '전시별 관람권 이용 · 아트존·아트북 구매는 별도',
      visitTip: '야간개장과 매장 운영시간은 같다고 볼 수 없습니다. 전시별 가격·관람 마감, 외국어 해설 일정, 큰 짐 보관 가능 여부를 확인하세요.',
      accessSummary: '실내 전시 중심 · 건물 사이 야외 이동 가능', access: '전시동·교육동 등 이용 목적에 맞는 입구를 확인하세요. 필요한 무단차 동선과 이동 지원은 미술관에 문의해 주세요.',
      unknown: '선택 전시의 당일 요금·폐실, 매장 재고·시간, 짐 보관 여유',
      address: '서울 종로구 삼청로 30', coords: [37.5785954802057, 126.979987623142],
      source: 'https://www.mmca.go.kr/visitingInfo/seoulInfo.do', sourceLabel: '국립현대미술관 서울 이용 안내', extraSource: 'https://www.mmca.go.kr/pr/FAQ.do', englishSource: kto(76101),
      phone: '02-3701-9500', checkLabel: '전시·시설 안내', photoSource: kto(76101), photoAuthor: '서울관광재단 · 한국관광공사 게시',
      photoLabel: '미술관 외관 · 현재 전시 사진 아님', imageAlt: '국립현대미술관 서울의 벽돌 외관과 간판'
    },
    {
      id: 'workshop', name: '북촌전통공예체험관', mapName: '전통공예체험관', englishName: 'Bukchon Traditional Crafts Experience Center', region: 'anguk', category: '전통공예 · 만들기',
      visitWhen: '요일별 공예 프로그램으로 직접 만들기', cost: '입장 무료 · 체험별 유료',
      description: '요일별로 마련된 전통공예 프로그램을 선택해 직접 만들어 보는 한옥 공간입니다. 가져갈 물건을 만들고 싶은 여행자에게 맞는 체험을 찾아보세요.',
      schedule: '3–10월 10–18시\n11–2월 17시 종료', closure: '설·추석 당일 휴관 · 체험 회차 확인',
      hoursSummary: '계절별 10–17/18시 · 체험은 회차·자리 확인',
      hours: '서울시 예약 안내: 3–10월 10:00–18:00, 11–2월 10:00–17:00. 설·추석 당일 휴관. 온라인 예약 회차 11·12·13·14시. 현장 접수도 가능하나 참여 가능 여부는 확인이 필요합니다.',
      useMode: '입장은 무료 · 체험은 현장 결제 · 온라인 예약 또는 현장 접수',
      visitTip: '체험 종류와 비용이 요일별로 다릅니다. 완성까지 걸리는 시간, 가져갈 수 있는 시점, 외국어 진행 여부를 예약 전에 확인하세요.',
      accessSummary: '한옥 마당과 문턱 · 체험 좌석 동선 확인', access: '한옥 내부 문턱과 체험실별 진입 경로가 다릅니다. 유모차·휠체어로 체험 가능한 자리는 운영자에게 문의해 주세요.',
      unknown: '요일별 재료비·소요시간·언어, 당일 잔여석, 어린이 대상 연령, 무단차 체험 좌석',
      address: '서울 종로구 북촌로12길 24-5', coords: [37.58253, 126.98602], locationSource: '서울시 공공서비스예약 지도',
      source: 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S240122144020674558', sourceLabel: '서울시 체험 예약 안내',
      phone: '02-741-2148', checkLabel: '체험·예약 확인', photoAuthor: '서울시 공공서비스예약 게시',
      photoLabel: '체험관 마당 · 프로그램은 날짜별 상이', imageAlt: '북촌전통공예체험관의 한옥 마당과 체험실'
    },
    {
      id: 'bukchoncenter', name: '북촌문화센터', englishName: 'Bukchon Traditional Culture Center', region: 'anguk', category: '한옥 · 문화 프로그램',
      visitWhen: '한옥 해설과 문화 프로그램 찾아보기', cost: '프로그램별 비용·예약 확인',
      description: '한옥 공간을 둘러보고 전통문화 강좌와 해설 등 프로그램을 만날 수 있는 곳입니다. 손으로 물건을 만드는 체험과, 한옥의 생활문화를 알아가는 경험을 비교하세요.',
      schedule: '시설·프로그램 시간 확인', closure: '월요일 휴관 안내 · 최신 일정 확인',
      hoursSummary: '공간 개방과 프로그램 운영시간 별도 확인',
      hours: '서울한옥포털 시설 목록에는 평일 09:00–18:00·주말 10:00–17:00, 2026년 별도 운영표에는 주말 09:00–17:00와 월요일 휴관이 안내되어 있습니다. 방문 전 최신 일정과 프로그램 회차를 확인하세요.',
      useMode: '한옥 공간 방문 · 강좌·해설·문화행사는 각각 신청 조건 확인',
      visitTip: '일정표에 있는 프로그램이 매일 열리는 것은 아닙니다. 여행 날짜에 가능한 일회성 체험인지, 장기 강좌인지 먼저 확인하세요.',
      accessSummary: '한옥 출입·문턱 · 프로그램 장소 확인', access: '프로그램별 이용하는 방과 동선이 다릅니다. 계단 없는 참여가 필요한 경우 센터에 문의해 주세요.',
      unknown: '당일 개방시간, 단기 참여 가능한 프로그램·언어·비용, 무단차 동선',
      address: '서울 종로구 계동길 37', coords: [37.57906987420643, 126.98642849263337], locationSource: '서울관광재단 장소 지도',
      source: hanok, sourceLabel: '서울한옥포털 시설 안내', extraSource: 'https://hanok.seoul.go.kr/front/kor/service.do',
      englishSource: 'https://english.visitseoul.net/PalaceArea/Bukchon-Traditional-Culture-Center-k/ENP018916',
      checkLabel: '프로그램 일정 확인', checkSource: 'extraSource', photoSource: 'https://english.visitseoul.net/PalaceArea/Bukchon-Traditional-Culture-Center-k/ENP018916',
      photoAuthor: '서울관광재단 게시', photoLabel: '문화센터 입구 · 사진 속 행사는 과거 안내', imageAlt: '북촌문화센터의 한옥 대문',
      reviewNote: '공식 자료 간 주말 개방시간 차이가 있어 단일 시간으로 확정하지 않음'
    }
  ];
  additions.forEach(place => {
    const defaults = {
      locationSource: '한국관광공사 장소 좌표', sourceLabel: '한국관광공사 장소 안내',
      checkSource: 'source', photoAuthor: '한국관광공사 게시', photoDate: '촬영일 미상',
      image: `images/places/${place.id}.jpg`, preview: `images/places/optimized/${place.id}-480.webp`,
      largePreview: `images/places/optimized/${place.id}-960.webp`
    };
    const record = { ...defaults, ...place };
    record.checkUrl = record[record.checkSource];
    record.review = { checkedAt: '2026-09-29', fields: '공개 방문 안내·주소·위치', note: record.reviewNote || '당일 운영·예약 가능 여부는 방문 전 확인' };
    if (!record.englishSource && record.source.startsWith('https://english.')) record.englishSource = record.source;
    window.ALLEY_PLACES.push(record);
  });

  window.ALLEY_CATEGORIES = [
    { id: 'all', label: '모두' }, { id: 'food', label: '먹거리' }, { id: 'rest', label: '쉬기·산책' },
    { id: 'culture', label: '문화·역사' }, { id: 'make', label: '체험·선물' },
    { id: 'weather', label: '비·더위' }, { id: 'family', label: '아이와' }
  ];
  const original = { jeongdok: ['rest', '쉬기'], suseongdong: ['rest', '바깥 풍경'], baeryeom: ['culture', '공예 전시'], yisang: ['culture', '골목 이야기'] };
  window.BLIND_SPOT_PAIRS.forEach(pair => {
    [pair.category, pair.shortTitle] = original[pair.id];
  });
  const newPairs = [
    { id: 'seochon-meal', region: 'seochon', category: 'food', shortTitle: '서촌 한 끼', title: '시장에서 고를까, 앉아서 먹을까?',
      reason: '음식을 골라 담는 도시락과 한옥 식당의 삼계탕을 비교해요.', placeIds: ['tongin', 'tosokchon'], notice: '도시락카페는 시장보다 일찍 닫아요. 늦은 식사라면 종료시간을 먼저 확인하세요.' },
    { id: 'anguk-meal', region: 'anguk', category: 'food', shortTitle: '안국 한 끼', title: '빵과 커피, 따뜻한 국수 한 그릇',
      reason: '베이커리에서 가볍게 먹을지, 식당에서 면 요리로 식사할지 골라요.', placeIds: ['onion', 'hwangsaengga'],
      choices: { onion: { visitWhen: '빵과 음료로 가볍게 먹기' } } },
    { id: 'royal-anguk', region: 'anguk', category: 'culture', shortTitle: '왕실 공간', title: '궁궐을 넓게, 왕실 가옥을 가까이',
      reason: '창덕궁의 여러 전각과 운현궁의 가옥·마당을 비교해요.', placeIds: ['changdeok', 'unhyeon'], notice: '두 곳 모두 기본 월요일 휴궁입니다. 창덕궁 후원은 전각과 별도 관람이에요.' },
    { id: 'royal-seochon', region: 'seochon', category: 'culture', shortTitle: '왕실 문화', title: '궁궐을 걸을까, 유물을 볼까?',
      reason: '경복궁역 주변에서 야외 궁궐과 실내 박물관을 골라요.', placeIds: ['gyeongbok', 'gogung'], notice: '경복궁은 화요일, 고궁박물관은 매월 마지막 월요일이 기본 휴관일입니다. 공휴일 예외를 확인하세요.' },
    { id: 'hands-on', region: 'anguk', category: 'make', shortTitle: '전통문화 체험', title: '직접 만들거나, 한옥문화를 배우거나',
      reason: '요일별 공예 만들기와 한옥 해설·문화 프로그램을 비교해요.', placeIds: ['workshop', 'bukchoncenter'], notice: '공간이 열려 있어도 원하는 프로그램은 없을 수 있어요. 날짜·비용·진행 언어를 먼저 확인하세요.' },
    { id: 'family-museum', region: 'anguk', category: 'family', shortTitle: '어린이박물관', title: '아이와 함께 체험할 곳을 찾는다면',
      reason: '공예를 만나는 어린이관과 생활문화를 만나는 어린이관을 비교해요.', placeIds: ['craft', 'folk'],
      choices: {
        craft: { visitWhen: '어린이박물관에서 공예 체험하기', cost: '어린이관 무료 · 사전 예약', schedule: '예약 회차별 이용', closure: '모든 월요일 휴관', checkLabel: '어린이관 예약 안내', checkUrl: craftBooking,
          accessSummary: '어린이관 예약 회차·대상 연령·보호자 인원 확인', notice: null,
          useMode: '어린이박물관 사전 예약 · 대상 연령과 동반 보호자 인원은 프로그램별 확인',
          visitTip: '일반 전시실 야간개관과 어린이관 회차는 다릅니다. 예약한 날짜와 회차, 입장 마감 조건을 확인하세요.',
          review: { checkedAt: '2026-09-29', fields: '어린이관 관람·예약 안내', note: '잔여석과 대상 연령은 선택한 프로그램에서 확인' } },
        folk: { visitWhen: '어린이박물관에서 생활문화 체험하기', cost: '어린이관 무료 · 사전 예약', schedule: '09:30–16:50 중 예약 회차', closure: '야간 미운영 · 휴관일 확인', checkLabel: '어린이관 예약 안내', checkUrl: folkChildren,
          accessSummary: '사전 예약 후 보호자와 관람 · 회차별 이용',
          useMode: '어린이박물관 사전 예약 후 보호자와 관람 · 본관 일반 전시와 별도 조건' }
      }, notice: '두 어린이박물관 모두 사전 예약이 필요해요. 대상 연령·보호자 인원·잔여 회차를 확인하세요.' },
    { id: 'rainy-day', region: 'anguk', category: 'weather', shortTitle: '실내 전시', title: '비가 오거나 너무 더운 날',
      reason: '실내 공예 전시와 현대미술 전시 중 관심 있는 쪽을 골라요.', placeIds: ['craft', 'mmca'],
      notice: '실내 전시 중심이지만 건물 사이에서는 밖으로 나올 수 있어요. 전시 교체와 휴관도 확인하세요.' },
    { id: 'souvenirs', region: 'anguk', category: 'make', shortTitle: '여행 선물', title: '여행을 기억할 작은 선물을 고른다면',
      reason: '생활문화 상품과 현대미술 상품·책의 차이를 살펴봐요.', placeIds: ['folk', 'mmca'],
      choices: {
        folk: { visitWhen: '박물관 가게에서 전통문화 상품 보기', cost: '상품별 유료', schedule: '매장 운영시간 별도 확인', closure: '본관 안내에서 매장 확인', checkLabel: '박물관 가게 안내', checkUrl: 'https://nfm.go.kr/home/subIndex/1239.do',
          useMode: '박물관 가게에서 상품별 결제 · 전시 관람료와 상품 가격은 별도', accessSummary: '가게 입구·재고·포장 가능 여부는 문의' },
        mmca: { visitWhen: '아트존·아트북에서 미술 상품과 책 보기', cost: '상품별 유료', schedule: '매장 운영시간 별도 확인', closure: '야간 전시와 매장 시간은 별도', checkLabel: '아트존·아트북 안내', checkUrl: 'https://www.mmca.go.kr/visitingInfo/seoulInfo.do',
          useMode: '아트존·아트북에서 상품별 결제 · 전시 관람권과 별도', accessSummary: '매장 입구·시간·재고는 방문 전 확인' }
      }, notice: '사진은 박물관 외관입니다. 전시 관람료와 상품 가격은 다르며, 상품 재고·가격·포장은 매장에 확인하세요.' }
  ];
  newPairs.forEach(pair => { pair.regionLabel = pair.region === 'anguk' ? '안국' : '서촌'; });
  window.BLIND_SPOT_PAIRS.unshift(...newPairs.slice(0, 4));
  window.BLIND_SPOT_PAIRS.push(...newPairs.slice(4));
  window.ALLEY_CHOICE = (place, pair) => ({ ...place, ...(pair?.choices?.[place.id] || {}) });
})();
