# 15. CSV import/export

## 고정 스키마
- 필수: date, type, category, amount
- 선택: memo, tags
- UTF-8, 헤더 포함
- tags는 CSV에서 쉼표 구분 문자열

## 공부할 개념
- `csv.DictReader`와 `csv.DictWriter`
- 헤더 유무와 누락된 컬럼
- UTF-8 및 한글 메모
- 쉼표·따옴표·줄바꿈이 포함된 셀
- import 시 데이터 검증과 중복 정책
- 잘못된 행을 중단/건너뛰는 정책
- 처리 건수와 건너뛴 행 수 출력

## 미션 적용
- `import --from FILE.csv`
- `export --out FILE.csv --month YYYY-MM`
- 또는 `--from DATE --to DATE` 범위 지정

## 확인 과제
한글·쉼표 포함 메모, 빈 memo, 여러 tags를 export한 뒤 import하고 값이 보존되는지 비교한다.
