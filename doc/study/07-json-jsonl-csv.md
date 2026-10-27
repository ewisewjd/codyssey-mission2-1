# 07. JSON, JSONL, CSV

## JSON
객체와 배열을 표현하는 텍스트 형식. Python의 `json.dumps()`와 `json.loads()`를 공부한다.

## JSONL
한 줄에 JSON 객체 하나를 기록한다. 한 줄씩 읽을 수 있어 대용량 데이터 스트리밍에 적합하다.

예시:
```json
{"id":"TX-000001","type":"expense","date":"2026-10-27","amount":5000,"category":"food","memo":"점심","tags":["meal"]}
{"id":"TX-000002","type":"income","date":"2026-10-27","amount":100000,"category":"salary","memo":"","tags":[]}
```

## CSV
행과 열로 표현되는 교환 형식. `csv.DictReader`, `csv.DictWriter`, 헤더, UTF-8, 쉼표가 포함된 문자열 처리를 공부한다.

## 미션 결정
기본 저장소는 JSONL로 통일하고, CSV는 외부 파일 import/export에 사용한다. 두 형식을 혼동하지 않는다.

## 확인 과제
거래 객체를 JSONL로 저장한 뒤 다시 읽어 값이 같은지 확인한다. CSV에는 tags를 쉼표로 구분된 문자열로 내보내는 규칙을 적용한다.
