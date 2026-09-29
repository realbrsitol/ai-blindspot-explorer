"""Map the existing synthetic cases to implementation changes; no user simulation."""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parent
CHANGES = {
    'R01': '비교 표·지도 카드에 기본 운영·휴관 배치',
    'R02': '비교와 상세 요약에 관련 출처 링크, 확인된 3곳 대표 전화',
    'R03': '공예박물관·배렴 공통 휴관 안내, 다른 상황 선택',
    'R04': '이용 방식·구매/예약 조건과 미확인 사항 분리; 현장 동선·가격은 잔여',
    'R05': '지도 JS/CSS 지연 로드, 사진 WebP, 글꼴 서브셋',
    'R06': '비교 번호·A/B·반복 분류/공간 행 제거',
    'R07': '지도 카드 가변 높이, 목록이 넘칠 때 스크롤 안내',
    'R08': '지도 진입 제목 초점·비교 복귀 원래 버튼 초점',
    'R09': '지도 카드 운영 정보·14px 안내, 일반 좌표 설명 상세 이동',
    'R10': '사진 설명·출처 유지, 실제 입구 사진 추가 확보는 잔여',
    'R11': '장소별 확인 범위·날짜/재확인 필요 구분, 임시 안내 기간 분리',
    'R12': '두 장소가 유지되는 비교 링크 복사와 수동 복사 대안',
    'R13': '지역별 지도 초기화 이름, 외부 지도에서 경로 설정 안내',
    'R14': '로딩 지연과 오류 분리, 늦게 성공하면 지연 안내 해제'
}

with (ROOT / 'recheck_v19_cases.csv').open(encoding='utf-8-sig', newline='') as handle:
    previous = list(csv.DictReader(handle))
rows = []
for case in previous:
    issues = [issue for issue in case['관련문제ID'].split('/') if issue]
    rows.append({
        '사례ID': case['사례ID'], '평가유형': '기존 합성 조건에 대한 구현 대응 기록',
        '지역': case['지역'], '비교쌍': case['비교쌍'], '사용조건_가정': case['사용조건_가정'],
        '관련문제ID': case['관련문제ID'],
        'v20_구현': '; '.join(f'{issue}: {CHANGES[issue]}' for issue in issues) or '수요 근거 부족으로 기능 추가 없음',
        '판정범위': '구현 대응; 사례별 사용 성공·만족도 판정 아님',
        '남은확인': case['다음확인'],
        '현장_실제참가자': '없음',
        '개별사례_브라우저세션': '실행하지 않음',
        '공통관찰': 'UPGRADE_V20.md에 명시한 대표 화면 미리보기만 공유'
    })
with (ROOT / 'upgrade_v20_cases.csv').open('w', encoding='utf-8-sig', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
files = ['index.html', 'js/data.js', 'js/media.js', 'js/app.js', 'js/map.js',
         'css/app.css', 'css/map-view.css', 'fonts/AlleySans.woff2',
         'images/places/optimized/manifest.json']
evidence = {'date': '2026-09-29', 'version': 'v20', 'real_participants': 0,
            'case_count': len(rows), 'case_ids': [row['사례ID'] for row in rows],
            'method': 'implementation mapping, not 100 participant sessions',
            'report': 'UPGRADE_V20.md',
            'source_sha256': {path: hashlib.sha256((PROJECT / path).read_bytes()).hexdigest() for path in files}}
(ROOT / 'upgrade_v20_evidence.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Wrote implementation mapping for {len(rows)} existing synthetic cases.')
