# 03. 데이터 파일과 CSV 형식

## JSONL 저장 파일

프로그램은 기본 `data/` 아래에 세 파일을 사용한다.

- `transactions.jsonl`: 거래
- `categories.jsonl`: 카테고리
- `budgets.jsonl`: 월 예산

JSONL은 한 줄마다 독립적인 JSON 객체 하나를 저장하는 형식이다. 예를 들어 거래 한 건은 다음처럼 저장된다.

```json
{"id":"TX-000001","type":"expense","date":"2026-10-28","amount":4500,"category":"food","memo":"점심","tags":["meal"]}
```

한글을 읽기 쉽게 유지하기 위해 UTF-8과 `ensure_ascii=False`를 사용한다. 파일을 수동 편집할 경우 각 줄의 JSON 문법을 지켜야 한다.

## CSV 스키마

첫 행에는 헤더가 있어야 한다.

| 열 | 필수 | 설명 | 예시 |
|---|---|---|---|
| date | 예 | YYYY-MM-DD 실제 날짜 | 2026-10-28 |
| type | 예 | income 또는 expense | expense |
| category | 예 | 등록된 카테고리 | food |
| amount | 예 | 양수 정수 | 4500 |
| memo | 아니오 | 거래 메모 | 점심, 특식 |
| tags | 아니오 | 쉼표 구분 태그 | meal,lunch |

예시 CSV:

```csv
date,type,category,amount,memo,tags
2026-10-28,expense,food,4500,"점심, 특식","meal,lunch"
2026-10-28,income,salary,100000,,payday
```

- 인코딩은 UTF-8이며 BOM이 있어도 읽을 수 있다.
- CSV의 쉼표가 포함된 메모는 큰따옴표로 감싼다.
- 태그는 앱 안에서는 리스트로, CSV에서는 쉼표로 구분한 문자열로 표현한다.
- 가져오기 전에는 CSV의 카테고리가 앱에 등록되어 있는지 확인한다.

## 백업과 복구

현재 기본 구현에는 전용 backup 명령이 없다. 중요한 데이터는 프로그램을 종료한 뒤 `data/` 폴더를 별도 위치에 복사해 보관한다. 복구 전에는 앱을 종료하고, 현재 데이터 폴더를 먼저 복사해 두는 것이 안전하다.
