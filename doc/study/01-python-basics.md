# 01. Python 기초 문법

## 왜 필요한가
가계부의 금액·메모를 변수에 저장하고, 조건을 검사하며, 여러 거래를 반복 처리하는 데 쓰인다.

## 공부할 개념
- 변수와 대입: `balance = 20000`
- 기본 자료형: `str`, `int`, `bool`, `None`
- 형 변환과 입력: `input()`, `int()`, `type()`
- 비교 연산자: `==`, `!=`, `<`, `<=`, `>`, `>=`
- 논리 연산자: `and`, `or`, `not`
- 조건문: `if`, `elif`, `else`
- 반복문: `for`, `while`, `break`, `continue`
- 문자열 보간: f-string
- 참/거짓으로 평가되는 값과 빈 문자열

## 작은 예제
```python
balance = 20000
expense = 5000

if expense > 0 and balance >= expense:
    balance -= expense

print(f"남은 잔액: {balance}원")
```

## 미션 적용
- 금액이 양수인지 검증
- 거래 유형과 입력 조건 확인
- 거래 목록과 CSV 행을 반복 처리

## 확인 과제
1. `<`와 `<=`의 차이를 같은 금액 예시로 설명한다.
2. `not ""`의 결과를 예측하고 실행한다.
3. 반복문으로 숫자 목록의 합계를 구한다.
