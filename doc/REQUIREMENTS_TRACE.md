# Requirements Trace & 4-Pass Audit

기준 문서: `mission_file/mission.md`, `mission_file/mission_요구사항_정리.md`, 학습 계획 v1.5.

## 코드 구조와 요구사항 연결

| 영역 | 구현 위치 | 검토 결과 |
|---|---|---|
| CLI와 진입점 | `budget_app/cli.py`, `budget_app/__main__.py` | argparse와 모듈 실행 경로 존재 |
| 모델/검증 | `budget_app/models.py` | Transaction dataclass, 날짜/월/거래 필드 검증 |
| 저장소 | `budget_app/storage.py` | JSONL 3개 파일, 한 줄씩 읽기, 임시 파일 교체 |
| 서비스 | `budget_app/service.py` | CRUD, 필터, 월 요약, 예산, 카테고리, CSV |
| 데코레이터 | `budget_app/decorators.py` | `@timed`가 `run`에 적용됨 |
| 테스트 | `tests/test_budget_app.py` | 핵심 서비스 경로, CSV 왕복을 테스트 |
| 사용자 문서 | `README.md`, `doc/user-guide/` | 실행법, 명령어, CSV, 시연 순서 |
| 학습 문서 | `doc/study/` | 문법과 구현 위치 연결 |

## 네 차례 코드 대조

### 1차 — 공식 요구사항 대 구현 구조

확인한 내용: 10개 주요 명령 그룹, 3개 JSONL 파일, dataclass와 여러 클래스, 타입 힌트, 데코레이터, 표준 라이브러리 사용, README 스키마.

결과: 주요 필수 기능의 코드 경로는 존재한다. 다만 코드가 존재한다는 사실만으로 각 기능이 모든 입력에서 정상 작동한다고 확정할 수는 없다.

### 2차 — 정상 경로 및 CLI 계약

확인한 내용: add/list/search/summary/budget/category/update/delete/import/export의 인자와 서비스 호출을 코드에서 대조했다. GitHub Actions는 CLI 최상위 도움말을 실행한다.

남은 점: 각 하위 명령 도움말과 모든 CLI 정상 시나리오를 실제 실행한 결과는 아직 확보되지 않았다. 특히 대화형 입력을 포함한 전체 평가 시연은 사용자 로컬 환경에서 실행해야 한다.

### 3차 — 오류, 경계, 저장 안전성

확인한 내용: 잘못된 날짜·금액·type·카테고리, 없는 ID, 사용 중 카테고리 삭제, JSONL 파싱 오류, 파일 I/O 오류 처리 경로를 검토했다. update/delete는 임시 파일에 쓴 뒤 `os.replace`를 사용한다.

주의/미충족:
- CSV import는 잘못된 행을 건너뛰지만 행별 오류 사유를 보고하지 않는다.
- 동시에 여러 프로세스가 같은 파일을 수정할 때의 동시성 제어가 없다.
- 임시 파일 생성 후 JSON 직렬화/데이터 순회 중 예외가 발생하면 임시 파일 정리가 모든 예외 유형에서 보장되는지 추가 점검할 수 있다.
- 빈 파일, 손상된 JSONL, 경로 권한 오류를 포함한 전체 오류 시나리오를 모두 자동 테스트한 것은 아니다.

### 4차 — 회귀, 문서, 평가 시연

조치: README를 재정비하고 `doc/user-guide/` 사용 설명서 4개와 Python 개념 참고 문서를 추가했다. CSV 테스트는 export 결과를 별도 저장소로 import하여 memo/tags/amount 보존까지 확인하도록 보강했다. list는 `heapq.nlargest`로 상위 limit개만 유지하도록 변경했다.

남은 점: 이 변경 후 GitHub Actions 결과를 다시 확인해야 하며, 검색의 최종 최신순 정렬은 여전히 일치 결과를 메모리에 모은다. 사용자 Mac에서 실제 대화형 시연도 남아 있다.

## 스트리밍 관련 판정 — 중요

- `JsonlStore.iter_transactions()`는 JSONL을 한 줄씩 `yield`한다.
- `list --limit N`은 `heapq.nlargest`로 전체 파일을 제너레이터 순회하며 상위 N개만 유지한다.
- `search`는 제너레이터로 필터링하지만, 전체 검색 결과를 최신순 정렬하기 위해 결과 리스트를 메모리에 모은다.

따라서 list는 limit에 비례하는 메모리로 처리하지만, search의 최종 정렬까지 완전한 스트리밍은 아니다. 요구사항을 엄격히 해석하면 이 부분은 **부분 충족/개선 필요**로 기록한다. 실제 동작보다 더 강한 보장을 주장하지 않는다.

## 자동 테스트 증거

- 테스트 파일: `tests/test_budget_app.py`
- 워크플로: `.github/workflows/tests.yml`
- 최근 실행 결과는 [GitHub Actions](https://github.com/ewisewjd/codyssey-mission2-1/actions)에서 확인한다.
- 테스트가 성공해도 테스트하지 않은 경로가 자동으로 검증되는 것은 아니다.

## 현재 판정

| 범주 | 판정 |
|---|---|
| 주요 기능의 코드 경로 | 존재 |
| 기본 자동 테스트 | 구성됨; 변경 후 CI 결과 확인 필요 |
| list의 스트리밍 | 상위 N개 제한 방식으로 개선 |
| search의 스트리밍 | 필터는 generator, 정렬은 메모리 사용 — 부분 충족 |
| 모든 CLI의 실제 시연 | 미완료 |
| 오류·경계·영속성 전체 검증 | 미완료 |
| 보너스 백업/반복 거래 | 미구현(선택 기능) |

실행하지 않은 항목은 `검증 완료`로 표시하지 않는다.
