# 02. 컬렉션과 함수

## 공부할 개념
- 리스트: 순서가 있는 여러 값
- 딕셔너리: 키와 값의 연결
- 튜플과 집합의 기본 용도
- 리스트 순회와 딕셔너리의 `.get()`, `.items()`
- 함수 정의, 인수, 매개변수, 반환값
- 기본 인수와 키워드 인수
- 지역 변수와 반환값
- 문자열의 `.strip()`, `.lower()`, `.split()`
- 정렬: `sorted()`, `key=`, `reverse=True`

## 작은 예제
```python
transaction = {
    "type": "expense",
    "amount": 5000,
    "category": "food",
}

def is_expense(item: dict) -> bool:
    return item["type"] == "expense"

print(is_expense(transaction))
```

## 미션 적용
- Transaction의 tags를 리스트로 다루기
- 카테고리별 합계를 딕셔너리로 모으기
- 검색 조건을 함수로 분리하기

## 확인 과제
거래 딕셔너리 목록에서 지출만 골라 합계를 반환하는 함수를 작성한다.
