# Progress

## 현재 상태
- 기준일: 2026-10-28
- 저장소: `ewisewjd/codyssey-mission2-1`
- 구현: 주요 필수 기능의 첫 구현본 존재
- 테스트: 핵심 unittest 구성; 최신 변경 후 GitHub Actions 결과 확인 필요
- 검증 상태: 문서/코드 정적 대조 진행. 모든 CLI의 로컬 수동 시연은 미완료.

## 완료/반영
- [x] 공식 미션과 요구사항 문서 정리
- [x] v1.5 계획을 참고한 개념별 study 자료
- [x] Python 문법 빠른 참고서 `doc/study/00-python-concepts-for-this-mission.md`
- [x] 주요 기능 구조: models/storage/service/cli/decorators
- [x] 거래·카테고리·예산 JSONL 파일 3개 생성
- [x] 거래 CRUD, 검색, 요약, 예산, 카테고리, CSV 경로 구현
- [x] update/delete의 임시 파일 교체
- [x] list에서 `heapq.nlargest`로 상위 limit개만 메모리에 유지
- [x] README 정비
- [x] `doc/user-guide/` 사용 설명서 생성
- [x] CSV export→import 필드 보존 테스트 추가

## 남은 검증
- [ ] 최신 GitHub Actions 결과 확인
- [ ] 모든 명령 및 하위 명령 `--help` 실행
- [ ] 실제 대화형 add/category add 시연
- [ ] 오류·경계·영속성 테스트(잘못된 JSONL, 경로 오류, 없는 ID, 빈 데이터)
- [ ] CSV 잘못된 행 및 중복 import 동작 확인
- [ ] 사용자 로컬 Mac에서 pull 후 실행
- [ ] 검색 정렬 단계의 스트리밍 요구를 충족하는지 재설계 또는 제한사항으로 명시적 합의

## 구현 위치
- `budget_app/models.py`: Transaction dataclass, 검증
- `budget_app/storage.py`: JSONL 3종, 파일 읽기, 원자적 교체
- `budget_app/service.py`: 거래 서비스와 CSV
- `budget_app/cli.py`: CLI와 사용자 입력
- `budget_app/decorators.py`: 실행 시간 측정
- `tests/test_budget_app.py`: 회귀 테스트
- `doc/REQUIREMENTS_TRACE.md`: 4회 대조 결과 및 남은 차이
