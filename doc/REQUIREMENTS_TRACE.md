# Requirements Trace & 4-Pass Audit

기준: `mission_file/mission.md` 및 `mission_file/mission_요구사항_정리.md`.

## 구현 위치
| 영역 | 구현 파일 | 주요 근거 |
|---|---|---|
| 실행/CLI | `budget_app/cli.py`, `budget_app/__main__.py` | argparse, --help, 종료 코드 |
| 모델/검증 | `budget_app/models.py` | Transaction dataclass, 날짜·타입·금액 검증 |
| 저장소 | `budget_app/storage.py` | 3개 JSONL 파일, 제너레이터, 임시 파일 교체 |
| 비즈니스 로직 | `budget_app/service.py` | CRUD, 검색, 요약, 예산, 카테고리, CSV |
| 데코레이터 | `budget_app/decorators.py` | `@timed` 실제 적용 |
| 테스트 | `tests/test_budget_app.py` | 7개 unittest |
| 사용법 | `README.md` | 실행법, 파일 형식, CSV 스키마 |

## 현재 검증 증거
- GitHub Actions run: https://github.com/ewisewjd/codyssey-mission2-1/actions/runs/40507152773
- 결과: success
- 성공 단계: unittest, `python -m budget_app --help`
- 테스트 범위: 거래 ID/저장, 잘못된 거래 입력, 수정/삭제/없는 ID, 검색/월 요약, 예산/카테고리 안전성, CSV 월말 export, 3개 파일 생성
- 이 증거는 테스트된 범위에 한정된다. 모든 CLI 조합과 오류 상황을 검증했다는 뜻은 아니다.

## 4회 코드 대조 기록

| 회차 | 범위 | 상태 | 남은 일 |
|---|---|---|---|
| 1차 | 요구사항 ↔ 파일/함수/클래스 구조 | 진행 중 | 모든 ID를 구현 위치에 연결하고 누락/차이를 표시 |
| 2차 | 모든 CLI 명령의 정상 경로 | 진행 중 | 로컬에서 명령별 실행 출력 확인 |
| 3차 | 오류·경계·영속성 | 진행 중 | 잘못된 JSONL, 잘못된 CSV, 저장 경로 오류, 재실행 확인 |
| 4차 | 회귀·README·평가 시연 | 대기 | 앞선 세 차례 수정 후 전체 재실행 |

## 현재 알려진 제약 및 점검할 점
- 최신순 정렬은 정렬을 위해 결과를 메모리에 모은다. 파일 자체는 제너레이터로 한 줄씩 읽지만, 정렬 단계까지 엄격한 O(1) 메모리 스트리밍은 아니다.
- 전역 옵션 `--data-dir`은 명령 앞에 둔다: `python -m budget_app --data-dir ./sample_data list`.
- CSV import는 유효하지 않은 행을 건너뛰고 건수를 보고한다. 잘못된 행의 상세 행별 원인은 현재 사용자에게 개별 표시하지 않는다.
- 현재 구현은 초기 버전이며, 로컬 환경에서 평가 시나리오를 실행한 뒤 추가 수정이 필요할 수 있다.

실행하지 않은 항목은 통과 처리하지 않는다.
