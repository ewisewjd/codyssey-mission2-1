# 02. 명령어 레퍼런스

아래 예시는 저장소 루트에서 실행한다. 거래 ID 예시 `TX-000001`은 실제로 존재하는 ID로 바꿔야 한다.

## 거래 추가

```bash
python3 -m budget_app add
```

대화형으로 날짜(비우면 오늘), 타입(`income` 또는 `expense`), 등록 카테고리, 양수 금액, 메모, 태그를 입력한다. 태그는 쉼표로 구분한다.

## 목록과 검색

```bash
python3 -m budget_app list
python3 -m budget_app list --limit 5
python3 -m budget_app search --from 2026-10-01 --to 2026-10-31
python3 -m budget_app search --category food --type expense
python3 -m budget_app search --q 점심
python3 -m budget_app search --tag meal
```

여러 검색 옵션을 함께 지정하면 해당 조건을 모두 만족하는 거래를 찾는다. 날짜 범위의 시작은 끝보다 늦을 수 없다.

## 월별 요약

```bash
python3 -m budget_app summary --month 2026-10
python3 -m budget_app summary --month 2026-10 --top 5
```

수입, 지출, 잔액, 카테고리별 지출 TOP N을 출력한다. 예산을 설정한 달은 사용률과 초과 경고도 표시한다.

## 예산

```bash
python3 -m budget_app budget set --month 2026-10 --amount 500000
```

예산 금액은 양수 정수여야 한다. 예산 조회는 해당 월의 `summary`를 실행한다.

## 카테고리

```bash
python3 -m budget_app category list
python3 -m budget_app category add
python3 -m budget_app category remove --name shopping
```

추가는 이름을 대화형으로 입력한다. 거래에서 사용 중인 카테고리는 삭제할 수 없다.

## 거래 수정과 삭제

```bash
python3 -m budget_app update --id TX-000001 --memo "점심 식사"
python3 -m budget_app update --id TX-000001 --amount 6500 --tags meal,lunch
python3 -m budget_app delete --id TX-000001
```

수정은 옵션 방식이다. 변경하지 않을 옵션은 생략한다. 삭제와 수정은 실제 데이터를 바꾸므로 ID를 확인한 뒤 실행한다.

## CSV 내보내기와 가져오기

```bash
python3 -m budget_app export --out october.csv --month 2026-10
python3 -m budget_app export --out range.csv --from 2026-10-01 --to 2026-10-15
python3 -m budget_app import --from october.csv
```

가져오기는 기존 거래를 지우지 않고 유효한 행을 추가한다. 잘못된 행은 건너뛰며 결과에 가져온 행과 건너뛴 행 수를 표시한다. 같은 파일을 여러 번 가져오면 중복 거래가 생길 수 있으므로 주의한다.

## 도움말

```bash
python3 -m budget_app add --help
python3 -m budget_app search --help
python3 -m budget_app category remove --help
```
