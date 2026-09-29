"""Reconcile the existing 100 synthetic case IDs with the v19 audit.

This is a report generator, not browser automation or a user simulation engine.
UI evidence comes from the representative observations documented in the report.
"""
import csv
import hashlib
import json
from pathlib import Path
from build_synthetic_cases import CONDITIONS, PAIRS

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parent

# condition -> verdict, evidence, observations, issue IDs, current assessment, next check
REVIEWS = {
    '초행·시간 여유·경험 비교': ('개선 유지·판단 정보 보완', 'UI/CODE/HYP', 'U01/U02/U03', 'R01/R06/R10', '사진과 공통 비교는 유지. 운영·제약 대조는 상세 왕복 필요.', '두 곳의 차이와 방문 제약을 목록에서 설명할 수 있는지 관찰'),
    '약속까지 30분 남음': ('부분 개선·잔여', 'UI/CODE/HYP', 'U02/U03/U05', 'R01/R02/R03', '운영 요약은 상세 상단에 있음. 목록·지도에서는 운영과 공통 휴무가 안 보임.', '짧은 시간에 양쪽 운영을 대조하는 실제 조작 관찰'),
    '추가 지출 없이 머물고 싶음': ('부분 개선·자료 부족', 'UI/CODE/HYP', 'U01/U02', 'R02/R04', '비용 행은 읽을 수 있음. 구매 조건과 금액 미확인은 남음.', '일반 이용 비용과 별도 프로그램 비용을 확인'),
    '비가 오는 상황을 가정': ('비교 근거 있음·조건 미실행', 'UI/CODE/HYP/UNTESTED', 'U02', 'R03/R04', '실내·야외 구분은 존재. 비 오는 날 두 후보의 목적 달성 여부는 미확인.', '우천 시 실제 이용 가능한 공간·동선 확인'),
    '유모차 동반': ('부분 개선·현장 미확인', 'CODE/HYP/UNTESTED', '', 'R02/R04', '방문 제약 요약은 존재. 출입 가능 경로를 보장할 자료는 부족.', '입구·단차·경사·이용 구간 현장 확인'),
    '계단 없는 이동이 필요함': ('부분 개선·현장 미확인', 'CODE/HYP/UNTESTED', '', 'R02/R04', '계단 없는 동선은 여러 장소에서 사전 확인 요구. 실제 접근성 미확인.', '운영기관의 확인된 동선과 미확인 항목 분리'),
    '긴 걷기를 피하고 싶음': ('부분 개선·경로 미확인', 'UI/CODE/HYP/UNTESTED', 'U05', 'R04/R09/R13', '축척·이름 지도 있음. 출발점·입구·경사 포함 실제 보행 부담은 판단 불가.', '외부 지도에서 출발점을 설정하고 경로 확인하는 흐름 관찰'),
    '큰 글씨를 선호함': ('기본 가독성 개선·확대 미실행', 'UI/CODE/UNTESTED', 'U01/U07', 'R06/R07/R09', '비교 값15px. 320px 가로 넘침은 없었으나 지도 주의문12px이고 실제 큰 글씨 미실행.', '기기 글자 확대와 브라우저 확대를 별도로 확인'),
    '한 손 사용': ('가림 개선·도달성 미실행', 'UI/CODE/HYP/UNTESTED', 'U01/U05/U06', 'R07', '내용 가림 제거. 상단 전환·하단 내부 스크롤의 엄지 도달성은 미확인.', '실제 한 손으로 지역 전환·마지막 장소 선택 관찰'),
    '390px 폭의 작은 화면': ('가림 개선·새 스크롤 마찰', 'UI/CODE/HYP', 'U01/U05/U06', 'R06/R07', '첫 비용 행 가림 없음. 지도 이름 목록 마지막 두 곳은 내부 스크롤 아래.', '8번째 이름을 별도 설명 없이 찾을 수 있는지 관찰'),
    '야외 강한 햇빛을 가정': ('개선 일부·환경 미실행', 'UI/CODE/UNTESTED', 'U05', 'R09', '선택 색·이름 표시는 있음. 실제 햇빛에서 읽기·명암은 미확인.', '야외에서 지도명·주의문 읽기와 조작 확인'),
    '한국어가 익숙하지 않음': ('수요·이해도 미확인', 'CODE/HYP/UNTESTED', '', '', '한국어 중심이며 번역은 없음. 언어 수요 조사 없이 다국어 기능을 추가하지 않음.', '필요 언어와 비용·운영 조건 이해도부터 조사'),
    '느린 데이터 연결을 가정': ('새 비용 확인·지연 미실행', 'CODE/HYP/UNTESTED', '', 'R05/R14', '지도 JS와 글꼴 파일이 큼. 목록이 지도 defer 스크립트 순서 뒤에 위치. 실제 대기시간 미측정.', '느린 통신에서 목록 독립 로딩 및 지도 지연 후 회복 측정'),
    '인터넷이 끊긴 상황을 가정': ('안내 구현·장애 미실행', 'CODE/UNTESTED', '', 'R05/R14', '연결 끊김·재시도·주소 정보 코드 있음. 최초 오프라인 로드와 복구 실행은 미확인.', '이미 연 상태와 최초 진입 실패를 나누어 확인'),
    '동네에 익숙한 재방문자': ('탐색 개선·중복 잔여', 'UI/CODE/HYP', 'U01/U02/U10', 'R06/R11', '상황 바로 이동은 작동. 지도와 연결되지 않는 A/B 및 반복 설명이 남음.', '알고 있는 장소에서 달라진 운영 정보만 쉽게 찾는지 관찰'),
    '나중에 다시 방문할 계획': ('링크 구현·미래 정보 보완', 'CODE/HYP/UNTESTED', '', 'R11/R12', '장소 hash 링크·복사 코드 있음. 임시 안내 유효기간 관리와 비교 맥락 공유는 부족.', '다른 날짜 재방문 및 직접 링크 재진입 확인'),
    '동행자와 선택을 상의함': ('전환 개선·비교 공유 잔여', 'UI/CODE/HYP', 'U03/U04/U05', 'R01/R12', '상대 상세·두 장소 전환 작동. 링크 복사는 현재 장소만 유지.', '장소 하나/두 곳 비교 중 무엇을 보내려 하는지 확인'),
    '현재 위치에서 가까운 곳 선호': ('위치 비교 개선·출발점 없음', 'UI/CODE/HYP/UNTESTED', 'U05/U09', 'R04/R13', '지도 이름·축척으로 상대 위치를 볼 수 있음. 현재 위치·실제 도보 경로는 없음.', '외부 경로 확인의 발견성과 앱 왕복 관찰'),
    '목적을 아직 정하지 않음': ('탐색 개선·둘 다 제외 경로 점검', 'UI/CODE/HYP', 'U02/U03', 'R03/R06', '4가지 상황 바로 이동 있음. 두 후보 모두 조건에 맞지 않을 때 별도 설명 없음.', '두 후보를 제외한 뒤 다른 상황을 찾게 하는 과제 관찰'),
    '정보 출처를 중요하게 봄': ('출처 유지·유효성 보완', 'UI/CODE/HYP', 'U03', 'R02/R11', '출처·확인일은 접힌 운영 안내에 있음. 항목별 미확인과 임시 정보 만료 관리 필요.', '자료 확인일과 실시간/현장 확인의 차이를 이해하는지 관찰'),
    '진행 중인 전시·행사를 찾음': ('공식 연결 일부·일정 미확인', 'CODE/HYP/UNTESTED', '', 'R02/R03/R11', '공간 설명과 공식 링크 중심. 오늘 진행 중인 행사를 보장하지 않음.', '해당 비교 목적에 행사 정보가 필요한지와 일정 링크 정확성 확인'),
    '잠깐 앉아 쉴 자리 필요': ('공간 비교 있음·좌석 조건 부족', 'CODE/HYP/UNTESTED', '', 'R03/R04', '실내/마당/산책로 정보는 있음. 앉을 수 있음·대화 가능·이용 조건은 별도 문제.', '앉기·대화·조용한 열람 중 실제 목적과 좌석 이용 조건 확인'),
    '사진으로 현장 입구를 찾음': ('사진 설명 개선·입구 미확인', 'UI/CODE/HYP/UNTESTED', 'U03/U05', 'R04/R10', '상세 사진 내용과 입구 사진 아님 표시는 있음. 실제 입구 도착은 미확인.', '출입구를 식별할 사진·좌표·단차를 확인'),
    '키보드로 지도 핀 조작': ('활성화 개선·전환 초점 잔여', 'UI/CODE/UNTESTED', 'U05/U06/U07/U08/U11', 'R07/R08', '스태픽스 핀 Enter·수성동 핀 Space 선택과 초점 유지 확인. 목록→지도 후 BODY 초점은 남음.', '지도 진입·선택·상세·목록 복귀 전체 초점 순서 확인'),
    '외부 지도에서 경로를 바로 기대': ('문구 개선·외부 실행 미확인', 'UI/CODE/UNTESTED', 'U03', 'R04/R13', '네이버 지도에서 보기 문구와 장소 검색 URL이 일치. 외부 앱 왕복 미실행.', '폰에서 검색→출발점 설정→경로→앱 복귀 관찰'),
}

def pair_question(pair, rule):
    if rule in ('space', 'cost', 'hours', 'access', 'location'):
        return pair[rule]
    if rule in ('seats', 'program'):
        return f"이 비교에서 필요한 경험: {pair['space']}. 행사/좌석 필요성이 다른 쌍과 같은지 먼저 확인."
    if rule == 'sources':
        return f"{pair['hours']}; {pair['cost']}"
    return '공통 UI 근거를 이 비교에도 적용한 가설이며, 별도의 사용자 세션은 실행하지 않음.'

def main():
    with (ROOT / 'synthetic_cases.csv').open(encoding='utf-8-sig', newline='') as handle:
        cases = list(csv.DictReader(handle))
    with (ROOT / 'upgrade_v18_cases.csv').open(encoding='utf-8-sig', newline='') as handle:
        previous = {row['사례ID']: row for row in csv.DictReader(handle)}
    pairs = {pair['name']: pair for pair in PAIRS}
    rules = {item[0]: item[2] for item in CONDITIONS}
    output = []
    for case in cases:
        condition = case['사용조건_가정']
        verdict, evidence, ui, issues, current, next_step = REVIEWS[condition]
        output.append({
            '사례ID': case['사례ID'], '평가유형': '합성 조건 재대조·실제 참가자 아님',
            '지역': case['지역'], '비교쌍': case['비교쌍'], '사용조건_가정': condition,
            'v18_구현대응상태_사용성과아님': previous[case['사례ID']]['대응상태'],
            'v19_재판정': verdict, '근거등급': evidence, '공통대표관찰ID_개별세션아님': ui,
            '현재근거와잔여': current, '비교쌍별점검': pair_question(pairs[case['비교쌍']], rules[condition]),
            '관련문제ID': issues, '다음확인': next_step,
            '실행범위': '대표 UI 관찰+코드 검토를 동일 조건에 연결; 개별 합성 사례의 브라우저 실행 아님',
        })
    ids = [row['사례ID'] for row in output]
    if len(output) != 100 or len(set(ids)) != 100 or set(ids) != {f'S{i:03}' for i in range(1, 101)}:
        raise ValueError('Original S001–S100 coverage must be preserved')
    with (ROOT / 'recheck_v19_cases.csv').open('w', encoding='utf-8-sig', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=output[0].keys())
        writer.writeheader()
        writer.writerows(output)

    files = ['index.html', 'js/app.js', 'js/map.js', 'js/data.js', 'css/app.css', 'css/map-view.css', 'maps/alley-style.json']
    metadata = {
        'date': '2026-09-29', 'app': 'UI/map v19, data v18', 'real_participants': 0,
        'case_count': len(output), 'case_method': 'existing rule-based hypotheses reconciled with shared evidence; not 100 sessions',
        'viewports_css_px': [[390, 844], [320, 568]],
        'evidence_report': 'SYNTHETIC_RECHECK_V19.md',
        'source_sha256': {name: hashlib.sha256((PROJECT / name).read_bytes()).hexdigest() for name in files},
        'asset_file_bytes_not_network_measurements': {
            name: (PROJECT / name).stat().st_size for name in ['fonts/PretendardVariable.woff2', 'vendor/maplibre/maplibre-gl.js', 'vendor/leaflet/leaflet.js']
        },
        'unexecuted': ['real visitors', 'outdoor walking', 'live venue verification', 'physical devices', 'screen readers', 'text scaling', 'external map app round trip', 'network fault injection'],
        'product_code_changed': False,
    }
    (ROOT / 'recheck_v19_evidence.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Preserved S001-S100: 100 unique case mappings. Real participants: 0. Product code unchanged.')

if __name__ == '__main__':
    main()
