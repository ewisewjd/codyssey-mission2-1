# Codyssey Mission 2-1 — 나만의 용돈 기입장

Python 표준 라이브러리만 사용한 JSONL 기반 콘솔 가계부입니다. Python 3.10 이상이 필요합니다.

## 실행

프로젝트 루트에서 실행합니다.

```bash
python -m budget_app --help
python -m budget_app add
python -m budget_app list --limit 10
python -m budget_app search --from 2026-10-01 --to 2026-10-31
python -m budget_app summary --month 2026-10 --top 3
```

데이터 폴더는 기본적으로 `./data`이며, 다른 경로를 사용하려면 전역 옵션을 명령보다 앞에 둡니다.

```bash
python -m budget_app --data-dir ./sample_data list
```

## 명령 예시

```bash
python -m budget_app category list
python -m budget_app category add
python -m budget_app category remove --name shopping
python -m budget_app budget set --month 2026-10 --amount 500000
python -m budget_app update --id TX-000001 --memo "점심 식사"
python -m budget_app delete --id TX-000001
python -m budget_app export --out october.csv --month 2026-10
python -m budget_app export --out range.csv --from 2026-10-01 --to 2026-10-15
python -m budget_app import --from transactions.csv
```

## 저장 파일

첫 실행 시 다음 파일을 자동 생성합니다.

- `data/transactions.jsonl`: 거래 내역
- `data/categories.jsonl`: 카테고리 목록
- `data/budgets.jsonl`: 월 예산

각 파일은 한 줄에 JSON 객체 하나를 저장하는 JSONL 형식이며 UTF-8을 사용합니다. 카테고리 파일이 비어 있으면 기본 카테고리가 생성됩니다.

## CSV 스키마

UTF-8(선택적으로 BOM 포함), 헤더 행 필수.

| column | 필수 | 설명 |
|---|---|---|
| date | 예 | YYYY-MM-DD |
| type | 예 | income 또는 expense |
| category | 예 | 등록된 카테고리 |
| amount | 예 | 0보다 큰 정수 |
| memo | 아니오 | 메모 문자열 |
| tags | 아니오 | 태그를 쉼표로 구분한 문자열 |

## 구조

- `models.py`: Transaction 데이터 모델과 날짜/금액 검증
- `storage.py`: JSONL 파일 입출력과 임시 파일 교체
- `service.py`: 거래, 검색, 요약, 예산, 카테고리, CSV 로직
- `cli.py`: argparse 기반 명령줄 인터페이스
- `decorators.py`: 명령 실행 시간 측정 데코레이터

## 구현상 주의점

JSONL 파일은 한 줄씩 읽는 제너레이터로 순회합니다. 다만 최신순 정렬은 전체 결과를 정렬해야 하므로 현재 목록/검색은 결과를 메모리에 모아 정렬합니다. 대용량 정렬까지 엄격히 스트리밍해야 한다면 저장 시 정렬 불변식을 유지하거나 외부 정렬 설계를 추가해야 합니다. update/delete는 임시 파일 작성 후 교체 방식으로 저장합니다.

## 검증 상태

현재 구현은 초기 버전입니다. README의 예시 명령을 실행하고 정상 입력, 오류 입력, 경계값, 재실행 후 저장 유지, CSV 왕복을 실제로 테스트한 뒤 요구사항 추적표의 상태를 갱신해야 합니다. 코드가 추가되었다는 사실만으로 검증 완료로 간주하지 않습니다.
