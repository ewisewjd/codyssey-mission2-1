# Codyssey Mission 2-1 — 나만의 용돈 기입장

Python 3.10 이상과 표준 라이브러리만으로 구현한 JSONL 기반 콘솔 가계부다. 거래를 추가·조회·검색·수정·삭제하고 월별 요약, 예산, 카테고리, CSV 입출력을 제공한다.

## 빠른 시작

프로젝트 루트에서 실행한다.

```bash
python3 --version
python3 -m budget_app --help
python3 -m budget_app category list
python3 -m budget_app add
python3 -m budget_app list --limit 10
```

첫 실행 때 `./data/`와 데이터 파일이 자동 생성된다. 다른 데이터 폴더를 쓰려면 전역 옵션을 명령보다 앞에 둔다.

```bash
python3 -m budget_app --data-dir ./demo_data list
python3 -m budget_app --data-dir ./demo_data add
```

## 명령어 예시

| 목적 | 명령 |
|---|---|
| 도움말 | `python3 -m budget_app --help` |
| 거래 추가 | `python3 -m budget_app add` |
| 최신 거래 5건 | `python3 -m budget_app list --limit 5` |
| 기간 검색 | `python3 -m budget_app search --from 2026-10-01 --to 2026-10-31` |
| 카테고리/유형 검색 | `python3 -m budget_app search --category food --type expense` |
| 메모 검색 | `python3 -m budget_app search --q 점심` |
| 태그 검색 | `python3 -m budget_app search --tag meal` |
| 월별 요약 | `python3 -m budget_app summary --month 2026-10 --top 3` |
| 월 예산 설정 | `python3 -m budget_app budget set --month 2026-10 --amount 500000` |
| 카테고리 목록 | `python3 -m budget_app category list` |
| 카테고리 추가 | `python3 -m budget_app category add` |
| 카테고리 삭제 | `python3 -m budget_app category remove --name shopping` |
| 거래 수정 | `python3 -m budget_app update --id TX-000001 --memo "점심 식사"` |
| 거래 삭제 | `python3 -m budget_app delete --id TX-000001` |
| 월 CSV 내보내기 | `python3 -m budget_app export --out october.csv --month 2026-10` |
| 기간 CSV 내보내기 | `python3 -m budget_app export --out range.csv --from 2026-10-01 --to 2026-10-15` |
| CSV 가져오기 | `python3 -m budget_app import --from transactions.csv` |

수정·삭제 명령은 실제 데이터를 바꾼다. 예시 ID를 그대로 쓰지 말고 `list`에서 실제 ID를 확인한다. 같은 CSV를 여러 번 가져오면 중복 거래가 추가될 수 있다. CSV 가져오기에서 행을 건너뛰면 각 행의 이유를 출력하고 종료 코드 1을 반환한다. 일부 행이 성공적으로 가져와졌더라도 누락 행이 있다는 뜻이다.

## 데이터 저장

| 파일 | 내용 |
|---|---|
| `data/transactions.jsonl` | 거래 내역 |
| `data/categories.jsonl` | 카테고리 |
| `data/budgets.jsonl` | 월 예산 |
| `data/transaction_sequence.json` | 마지막으로 예약한 거래 ID 번호 |

JSONL은 한 줄에 JSON 객체 하나를 저장하는 형식이다. UTF-8과 한글 보존을 사용한다. `update`, `delete`, CSV `export`는 임시 파일에 새 내용을 쓴 뒤 `os.replace()`로 교체한다. 거래 ID 번호는 별도 기록을 유지하므로 가장 큰 ID를 삭제해도 해당 번호를 재사용하지 않는다. 기존 데이터 폴더를 처음 업그레이드할 때는 현재 저장된 ID 중 가장 큰 번호를 기준으로 기록을 시작한다.

## CSV 스키마

UTF-8(읽을 때 BOM 허용), 헤더 필수.

| 열 | 필수 | 의미 |
|---|---|---|
| `date` | 예 | 유효한 `YYYY-MM-DD` 날짜 |
| `type` | 예 | `income` 또는 `expense` |
| `category` | 예 | 이미 등록된 카테고리 |
| `amount` | 예 | 양수 정수 |
| `memo` | 아니오 | 메모 문자열 |
| `tags` | 아니오 | 쉼표로 구분한 태그 문자열 |

예시:

```csv
date,type,category,amount,memo,tags
2026-10-28,expense,food,4500,"점심, 특식","meal,lunch"
```

## 코드 구조

- `budget_app/models.py`: Transaction dataclass, 날짜·월·거래 필드 검증
- `budget_app/storage.py`: JSONL 파일, 제너레이터 읽기, 임시 파일 교체, 거래 ID 번호 기록
- `budget_app/service.py`: 거래 로직, 필터, 요약, 예산, 카테고리, CSV
- `budget_app/cli.py`: argparse 명령어, 대화형 입력, 사용자 오류 메시지
- `budget_app/decorators.py`: 실행 시간 측정 데코레이터
- `budget_app/__main__.py`: 모듈 실행 진입점
- `tests/test_budget_app.py`: unittest 회귀 테스트

실행 시간 출력은 기본적으로 꺼져 있다. 필요할 때만 환경 변수를 설정한다.

```bash
BUDGET_APP_SHOW_TIMING=1 python3 -m budget_app list
```

## 테스트

```bash
python3 -m unittest discover -s tests -v
python3 -m budget_app --help
```

GitHub Actions는 push와 pull request 때 테스트를 실행한다. 테스트 통과는 테스트에 포함된 경로의 증거이며 모든 입력 조합이 검증됐다는 뜻은 아니다.

## 문서

- [사용자 설명서](doc/user-guide/README.md)
- [Python 개념 빠른 참고서](doc/study/00-python-concepts-for-this-mission.md)
- [전체 학습 순서](doc/study/README.md)
- [요구사항 추적 및 코드 감사](doc/REQUIREMENTS_TRACE.md)
- [진행 현황](doc/PROGRESS.md)

## 현재 제한사항과 미완료 검증

- `list`는 제너레이터를 순회하면서 `--limit`개 상위 항목만 유지한다.
- `search`는 제너레이터로 필터링하지만, 최신순 전체 정렬 단계에서 일치하는 결과를 메모리에 모은다. 따라서 검색의 최종 단계까지 완전한 상수 메모리 스트리밍은 아니다.
- CSV 가져오기는 잘못된 행을 건너뛰고 행별 원인을 표시한다. 일부라도 건너뛴 경우 명령은 종료 코드 1을 반환한다.
- 동시에 여러 프로세스가 같은 데이터 파일을 수정하는 상황의 동시성 제어는 없다.
- 자동 백업과 반복 거래 생성은 선택 보너스이며 현재 구현하지 않았다.
- 새 회귀 테스트를 추가했지만, 이 브랜치의 GitHub Actions 실행 결과를 확인하기 전까지 전체 테스트 통과로 단정하지 않는다. 평가 전에 모든 CLI 명령, 오류·경계 조건, 재실행 후 데이터 유지, CSV 왕복을 직접 실행해 확인해야 한다.
