# 장소 정보 확인 기록

자료 정리일: 2026-09-29. 웹에 게시된 자료를 바탕으로 하며 현장 조사나 실시간 영업 상태 확인은 하지 않았다. v20부터 상세 화면에 장소별 확인 범위와 날짜를 표시하며, 원문을 다시 확인하지 못한 자료에는 날짜를 임의로 부여하지 않는다.

## v26 확장 — 2026-09-30

새 17곳의 장소·기본 방문 정보·주소·대표 위치를 추가했다. 전체는 36곳, 목적 9개이며 각각 4쌍·8곳이다. 새 장소별 출처 링크와 자료 간 차이, 카테고리 선정 근거는 [v26 기록](research/CATEGORY_EXPANSION_V26.md), 원본 사진 URL·좌표는 [자산 명세](research/catalog_assets_v26.json)를 참고한다.

잘빠진메밀은 국·영문 주소 차이 때문에 대략적 지도 핀으로 구분했다. 체부동잔치집돼지갈비와 삼청동수제비는 종료시간 재확인을 표시했다. 무료 관람은 일반 공개 구역 기준이며 체험·상품·예약 조건을 분리했다. 기존 장소의 자료 확인일은 유지했다.

## v20 재확인 범위

아래 v20 표는 당시 범위다. v23 확장은 문서 하단 표, 최신 v26 확장은 위 연결 문서를 참고한다.

| 장소 | 이번에 읽은 근거 | 앱 반영 / 남은 사항 |
| --- | --- | --- |
| 서울공예박물관 | [관람안내](https://craftmuseum.seoul.go.kr/preview/visit) | 기본 시간·월요일 예외·입장 마감·무료 관람 예외·어린이 예약·음식물 제한·대표 전화 02-6450-7000. 2026-09-15~11-30 야간개관 안내는 기본 시간과 분리; 요일별 정확한 종료시간은 링크 확인 |
| 배렴 가옥 | [서울한옥포털](https://hanok.seoul.go.kr/front/util/bcgTour03.do?lang=KOR) | 10–18시·월요일 휴관·02-765-1375. 운영자 프로그램 사이트는 이번 열람이 시간 초과되어 관람료·프로그램 조건 미확인 유지 |
| 대오서점 | [한국관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=198592) | 12–21시·음료 또는 관람 엽서 세트 구매·02-735-1349. 가격·휴무와 무단차 진입은 미확인 |
| 스태픽스 | [열린관광](https://access.visitkorea.or.kr/food/detail.do?cotId=5fcd1c8c-4d80-443e-a5ed-3bad2e9ebbaf) | 언덕·야외 테이블 및 매장 Instagram 연결 확인. 페이지에 현재 시간·가격 없음. 편의시설 표는 다른 기존 자료와 상충하므로 접근 가능 보장으로 사용하지 않음 |
| 수성동 계곡 | [한국관광공사](https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=a60c5c16-e507-478a-b3e4-998ee5ccca7a) | 장소와 주출입구 단차 안내 확인. 정확한 입구·무단차 구간·당일 통제는 미확인. 상시 개방은 기존 수집 안내로 유지 |
| 정독도서관·이상의 집 | 기존 공식 링크 재접근 실패 | 기본 정보 유지, ‘기존 수집 자료·재확인 필요’로 표시. 이번 날짜를 새로운 출처 확인일로 넣지 않음 |
| 어니언 안국 | 이번 작업에서 원문 재확인하지 않음 | 기존 수집 자료 유지, 영업시간·이용 조건 재확인 표시 |

전화번호는 공개된 기관·매장 대표 번호 세 곳만 표시한다. 수집 날짜는 영업 상태·좌석·접근성에 대한 실시간 보증이 아니다. 알려진 조건과 미확인 질문은 `js/data.js`의 `visitConditions`에서 분리하며, 날짜가 있는 임시 안내는 한국 날짜 기준으로 만료 처리한다.

## 방문 정보와 좌표

| 장소 | 방문 정보 출처 | 지도 좌표 근거 / 남은 사항 |
| --- | --- | --- |
| 어니언 안국 | [한국관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=191156) | 해당 페이지 위치 메타데이터로 기존 좌표 수정 |
| 정독도서관 | [공식 이용시간](https://jdlib.sen.go.kr/jdlib/html.do?menu_idx=93) | OpenStreetMap 건물 중심, 출입구 좌표 아님 |
| 스태픽스 | [한국관광공사](https://access.visitkorea.or.kr/food/detail.do?cotId=5fcd1c8c-4d80-443e-a5ed-3bad2e9ebbaf) | 페이지 위치 데이터로 수정. 관광 페이지 간 운영·접근성 정보가 달라 확정 안내 대신 매장 확인 표시 |
| 수성동 계곡 | [한국관광공사](https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=a60c5c16-e507-478a-b3e4-998ee5ccca7a) | 기존 대략적 좌표 유지. 점선 핀과 설명으로 구분. 실제 입구 좌표 추가 확인 필요 |
| 서울공예박물관 | [공식 관람안내](https://craftmuseum.seoul.go.kr/preview/visit) | [한국관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=186458) 위치 메타데이터. 2026년 한시적 야간 운영은 공식 안내 링크로 확인 |
| 계동 배렴 가옥 | [서울한옥포털](https://hanok.seoul.go.kr/front/util/bcgTour03.do?lang=KOR) | [국가유산포털](https://www.heritage.go.kr/heri/cul/culSelectDetail.do?ccbaCpno=4411100850000&pageNo=1_1_1_1) 지도 연결 좌표로 수정. 참가비는 프로그램별 확인 |
| 대오서점 | [한국관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=198592) | 해당 페이지 위치 메타데이터로 수정. 운영시간에 출처와 방문 전 확인 안내 병기 |
| 이상의 집 | [문화유산국민신탁](https://nationaltrustkorea.org/document/location) | 기존 대략적 좌표 유지. 점선 핀으로 구분. 실제 입구 좌표 및 최신 관람료 추가 확인 필요 |

좌표가 확인된 곳도 건물 또는 장소의 대표 위치이며 보행 출입구를 보장하지 않는다. 길찾기는 이름과 주소로 네이버 지도 검색에 연결한다. 임의의 도보 소요시간, 혼잡도, 영업 중 상태는 표시하지 않는다.

## 사진

19곳 모두 실제 장소 사진으로 연결했다. Commons 2장과 공식 관광·운영기관 참고 사진 17장의 출처 및 이용허락 확인 상태는 [사진 기록](images/places/README.md)에 구분했다. 이 작업에는 공개 배포가 포함되지 않는다.

## 비교 선정

식사와 전시를 다음 방문 순서로 묶었던 런던베이글뮤지엄–배렴 가옥 비교를 서울공예박물관–배렴 가옥으로 변경했다. 네 쌍 모두 같은 방문 목적 안에서 경험과 공간의 차이를 비교하도록 편집했다. 특정 장소가 더 낫다는 점수나 추천 순위는 부여하지 않는다.

## 실제 이용자 관찰

실제 참가자 관찰은 아직 진행하지 않았다. 향후 휴대폰으로 ① 쉴 곳 두 곳 비교 ② 상대 장소 상세 열기 ③ 지도 위치 확인 ④ 목록 복귀를 요청하고, 망설인 지점·잘못 누른 곳·선택 이유를 기록한다. 화면 개선만으로 사용성 검증이 완료됐다고 간주하지 않는다.

## v23 신규·용도별 정보 확인

2026-09-29 공개 자료 기준. 아래 출처의 주소·기본 운영·방문 조건을 반영했다. 가격 미확인 항목은 숫자로 추정하지 않았다. 새 장소의 대표 위치는 한국관광공사(9곳), 서울시 공공서비스예약(체험관), 서울관광재단(문화센터)의 페이지 메타데이터다.

| 장소 | 근거 | 적용 / 남은 확인 |
| --- | --- | --- |
| 통인시장 | [관광공사 장소](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=79811), [도시락 이용 설명](https://english.visitkorea.or.kr/svc/contents/infoHtmlView.do?menuSn=219&vcontsId=194514) | 시장·도시락 시간 분리, 엽전 이용 과정. 주말 시간·휴무·최소 구매액 자료 상충 → 최신 시장 안내 확인 |
| 토속촌삼계탕 | [관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=97919) | 10–22시·주문 마감 21시, 주소·전화. 현재 가격·대기 미확인, 접근성 자료 상충 |
| 황생가칼국수 | [관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=86236) | 11–21:30, 주소·전화·사골 칼국수. 가격·대기·주문 마감 별도 문의 |
| 창덕궁 | [관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=94399), [궁능유적본부](https://royal.khs.go.kr/ROYAL/contents/R404000000.do?schGroupCode=cdg) | 계절별 종료·월요일 휴궁, 전각 일반 3,000원, 후원 별도 요금·예약·회차 |
| 운현궁 | [운영기관](https://www.unhyeongung.or.kr/), [야간 시범 공지](https://www.unhyeongung.or.kr/sub/notice_guide/notice.php?abmode=view&bfsort=ino&bsort=desc&code=B10&group=basic&no=1974), [관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=111253) | 기본 계절별 시간과 가을 한시 야간개방 분리. 목요일 종료시간은 홈페이지의 별도 안내 확인 |
| 경복궁 | [관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=87740) | 계절별 종료·화요일 휴궁, 일반 3,000원. 감면·특별 관람 개별 확인 |
| 국립고궁박물관 | [운영기관](https://gogung.go.kr/gogung/main/contents.do?menuNo=800011), [사진·좌표](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=106970) | 09:30–17:30, 토·마지막 수요일 21시. 마지막 월요일 휴관·공휴일 예외. 운영기관 우선 |
| 국립민속박물관 | [본관·편의시설](https://nfm.go.kr/home/subIndex/1239.do), [어린이관](https://nfm.go.kr/home/subIndex/1186.do), [사진·좌표](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=110875) | 본관·어린이관·가게 용도 분리, 어린이 예약·야간 미운영, 대여 안내. 가게 시간·재고 미확인 |
| 국립현대미술관 서울 | [이용 안내](https://www.mmca.go.kr/visitingInfo/seoulInfo.do), [FAQ](https://www.mmca.go.kr/pr/FAQ.do), [사진·좌표](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=76101) | 기본 10–18시·수토 21시, 전시별 요금, 아트존·아트북. 매장 시간·재고는 야간 전시와 분리 |
| 북촌전통공예체험관 | [서울시 예약](https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S240122144020674558) | 계절별 시설 시간·회차·유료 체험·현장 접수. 현재 프로그램별 가격·언어·자리 확인 |
| 북촌문화센터 | [시설 목록](https://hanok.seoul.go.kr/front/util/bcgTour03.do?lang=KOR), [2026 운영표](https://hanok.seoul.go.kr/m/kor/bbs/selectBoardArticle.do?bbsId=BBSMSTR_000000000031&nttId=2717), [프로그램](https://hanok.seoul.go.kr/front/kor/service.do), [관광재단](https://english.visitseoul.net/PalaceArea/Bukchon-Traditional-Culture-Center-k/ENP018916) | 공식 주말 시간 상충 → 최신 일정 확인. 단기 참여·장기 강좌 구분 |
| 서울공예박물관 어린이관 | [관람](https://craftmuseum.seoul.go.kr/preview/visit), [개인 예약 목록](https://craftmuseum.seoul.go.kr/chimsm/exhibit/plan/list/1) | 무료 사전 예약·모든 월요일 휴관. 프로그램별 나이·인원·잔여석 확인, 일반 전시 야간 안내와 분리 |

v23에서는 기관·매장에 공개된 대표 전화를 새 장소 상세에도 추가했다. 영문명과 공개 영어 관광 안내는 확인된 곳에만 제공한다. 기존 장소의 모든 정보를 새로 확인한 것은 아니며, 기존 확인일을 일괄 갱신하지 않았다.
