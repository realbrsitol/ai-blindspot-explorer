"""Create 100 explicitly synthetic, rule-based cases; never field responses.

No network or browser interaction. Source assertions were manually reviewed.
The seed shuffles presentation order only, not a real visitor population.
"""
import csv
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAIRS = [
    dict(region='안국', name='어니언 안국 / 정독도서관',
         space='한옥 실내·마당 / 자료실·야외 정원',
         cost='음료·빵 구매 / 자료 열람 무료',
         hours='카페와 도서관의 서로 다른 운영시간은 각각 상세에서 확인',
         access='어니언 단차 안내, 도서관의 계단 없는 경로는 확인 필요',
         location='장소 대표 좌표이며 실제 입구 확정 정보 없음'),
    dict(region='서촌', name='스태픽스 / 수성동 계곡',
         space='실내·야외 테라스 / 야외 산책로',
         cost='음료·디저트 구매 / 무료',
         hours='스태픽스 최신 운영시간은 매장 확인, 계곡은 기상·현장 통제 확인',
         access='카페 언덕 및 편의시설 정보 충돌, 계곡의 경사·이용 구간 확인 필요',
         location='수성동 계곡은 대략적 좌표이며 점선 핀으로 표시'),
    dict(region='안국', name='서울공예박물관 / 계동 배렴 가옥',
         space='실내 전시실 / 한옥 실내·마당',
         cost='무료·대관전시 예외 / 프로그램별 확인',
         hours='양쪽 월요일 휴관 안내, 박물관 야간 운영 예외는 공식 안내 확인',
         access='박물관 시설 안내와 문의 제공, 배렴 가옥 문턱·마당 동선 확인 필요',
         location='장소 대표 좌표이며 실제 입구 확정 정보 없음'),
    dict(region='서촌', name='대오서점 / 이상의 집',
         space='옛 서점 실내·마당 / 실내 기념공간',
         cost='음료 또는 관람 엽서 구매 / 최신 관람료 확인 필요',
         hours='대오서점 출처별 시간 확인 필요, 이상의 집 월요일 휴관 안내',
         access='대오서점 단차 안내, 이상의 집 계단 없는 관람 동선 확인 필요',
         location='이상의 집은 대략적 좌표이며 점선 핀으로 표시'),
]

# condition, proposed path, rule, synthetic voice, minimal next step
CONDITIONS = [
 ('초행·시간 여유·경험 비교', '목록→양쪽 상세→선택', 'space', '어떤 경험이 다른지는 알겠어요.', '사진·공간·비용의 공통 비교 구조 유지'),
 ('약속까지 30분 남음', '목록→운영 정보→지도', 'hours', '지금 가도 되는지부터 알고 싶어요.', '운영 요약을 상세 상단에 올리고 확인 링크를 구체적으로 표기'),
 ('추가 지출 없이 머물고 싶음', '비용 행→상세', 'cost', '무료인지와 꼭 구매해야 하는 조건을 먼저 보고 싶어요.', '무료·구매 필요·금액 미확인을 구분'),
 ('비가 오는 상황을 가정', '공간 행→방문 팁', 'space', '실내에서 머물 수 있는지 먼저 비교하고 싶어요.', '실내·야외 구분 유지; 자동 날씨 기능은 보류'),
 ('유모차 동반', '상세→방문 팁과 이동 편의', 'access', '도착해도 들어갈 수 있는지 확신하기 어려워요.', '입구 사진·단차 정보를 확인해 핵심 제약만 앞에 표시'),
 ('계단 없는 이동이 필요함', '상세→접근성→운영자 확인', 'access', '사전 문의만으로는 지금 장소를 정하기 어려워요.', '확인한 경로와 미확인 경로를 명확하게 구분'),
 ('긴 걷기를 피하고 싶음', '지도→입구·경사 확인', 'location', '지도상 위치보다 실제로 걷는 길이 중요해요.', '입구 좌표부터 확인; 임의 도보 시간 생성 금지'),
 ('큰 글씨를 선호함', '목록의 보조 설명과 비용 읽기', 'type', '작은 회색 설명을 더 편하게 읽고 싶어요.', '핵심 정보 글씨 확대 후 실제 확대·읽기 관찰'),
 ('한 손 사용', '목록→지도 전환', 'overlay', '아래 버튼은 누르기 쉬운데 내용을 덮어요.', '버튼 전용 하단 영역을 확보하거나 겹치지 않는 배치로 변경'),
 ('390px 폭의 작은 화면', '첫 화면→비용 행', 'overlay', '처음 보이는 카드의 비용을 버튼이 가려요.', '390px에서 확인된 가림부터 수정'),
 ('야외 강한 햇빛을 가정', '지도 라벨과 보조 문구 읽기', 'type', '지도 이름과 작은 설명이 더 또렷했으면 해요.', '실제 야외 관찰 후 글자·면 대비 조정'),
 ('한국어가 익숙하지 않음', '지역→설명→지도', 'language', '장소 사진은 보이는데 이용 조건을 이해하기 어려워요.', '대상 언어 수요 확인 후 짧은 핵심 정보부터 지원 검토'),
 ('느린 데이터 연결을 가정', '사진 목록→지도 타일', 'network', '사진과 지도가 늦을 때 먼저 읽을 정보가 필요해요.', '이미지 크기·로딩 상태를 먼저 측정; 무조건 PWA 추가하지 않기'),
 ('인터넷이 끊긴 상황을 가정', '열어둔 상세→지도', 'offline', '주소라도 남아 있으면 좋겠어요.', '오류 시 주소·출처와 재시도 경로 유지'),
 ('동네에 익숙한 재방문자', '지역 선택→공간 비교', 'space', '위치 설명보다 두 공간의 차이가 유용해요.', '목적별 비교를 유지하고 반복적인 소개 문장을 줄이기'),
 ('나중에 다시 방문할 계획', '상세→다시 찾을 방법', 'revisit', '나중에 이 장소만 다시 찾고 싶어요.', '기존 상세 URL 공유 가능성을 먼저 활용; 계정·즐겨찾기는 보류'),
 ('동행자와 선택을 상의함', '양쪽 상세→상대 장소 전환', 'counterpart', '같이 보는 장소로 빨리 바꾸고 싶어요.', '상대 장소 링크를 운영 정보보다 위에서 찾을 수 있게 배치 검토'),
 ('현재 위치에서 가까운 곳 선호', '전체 지도→출발점 찾기', 'origin', '내가 어디 있는지 모르니 가까운 쪽을 못 고르겠어요.', '외부 지도에서 거리 확인 흐름을 명확히; GPS 재도입은 별도 판단'),
 ('목적을 아직 정하지 않음', '네 상황 목록 훑기', 'navigation', '네 가지 상황을 먼저 한눈에 보고 싶어요.', '짧은 상황별 이동 링크로 긴 스크롤 줄이기'),
 ('정보 출처를 중요하게 봄', '상세→확인일→출처', 'sources', '언제 어디서 확인한 정보인지 보여서 좋아요.', '출처와 확인일 유지; 현재 영업 중으로 오해할 표시 금지'),
 ('진행 중인 전시·행사를 찾음', '상세→공식 일정', 'program', '공간 소개 다음에는 오늘 무엇을 볼 수 있는지 궁금해요.', '해당 장소의 공식 일정 링크 이름을 구체화'),
 ('잠깐 앉아 쉴 자리 필요', '목적 설명→좌석 조건', 'seats', '쉴 수 있다는 말과 실제 앉을 수 있다는 건 달라요.', '좌석 종류·이용 조건 확인; 실시간 빈자리 추정 금지'),
 ('사진으로 현장 입구를 찾음', '사진→지도→현장 식별 가정', 'location', '이 사진이 입구인지 알면 찾기 쉬울 것 같아요.', '사진에 외관·내부·입구 구분을 제공'),
 ('키보드로 지도 핀 조작', '지도 핀 초점→Enter→선택', 'keyboard', '핀에 초점은 가는데 선택이 안 되는지 헷갈려요.', '관찰 환경의 Enter 미반응 재현 및 표준 키보드 지원 점검'),
 ('외부 지도에서 경로를 바로 기대', '상세 길찾기→연결 주소 확인', 'routing', '길찾기를 눌렀는데 장소 검색부터 해야 하나요?', '검색 링크라면 네이버 지도에서 보기로 정확히 표기'),
]

COMMON = {
 'type': ('CODE: 보조 라벨 12px·비교 값 14px; UI: 390px 화면 확인. 야외·확대 환경 미실행', 'UI 마찰 가능'),
 'overlay': ('UI: 390×844 첫 화면의 고정 지도 버튼이 비용 행 일부와 겹침', 'UI 마찰 확인'),
 'language': ('CODE: 한국어 콘텐츠, 언어 전환 없음. 외국어 이용자 세션 미실행', '추가 확인 필요'),
 'network': ('CODE: 이미지 lazy loading·오류 대체 문구 및 외부 지도 타일. 지연 주입 미실행', '실행 미확인'),
 'offline': ('CODE: 외부 타일 필요; 기존 서비스워커 해제 코드. 실제 오프라인 전환 미실행', '실행 미확인'),
 'revisit': ('CODE: #place/id 직접 링크 제공, 저장 전용 기능 없음', '판단 근거 일부 있음'),
 'counterpart': ('UI: 상세 하단의 상대 장소 링크로 전환 가능. 첫 상세 화면에서는 링크가 아래에 있음', 'UI 마찰 가능'),
 'origin': ('CODE/UI: 지도에 현재 위치·출발점·내 경로 표시 없음', '추가 확인 필요'),
 'navigation': ('UI/CODE: 목적별 네 카드가 세로 배치, 지역 필터만 있음', 'UI 마찰 가능'),
 'sources': ('UI: 상세에 자료 확인일과 공식 출처 링크 제공', '판단 근거 있음'),
 'program': ('CODE: 장소 설명과 공식 출처는 있으나 진행 중인 프로그램 목록은 없음', '추가 확인 필요'),
 'seats': ('CODE: 공간 유형·방문 팁은 있으나 실시간 좌석 상태는 없음', '추가 확인 필요'),
 'keyboard': ('UI: 수성동 핀 Enter 후 미선택, 포인터 클릭 후 선택 확인. 다른 환경 미확인', '재현 범위 확인 필요'),
 'routing': ('CODE/UI: 길찾기 링크 주소가 map.naver.com/p/search/…임. 외부 앱 실행·복귀 미실행', '문구와 연결 기능 불일치'),
}

def evaluate(pair, rule):
    if rule in COMMON:
        return COMMON[rule]
    detail = pair[rule]
    state = '판단 근거 있음' if rule == 'space' else '추가 확인 필요'
    return f'CODE: js/data.js — {detail}', state

def main():
    combinations = [(pair, condition) for pair in PAIRS for condition in CONDITIONS]
    random.Random(20260929).shuffle(combinations)
    rows = []
    for number, (pair, condition) in enumerate(combinations, 1):
        context, path, rule, voice, change = condition
        evidence, outcome = evaluate(pair, rule)
        rows.append({
            '사례ID': f'S{number:03}', '유형': '합성·가설·실제응답아님',
            '지역': pair['region'], '비교쌍': pair['name'], '사용조건_가정': context,
            '가상탐색경로_실행로그아님': path, '판단': outcome,
            '근거': evidence, '합성발언_실제인용아님': voice,
            '최소개선안': change, '현장확인질문': f'{context} 조건에서 {pair["name"]} 중 한 곳을 고를 때 무엇을 먼저 확인하나요?',
            '실행범위': '공통 대표 흐름 관찰+코드 기반 규칙평가; 개별 브라우저 세션 미실행',
        })
    output = ROOT / 'synthetic_cases.csv'
    with output.open('w', encoding='utf-8-sig', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f'{len(rows)} synthetic cases written to {output}; real respondents: 0')

if __name__ == '__main__':
    main()
