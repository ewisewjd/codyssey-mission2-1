# 00. 이 미션에 필요한 Python 개념 한눈에 보기

이 문서는 처음부터 모든 문법을 암기하기 위한 자료가 아니다. 각 항목을 읽고 작은 예제를 실행한 뒤, 실제 코드에서 같은 문법을 찾아보자.

## 1. 변수와 기본 자료형

```python
amount = 4500          # int: 정수
memo = "점심"          # str: 문자열
tags = ["meal", "food"] # list: 여러 값
transaction = {"amount": 4500, "memo": "점심"} # dict: 이름과 값
has_memo = bool(memo)  # bool: True 또는 False
```

- `=`는 값을 저장한다. `==`는 두 값이 같은지 비교한다.
- `!=`는 같지 않다는 뜻이다.
- `None`은 값이 없음을 나타내는 특별한 객체다. JavaScript의 `null`과 비슷한 용도지만 Python에서는 `None`이라고 쓴다.
- `memo != None`은 빈 문자열을 걸러내지 못한다. `memo == ""` 또는 `not memo`로 빈 문자열을 검사한다. 보통 None 여부만 검사할 때는 `memo is None`을 쓴다.

## 2. 조건식과 참/거짓

```python
balance = 20000
expense = 5000
memo = ""

if not memo:
    print("메모를 입력하세요.")
elif expense <= 0:
    print("금액은 양수여야 합니다.")
elif balance < expense:
    print("잔액이 부족합니다.")
else:
    balance -= expense
    print("지출 완료")
```

- `if`는 첫 조건이 참이면 실행한다.
- `elif`는 앞의 조건이 모두 거짓일 때 검사한다.
- `else`는 위의 조건이 모두 거짓일 때 실행한다.
- `and`는 양쪽 조건이 모두 참이어야 참, `or`는 하나라도 참이면 참, `not`은 참/거짓을 뒤집는다.
- 빈 문자열 `""`, 숫자 `0`, 빈 리스트 `[]`, `None`은 조건식에서 거짓처럼 평가된다. 하지만 이 값들은 서로 같은 값은 아니다.
- Python에는 논리 부정 기호 `!`가 없다. `!=`는 사용할 수 있지만 `!memo`는 문법 오류다.

## 3. 반복문, 리스트, 딕셔너리

```python
for tag in ["meal", "food"]:
    print(tag)

record = {"date": "2026-10-28", "amount": 4500}
print(record["amount"])
```

- `for`는 항목을 하나씩 처리한다.
- 리스트는 순서가 있는 여러 값, 딕셔너리는 키와 값의 묶음이다.
- `dict.get("memo", "")`는 memo 키가 없을 때 기본값을 돌려준다.
- `[x for x in values if condition]`은 조건에 맞는 값으로 새 리스트를 만든다.

## 4. 함수, 인수, 반환값

```python
def add_tax(amount: int, rate: float = 0.1) -> float:
    return amount * (1 + rate)

total = add_tax(1000)
```

- 함수는 `def`로 만든다.
- 매개변수는 함수가 받을 입력 이름이다.
- 기본값 `rate=0.1`은 호출할 때 생략할 수 있는 값이다.
- `return`은 결과를 호출한 곳에 돌려준다. `print()`는 화면에 표시할 뿐, 결과를 반환하는 것과 다르다.
- 타입 힌트 `: int`, `-> float`는 의도를 설명하지만 실행 시 자동으로 값을 검증하지 않는다.

## 5. 파일과 예외

```python
from pathlib import Path
import json

path = Path("data/example.jsonl")
with path.open("a", encoding="utf-8") as file:
    file.write(json.dumps({"amount": 4500}, ensure_ascii=False) + "\n")
```

- `Path`는 파일·폴더 경로를 다루는 객체다.
- `with`는 파일을 사용한 뒤 자동으로 닫도록 돕는다.
- `encoding="utf-8"`은 한글 저장을 위해 명시한다.
- `try/except`는 예상 가능한 오류를 처리한다. 모든 오류를 무조건 숨기면 원인을 찾기 어려우므로 구체적으로 처리한다.

## 6. 제너레이터와 yield

```python
def numbers():
    for number in range(3):
        yield number
```

`yield`는 값을 하나씩 제공하며 함수의 진행 상태를 기억한다. `return`은 함수에서 빠져나오고 결과 하나를 돌려준다. JSONL 파일을 한 줄씩 읽을 때 유용하다.

## 7. 클래스와 dataclass

```python
from dataclasses import dataclass

@dataclass
class Transaction:
    id: str
    amount: int
    memo: str = ""
```

클래스는 데이터와 관련 동작을 묶는 설계도다. 인스턴스는 그 설계도로 만든 실제 객체다. `@dataclass`는 초기화 함수 등 반복 코드를 자동 생성해 준다.

## 8. 데코레이터

```python
@timed("명령 실행")
def run():
    ...
```

`@timed("명령 실행")`은 `run` 함수를 감싸는 함수를 연결한다. 미션에서는 실행 시간 출력 같은 공통 동작을 본래 로직과 분리한다.

## 9. import와 모듈

- `from .models import Transaction`은 같은 패키지의 models.py에서 Transaction을 가져온다.
- `python -m budget_app`은 패키지를 모듈 실행 방식으로 시작한다. `__main__.py`가 진입점 역할을 한다.

## 10. 미션 코드 연결

| 개념 | 찾아볼 파일 |
|---|---|
| 조건문, 입력, f-string | `budget_app/cli.py` |
| dataclass, 타입 힌트, 날짜 검증 | `budget_app/models.py` |
| JSONL, Path, 제너레이터, 임시 파일 교체 | `budget_app/storage.py` |
| 함수, 필터링, 정렬, 집계, CSV | `budget_app/service.py` |
| 데코레이터 | `budget_app/decorators.py` |
| 예외와 종료 코드 | `budget_app/cli.py` |

## 셀프 체크

1. `memo = ""`일 때 `bool(memo)`와 `not memo`의 결과는?
2. `amount = 100`과 `amount == 100`의 차이는?
3. `yield`와 `return`은 어떻게 다른가?
4. 타입 힌트가 잘못된 입력을 자동으로 막아 주는가?
5. `with open(...)`을 사용하는 이유는?
