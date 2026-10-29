# 용돈 기입장 학습 가이드 ver2.0 — 파이썬 입문에서 숙련까지

Oct 27, 2026 · @안흥

## 0. 이 가이드 사용법

이 가이드는 파이썬을 한 번도 안 써 본 사람이 용돈 기입장 미션을 끝내고, 그 과정에서 파이썬 전반을 익히도록 만든 학습서입니다. 읽기만 하면 실력이 늘지 않으므로 모든 장이 같은 네 단계로 움직입니다.

1. 읽기: 개념을 짧게 읽습니다. 모든 개념은 용돈 기입장의 장면(거래 한 건, 월 합계, 카테고리)으로 설명합니다.
2. 따라 치기: 예제 코드를 복사하지 말고 직접 타이핑해서 실행합니다. 오타를 내고 에러 메시지를 읽는 경험이 학습의 절반입니다.
3. 연습문제: 정답을 가린 채 먼저 풀어 봅니다. 막히면 힌트만 보고, 그래도 안 되면 정답을 봅니다.
4. 정답 비교: 정답과 내 코드를 나란히 놓고 다른 점을 찾습니다. 동작은 같아도 읽기 쉬운 쪽이 어느 쪽인지 고민하는 것이 숙련으로 가는 길입니다.

각 장의 구성은 다음과 같습니다.

| 블록 | 하는 일 |
| --- | --- |
| 핵심 개념 | 그 장에서 꼭 알아야 할 것 3\~5가지 |
| 따라 하기 | 한 줄씩 실행해 보는 예제 |
| 연습문제 | 쉬운 것부터 순서대로, 장마다 5\~7문제 |
| 정답과 해설 | 실행해서 확인한 코드와 출력 |
| 미션 연결 | 이 장의 내용이 과제 요구사항 중 어디에 쓰이는지 |

### 0.1 환경 준비

터미널(Windows는 PowerShell, macOS/Linux는 Terminal)을 열고 다음을 확인합니다. 미션은 Python 3.10 이상을 요구합니다.

```bash
python --version      # Python 3.10 이상이어야 함 (안 되면 python3 --version)
python -c "print('hello')"
```

`python`이 없다고 나오면 python.org에서 설치하고, Windows는 설치 화면에서 Add python.exe to PATH를 꼭 체크합니다. 편집기는 VS Code를 권장합니다. 연습용 폴더를 하나 만들어 둡니다.

```bash
mkdir pylab
cd pylab
```

이 폴더에 `ch01.py`, `ch02.py`처럼 장마다 파일을 만들어 실행합니다.

```bash
python ch01.py
```

터미널에서 한 줄씩 실험하고 싶으면 `python`만 입력해 대화 모드(`>>>`)로 들어갑니다. 나올 때는 `exit()`입니다.

### 0.2 학습 계획표

하루 2시간 기준입니다. 정보처리기사 실기 일정과 겹치는 주는 한 단계 뒤로 미루고, 동료 평가 일정에서 거꾸로 계산해 18장(단계별 구현)에 최소 5일을 남겨 두세요.

| 기간 | 범위 | 목표 |
| --- | --- | --- |
| 1주차 | 1\~6장 | 변수, 제어문, 컨테이너, 함수, 컴프리헨션을 연습문제로 체화 |
| 2주차 | 7\~10장 | 예외, 파일, 클래스, 모듈로 프로그램 뼈대 만들기 |
| 3주차 | 11\~13장 | 제너레이터, 데코레이터, 타입 힌트 (미션의 핵심 평가 포인트) |
| 4주차 | 14\~17장 | 표준 라이브러리, argparse, 테스트, Git |
| 5주차 이후 | 18\~20장 | 용돈 기입장 단계별 구현, 종합 문제, 동료 평가 준비 |

시간이 부족하면 최소 경로는 1, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 18, 20장입니다. 6, 14, 16, 17, 19장은 구현이 막힐 때 해당 부분만 찾아 읽어도 됩니다.

### 0.3 막혔을 때의 규칙

- 에러 메시지는 맨 아래 줄부터 읽습니다. 종류(`TypeError` 등)와 이유가 거기에 있습니다.
- 15분 이상 같은 곳에서 막히면 정답을 봐도 됩니다. 단, 본 뒤에는 정답을 덮고 처음부터 다시 직접 써 봅니다.
- 장을 넘어갈 때는 그 장의 연습문제를 절반 이상 정답 없이 풀 수 있어야 합니다.

## 1장. 변수, 자료형, 연산자

변수는 값에 붙이는 이름표입니다. 문자와 숫자처럼 서로 다른 종류(자료형)의 값이 있고, 종류마다 할 수 있는 연산이 다릅니다. 용돈 기입장에서는 금액(숫자), 카테고리(문자), 날짜(문자열 또는 date)가 전부 이것들로 시작합니다.

### 핵심 개념

- 파이썬은 변수에 타입을 선언하지 않습니다. 값이 타입을 가집니다(동적 타이핑).
- 기본 타입: `int`(정수), `float`(실수), `str`(문자열), `bool`(참/거짓), `None`(값 없음).
- 나눠서 소수가 나오는 `/`와 몰만 구하는 `//`는 다릅니다.
- 타입이 다른 값을 섞으면 `TypeError`가 나오고, 타입 변환은 `int()`, `str()`, `float()`로 직접 합니다.
- 돈은 `float`을 쓰지 않고 정수(원 단위)로 다룹니다. 이유는 아래 따라 하기에 있습니다.

### 따라 하기

`ch01.py`로 저장해 실행합니다.

```python
income = 50000
spent = 18500
balance = income - spent
print("잔액:", balance)          # 잔액: 31500

print(7 // 2, 7 % 2, 7 / 2, 2 ** 10)   # 3 1 3.5 1024
print(-7 // 2)                        # -4  (음수는 내림이라 -3이 아님)

man, rest = divmod(12345, 10000)      # 몰과 나머지를 한 번에
print(man, rest)                      # 1 2345

print(0.1 + 0.2)                      # 0.30000000000000004
print(0.1 + 0.2 == 0.3)               # False
```

마지막 두 줄이 돈을 `float`으로 다루면 안 되는 이유입니다. 이진수로는 0.1을 정확히 표현할 수 없어 작은 오차가 쌓입니다. 원 단위로 무조건 정수를 쓰면 이 문제가 아예 생기지 않습니다.

```python
# 타입 섞기 실험
try:
    print("1000" + 1)
except TypeError as e:
    print("TypeError:", e)           # can only concatenate str (not "int") to str
print(int("1000") + 1)               # 1001

# 타입 확인과 참/거짓 판정
print(type(3), type(3.0), type("3"), type(True), type(None))
print(bool(0), bool(""), bool([]), bool("0"))   # False False False True
```

빈 값(0, 빈 문자열, 빈 리스트, None)은 조건문에서 거짓으로 취급됩니다. 단 `"0"`처럼 내용이 있는 문자열은 참입니다. 나중에 `if not name:`처럼 문자열 검사를 할 때 이 성질을 씁니다.

### 연습문제

아래 6문제를 `ex01.py`에 풀어 보세요.

1. 수입 50000, 지출 18500일 때 잔액을 `잔액: 31500` 형태로 출력하세요.
2. 예산 300000, 사용 187500일 때 사용률을 퍼센트로 계산해 `62.5`와 정수 반올림 값을 각각 출력하세요. 반올림은 `round()`를 씁니다.
3. 12345원을 만 원 단위 몰과 나머지로 나눠 숫자 두 개를 출력하세요. 한 줄로 끝내야 합니다.
4. `"1000" + 1`이 왜 에러인지 한 줄로 설명하고, 고쳐서 1001을 출력하세요.
5. 예산 300000, 사용 250000일 때 “예산 초과 여부”와 “80% 이상 사용 경고 여부”를 `True/False`로 출력하세요.
6. 사용자가 `"12,500"`처럼 콤마를 넣어 입력했을 때 이것을 정수 12500으로 바꾸세요.

힌트: 2번은 `used / budget * 100`, 3번은 `divmod`, 5번은 비교 연산자의 결과가 그대로 `bool`입니다, 6번은 문자열의 `replace`입니다.

### 정답과 해설

```python
# 1
income, spent = 50000, 18500
print("잔액:", income - spent)               # 잔액: 31500

# 2
budget, used = 300000, 187500
rate = used / budget * 100
print(rate, round(rate))                       # 62.5 62

# 3
print(*divmod(12345, 10000))                   # 1 2345

# 4  문자열과 정수는 더할 수 없어서 TypeError. 문자열을 int로 바꾼다.
print(int("1000") + 1)                        # 1001

# 5
budget, used = 300000, 250000
print(used > budget, used >= budget * 0.8)     # False True

# 6
print(int("12,500".replace(",", "")))          # 12500
```

- 2번: `round(62.5)`가 63이 아니라 62가 나옵니다. 파이썬은 정확히 중간인 수를 짝수 쪽으로 맞춥니다(반올림의 한 방식). 화면에 보여줄 때는 반올림보다 `f"{rate:.1f}"`처럼 포맷을 쓰는 것이 보통입니다(2장).
- 3번: `print(*divmod(...))`의 `*`는 튜플을 풀어 인자 두 개로 넘긴다는 뜻입니다(5장에서 다시 나옵니다).
- 5번: `used >= budget * 0.8`의 0.8은 float이지만 비교에만 쓰이고 저장되는 금액이 아니라서 괜찮습니다. 정수만 쓰려면 `used * 100 >= budget * 80`도 됩니다.

### 미션 연결

금액 `amount`를 정수로 두는 결정과, 사용자가 `abc`나 `12,5oo`를 넣었을 때 변환 실패를 설명하는 에러로 만드는 일(7장)이 이 장에서 시작됩니다.

## 2장. 문자열, f-string, 입력과 출력

문자열은 글자를 순서대로 늘어놓은 값입니다. 날짜(`"2026-10-27"`), 카테고리(`"식비"`), 메모, 태그가 모두 문자열이고, 화면에 금액을 예쁘게 찍는 일도 이 장의 기술입니다.

### 핵심 개념

- 인덱싱 `s[0]`, 슬라이싱 `s[2:5]`: 끝 번호는 포함하지 않습니다. 음수는 뒤에서부터 셉니다.
- 문자열은 바꿀 수 없습니다(불변). `strip()`, `replace()` 같은 메서드는 원본을 고치지 않고 새 문자열을 돌려줍니다.
- 자주 쓰는 메서드: `strip`, `split`, `join`, `replace`, `startswith`, `lower`.
- f-string: `f"{값:서식}"`. 천 단위 콤마 `,`, 소수 자릿수 `.1f`, 정렬 `<` `>` `^`, 0 채우기 `03d`.
- `input()`은 항상 문자열을 돌려줍니다. 숫자로 쓰려면 `int()`로 바꿔야 합니다.

### 따라 하기

```python
s = "2026-10-27"
print(s[:4], s[5:7], s[-2:], s[::-1])   # 2026 10 27 72-01-6202
y, m, d = (int(p) for p in s.split("-"))
print(y, m, d)                          # 2026 10 27

print(f"{1234567:,}원")                  # 1,234,567원
print(f"{62.5:.1f}%")                    # 62.5%
print(f"[{'식비':<6}] [{'food':>8}] [{42:>8,}] [{7:03d}]")
# [식비    ] [    food] [      42] [007]

print("  식비 ".strip())                 # 식비
tags = [t.strip() for t in "a, b ,c".split(",")]
print(tags, ";".join(tags))             # ['a', 'b', 'c'] a;b;c

date, cat, amount = "2026-10-27", "food", 12500
print(f"{date:<12}{cat:<8}{amount:>10,}")
# 2026-10-27  food        12,500
print(f"TX-{12:06d}")                    # TX-000012  (거래 id 만들기)

print("나이", 3, sep=":", end="!\n")      # 나이:3!
```

`split`은 문자열을 쪼개 리스트로, `join`은 리스트를 다시 문자열로 합칩니다. 둘은 서로 반대입니다. CSV의 `tags` 칸에 여러 태그를 `;`로 묶어 넣을 때 바로 씁니다.

```python
raw = input("금액: ")        # 사용자가 12500 입력
print(f"{int(raw):,}원")      # 12,500원
```

### 한글이 섞이면 표 정렬이 틀어지는 이유

터미널에서 한글은 영문보다 두 칸을 차지합니다. 그런데 `ljust`나 `{:<8}`은 글자 수만 셉니다. 그래서 `식비`와 `food`를 같은 폭으로 맞춰도 줄이 어긋납니다. 미션의 보너스 항목인 표 정렬에서 만나게 됩니다. 해법은 글자의 화면 폭을 직접 계산하는 것입니다.

```python
import unicodedata

def width(text: str) -> int:
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in text)

def pad(text: str, w: int) -> str:
    return text + " " * (w - width(text))

print(pad("식비", 8) + "|")   # 식비    |
print(pad("food", 8) + "|")   # food    |
```

### 연습문제

1. `1234567`을 `1,234,567원`으로 출력하세요.
2. `"2026-10-27"`에서 연, 월, 일을 정수 세 개로 꺼내세요.
3. 사용자가 `"  식비 "`처럼 앞뒤에 공백을 넣어 입력했습니다. 공백을 없앤 `"식비"`로 만드세요.
4. `"a, b ,c"`를 `["a", "b", "c"]`로 바꾸고, 다시 `"a;b;c"`로 합치세요.
5. 날짜, 카테고리, 금액을 받아 `2026-10-27  food        12,500`처럼 날짜는 왼쪽 12칸, 카테고리는 왼쪽 8칸, 금액은 오른쪽 10칸으로 맞춰 한 줄로 찍는 코드를 작성하세요.
6. 입력을 받아 금액을 `12,500원`처럼 출력하는 프로그램 `ex02.py`를 만드세요. 사용자가 `12,500`처럼 콤마를 넣어도 동작해야 합니다.
7. (도전) 거래 번호 12를 `TX-000012`로 만드는 코드를 작성하세요.

힌트: 2번은 `split("-")`, 5번은 `{값:<12}`와 `{값:>10,}`, 6번은 1장 6번 답과 `input()`을 합칩니다.

### 정답과 해설

```python
# 1
print(f"{1234567:,}원")

# 2
y, m, d = (int(p) for p in "2026-10-27".split("-"))

# 3
name = "  식비 ".strip()

# 4
tags = [t.strip() for t in "a, b ,c".split(",")]
print(";".join(tags))

# 5
date, cat, amount = "2026-10-27", "food", 12500
print(f"{date:<12}{cat:<8}{amount:>10,}")

# 6
raw = input("금액: ")
print(f"{int(raw.replace(',', '')):,}원")

# 7
print(f"TX-{12:06d}")        # TX-000012
```

- 2번의 `(int(p) for p in ...)`는 컴프리헨션 형태입니다. 6장과 11장에서 자세히 다룹니다. 지금은 세 값을 언패킹해서 받는다는 점만 보면 됩니다.
- 4번에서 `strip()`을 빼면 `" b "`처럼 공백이 남습니다. 사용자 입력은 항상 `strip()`부터 합니다.
- 6번은 `int("12,500")`이 `ValueError`가 되는 문제를 `replace`로 피한 것입니다. 숫자가 아닌 입력에는 아직 대응하지 못합니다. 7장에서 예외 처리로 막습니다.

### 미션 연결

`TX-000012` 같은 id 생성, CSV의 `tags`를 `;`로 합치고 나누는 처리, `list` 명령의 금액 천 단위 표시와 표 정렬이 모두 이 장의 내용입니다.

## 3장. 조건문과 반복문

프로그램이 “만약 이러면 저렇게, 아니면 이렇게”와 “이 작업을 여러 번”을 할 수 있게 해 주는 문법입니다. 거래 목록을 하나씩 훑으며 합계를 내고, 예산의 80%를 넘으면 경고하는 일이 전부 여기서 나옵니다.

### 핵심 개념

- 파이썬은 들여쓰기(스페이스 4칸)로 블록을 구분합니다. `:`로 끝나는 줄 다음은 반드시 들여쓰기입니다.
- `if` / `elif` / `else`는 위에서부터 순서대로 보고 첫 번째로 참인 가지 하나만 실행합니다.
- `for x in 묶음:`은 묶음의 원소를 하나씩 꺼냅니다. `range(n)`은 0부터 n-1까지의 수, `enumerate`는 번호와 값을 함께 줍니다.
- `while 조건:`은 조건이 참인 동안 되풀이합니다. 조건을 바꾸는 코드가 없으면 무한 루프가 됩니다.
- `break`는 반복을 끝내고, `continue`는 이번 회차만 건너뜁니다.
- 비교 연산은 `1 < x < 10`처럼 이어 쓸 수 있고, 논리는 `and`, `or`, `not`입니다.

### 따라 하기

```python
def grade(a):
    if a < 10000:
        return "소액"
    elif a < 100000:
        return "보통"
    else:
        return "고액"

print(grade(500), grade(10000), grade(250000))   # 소액 보통 고액

amounts = [12000, 4500, 38000, 900]
total = 0
for a in amounts:
    total += a
print(total)                                     # 55400

for no, a in enumerate(amounts, start=1):
    print(f"{no}. {a:,}원")                       # 1. 12,000원 ...

# break: 예산 50000의 80%를 처음 넘긴 거래 번호
budget, run, hit = 50000, 0, None
for no, a in enumerate(amounts, start=1):
    run += a
    if run >= budget * 0.8:
        hit = no
        break
print(hit, run)                                  # 3 54500

# continue: 1000원 미만은 건너뛰기
for a in amounts:
    if a < 1000:
        continue
    print("ok", a)
```

`for`에도 `else`가 붙을 수 있습니다. `break` 없이 끝까지 돈 경우에만 실행됩니다. “찾지 못했다”를 처리할 때 쓰지만, 처음에는 `hit = None` 방식이 더 읽기 쉽습니다.

```python
for n in range(2, 8):
    for d in range(2, n):
        if n % d == 0:
            break
    else:
        print("소수", n)        # 소수 2, 3, 5, 7
```

입력을 받는 `while` 패턴은 미션의 대화형 모드에서 다시 씁니다.

```python
total = 0
while True:
    raw = input("금액(끝내려면 q): ").strip()
    if raw == "q":
        break
    total += int(raw)
print(f"합계 {total:,}원")      # 1000, 2500, q 입력 시: 합계 3,500원
```

### 연습문제

1. 금액이 1만 원 미만이면 “소액”, 10만 원 미만이면 “보통”, 그 이상이면 “고액”을 돌려주는 함수 `grade(amount)`를 만드세요.
2. `for`로 1부터 10까지의 합을 구하세요(내장 `sum`은 쓰지 마세요).
3. `[12000, 4500, 38000, 900]`의 합계와 최댓값을 `sum`, `max` 없이 구하세요.
4. 같은 리스트를 `1. 12,000원` 형태로 번호를 붙여 출력하세요.
5. `q`를 입력할 때까지 금액을 받아 누적하고, 끝내면 합계를 출력하는 프로그램을 만드세요. 공백 입력(`" q "`)도 처리해야 합니다.
6. 예산 50000원에서 지출을 순서대로 누적할 때, 누적액이 처음 예산의 80% 이상이 되는 거래의 번호를 구하세요. 해당 없으면 `None`입니다.
7. (도전) 연도가 윤년인지 판별하는 `is_leap(year)`를 만드세요. 4로 나눠지고 100으로 나눠지지 않아야 하며, 400으로 나눠지면 윤년입니다. 1900, 2000, 2024, 2026을 시험해 보세요.

힌트: 3번은 시작값을 리스트의 첫 원소로 두고, 5번은 `while True` + `break`, 7번은 `and`/`or`을 조합합니다.

### 정답과 해설

```python
# 1
def grade(amount):
    if amount < 10000:
        return "소액"
    if amount < 100000:
        return "보통"
    return "고액"

# 2
total = 0
for i in range(1, 11):
    total += i
print(total)                 # 55

# 3
amounts = [12000, 4500, 38000, 900]
t, mx = 0, amounts[0]
for a in amounts:
    t += a
    if a > mx:
        mx = a
print(t, mx)                 # 55400 38000

# 4
for no, a in enumerate(amounts, start=1):
    print(f"{no}. {a:,}원")

# 5
total = 0
while True:
    raw = input("금액(끝내려면 q): ").strip()
    if raw == "q":
        break
    total += int(raw)
print(f"합계 {total:,}원")

# 6
budget, run, hit = 50000, 0, None
for no, a in enumerate(amounts, start=1):
    run += a
    if run >= budget * 0.8:
        hit = no
        break
print(hit)                   # 3

# 7
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print([is_leap(y) for y in (1900, 2000, 2024, 2026)])   # [False, True, True, False]
```

- 1번의 `if` 다음에 `return`이 있으면 `elif`/`else`를 쓰지 않아도 같은 동작입니다. 이를 조기 반환(early return)이라고 부르고, 중첩을 줄이는 데 좋습니다.
- 3번의 최댓값 시작값을 0으로 두면 음수만 들어 있는 리스트에서 틀리고, 빈 리스트에서는 `amounts[0]`이 에러가 됩니다. 빈 리스트 처리는 항상 따로 생각해야 합니다.
- 5번은 `int(raw)`에서 `abc`를 넣으면 프로그램이 죽습니다. 7장에서 고칩니다.
- 7번의 결과는 1900은 평년, 2000은 윤년입니다. 이 규칙은 이후 날짜 검증에서 그대로 쓸 수 있지만, 실제로는 `datetime`이 대신 알아서 처리합니다(14장).

### 미션 연결

대화형 입력 루프, 예산 경고(사용률 80% 이상), 거래 목록 출력 반복문이 이 장의 응용입니다.

## 4장. 리스트, 튜플, 딕셔너리, 집합

값을 여러 개 담는 상자를 컨테이너라고 합니다. 거래 한 건은 딕셔너리로, 거래 여러 건은 리스트로, 카테고리 목록은 집합으로 다룹니다. 이 장을 끝내면 미션의 데이터 모양이 머릿속에 그려집니다.

### 핵심 개념

| 종류 | 모양 | 특징 | 용돈 기입장에서 |
| --- | --- | --- | --- |
| list | `[1, 2]` | 순서 있음, 바꿀 수 있음 | 거래 목록 |
| tuple | `(3, 4)` | 순서 있음, 바꿀 수 없음 | 함수가 값 여러 개 돌려줄 때 |
| dict | `{"a": 1}` | 키로 값을 찾음 | 거래 한 건, 카테고리별 합계 |
| set | `{1, 2}` | 중복 없음, 순서 없음 | 카테고리 중복 제거, 포함 여부 검사 |

- 리스트는 `b = a`로 대입해도 복사되지 않고 같은 리스트를 가리킵니다. 복사하려면 `a.copy()`를 씁니다.
- 딕셔너리에서 없는 키를 `d["x"]`로 읽으면 `KeyError`입니다. 없을 수 있으면 `d.get("x", 기본값)`을 씁니다.
- 파이썬 3.7부터 딕셔너리는 넣은 순서를 기억합니다. 집합은 순서를 보장하지 않습니다. 출력 순서가 실행마다 달라질 수 있으므로 화면에 보여줄 때는 `sorted(set)`으로 정렬합니다.

### 따라 하기

```python
amounts = [12000, 4500, 38000]
amounts.append(900)             # 끝에 추가
amounts.insert(0, 100)          # 맨 앞에 추가
print(amounts, amounts[-1], amounts[1:3], len(amounts))
# [100, 12000, 4500, 38000, 900] 900 [12000, 4500] 5
print(amounts.pop(), amounts.pop(0), amounts)   # 900 100 [12000, 4500, 38000]
amounts.remove(4500)            # 값으로 지움(첫 번째 것만)
print(amounts, 38000 in amounts)  # [12000, 38000] True

a = [1, 2]
b = a                           # 복사가 아니라 동일한 리스트
b.append(3)
print(a)                        # [1, 2, 3]  ← a도 바뀜
c = a.copy()
c.append(4)
print(a, c)                     # [1, 2, 3] [1, 2, 3, 4]

first, *rest = [10, 20, 30]     # 언패킹
print(first, rest)              # 10 [20, 30]
x, y = 1, 2
x, y = y, x                     # 두 값 바꾸기
print(x, y)                     # 2 1
```

```python
tx = {"id": "TX-000001", "date": "2026-10-27", "amount": 12500, "memo": ""}
print(tx["amount"], tx.get("category", "미분류"))   # 12500 미분류
tx["amount"] = 13000            # 수정
tx["category"] = "식비"         # 추가
for k, v in tx.items():
    print(k, v)
print("memo" in tx)             # True  (키 검사)
del tx["memo"]                  # 삭제

cats = ["식비", "교통", "식비", "문화", "교통"]
print(sorted(set(cats)))        # ['교통', '문화', '식비']

# 카테고리별 합계: 딕셔너리 누적 패턴
sums = {}
for cat, amt in [("식비", 12000), ("교통", 1500), ("식비", 8000)]:
    sums[cat] = sums.get(cat, 0) + amt
print(sums)                     # {'식비': 20000, '교통': 1500}

print({"a", "b"} & {"b", "c"}, {"a", "b"} - {"b"})   # {'b'} {'a'}
```

마지막의 “`get(k, 0) + 값`” 패턴이 월별·카테고리별 합계의 표준 형태입니다. 6장에서 `defaultdict`로 더 짧게 만듭니다.

### 연습문제

1. `[12000, 4500, 38000]`에 900을 끝에 추가하고, 마지막 원소를 꺼내서 출력하세요.
2. `a = [1, 2]`, `b = a`로 두고 `b.append(3)`을 했을 때 `a`가 왜 바뀌는지 한 문장으로 설명하고, `a`는 그대로 두는 방법을 쓰세요.
3. 거래 딕셔너리 `{"id": "TX-000001", "amount": 12500}`에서 `category`를 읽되, 없으면 “미분류”를 쓰도록 하세요. 그 다음 `memo`를 빈 문자열로 추가하세요.
4. `["식비", "교통", "식비", "문화", "교통"]`에서 중복 없는 카테고리를 가나다순으로 정렬해 출력하세요.
5. `[("식비", 12000), ("교통", 1500), ("식비", 8000)]`에서 카테고리별 합계 딕셔너리를 만드세요.
6. `first, *rest = [10, 20, 30]`의 결과를 예측하고 실행해 확인하세요. 그 다음 변수 두 개의 값을 한 줄로 바꾸세요.
7. (도전) `[{"id": "TX-1", "amount": 5000}, {"id": "TX-2", "amount": 30000}, {"id": "TX-3", "amount": 12000}]`에서 금액 1만 원 이상인 거래의 id만 리스트로 뽑으세요. 컴프리헨션(6장)을 아직 모른다면 `for`와 `append`로 풀어도 됩니다.

힌트: 3번은 `get`, 4번은 `set`과 `sorted`, 5번은 `sums.get(cat, 0) + amt`입니다.

### 정답과 해설

```python
# 1
lst = [12000, 4500, 38000]
lst.append(900)
print(lst.pop())                         # 900

# 2  b는 a와 같은 리스트를 가리키는 또 다른 이름일 뿐이라서다.
a = [1, 2]
b = a.copy()
b.append(3)
print(a, b)                              # [1, 2] [1, 2, 3]

# 3
tx = {"id": "TX-000001", "amount": 12500}
print(tx.get("category", "미분류"))         # 미분류
tx["memo"] = ""

# 4
print(sorted(set(["식비", "교통", "식비", "문화", "교통"])))   # ['교통', '문화', '식비']

# 5
sums = {}
for cat, amt in [("식비", 12000), ("교통", 1500), ("식비", 8000)]:
    sums[cat] = sums.get(cat, 0) + amt
print(sums)                              # {'식비': 20000, '교통': 1500}

# 6
first, *rest = [10, 20, 30]              # 10, [20, 30]
x, y = 1, 2
x, y = y, x

# 7
txs = [{"id": "TX-1", "amount": 5000}, {"id": "TX-2", "amount": 30000}, {"id": "TX-3", "amount": 12000}]
big = []
for t in txs:
    if t["amount"] >= 10000:
        big.append(t["id"])
print(big)                               # ['TX-2', 'TX-3']
```

- 2번은 파이썬의 가장 크라시한 함정입니다. 변수는 값을 담은 상자가 아니라 값에 붙은 이름표이므로, 이름을 두 개 붙이면 같은 값이 두 이름으로 불릴 뿐입니다. 함수에 리스트를 넘기면 함수 안에서 고친 결과가 밖에도 보인다는 뜻이기도 합니다.
- `copy()`는 바깥 리스트만 복사하는 얕은 복사입니다. 리스트 안에 딕셔너리가 들어 있으면 안쪽 딕셔너리는 여전히 공유됩니다. 완전히 독립된 복사가 필요하면 `copy.deepcopy`를 씁니다.
- 5번의 패턴에서 `sums[cat] += amt`로 만 쓰면 처음 만나는 카테고리에서 `KeyError`가 나옵니다. 그래서 `get(cat, 0)`이 필요한 겁니다.

### 미션 연결

거래 한 건 = dict(나중에 `dataclass`로 포장, 9장), 거래 목록 = list, 카테고리 유일성 검사 = set, `summary`의 카테고리별 합계 = dict 누적입니다.

## 5장. 함수

함수는 이름을 붙인 작업 덩어리입니다. 같은 코드를 여러 번 복사하지 않고 한 번 정의해 두고 부릅니다. 미션의 계층 분리, 데코레이터, 타입 힌트가 전부 함수를 전제로 하므로 여기서 탄탄히 다져야 합니다.

### 핵심 개념

- `def 이름(인자):` 으로 정의하고 `return`으로 값을 돌려줍니다. `return`이 없으면 `None`을 돌려줍니다.
- 기본값 인자, 키워드 인자, `*args`(위치 인자 묶음), `**kwargs`(키워드 인자 묶음)를 구분합니다.
- `*` 뒤에 쓴 인자는 반드시 이름을 붙여서 넘겨야 합니다(키워드 전용).
- 함수 안에서 만든 변수는 그 함수 안에서만 유효합니다(지역 변수). 바깥 변수를 고치려면 `global`이 필요하지만 가능한 한 쓰지 않는 편이 좋습니다.
- 함수는 값입니다. 변수에 담고, 다른 함수에 넘기고, 리스트에 넣을 수 있습니다(일급 객체). 데코레이터와 `sorted(key=...)`의 기반입니다.
- 기본값에 리스트나 딕셔너리를 쓰면 안 됩니다(아래 함정).

### 따라 하기

```python
def format_won(amount, suffix="원"):
    """금액을 천 단위 콤마 문자열로 바꾼다."""
    return f"{amount:,}{suffix}"

print(format_won(12500))                    # 12,500원
print(format_won(12500, suffix=" KRW"))     # 12,500 KRW

def min_max(values):
    return min(values), max(values)         # 튜플로 두 값을 돌려줌
lo, hi = min_max([3, 9, 1])
print(lo, hi)                               # 1 9

def total(*nums):                           # nums는 튜플
    return sum(nums)
print(total(1, 2, 3), total())              # 6 0

def add_tx(date, amount, *, category="미분류", memo=""):
    return {"date": date, "amount": amount, "category": category, "memo": memo}
print(add_tx("2026-10-27", 5000, category="식비"))
try:
    add_tx("2026-10-27", 5000, "식비")      # 카테고리를 이름 없이 넣으면 오류
except TypeError as e:
    print("TypeError:", e)                  # add_tx() takes 2 positional arguments but 3 were given
```

`add_tx`처럼 부가 정보를 `*` 뒤에 두면 호출하는 쪽이 `category="식비"`라고 적어야 하므로 인자 순서를 헷갈릴 염려가 없습니다.

```python
# 함정 1: 가변 기본값
def bad(item, bucket=[]):
    bucket.append(item)
    return bucket
print(bad(1), bad(2))        # [1, 2] [1, 2]  ← 호출마다 새 리스트가 아니라 같은 리스트를 재사용

def good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
print(good(1), good(2))      # [1] [2]

# 함정 2: 지역/전역 변수
count = 0
def broken():
    count += 1               # UnboundLocalError
try:
    broken()
except UnboundLocalError as e:
    print(e)                 # cannot access local variable 'count' where it is not associated with a value
```

기본값은 함수를 정의할 때 단 한 번 만들어집니다. 그래서 바꿀 수 있는 값(리스트, 딕셔너리)을 기본값으로 쓰면 호출들이 서로 영향을 줍니다. `None`을 두고 함수 안에서 만드는 것이 관례입니다.

```python
# 함수를 값으로 다루기
print(sorted([5, 3, 8], key=lambda n: -n))    # [8, 5, 3]
txs = [{"d": "2026-10-02", "a": 3}, {"d": "2026-10-01", "a": 9}]
print(sorted(txs, key=lambda t: t["d"])[0]["a"])   # 9  (날짜 오름차순 첫 항목)

def apply(f, x):
    return f(x)
print(apply(format_won, 1000), apply(len, "abc"))   # 1,000원 3
```

`lambda 인자: 식`은 이름 없는 한 줄짜리 함수입니다. 정렬 기준(`key`)처럼 잠깐 쓰고 버릴 때만 쓰고, 두 줄 이상이면 `def`로 쓰세요.

### 연습문제

1. 잔액을 계산하는 `balance(income, spent)` 함수를 만들고, `balance(50000, 18500)`의 결과를 확인하세요.
2. 사용률(%)을 돌려주는 `usage_rate(used, budget)`를 만드세요. 예산이 0 이하면 나눔셈을 하지 말고 `None`을 돌려주세요.
3. `make_id(n)`을 만들어 `make_id(7)`이 `"TX-000007"`이 되게 하세요.
4. `clamp(value, lo=0, hi=100)`를 만드세요. 값을 `lo`와 `hi` 사이로 자른 결과를 돌려줍니다. `clamp(150)`, `clamp(-5)`, `clamp(50, hi=40)`을 시험하세요.
5. `add_tx(date, amount, *, category="미분류", memo="")`에 대해 `add_tx("2026-10-27", 5000, "식비")`가 왜 오류인지 설명하고, 올바른 호출을 쓰세요.
6. `bad(item, bucket=[])` 함수의 문제를 직접 재현하고, 고쳐 보세요.
7. (도전) 거래 딕셔너리 리스트를 금액 내림차순으로 정렬해 가장 큰 거래의 id를 돌려주는 `biggest_id(txs)`를 `sorted`와 `lambda`로 만드세요.

힌트: 2번은 `if budget <= 0: return None`, 3번은 2장의 `{n:06d}`, 7번은 `key=lambda t: t["amount"]`와 `reverse=True`입니다.

### 정답과 해설

```python
# 1
def balance(income, spent):
    return income - spent
print(balance(50000, 18500))                  # 31500

# 2
def usage_rate(used, budget):
    if budget <= 0:
        return None
    return used / budget * 100
print(usage_rate(187500, 300000), usage_rate(1, 0))   # 62.5 None

# 3
def make_id(n):
    return f"TX-{n:06d}"
print(make_id(7))                              # TX-000007

# 4
def clamp(value, lo=0, hi=100):
    return max(lo, min(value, hi))
print(clamp(150), clamp(-5), clamp(50, hi=40))  # 100 0 40

# 5  category는 키워드 전용이라 이름을 붙여야 한다.
add_tx("2026-10-27", 5000, category="식비")

# 6
def good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

# 7
def biggest_id(txs):
    return sorted(txs, key=lambda t: t["amount"], reverse=True)[0]["id"]
```

- 2번의 `None`은 “계산할 수 없음”을 뜻하는 값입니다. 뒤에서 이 함수를 부르는 쪽이 `None`을 처리해야 합니다. 타입 힌트로는 `float | None`이며 13장에서 다룹니다.
- 4번의 `max(lo, min(value, hi))` 한 줄이 기본 모양입니다. 사용률 막대를 0\~100으로 제한하는 데 쓸 수 있습니다.
- 7번은 정렬 전체가 아니라 최댓값만 필요하므로 `max(txs, key=lambda t: t["amount"])["id"]`가 더 간단하고 빠릅니다. 빈 리스트가 들어오면 두 방식 모두 오류가 나므로 `max(..., default=None)` 같은 처리가 필요합니다.

### 미션 연결

`format_won`은 `list`의 출력에, `usage_rate`는 `budget`의 화면에, `make_id`는 거래 추가에, 키워드 전용 인자는 서비스 함수의 정의에 그대로 쓰입니다.

## 6장. 컴프리헨션, 정렬, 집계

반복문 네 줄이 하던 일을 한 줄로 쓰는 문법과, 데이터를 정렬·합산·묶는 도구들입니다. `summary`(월 합계, 카테고리별 합계), `list`의 최신순 정렬, `search`의 조건 필터가 전부 이 장의 응용입니다.

### 핵심 개념

- 리스트 컴프리헨션: `[식 for x in 묶음 if 조건]`. 딕셔너리·집합도 같은 모양이고, 대괄호를 `()`로 바꾸면 제너레이터 표현식이 됩니다(11장).
- `sorted(묶음, key=..., reverse=...)`는 새 리스트를 돌려주고, `list.sort()`는 원본을 제자리에서 정렬합니다. 두 기준이 필요하면 `key`가 튜플을 돌려주면 됩니다.
- `sum`, `min`, `max`는 제너레이터 표현식과 잘 어울립니다. `any`/`all`은 “하나라도/전부 만족”을 검사합니다.
- `defaultdict(int)`는 없는 키를 읽으면 0으로 시작하고, `defaultdict(list)`는 빈 리스트로 시작합니다. `Counter`는 개수 세기 전용입니다.
- 너무 복잡해지면 컴프리헨션을 포기하고 일반 `for`를 씁니다. 기준은 “한 번에 읽히는가”입니다.

### 따라 하기

아래 데이터를 `ch06.py` 맨 위에 두고 실험합니다.

```python
from collections import defaultdict, Counter

txs = [
    {"id": "TX-1", "date": "2026-10-03", "type": "expense", "category": "식비", "amount": 12000},
    {"id": "TX-2", "date": "2026-10-05", "type": "income",  "category": "용돈", "amount": 50000},
    {"id": "TX-3", "date": "2026-10-09", "type": "expense", "category": "교통", "amount": 1500},
    {"id": "TX-4", "date": "2026-11-01", "type": "expense", "category": "식비", "amount": 8000},
]

print([n * n for n in range(5)])                      # [0, 1, 4, 9, 16]
print([t["id"] for t in txs if t["amount"] >= 10000])  # ['TX-1', 'TX-2']
print({t["id"]: t["amount"] for t in txs})            # {'TX-1': 12000, ...}

print(sum(t["amount"] for t in txs if t["type"] == "expense"))   # 21500
print(max(txs, key=lambda t: t["amount"])["id"])                # TX-2

# 최신순: 날짜가 같으면 id로 한 번 더 비교
print([t["id"] for t in sorted(txs, key=lambda t: (t["date"], t["id"]), reverse=True)])
# ['TX-4', 'TX-3', 'TX-2', 'TX-1']

# 금액 큰 순, 같으면 id 순: 숫자는 부호를 바꿔 내림차순을 만든다
print([t["id"] for t in sorted(txs, key=lambda t: (-t["amount"], t["id"]))])
# ['TX-2', 'TX-1', 'TX-4', 'TX-3']

# 카테고리별 지출 합계
by = defaultdict(int)
for t in txs:
    if t["type"] == "expense":
        by[t["category"]] += t["amount"]
print(dict(by))                                              # {'식비': 20000, '교통': 1500}
print(sorted(by.items(), key=lambda kv: kv[1], reverse=True))  # [('식비', 20000), ('교통', 1500)]

# 월별 묶기: 날짜 문자열의 앞 7글자가 월
month = defaultdict(list)
for t in txs:
    month[t["date"][:7]].append(t["id"])
print(dict(month))      # {'2026-10': ['TX-1', 'TX-2', 'TX-3'], '2026-11': ['TX-4']}

print(Counter(t["category"] for t in txs).most_common(1))   # [('식비', 2)]
print(any(t["amount"] > 40000 for t in txs), all(t["amount"] > 0 for t in txs))   # True True
print(next((t for t in txs if t["id"] == "TX-9"), None))    # None  (찾지 못하면 기본값)

names, vals = ["a", "b"], [1, 2]
print(dict(zip(names, vals)))                                # {'a': 1, 'b': 2}
```

`next(제너레이터, 기본값)`은 “조건에 맞는 첫 원소”를 찾는 관용구입니다. 거래 id로 한 건을 찾는 `update`/`delete`에서 그대로 씁니다.

주의할 점이 하나 있습니다. `[[0] * 2 for _ in range(2)]`는 독립된 두 행이지만 `[[0] * 2] * 2`는 같은 행을 두 번 참조합니다(4장의 리스트 복사 함정과 같은 원리).

### 연습문제

위 `txs`를 그대로 쓰세요.

1. 1부터 10까지 수 중 짝수의 제곱을 리스트 컴프리헨션으로 만드세요.
2. 지출(`expense`) 거래의 id 리스트를 만드세요.
3. 총수입과 총지출과 잔액을 각각 계산하세요(제너레이터 표현식과 `sum`).
4. 10월(`"2026-10"`)의 지출 합계를 구하세요. `date`가 `"2026-10"`로 시작하는지는 `startswith`로 봅니다.
5. 카테고리별 지출 합계를 `defaultdict`로 만들고, 큰 순으로 정렬해 `식비: 20,000원` 형태로 한 줄씩 출력하세요.
6. 최신 날짜순(같은 날짜면 id 내림차순)으로 정렬한 뒤 상위 2건의 id를 출력하세요.
7. id가 `TX-3`인 거래를 찾고, 없으면 “없음”을 출력하세요(`next` 사용).
8. (도전) 월별 수입, 지출, 잔액 표를 `2026-10  수입 50,000  지출 13,500  잔액 36,500` 형태로 출력하세요. 11월은 수입이 없으므로 0으로 나와야 합니다.

힌트: 4번은 `t["date"].startswith("2026-10")`, 5번은 `sorted(by.items(), key=..., reverse=True)`, 8번은 `defaultdict`를 월마다 두 개(수입, 지출) 두면 편합니다.

### 정답과 해설

```python
# 1
print([n * n for n in range(1, 11) if n % 2 == 0])     # [4, 16, 36, 64, 100]

# 2
print([t["id"] for t in txs if t["type"] == "expense"])   # ['TX-1', 'TX-3', 'TX-4']

# 3
income = sum(t["amount"] for t in txs if t["type"] == "income")
expense = sum(t["amount"] for t in txs if t["type"] == "expense")
print(income, expense, income - expense)               # 50000 21500 28500

# 4
print(sum(t["amount"] for t in txs
          if t["type"] == "expense" and t["date"].startswith("2026-10")))   # 13500

# 5
by = defaultdict(int)
for t in txs:
    if t["type"] == "expense":
        by[t["category"]] += t["amount"]
for cat, amt in sorted(by.items(), key=lambda kv: kv[1], reverse=True):
    print(f"{cat}: {amt:,}원")      # 식비: 20,000원 / 교통: 1,500원

# 6
latest = sorted(txs, key=lambda t: (t["date"], t["id"]), reverse=True)
print([t["id"] for t in latest[:2]])    # ['TX-4', 'TX-3']

# 7
found = next((t for t in txs if t["id"] == "TX-3"), None)
print(found if found else "없음")

# 8
income_by, expense_by = defaultdict(int), defaultdict(int)
for t in txs:
    target = income_by if t["type"] == "income" else expense_by
    target[t["date"][:7]] += t["amount"]
for ym in sorted(set(income_by) | set(expense_by)):
    i, e = income_by[ym], expense_by[ym]
    print(f"{ym}  수입 {i:,}  지출 {e:,}  잔액 {i - e:,}")
# 2026-10  수입 50,000  지출 13,500  잔액 36,500
# 2026-11  수입 0  지출 8,000  잔액 -8,000
```

- 3번의 `sum(... for ...)`에는 대괄호가 없습니다. 제너레이터 표현식은 리스트를 만들지 않고 하나씩 넘겨주므로 메모리를 아끷니다.
- 4번의 `date` 처리는 문자열이 `YYYY-MM-DD` 형식일 때만 정확합니다. 이 형식을 강제하는 검증이 왜 필요한지 11장·14장에서 다시 다룹니다.
- 8번에서 `income_by[ym]`처럼 없는 키를 읽으면 `defaultdict`는 0을 만들어 돌려줍니다. 일반 딕셔너리였다면 `KeyError`였을 겁니다.

### 미션 연결

`summary` 명령의 월 합계·카테고리별 합계·잔액 계산, `list`의 최신순 정렬, `update`/`delete`의 id 검색이 모두 이 장의 도구로 끝납니다.

## 7장. 예외 처리

예외는 “프로그램이 계속할 수 없는 상황”을 알리는 파이썬의 방식입니다. 잡지 않으면 프로그램이 죽고 긴 오류 추적(traceback)이 출력됩니다. 이 미션은 사용자에게 원인과 힌트만 보여주고 스택 트레이스는 보여주지 않으며, 실패 시 종료 코드를 0이 아닌 값으로 돌려주라고 요구합니다. 이 장이 그 요구사항의 문법적 기반입니다.

### 핵심 개념

- `try` 안에서 오류가 나면 해당 종류의 `except`로 점프합니다. `else`는 오류가 없을 때, `finally`는 무조건 실행됩니다(파일 닫기 등 정리 작업).
- 예외는 종류가 있습니다: `ValueError`, `TypeError`, `KeyError`, `FileNotFoundError` 등. 바로 그 종류만 잡는 것이 좋습니다.
- `except Exception`으로 모든 것을 잡으면 프로그램 버그도 존리시켜 버려 원인 추적이 어렵습니다. 맨 바깥 한 곳(`main`)에서만 마지막 안전망으로 쓰세요.
- `raise`로 직접 예외를 발생시킵니다. `raise 새예외 from 원인`은 원인 연결, `from None`은 원래 오류를 숨깁니다.
- 자신만의 예외 클래스는 `Exception`을 상속해 만듭니다. 이 예외에 `hint`와 `exit_code`를 넣어 두면 오류 출력이 일관됩니다.
- 프로그램의 종료 코드: 성공 0, 실패는 0이 아닌 값. 터미널에서 `echo $?`(Windows는 `echo %ERRORLEVEL%`)로 확인합니다.

### 따라 하기

```python
try:
    int("12,5oo")
except ValueError as e:
    print("ValueError:", e)     # invalid literal for int() with base 10: '12,5oo'

def demo():
    try:
        print("try")
        return 1
    except Exception:
        print("except")
    else:
        print("else")
    finally:
        print("finally")
print(demo())      # try, finally, 1  (return 전에도 finally는 실행)
```

이번에는 미션 스타일의 오류 체계를 직접 만듭니다. `ch07.py`로 저장해 실행합니다.

```python
import sys

class BudgetError(Exception):
    exit_code = 1
    def __init__(self, cause: str, hint: str = ""):
        super().__init__(cause)
        self.cause = cause
        self.hint = hint

class ValidationError(BudgetError):
    exit_code = 2

class NotFoundError(BudgetError):
    exit_code = 3

def find(txs, tx_id):
    for t in txs:
        if t["id"] == tx_id:
            return t
    raise NotFoundError(f"거래 {tx_id}를 찾을 수 없습니다.", "list 명령으로 id를 확인하세요.")

def main() -> int:
    try:
        find([{"id": "TX-1"}], "TX-9")
        return 0
    except BudgetError as e:
        print(f"오류: {e.cause}", file=sys.stderr)
        if e.hint:
            print(f"힌트: {e.hint}", file=sys.stderr)
        return e.exit_code
    except Exception as e:
        print(f"예상하지 못한 오류: {type(e).__name__}", file=sys.stderr)
        return 99

if __name__ == "__main__":
    sys.exit(main())
```

실행하면 스택 트레이스 없이 다음처럼 나오고 종료 코드는 3입니다.

```text
오류: 거래 TX-9를 찾을 수 없습니다.
힌트: list 명령으로 id를 확인하세요.
```

오류 메시지를 `stderr`(`file=sys.stderr`)로 보내는 이유는 정상 출력과 오류 출력을 터미널에서 따로 다룰 수 있게 하기 위함입니다. 예를 들어 `> out.txt`로 파일에 저장해도 오류는 화면에 남습니다.

```python
# 원인 연결과 파일 오류
try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise ValueError("계산 실패") from e
except ValueError as e:
    print(repr(e.__cause__))       # ZeroDivisionError('division by zero')

try:
    open("no_such.txt")
except FileNotFoundError as e:
    print(type(e).__name__, e.filename)   # FileNotFoundError no_such.txt
```

### 연습문제

1. `int("abc")`이 만드는 예외를 잡아 “숫자가 아닙니다”를 출력하세요.
2. `BudgetError`/`ValidationError`를 위의 코드로 정의하고, `parse_amount(raw)`를 만드세요. 콤마는 허용하고, 숫자가 아니거나 0 이하이면 원인과 힌트가 들어 있는 `ValidationError`를 발생시킵니다.
3. 아래 코드의 출력 순서를 먼저 예상한 뒤 실행해 확인하세요.

```python
def f():
    try:
        return "A"
    finally:
        print("B")
print(f())
```

4. 파일이 없으면 빈 리스트를, 있으면 줄 리스트를 돌려주는 `load_lines(path)`를 만드세요.
5. `main()`이 종료 코드를 돌려주고, 오류는 `stderr`로 원인과 힌트를 출력하도록 만드세요. 실행 후 터미널에서 종료 코드를 확인하세요.
6. 아래 코드가 왜 나쁜 습관인지 한 두 문장으로 설명하고 고치세요.

```python
try:
    value = int(raw)
except:
    pass
```

7. (도전) `ask(prompt, parse)`를 만드세요. `parse`가 `ValidationError`를 내면 원인과 힌트를 화면에 보여주고 다시 입력을 받습니다. 올바른 값이 들어올 때까지 되풀이합니다.

힌트: 2번은 `int()` 변환을 `try`로 감싼 뒤 `raise ... from None`, 4번은 `except FileNotFoundError`, 7번은 `while True` + `try/except` + `return`입니다.

### 정답과 해설

```python
# 1
try:
    int("abc")
except ValueError:
    print("숫자가 아닙니다")

# 2
def parse_amount(raw):
    try:
        value = int(raw.strip().replace(",", ""))
    except ValueError:
        raise ValidationError(f"금액 '{raw}'은(는) 숫자가 아닙니다.", "예: 12500 또는 12,500") from None
    if value <= 0:
        raise ValidationError(f"금액은 1 이상이어야 합니다. (입력: {value})", "지출/수입은 양수로 입력하세요.")
    return value

# 3  B 출력 후 A  (return 값이 정해진 뒤에 finally가 실행되고, 그 다음 print가 A를 출력)

# 4
def load_lines(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

# 5  본문의 main() 코드
#    python ch07.py; echo $?   → 3

# 6  모든 오류(심지어 Ctrl+C)를 삼켜 실패해도 아무일 없는 것처럼 보이고, value도 정의되지 않는다.
try:
    value = int(raw)
except ValueError:
    value = None        # 또는 사용자에게 알리고 다시 입력

# 7
def ask(prompt, parse):
    while True:
        raw = input(prompt)
        try:
            return parse(raw)
        except ValidationError as e:
            print(f"  ! {e.cause} ({e.hint})")
```

- 2번의 `from None`은 사용자에게 내부 오류 이름(`ValueError: invalid literal...`)을 숨기기 위한 것이지, 디버깅 정보를 잃는 것이 아닙니다. 로그에는 원래 오류를 남기고 싶다면 `from e`를 쓰고 사용자 화면에는 `e.cause`만 보이면 됩니다.
- 3번은 답이 “B가 먼저, 다음에 A”입니다. `print(f())`에서 `f()`가 끝나야 출력되기 때문입니다.
- 6번의 `except:`만 쓰는 형태는 `KeyboardInterrupt`까지 잡아 Ctrl+C로 종료할 수도 없게 됩니다.
- 7번은 15장의 대화형 입력에서 그대로 쓰입니다.

### 미션 연결

“원인 + 힌트” 메시지, 스택 트레이스 숨기기, 0이 아닌 종료 코드가 이 장의 내용입니다. 이것을 12장의 `@handle_errors` 데코레이터로 한 번 더 묶으면 모든 명령에 같은 규칙이 적용됩니다.

## 8장. 파일 입출력

프로그램이 꺼지면 메모리의 데이터는 사라집니다. 거래 내역을 남기려면 파일에 저장해야 합니다. 미션의 핵심 평가 항목인 “저장 방식 설명”이 이 장에 다 들어 있습니다.

### 핵심 개념

- 파일은 항상 `with open(...) as f:`로 열어야 합니다. 블록이 끝나면 오류가 나도 자동으로 닫힙니다.
- 모드: `"r"` 읽기, `"w"` 쓰기(기존 내용 삭제), `"a"` 끝에 추가. 한글이 있는 파일은 `encoding="utf-8"`을 반드시 지정합니다. 지정하지 않으면 운영체제마다 기본 인코딩이 달라(Windows는 cp949가 될 수 있음) 다른 컴퓨터에서 깨집니다.
- JSON은 딕셔너리·리스트를 문자열로 바꾸는 형식입니다. 한글을 그대로 쓰려면 `ensure_ascii=False`를 넣습니다.
- JSONL(JSON Lines)은 한 줄에 JSON 하나씩 쓰는 형식입니다. 줄 단위로 읽을 수 있어 큰 파일도 한 번에 메모리에 올리지 않고 스트리밍할 수 있고, 새 거래는 파일 끝에 한 줄만 추가하면 됩니다.
- CSV는 표 형식의 문자열입니다. `csv` 모듈을 쓰면 메모 안의 콤마나 따옴표를 알아서 처리해 줍니다. `open(..., newline="")`를 빼먹으면 Windows에서 빈 줄이 끼어듭니다.
- `pathlib.Path`는 경로를 객체로 다룹니다. `/` 연산자로 이어 붙이고, `exists()`, `mkdir(parents=True, exist_ok=True)`, `read_text`, `write_text`를 제공합니다.
- 저장 도중 오류로 파일이 절반만 써지면 데이터가 손상됩니다. 임시 파일에 많든 뒤 `os.replace`로 한 번에 바꾸는 것이 원자적 저장이며 미션의 보너스 항목입니다.

### 따라 하기

`ch08.py`로 저장해 실행합니다. 현재 폴더 아래에 `data/`가 생깁니다.

```python
import csv, json, os, tempfile
from pathlib import Path

data_dir = Path("data")
data_dir.mkdir(parents=True, exist_ok=True)

# 1) 텍스트
p = data_dir / "memo.txt"
p.write_text("점심\n커피\n", encoding="utf-8")
print(p.read_text(encoding="utf-8").splitlines())      # ['점심', '커피']
with open(p, "a", encoding="utf-8") as f:               # 끝에 추가
    f.write("택시\n")
with open(p, encoding="utf-8") as f:
    for line in f:                                       # 한 줄씩 스트리밍
        print(line.rstrip("\n"), end="|")                # 점심|커피|택시|
print()

# 2) JSON
tx = {"id": "TX-000001", "date": "2026-10-27", "type": "expense",
      "category": "식비", "amount": 12500, "memo": "점심", "tags": ["lunch"]}
print(json.dumps(tx, ensure_ascii=False))   # 한글 그대로
print(json.dumps(tx))                       # "식비" 처럼 이스케이프됨
print(json.loads(json.dumps(tx, ensure_ascii=False)) == tx)   # True
```

`ensure_ascii`를 생략해도 프로그램이 다시 읽을 때는 같은 값이지만, 사람이 파일을 열어 확인할 때 읽기 힘들어집니다. 미션 평가에서 저장 파일을 보여 줄 때 반드시 한글이 읽히도록 해 두세요.

```python
# 3) JSONL: 쓰기와 제너레이터로 읽기
jl = data_dir / "transactions.jsonl"
with open(jl, "w", encoding="utf-8") as f:
    for i in (1, 2):
        f.write(json.dumps({**tx, "id": f"TX-{i:06d}"}, ensure_ascii=False) + "\n")

def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue                    # 빈 줄은 건너뜀
            try:
                yield json.loads(line)
            except json.JSONDecodeError as e:
                raise ValueError(f"{path}:{n}행이 올바른 JSON이 아닙니다 ({e.msg})") from None

print([r["id"] for r in read_jsonl(jl)])    # ['TX-000001', 'TX-000002']
```

`read_jsonl`의 `yield`는 11장에서 자세히 배웁니다. 지금은 “줄 하나를 읽을 때마다 바깥에 하나씩 내준다”는 정도로 이해하면 충분합니다.

```python
# 4) CSV: 메모에 콤마가 있어도 안전
cp = data_dir / "export.csv"
fields = ["date", "type", "category", "amount", "memo", "tags"]
with open(cp, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerow({"date": "2026-10-27", "type": "expense", "category": "식비",
                "amount": 12500, "memo": "점심, 김밥", "tags": "lunch;work"})
print(cp.read_text(encoding="utf-8"))
# date,type,category,amount,memo,tags
# 2026-10-27,expense,식비,12500,"점심, 김밥",lunch;work

with open(cp, encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        print(row["memo"], int(row["amount"]), row["tags"].split(";"))
# 점심, 김밥 12500 ['lunch', 'work']
```

읽어 온 CSV의 모든 값은 문자열입니다. `amount`는 `int()`로 변환하고, 변환 실패를 어느 행에서 났는지 알려 주는 것이 가져오기(import)의 품질을 좌우합니다(15장).

```python
# 5) 원자적 저장: 임시 파일에 쓰고 한 번에 교체
def atomic_write_text(path: Path, text: str) -> None:
    fd, tmp = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        os.replace(tmp, path)           # 실패해도 원본은 온전
    except BaseException:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise

atomic_write_text(data_dir / "budgets.json",
                  json.dumps({"2026-10": 300000}, ensure_ascii=False, indent=2))
```

`os.replace`는 같은 파일 시스템 안에서 이름을 한 번에 바꾸므로, 독자는 “옛 파일 전체” 또는 “새 파일 전체”만 보게 됩니다. 임시 파일을 같은 폴더(`dir=path.parent`)에 만드는 이유가 이것입니다.

### 연습문제

1. `memo.txt`에 세 줄을 쓰고, 다시 읽어 줄 리스트로 출력하세요. 그 다음 한 줄을 끝에 추가하세요.
2. 거래 딕셔너리를 JSON 문자열로 바꾸되 한글이 그대로 보이게 하고, 다시 딕셔너리로 되돌려 같은지 비교하세요.
3. 거래 3건을 JSONL로 저장하고, 줄 단위로 읽어 `amount`의 합계를 구하세요. 읽는 함수는 제너레이터로 만드세요.
4. 읽는 함수가 깨진 줄을 만나면 “파일명 + 몇 번째 줄 + 이유”를 담은 `ValueError`를 발생시키도록 고치세요. `{oops}` 같은 줄을 직접 넣어 시험합니다.
5. 메모에 `점심, 김밥`처럼 콤마가 들어 있는 거래를 CSV로 내보내고 다시 읽어서 행이 망가지지 않는지 확인하세요.
6. `Path`로 `data` 폴더가 없으면 만들고, `data/transactions.jsonl`이 있는지 검사하세요. 없으면 빈 파일을 만드는 것까지 해 보세요.
7. (도전) `atomic_write_text`를 본문을 보지 않고 직접 쓰고, 도중에 예외가 나도 원본이 남는지 시험하세요(쓰는 도중 `raise RuntimeError`를 일부러 내봅니다).

힌트: 3번은 `yield json.loads(line)`, 4번은 `enumerate(f, start=1)`와 `json.JSONDecodeError`, 6번은 `Path.touch()`, 7번은 `tempfile.mkstemp`와 `os.replace`입니다.

### 정답과 해설

```python
# 1
from pathlib import Path
p = Path("memo.txt")
p.write_text("a\nb\nc\n", encoding="utf-8")
print(p.read_text(encoding="utf-8").splitlines())    # ['a', 'b', 'c']
with open(p, "a", encoding="utf-8") as f:
    f.write("d\n")

# 2
import json
tx = {"id": "TX-1", "memo": "점심", "amount": 12500}
s = json.dumps(tx, ensure_ascii=False)
print(s, json.loads(s) == tx)                          # {..."점심"...} True

# 3
def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)

with open("t.jsonl", "w", encoding="utf-8") as f:
    for a in (1000, 2000, 3000):
        f.write(json.dumps({"amount": a}) + "\n")
print(sum(r["amount"] for r in read_jsonl("t.jsonl")))    # 6000

# 4  본문의 read_jsonl 시험 결과 예
#    bad.jsonl 2행: JSON 형식 오류 (Expecting property name enclosed in double quotes)

# 5  본문의 DictWriter/DictReader 예제에서 memo 값이 그대로 돌아오면 성공

# 6
d = Path("data")
d.mkdir(parents=True, exist_ok=True)
f = d / "transactions.jsonl"
if not f.exists():
    f.touch()

# 7  본문의 atomic_write_text에 쓰는 도중 raise를 넣으면
#    원본 내용이 그대로 남고 .tmp 조각도 지워진다.
```

- 3번에서 읽기 함수가 리스트를 만들지 않고 `yield`하는 것이 포인트입니다. 거래가 백만 건이어도 `sum(... for ...)`은 한 줄씩만 메모리에 올립니다.
- 4번의 오류 문구는 사용자가 스스로 고칠 수 있게 “어느 파일의 몇 번째 줄”을 알려주는 것이 핵심입니다. 미션의 “원인 + 힌트” 요구와 정확히 일치합니다.
- 7번은 “파일이 절반만 써지는 사고”를 막는 장치입니다. 소규모 프로젝트에서는 보너스 수준이지만, 수정·삭제처럼 파일 전체를 다시 쓰는 연산에서는 꼭 필요합니다.

### 미션 연결

저장 파일 3개(transactions·categories·budgets)의 형식 선택, `--data-dir` 옵션의 경로 처리, 제너레이터 스트리밍 읽기, CSV 가져오기·내보내기, 원자적 저장 보너스가 모두 여기서 나옵니다.

## 9장. 클래스와 dataclass

클래스는 “데이터와 그 데이터를 다루는 함수를 한 묶음으로 만든 설계도”입니다. 용돈 기입장에서 거래 한 건(`Transaction`)은 데이터 묶음, 거래를 저장하는 일(`Repository`)과 규칙을 적용하는 일(`Service`)은 역할 묶음입니다. 미션이 요구하는 “클래스 2개 이상, dataclass 1개 이상, 계층별 책임 설명”이 모두 여기서 나옵니다.

### 핵심 개념

- `class` 는 설계도, 실제로 만든 것이 인스턴스(객체)입니다. `__init__`은 인스턴스를 만들 때 초기값을 넣는 메서드입니다.
- `self`는 메서드를 부른 그 객체 자신입니다. 호출할 때는 쓰지 않지만 정의할 때는 반드시 첫 인자로 적습니다(자주 나는 실수).
- `__repr__`는 객체를 출력할 때의 모양을 정합니다. 디버깅에 큰 도움이 됩니다.
- `@dataclass`는 `__init__`, `__repr__`, `__eq__`를 자동으로 만들어 주는 데이터 전용 클래스 도구입니다. 필드마다 타입 힌트를 적습니다.
- 리스트·딕셔너리 같은 가변 값의 기본값은 `field(default_factory=list)`로 지정합니다.
- `__post_init__`은 객체가 만들어진 직후에 자동으로 호출되는 훅으로, 값 검증에 좋습니다.
- `@property`는 메서드를 속성처럼 `t.signed_amount`로 읽게 합니다. `@classmethod`는 인스턴스 없이 `Transaction.from_dict(...)`로 호출하는 생성 함수입니다.
- `@dataclass(frozen=True)`는 만든 뒤 값을 바꿀 수 없게 합니다.

### 따라 하기

```python
from dataclasses import dataclass, field, asdict
from datetime import date

class Counter:
    def __init__(self, start: int = 0):
        self.value = start
    def inc(self) -> None:
        self.value += 1
    def __repr__(self) -> str:
        return f"Counter({self.value})"

c = Counter(); c.inc(); c.inc()
print(c, c.value)                  # Counter(2) 2
```

이제 거래 한 건을 클래스로 만듭니다. 이것이 미션의 `models` 모듈입니다.

```python
@dataclass
class Transaction:
    id: str
    date: str
    type: str          # "income" | "expense"
    category: str
    amount: int
    memo: str = ""
    tags: list[str] = field(default_factory=list)

    def __post_init__(self):
        if self.type not in ("income", "expense"):
            raise ValueError(f"type은 income 또는 expense여야 합니다: {self.type!r}")
        if self.amount <= 0:
            raise ValueError("amount는 1 이상이어야 합니다")
        date.fromisoformat(self.date)      # 형식이 틀리면 ValueError

    @property
    def signed_amount(self) -> int:
        return self.amount if self.type == "income" else -self.amount

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "Transaction":
        return cls(id=d["id"], date=d["date"], type=d["type"], category=d["category"],
                   amount=int(d["amount"]), memo=d.get("memo", ""), tags=list(d.get("tags", [])))

t = Transaction("TX-000001", "2026-10-27", "expense", "식비", 12500, "점심")
print(t)
# Transaction(id='TX-000001', date='2026-10-27', type='expense', category='식비', amount=12500, memo='점심', tags=[])
print(t.signed_amount)                         # -12500
print(Transaction.from_dict(t.to_dict()) == t) # True  (dataclass가 == 도 만들어 줬다)
```

필드마다 리스트 `tags`를 독립적으로 갖게 하는 이유를 확인해 봅시다. 아래처럼 쓰면 파이썬이 정의 시점에 오류로 막아 줍니다.

```python
try:
    @dataclass
    class X:
        tags: list = []
except ValueError as e:
    print(e)   # mutable default <class 'list'> for field tags is not allowed: use default_factory
```

그리고 이제 계층을 나눕니다. 저장소는 “어디에 어떻게 넣고 뽑는가”만, 서비스는 “어떤 규칙으로 만들고 계산하는가”를 담당합니다. 여기서는 메모리에 저장하는 버전으로 원리만 봅니다.

```python
class TransactionRepository:                 # 저장소: 저장과 조회만
    def __init__(self):
        self._items: list[Transaction] = []
    def add(self, t: Transaction) -> None:
        self._items.append(t)
    def all(self):
        yield from self._items
    def next_id(self) -> str:
        return f"TX-{len(self._items) + 1:06d}"

class TransactionService:                    # 서비스: 규칙과 계산
    def __init__(self, repo: TransactionRepository):
        self.repo = repo
    def add_expense(self, d: str, category: str, amount: int, memo: str = "") -> Transaction:
        t = Transaction(self.repo.next_id(), d, "expense", category, amount, memo)
        self.repo.add(t)
        return t
    def balance(self) -> int:
        return sum(t.signed_amount for t in self.repo.all())

svc = TransactionService(TransactionRepository())
svc.add_expense("2026-10-27", "식비", 12500)
svc.add_expense("2026-10-28", "교통", 1500)
print(svc.balance(), [t.id for t in svc.repo.all()])   # -14000 ['TX-000001', 'TX-000002']
```

저장소를 파일 기반으로 바꿔도 `TransactionService`는 한 줄도 고칠 필요가 없습니다. 이것이 계층 분리의 이득입니다. 평가에서 “계층별 책임”을 물으면 다음 표로 답합니다.

| 계층 | 역할 | 하면 안 되는 것 |
| --- | --- | --- |
| models | 데이터 모양과 값 검증 | 파일 읽기, 화면 출력 |
| repository | 파일에 저장·조회 | 예산 계산 같은 업무 규칙, print |
| service | 업무 규칙, 집계, 검증 | 파일 경로·형식, argparse |
| cli | 명령 파싱과 출력 | 파일 직접 접근, 집계 계산 |

### 연습문제

1. `Wallet` 클래스를 만드세요. `balance` 속성, `deposit(n)`, `withdraw(n)` 메서드를 가집니다. 입금액이 0 이하이거나 잔액보다 큰 출금은 `ValueError`로 거부합니다.
2. 위 `Wallet`에 `__repr__`을 추가해 `print(w)`가 `Wallet(balance=1,200)`처럼 나오게 하세요.
3. `@dataclass`로 `Category(id: str, name: str, kind: str = "expense")`를 만들고, 값이 같은 두 객체가 `==`으로 같다고 나오는지 확인하세요.
4. `tags: list[str] = []`로 쓰면 무슨 일이 일어나는지 실제로 실행해 보고, 올바른 방식으로 고치세요.
5. `Transaction.__post_init__`에서 날짜가 `2026-13-01`처럼 잘못되면 한국어 메시지의 `ValueError`를 내게 하세요. 또 `2026-1-5`처럼 자릿수가 틀린 날짜도 거부해야 합니다.
6. `to_dict`/`from_dict`를 만들고, `memo`가 없는 딕셔너리로도 객체가 만들어지는지 시험하세요.
7. (도전) `TransactionService`에 `monthly_total(ym, type)`을 추가하세요. `ym`은 `"2026-10"` 형태이고, 저장소에 접근할 때는 `self.repo.all()`만 써야 합니다.

힌트: 1번은 `if n > self.balance: raise ...`, 2번의 천 단위는 `{self.balance:,}`, 5번은 `date.fromisoformat(s).isoformat() == s`를 비교합니다.

### 정답과 해설

```python
# 1, 2
class Wallet:
    def __init__(self, balance: int = 0):
        self.balance = balance
    def deposit(self, n: int) -> None:
        if n <= 0:
            raise ValueError("입금액은 1 이상이어야 합니다")
        self.balance += n
    def withdraw(self, n: int) -> None:
        if n > self.balance:
            raise ValueError(f"잔액 부족: 잔액 {self.balance:,}원, 요청 {n:,}원")
        self.balance -= n
    def __repr__(self) -> str:
        return f"Wallet(balance={self.balance:,})"

# 3
@dataclass
class Category:
    id: str
    name: str
    kind: str = "expense"
print(Category("C1", "식비") == Category("C1", "식비"))   # True

# 4  ValueError: mutable default ... use default_factory
@dataclass
class Y:
    tags: list[str] = field(default_factory=list)

# 5
def _check_date(s: str) -> None:
    try:
        ok = date.fromisoformat(s).isoformat() == s
    except ValueError:
        ok = False
    if not ok:
        raise ValueError(f"날짜 '{s}'이(가) 올바르지 않습니다. YYYY-MM-DD 형태로 입력하세요.")
#    __post_init__ 마지막 줄에서 _check_date(self.date)를 호출

# 6  본문의 from_dict: d.get("memo", "")  → 없으면 빈 문자열

# 7
#    class TransactionService 안에
    def monthly_total(self, ym: str, type_: str) -> int:
        return sum(t.amount for t in self.repo.all()
                   if t.type == type_ and t.date.startswith(ym))
```

- 5번의 `date.fromisoformat`은 파이썬 버전에 따라 `20261027` 같은 형식도 받아들일 수 있습니다(3.11 이후). 그래서 `isoformat() == s` 비교로 정확히 `YYYY-MM-DD`만 허용하는 것이 안전합니다. 미션이 3.10 이상을 요구하므로 버전 차이에 맞서 더욱 중요합니다.
- `__post_init__`에서 검증하면 “잘못된 객체는 만들어지지 않는다”는 보장이 생깁니다. 파일에서 읽어 온 데이터도 `from_dict`를 거치면 같은 검사를 받습니다.
- 7번에서 파일 절대 경로나 `open()`을 서비스가 직접 쓰지 않는 것이 중요합니다. 서비스는 “어떤 저장소인지 모른다”는 상태여야 테스트도 쉬워집니다(16장).

### 미션 연결

`Transaction`은 요구사항의 dataclass, `Repository`와 `Service`는 클래스 2개 이상 조건, 위의 계층 표는 동료 평가의 “계층별 책임” 답변의 뼈대입니다.

## 10장. 모듈과 패키지

파일 하나가 모듈, 모듈을 담은 폴더가 패키지입니다. 미션은 소스를 최소 3개 모듈로 나누고 `python -m budget_app`으로 실행되게 만들라고 요구합니다. 이 장을 끝내면 그 구조를 직접 만들 수 있습니다.

### 핵심 개념

- `import x`, `from x import y`, `from . import z`(같은 패키지 안의 모듈, 상대 import)를 구분합니다.
- `__init__.py`는 폴더를 패키지로 만들고, 패키지가 불러올 때 처음 실행됩니다. 내용을 비워 두거나 버전·공개 이름 정도만 둡니다.
- `__main__.py`는 `python -m 패키지명`으로 실행할 때 시작되는 파일입니다.
- `if __name__ == "__main__":`은 “이 파일을 직접 실행했을 때만” 부분을 실행하라는 뜻입니다. import되면 `__name__`은 모듈 이름이 됩니다.
- 직접 `python budget_app/service.py`처럼 패키지 안의 파일을 실행하면 상대 import가 깨집니다. 항상 패키지의 부모 폴더에서 `python -m`으로 실행합니다.
- 두 모듈이 서로를 import하면 순환 import 오류가 납니다. 의존 방향을 한쪽으로만 두면 해결됩니다(`cli → service → repository → models`).

### 따라 하기

먼저 `__name__` 동작을 봅니다. `helper.py`를 만듭니다.

```python
print("helper __name__ =", __name__)
if __name__ == "__main__":
    print("직접 실행됨")
```

```bash
python helper.py          # helper __name__ = __main__  /  직접 실행됨
python -c "import helper" # helper __name__ = helper
```

이제 패키지를 만듭니다. 폴더 구조는 다음과 같습니다.

```text
pylab/
└── budget_app/
    ├── __init__.py
    ├── __main__.py
    ├── cli.py
    ├── service.py
    └── models.py
```

```python
# budget_app/__init__.py
"""용돈 기입장 패키지."""
__version__ = "0.1.0"
```

```python
# budget_app/models.py
from dataclasses import dataclass

@dataclass
class Transaction:
    id: str
    amount: int
```

```python
# budget_app/service.py
from .models import Transaction

def make(n: int, amount: int) -> Transaction:
    return Transaction(f"TX-{n:06d}", amount)
```

```python
# budget_app/cli.py
import sys
from . import __version__
from .service import make

def main(argv=None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if args[:1] == ["--version"]:
        print(__version__)
        return 0
    print(make(1, 5000))
    return 0
```

```python
# budget_app/__main__.py
import sys
from .cli import main

if __name__ == "__main__":
    sys.exit(main())
```

`pylab` 폴더에서 실행합니다.

```bash
python -m budget_app             # Transaction(id='TX-000001', amount=5000)
python -m budget_app --version   # 0.1.0
python budget_app/service.py     # ImportError: attempted relative import with no known parent package
```

마지막 명령이 실패하는 것이 정상입니다. 파이썬이 이 파일을 패키지의 일부가 아니라 독립 스크립트로 실행하기 때문에 `.models`가 어느 패키지의 것인지 모릅니다. `python -m budget_app.cli`와 같이 `-m`을 쓰면 패키지 문맥이 살아있습니다.

또 하나 함정인 순환 import를 일부러 만들어 봅니다. `pkg/a.py`에 `from .b import fb`, `pkg/b.py`에 `from .a import fa`를 쓰고 `python -c "import pkg.a"`를 실행하면 다음 오류가 납니다.

```text
ImportError: cannot import name 'fa' from partially initialized module 'pkg.a' (most likely due to a circular import)
```

`a`가 `b`를 가져오는 도중에 `b`가 다시 `a`를 가져오려 하는데 `a`는 아직 다 만들어지지 않았기 때문입니다. `b`가 `a`를 가져오는 일을 없앤 뒤(더 기초적인 쪽이 위쪽을 모르게 하기) 정상 실행됩니다.

패키지 공개 이름을 `__init__.py`에서 정리하는 방법도 봅시다.

```python
# tools/__init__.py
from .money import format_won
__all__ = ["format_won"]          # from tools import * 에서 노출할 이름
```

```python
from tools import format_won       # 패키지 안쪽 파일 위치를 알 필요가 없다
import tools.money as m            # 아니면 하위 모듈을 바로
```

### 연습문제

1. `helper.py`를 만들어 직접 실행할 때와 import할 때의 출력이 다른지 확인하세요.
2. 본문의 `budget_app` 패키지를 직접 타이핑해 만들고 `python -m budget_app`을 실행하세요.
3. `python budget_app/service.py`로 실행해 오류를 재현하고, 왜 오류인지와 올바른 실행 방법을 한 문장씩 쓰세요.
4. `models.py`, `repository.py`, `service.py`를 각각 만들어 의존 방향이 `service → repository → models` 한 방향이 되게 하세요. 저장소는 `Transaction`을 저장하고, 서비스는 저장소를 사용합니다.
5. 일부러 순환 import를 만들어 오류 메시지를 읽고, 의존 방향을 고쳐 해결하세요.
6. (도전) `--version`뿐 아니라 `--help`도 처리하고, 모르는 명령이 들어오면 종료 코드 2를 돌려주는 `main`을 만드세요(argparse는 쓰지 마세요. 15장에서 argparse로 교체합니다).

힌트: 3번은 `python -m budget_app.service`, 6번은 `main`이 `int`를 돌려주고 `__main__.py`가 `sys.exit`로 넘깁니다.

### 정답과 해설

```python
# 3  독립 스크립트로 실행되어 상대 import가 기준으로 삼을 패키지를 모른다.
#    올바른 방법: pylab 폴더에서  python -m budget_app.service

# 4  repository.py
from .models import Transaction

class TransactionRepository:
    def __init__(self) -> None:
        self._items: list[Transaction] = []
    def add(self, t: Transaction) -> None:
        self._items.append(t)
    def all(self):
        yield from self._items

# service.py
from .models import Transaction
from .repository import TransactionRepository

class TransactionService:
    def __init__(self, repo: TransactionRepository) -> None:
        self.repo = repo
    def add(self, amount: int) -> Transaction:
        t = Transaction(f"TX-{len(list(self.repo.all())) + 1:06d}", amount)
        self.repo.add(t)
        return t

# 6
def main(argv=None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if not args:
        print("사용법: python -m budget_app [--version|--help]")
        return 0
    if args[0] == "--version":
        print(__version__)
        return 0
    if args[0] == "--help":
        print("명령: --version, --help")
        return 0
    print(f"오류: 알 수 없는 명령 '{args[0]}'", file=sys.stderr)
    print("힌트: --help로 사용법을 확인하세요.", file=sys.stderr)
    return 2
```

- 4번에서 `models.py`는 아무 모듈도 import하지 않습니다. 가장 아래에 있는 모듈은 위를 모른다는 원칙입니다.
- 4번의 `len(list(self.repo.all()))`는 비효율적이고 임시방편입니다. 실제로는 저장소가 `next_id()`를 제공하는 쪽이 낫습니다(9장, 18장).
- 6번의 종료 코드 2는 인자 오류에 관한 관례적인 값이며 argparse도 잘못된 명령에 같은 2를 씁니다.

### 미션 연결

요구사항의 “모듈 3개 이상”, “`python -m budget_app <command>`”이 이 장입니다. README에 실행 방법을 쓸 때 반드시 패키지 부모 폴더에서 실행한다는 조건을 적으세요.

## 11장. 이터레이터와 제너레이터

제너레이터는 값을 한 번에 다 만들어 두지 않고, 달라고 할 때마다 하나씩 만들어 주는 함수입니다. 미션은 파일을 읽을 때 제너레이터로 스트리밍하라고 요구하고, 평가에서 “왜 제너레이터를 쏨느냐”를 물을 가능성이 높습니다. 어려운 문법처럼 보이지만 핵심은 한 줄입니다. `return` 대신 `yield`.

### 핵심 개념

- 반복 가능(iterable)한 값은 `for`에 넣을 수 있는 값(리스트, 파일, `range`)이고, 이터레이터는 `next()`를 부를 때마다 다음 값을 주는 객체입니다. 다 떨어지면 `StopIteration`이 나고, `for`문이 알아서 처리합니다.
- 함수 안에 `yield`가 하나라도 있으면 그 함수는 제너레이터 함수가 됩니다. 호출해도 본문이 실행되지 않고 제너레이터 객체만 돌려줍니다. `next()`를 부를 때마다 다음 `yield`까지 실행하고 멈춥니다.
- 장점: 메모리를 거의 쓰지 않습니다(한 번에 하나만 존재). 앞부분만 필요할 때 나머지를 읽지 않아 빠릅니다. 무한 수열도 표현합니다.
- 단점: 한 번 쓰면 끝입니다(재사용 불가). `len()`이나 인덱스 접근이 안 됩니다. 두 번 필요하면 함수를 다시 호출해 새 제너레이터를 만듭니다.
- 제너레이터 표현식 `(x for x in ...)`은 리스트 컴프리헨션의 대괄호를 소괄호로 바꾼 것입니다.
- `yield from 묶음`은 묶음의 값을 그대로 이어서 내보냅니다. `itertools.islice`, `heapq.nlargest` 같은 표준 도구가 제너레이터와 잘 맞습니다.

### 따라 하기

먼저 “실행이 멈추고 다시 이어진다”는 감각을 익힙니다. `print`로 실행 시점을 표시해 두었습니다.

```python
def count_up(n):
    print("시작")
    for i in range(1, n + 1):
        print(f"  yield {i}")
        yield i
    print("끝")

g = count_up(2)
print(type(g).__name__)     # generator   (아직 "시작"이 찍히지 않았다!)
print(next(g))              # 시작 / yield 1 / 1
print(next(g))              # yield 2 / 2
try:
    next(g)                 # 끝 출력 후 StopIteration
except StopIteration:
    print("StopIteration")
```

`count_up(2)`를 부른 시점에는 아무것도 출력되지 않고, `next`를 처음 부를 때 비로소 본문이 시작됩니다. 이것이 지연 평가(lazy evaluation)입니다.

```python
# 한 번밖에 못 쓴다
g2 = (n * n for n in range(5))
print(sum(g2), sum(g2))        # 30 0   ← 두 번째는 이미 다 써서 0
lst = [n * n for n in range(5)]
print(sum(lst), sum(lst))      # 30 30

# 기본 값 함수들
it = iter([10, 20])
print(next(it), next(it), next(it, "끝"))   # 10 20 끝
```

이제 미션과 같은 파이프라인을 만듭니다. 파일 읽기, 필터, 합계가 한 줄씩 흘러갑니다.

```python
import heapq, itertools, json
from pathlib import Path

def read_jsonl(path):
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                yield json.loads(line)

def only(rows, type_):
    return (r for r in rows if r["type"] == type_)

def amounts(rows):
    return (r["amount"] for r in rows)

# 시험용 파일: 거래 7건 (홀수번은 expense, 짝수번은 income)
f = Path("tx.jsonl")
with open(f, "w", encoding="utf-8") as fh:
    for i in range(1, 8):
        row = {"id": f"TX-{i:06d}", "date": f"2026-10-{i:02d}",
               "type": "expense" if i % 2 else "income", "amount": i * 1000}
        fh.write(json.dumps(row) + "\n")

print(sum(amounts(only(read_jsonl(f), "expense"))))      # 16000
print([r["id"] for r in itertools.islice(read_jsonl(f), 3)])   # ['TX-000001', 'TX-000002', 'TX-000003']
print(next(read_jsonl(f), None)["id"])                   # TX-000001  (첫 건만 읽고 멈춤)
print([r["id"] for r in heapq.nlargest(3, read_jsonl(f), key=lambda r: (r["date"], r["id"]))])
# ['TX-000007', 'TX-000006', 'TX-000005']   최신 3건
```

마지막 줄이 미션의 “최신순 N건” 설계입니다. `sorted`는 전부를 메모리에 올려야 하지만 `heapq.nlargest(N, ...)`은 제너레이터를 한 번 훑으면서 상위 N개만 기억합니다. 파일이 아무리 커도 메모리는 N개 분량입니다.

```python
# 배치로 나눠 연산, yield from, 무한 제너레이터
def chunks(it, size):
    it = iter(it)
    while batch := list(itertools.islice(it, size)):
        yield batch
print(list(chunks(range(7), 3)))          # [[0, 1, 2], [3, 4, 5], [6]]

def chain_all(*its):
    for it in its:
        yield from it
print(list(chain_all([1, 2], (3,), range(4, 6))))    # [1, 2, 3, 4, 5]

def fib():
    a, b = 0, 1
    while True:            # 무한 루프여도 괜찮다: 달라고 할 때만 만든다
        yield a
        a, b = b, a + b
print(list(itertools.islice(fib(), 8)))   # [0, 1, 1, 2, 3, 5, 8, 13]
```

메모리 차이를 직접 재봅시다. 모든 숫자를 리스트로 만들면 수 MB, 제너레이터는 거의 0입니다. 정확한 숫자는 환경마다 다릅니다.

```python
import tracemalloc

def peak_kb(fn):
    tracemalloc.start()
    fn()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak // 1000

print(peak_kb(lambda: sum([i for i in range(200_000)])))   # 수백~수천 KB (예: 8015)
print(peak_kb(lambda: sum(i for i in range(200_000))))     # 거의 0
```

발표를 준비할 때 이 실험을 그대로 보여 주면 “제너레이터가 실제로 메모리를 아낀다”를 숫자로 설명할 수 있습니다.

### 연습문제

1. `countdown(n)` 제너레이터를 만들어 `list(countdown(3))`이 `[3, 2, 1]`이 되게 하세요.
2. `g = (n for n in range(3))`에 `list(g)`를 두 번 연달아 호출하면 결과가 어떻게 나올지 예상하고 확인하세요. 왜 그런지도 설명하세요.
3. 본문의 `read_jsonl`, `only`, `amounts`로 수입(`income`)의 합계를 구하세요.
4. `islice`로 앞 2건만 읽고, 파일이 비어 있을 때는 `None`을 돌려주는 “첫 거래 읽기”를 `next`로 만드세요.
5. `heapq.nlargest`로 금액이 가장 큰 거래 2건의 id를 구하세요. 파일을 전부 리스트로 만들지 마세요.
6. 아무 거래나 읽어 학습할 때 쓸 수 있게 `chunks(rows, 3)`으로 거래를 3개씩 묶어 각 묶음의 금액 합계를 출력하세요.
7. (도전) 다음 숫자를 이어서 주는 무한 제너레이터 `id_stream(start)`를 만들어 `TX-000008`, `TX-000009`, ...를 얻으세요. 그 다음 “이 방식이 거래 id 만들기에 적합한가”를 생각해 보세요.

힌트: 1번은 `for i in range(n, 0, -1): yield i`, 4번은 `next(read_jsonl(f), None)`, 6번은 `chunks`의 결과가 리스트인 점을 이용합니다.

### 정답과 해설

```python
# 1
def countdown(n):
    for i in range(n, 0, -1):
        yield i
print(list(countdown(3)))          # [3, 2, 1]

# 2  [0, 1, 2] 다음에 []
#    제너레이터는 한 번 소비하면 끝이라 두 번째 list(g)는 빈 리스트를 돌려준다.

# 3
print(sum(amounts(only(read_jsonl(f), "income"))))     # 12000  (2000 + 4000 + 6000)

# 4
first = next(read_jsonl(f), None)

# 5
top = heapq.nlargest(2, read_jsonl(f), key=lambda r: r["amount"])
print([r["id"] for r in top])      # ['TX-000007', 'TX-000006']

# 6
for batch in chunks(read_jsonl(f), 3):
    print(sum(r["amount"] for r in batch))      # 6000, 15000, 7000

# 7
def id_stream(start):
    n = start
    while True:
        yield f"TX-{n:06d}"
        n += 1
gen = id_stream(8)
print(next(gen), next(gen))        # TX-000008 TX-000009
```

- 2번은 제너레이터의 가장 흐한 함정입니다. 예를 들어 `rows = read_jsonl(f)` 한 번으로 합계를 구하고 같은 `rows`로 개수를 세면 0이 나옵니다. 두 번 필요하면 `read_jsonl(f)`를 두 번 호출합니다.
- 4번에서 `next(..., None)`을 쓰지 않으면 빈 파일에서 `StopIteration`이 나옵니다.
- 6번의 합계는 (1000+2000+3000)=6000, (4000+5000+6000)=15000, 7000입니다.
- 7번은 기술적으로는 동작하지만 프로그램을 다시 실행하면 상태가 사라집니다. 거래 id는 저장된 최댓값을 기준으로 만드는 쪽이 안전합니다(18장).

### 미션 연결

“목록 조회·검색을 제너레이터로 스트리밍하라”, “최신순을 모든 데이터를 올리지 않고 어떻게 할 것인가”, “왜 제너레이터는 한 번만 쓸 수 있는가”라는 평가 질문의 답이 이 장에 있습니다.

## 12장. 데코레이터

데코레이터는 함수를 감싼 새 함수를 돌려주는 함수입니다. 원래 함수의 코드를 고치지 않고 “실행 시간 측정”, “로그 출력”, “오류 처리” 같은 공통 기능을 덧붙일 때 씁니다. 시작은 어렵지만 5장에서 배운 “함수는 값”이라는 사실만 받아들이면 생각보다 쉽습니다.

### 핵심 개념

- `@deco`를 함수 위에 쓰는 것은 `f = deco(f)`와 정확히 같은 뜻입니다. 문법적 설탕일 뿐입니다.
- 데코레이터 안에는 보통 `wrapper`라는 함수가 있고, 원래 함수 `fn`을 기억합니다(클로저). 인자 종류에 상관없이 감싸려면 `*args, **kwargs`로 받아 그대로 넘깁니다.
- `@functools.wraps(fn)`을 빼먹으면 함수의 이름과 설명이 `wrapper`로 바뀝니다. 디버깅과 문서화에 피해가 있으므로 항상 넣습니다.
- 인자가 있는 데코레이터 `@retry(times=3)`는 한 겹 더 싸는 구조(데코레이터를 만드는 함수)입니다.
- 여러 개를 쌓으면 아래에 있는 것이 맨 안쪽이고, 실행은 위에 있는 것부터 바깥 격으로 진입합니다.
- 제너레이터 함수에 일반 데코레이터를 붙이면 “제너레이터 객체를 만드는 순간”만 재게 됩니다(아래 실험).

### 따라 하기

단계를 나눠 봅니다. 우선 `@` 문법 없이 데코레이터의 정체를 봅니다.

```python
def shout(fn):
    def wrapper(*args, **kwargs):
        print("before")
        result = fn(*args, **kwargs)
        print("after")
        return result
    return wrapper

@shout                      # hello = shout(hello) 와 같다
def hello(name):
    """인사한다."""
    return f"hi {name}"

print(hello("a"))           # before / after / hi a
print(hello.__name__, hello.__doc__)    # wrapper None   ← 이름과 설명이 사라졌다
```

`@functools.wraps`를 넣어 고칩니다. 실제로 쓰는 실전 데코레이터 세 개입니다.

```python
import functools, sys, time

def timed(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:                            # 오류가 나도 시간은 찍는다
            ms = (time.perf_counter() - start) * 1000
            print(f"[timed] {fn.__name__} {ms:.1f}ms", file=sys.stderr)
    return wrapper

def logged(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"[log] {fn.__name__} args={args} kwargs={kwargs}")
        return fn(*args, **kwargs)
    return wrapper

def handle_errors(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs) -> int:
        try:
            return fn(*args, **kwargs)
        except BudgetError as e:            # 7장의 BudgetError
            print(f"오류: {e.cause}", file=sys.stderr)
            if e.hint:
                print(f"힌트: {e.hint}", file=sys.stderr)
            return e.exit_code
    return wrapper
```

`handle_errors`는 7장에서 만든 `BudgetError`를 그대로 사용합니다. 같은 파일에 클래스 정의를 함께 두고 실행해 보세요.

```python
@handle_errors
@logged
def cmd_delete(tx_id):
    raise BudgetError(f"{tx_id} 없음", "list로 확인")

print(cmd_delete("TX-9"))
# [log] cmd_delete args=('TX-9',) kwargs={}
# 오류: TX-9 없음            (stderr)
# 힌트: list로 확인             (stderr)
# 1                          (종료 코드)
```

모든 명령 함수에 `@handle_errors` 한 줄만 붙이면 오류 출력 형식이 한 곳에서 관리됩니다. 미션이 데코레이터를 요구하는 이유가 이것입니다.

```python
# 인자가 있는 데코레이터: 한 겹 더
def retry(times=3, exceptions=(Exception,)):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*a, **kw):
            last = None
            for i in range(1, times + 1):
                try:
                    return fn(*a, **kw)
                except exceptions as e:
                    last = e
                    print(f"시도 {i} 실패: {e}")
            raise last
        return wrapper
    return deco

calls = {"n": 0}
@retry(times=3, exceptions=(ValueError,))
def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise ValueError("일시 오류")
    return "ok"
print(flaky())     # 시도 1 실패 / 시도 2 실패 / ok
```

`@retry(times=3, ...)`는 먼저 `retry(times=3, ...)`를 호출해 `deco`를 얻고, 그 `deco`가 다시 `flaky`를 감쌉니다. 괄호가 있으면 한 겹 더 있다고 기억하세요.

```python
# 쌓는 순서
def order(tag):
    def deco(fn):
        @functools.wraps(fn)
        def w(*a, **k):
            print("enter", tag)
            r = fn(*a, **k)
            print("exit", tag)
            return r
        return w
    return deco

@order("A")
@order("B")
def f():
    print("body")
f()     # enter A / enter B / body / exit B / exit A

# 등록 데코레이터: 함수를 감싸지 않고 목록에 등록만 한다
COMMANDS = {}
def command(name):
    def deco(fn):
        COMMANDS[name] = fn
        return fn
    return deco

@command("add")
def add(): return "add!"
@command("list")
def lst(): return "list!"
print(sorted(COMMANDS), COMMANDS["add"]())    # ['add', 'list'] add!
```

등록 데코레이터는 미션의 명령 디스패치(`add`, `list`, ...를 이름으로 찾아 호출)에 쏔쏔히 쓸 수 있습니다. 15장의 `set_defaults(func=...)`도 같은 목적의 다른 방법입니다.

마지막으로 제너레이터에 일반 `@timed`를 붙이면 어떤 일이 일어나는지 봅니다.

```python
@timed
def gen():
    yield 1
    time.sleep(0.02)
    yield 2

g = gen()                   # [timed] gen 0.0ms  ← 본문은 아직 실행되지 않았는데 시간이 찍혔다
print(list(g))              # [1, 2]
```

`gen()`은 제너레이터 객체를 만들어 반환하는 데는 거의 시간이 걸리지 않습니다. 실제 작업은 나중에 `list(g)`에서 일어납니다. 그래서 제너레이터에는 전용 데코레이터가 필요합니다.

```python
def timed_gen(fn):
    @functools.wraps(fn)
    def wrapper(*a, **k):
        start = time.perf_counter()
        yield from fn(*a, **k)               # wrapper 자체도 제너레이터로 만든다
        ms = (time.perf_counter() - start) * 1000
        print(f"[timed_gen] {fn.__name__} {ms:.0f}ms", file=sys.stderr)
    return wrapper
# list(gen()) 실행 시 [timed_gen] gen 20ms 남음
```

### 연습문제

1. 본문의 `shout`에 `@functools.wraps(fn)`을 넣어 `hello.__name__`이 `hello`로 나오게 하세요.
2. `time.sleep(0.01)`을 하는 함수에 `@timed`를 붙여 실행 시간이 대략 10ms로 나오는지 확인하세요.
3. `@logged`를 만들어 함수 이름과 인자를 한 줄로 출력하고, 원래 함수의 반환값은 그대로 돌려주게 하세요.
4. 함수가 호출된 횟수를 세는 `@count_calls`를 만들고, `f.calls`로 횟수를 읽게 하세요. 힌트: 함수도 객체라 속성을 붙일 수 있습니다.
5. `@order("A")` 아래에 `@order("B")`를 쌓았을 때의 출력 순서를 먼저 예상하고 실행해 확인하세요. 그 다음 순서를 바꿔 보세요.
6. 인자를 받는 `@retry(times)`를 직접 만들어, 세 번째 시도에서 성공하는 함수로 시험하세요.
7. (도전) `@command("add")`로 등록한 함수들의 이름으로 디스패치하는 `run(name)`을 만들어, 모르는 이름이면 `BudgetError`(원인+힌트)를 발생시키세요.

힌트: 4번은 `wrapper.calls += 1`, 6번은 바깥 함수→중간 함수→래퍼의 3단 구조, 7번은 `COMMANDS.get(name)`이 `None`인지 봅니다.

### 정답과 해설

```python
# 1
def shout(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print("before")
        result = fn(*args, **kwargs)
        print("after")
        return result
    return wrapper

# 2  본문의 timed 사용. 출력 예: [timed] slow 10.1ms

# 3  본문의 logged

# 4
def count_calls(fn):
    @functools.wraps(fn)
    def wrapper(*a, **k):
        wrapper.calls += 1
        return fn(*a, **k)
    wrapper.calls = 0
    return wrapper

@count_calls
def f(): pass
f(); f()
print(f.calls)                 # 2

# 5  enter A, enter B, body, exit B, exit A  (순서를 바꾸면 A와 B가 뒤바뀝)

# 6  본문의 retry

# 7
def run(name):
    fn = COMMANDS.get(name)
    if fn is None:
        raise BudgetError(f"알 수 없는 명령 '{name}'", f"사용 가능: {', '.join(sorted(COMMANDS))}")
    return fn()
```

- 1번의 `wraps`는 `__name__`, `__doc__`뿐 아니라 `__wrapped__`로 원본 함수를 가리키는 연결도 남깁니다. 데코레이터를 거치지 않고 원본을 호출하고 싶을 때(테스트) `f.__wrapped__(...)`를 씁니다.
- 4번에서 속성을 함수에 붙이는 것은 간단하지만 용도가 크면 클래스로 만드는 편이 좋습니다.
- 5번에서 바깥 데코레이터가 먼저 실행되는 이유는 바깥 것이 안쪽 것을 감싼 함수를 호출하기 때문입니다. `@handle_errors`를 맨 위에 두어야 아래 데코레이터의 예외까지 잡습니다.

### 미션 연결

데코레이터 1개 이상이 필수 요구사항입니다. 가장 안전한 선택은 `@handle_errors`(오류 처리)이고, 여유가 있으면 `@timed`를 더해 스트리밍 읽기의 성능을 재는 데 쓰세요.

## 13장. 타입 힌트

타입 힌트는 함수의 입력과 출력이 무엇인지 적어 두는 주석입니다. 파이썬은 실행할 때 이것을 강제하지 않습니다. 대신 사람이 읽을 때, 그리고 편집기와 `mypy` 같은 도구가 미리 실수를 찾을 때 도움이 됩니다. 미션이 “타입 힌트의 이점을 설명하라”고 하므로 이점을 직접 실험으로 보여 주는 것이 좋습니다.

### 핵심 개념

- 함수: `def f(a: int, b: str = "x") -> bool:`. 변수: `x: int = 3`.
- `list[int]`, `dict[str, int]`, `tuple[int, str]`, `set[str]`처럼 안에 들어 가는 타입을 대괄호로 적습니다(3.9 이상).
- `int | None`은 “정수이거나 없음”(3.10 이상, 예전의 `Optional[int]`). `None`을 돌려줄 수 있는 함수를 부르는 쪽은 반드시 `None` 검사를 해야 합니다.
- `Iterable[int]`은 “for로 돌릴 수 있는 것”, `Iterator[str]`는 “`next`로 하나씩 꺼내는 것”입니다. 제너레이터 함수의 반환 타입은 `Iterator[타입]`으로 씁니다.
- `Callable[[int], int]`은 “정수 하나를 받아 정수를 돌려주는 함수”입니다.
- `Literal["income", "expense"]`는 정해진 값 중 하나만 허용합니다. `TypedDict`는 키마다 값의 타입이 정해진 딕셔너리입니다. `Protocol`은 “이 메서드들만 있으면 되는 인터페이스”입니다.
- 타입 힌트는 실행을 막지 않습니다. `add("1", 2)`는 타입 힌트가 있어도 실행 시점에 나야 오류가 납니다. 정적 검사는 `mypy`가 따로 합니다.

### 따라 하기

```python
from __future__ import annotations
import functools
from collections.abc import Callable, Iterable, Iterator
from dataclasses import dataclass, field
from typing import Literal, TypedDict, TypeVar, ParamSpec, Protocol

TxType = Literal["income", "expense"]

def add(a: int, b: int) -> int:
    return a + b

def usage_rate(used: int, budget: int) -> float | None:
    if budget <= 0:
        return None
    return used / budget * 100

def total(amounts: Iterable[int]) -> int:          # list도 제너레이터도 받을 수 있다
    return sum(amounts)

def read_lines(path: str) -> Iterator[str]:        # yield하는 함수의 반환 타입
    with open(path, encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")

class TxDict(TypedDict):
    id: str
    amount: int
    memo: str

@dataclass
class Transaction:
    id: str
    type: TxType
    amount: int
    tags: list[str] = field(default_factory=list)

def apply(fn: Callable[[int], int], x: int) -> int:
    return fn(x)

T = TypeVar("T")
def first(items: list[T]) -> T | None:             # 제네릭: 들어간 타입이 그대로 나온다
    return items[0] if items else None

P = ParamSpec("P")
R = TypeVar("R")
def timed(fn: Callable[P, R]) -> Callable[P, R]:   # 데코레이터 타입: 원래 함수 시그니처를 유지
    @functools.wraps(fn)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return fn(*args, **kwargs)
    return wrapper

class Store(Protocol):
    def save(self, tx: Transaction) -> None: ...

class MemoryStore:                                 # Store를 상속하지 않아도 이 메서드만 있으면 통과
    def __init__(self) -> None:
        self.items: list[Transaction] = []
    def save(self, tx: Transaction) -> None:
        self.items.append(tx)

def persist(store: Store, tx: Transaction) -> None:
    store.save(tx)

def show_rate(used: int, budget: int) -> str:
    rate = usage_rate(used, budget)
    if rate is None:                               # None 검사 후에야 float로 취급된다(좌힌)
        return "예산 없음"
    return f"{rate:.1f}%"
```

이 파일을 그대로 실행해도 아무 일이 없고, `mypy`로 검사하면 통과합니다.

```bash
pip install mypy
python -m mypy ch13.py     # Success: no issues found in 1 source file
```

이제 일부러 틀린 코드로 타입 힌트의 가치를 봅니다. `bad13.py`로 저장합니다.

```python
from typing import Literal

def usage_rate(used: int, budget: int) -> float | None:
    if budget <= 0:
        return None
    return used / budget * 100

def add(a: int, b: int) -> int:
    return a + b

x: str = add(1, 2)
print(add("1", 2))
rate = usage_rate(1, 2)
print(rate + 1)
t: Literal["income", "expense"] = "gift"
def f(n: int) -> str:
    return n
```

```text
bad13.py:11: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
bad13.py:12: error: Argument 1 to "add" has incompatible type "str"; expected "int"  [arg-type]
bad13.py:14: error: Unsupported operand types for + ("None" and "int")  [operator]
bad13.py:14: note: Left operand is of type "float | None"
bad13.py:15: error: Incompatible types in assignment (expression has type "Literal['gift']", variable has type "Literal['income', 'expense']")  [assignment]
bad13.py:17: error: Incompatible return value type (got "int", expected "str")  [return-value]
Found 5 errors in 1 file
```

프로그램을 실행하기도 전에 다섯 개의 문제가 잡혔습니다. 특히 14번째 줄이 핵심입니다. `usage_rate`가 `None`을 돌려줄 수 있다는 사실을 타입 힌트가 알려 주기 때문에, 호출하는 쪽에서 `None` 검사를 빼먹은 실수를 실행 전에 볼 수 있습니다. 이것이 미션이 묻는 “타입 힌트의 이점”의 가장 좋은 증거입니다.

이점을 정리하면 다섯 가지입니다.

1. 함수를 열어 보지 않고도 입력과 출력을 알 수 있습니다(문서 역할).
2. 편집기의 자동 완성이 정확해집니다.
3. `mypy`가 실행 전에 타입 실수를 잡습니다.
4. `None`을 처리하지 않은 경우 같은 논리 누락을 발견합니다.
5. 리팩토링할 때 함수 계약을 바꾸면 영향 받는 호출부가 한번에 보입니다.

### 연습문제

1. `def format_won(amount, suffix="원")`에 타입 힌트를 달아 보세요.
2. 숫자 변환이 실패하면 `None`을 돌려주는 `parse_amount(raw: str)`를 만들고, 호출하는 쪽에서 `None` 검사를 하세요. 반환 타입은 `int | None`입니다.
3. 아래 파일을 `ex13_3.py`로 저장하고 `mypy`가 잡아주는 오류를 모두 설명하세요.

```python
def total(amounts: list[int]) -> int:
    return sum(amounts)

print(total([1, "2"]))

def label(n: int) -> str:
    return n

x: int = "a"
```

4. JSONL을 읽는 함수 `read_jsonl(path)`의 반환 타입을 `Iterator[dict[str, Any]]`로 지정하고, `list[dict]`로 쓰면 왜 틀린지 설명하세요.
5. `Literal["income", "expense"]`를 써서 `type` 필드를 제한하고, `"gift"`를 넣어 `mypy`가 지적하는지 확인하세요. 그 다음 런타임에서는 막히지 않는다는 것도 확인하세요.
6. `Callable[[int], int]`을 받는 `apply_twice(fn, x)`를 만들어 타입 힌트를 달아 보세요.
7. (도전) `Protocol`로 `add`와 `all` 메서드를 가진 `Repo`를 정의하고, `MemoryRepo`와 `JsonlRepo` 두 구현을 만들어 같은 `count(repo: Repo)` 함수에 두 개 모두 넣으세요.

힌트: 4번은 제너레이터가 리스트가 아니라는 점, 6번은 `from collections.abc import Callable`입니다.

### 정답과 해설

```python
# 1
def format_won(amount: int, suffix: str = "원") -> str:
    return f"{amount:,}{suffix}"

# 2
def parse_amount(raw: str) -> int | None:
    try:
        return int(raw.replace(",", ""))
    except ValueError:
        return None

v = parse_amount("1,000")
print(v + 1 if v is not None else "숫자 아님")    # 1001

# 3  mypy 출력
#   ex13_3.py:4: error: List item 1 has incompatible type "str"; expected "int"
#   ex13_3.py:7: error: Incompatible return value type (got "int", expected "str")
#   ex13_3.py:9: error: Incompatible types in assignment (expression has type "str", variable has type "int")

# 4
from typing import Any, Iterator
import json

def read_jsonl(path: str) -> Iterator[dict[str, Any]]:
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)

# 6
from collections.abc import Callable
def apply_twice(fn: Callable[[int], int], x: int) -> int:
    return fn(fn(x))
print(apply_twice(lambda n: n * 2, 3))       # 12

# 7
from typing import Protocol

class Repo(Protocol):
    def add(self, tx: dict[str, Any]) -> None: ...
    def all(self) -> Iterator[dict[str, Any]]: ...

class MemoryRepo:
    def __init__(self) -> None:
        self._d: list[dict[str, Any]] = []
    def add(self, tx: dict[str, Any]) -> None:
        self._d.append(tx)
    def all(self) -> Iterator[dict[str, Any]]:
        yield from self._d

class JsonlRepo:
    def __init__(self, path: str) -> None:
        self.path = path
    def add(self, tx: dict[str, Any]) -> None:
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(tx, ensure_ascii=False) + "\n")
    def all(self) -> Iterator[dict[str, Any]]:
        return read_jsonl(self.path)

def count(repo: Repo) -> int:
    return sum(1 for _ in repo.all())
```

- 3번에서 `mypy`가 지적한 것은 세 가지입니다. 리스트 원소 타입, 반환 타입 불일치, 변수 할당 불일치입니다. 실행하면 때로는 정상 동작하는 줄(`label`은 호출하지 않았으므로)이 있다는 점에 주목하세요. 런타임에서는 직접 실행되기 전까지 발견하지 못하는 오류를 정적 분석이 미리 보여 주는 것입니다.
- 4번에서 `list[...]`로 쓰면 읽는 사람이 전체가 메모리에 올라온다고 오해하고, 반환값에 `len()`이나 인덱스를 써도 된다고 믿게 됩니다. 실제로는 제너레이터라서 그렇게 하면 런타임 오류가 납니다.
- 7번의 `JsonlRepo`와 `MemoryRepo`는 `Repo`를 상속받지 않았습니다. 메서드 모양만 같으면 되는 것이 구조적 타이핑(Protocol)의 장점이고, 테스트에서 가짜 저장소를 쉽게 끼울 수 있게 해 줍니다.

### 미션 연결

요구사항의 “타입 힌트 적용”과 질문 “타입 힌트의 이점”에 답하는 장입니다. 발표에서는 `bad13.py`의 실험과 14번째 줄 설명을 그대로 시연하면 설득력이 높습니다.

## 14장. 표준 라이브러리 활용

미션은 외부 패키지를 금지하고 표준 라이브러리만 쓰게 합니다. 파이썬은 "배터리 포함"이라 불릴 만큼 표준 라이브러리가 풍부하므로, 직접 짜기 전에 "이미 있는 건 아닐까"를 먼저 떠올리는 습관이 숙련의 지름길입니다. 이 장은 용돈 기입장에서 실제로 쓰는 것만 모았습니다.

### 핵심 개념

- `datetime.date`: 날짜 검증과 계산. `date.fromisoformat`은 존재하지 않는 날짜를 `ValueError`로 걸러 줍니다.
- `collections`: `Counter`(개수 세기), `defaultdict`(합계 누적), `deque`(최근 N개), `namedtuple`.
- `itertools`: 제너레이터를 다루는 도구 상자(`islice`, `chain`, `groupby`, `accumulate`, `pairwise`).
- `functools`: `lru_cache`(결과 기억), `partial`(인자 미리 채우기), `wraps`(12장).
- `re`: 정규표현식. 형식 검사와 태그 추출에 씁니다.
- `enum.Enum`: 정해진 선택지(수입/지출)를 오타 없이 다루기.

### 따라 하기

```python
from datetime import date, datetime, timedelta
import calendar

d = date.fromisoformat("2026-10-27")
print(d.year, d.month, d.weekday())        # 2026 10 1   (월요일=0, 화요일=1)
print(d + timedelta(days=5))               # 2026-11-01
print((date(2026, 12, 25) - d).days)       # 59
print(d.strftime("%Y/%m/%d"), d.isoformat()[:7])   # 2026/10/27 2026-10
print(calendar.monthrange(2026, 2)[1])     # 28  (그 달의 일수)

try:
    date.fromisoformat("2026-02-30")
except ValueError as e:
    print("ValueError:", e)                # day is out of range for month

# 한 자리 월·일도 받아 주는 파서
print(datetime.strptime("2026-1-5", "%Y-%m-%d").date().isoformat())   # 2026-01-05
```

`strptime`은 `2026-1-5`처럼 0 없이 쓴 날짜도 읽지만, `fromisoformat`은 엄격해서 `2026-01-05` 형태만 받습니다. 미션이 YYYY-MM-DD를 요구하므로, 입력은 `strptime`으로 느슨하게 읽고 저장할 때는 `isoformat()`으로 통일하는 방식이 사용자에게 친절합니다.

```python
from collections import Counter, defaultdict, deque

cats = ["food", "food", "traffic", "food", "cafe", "cafe"]
c = Counter(cats)
print(c.most_common(2), c["food"], c["none"])   # [('food', 3), ('cafe', 2)] 3 0

sums = defaultdict(int)
for cat, amt in [("food", 100), ("cafe", 50), ("food", 30)]:
    sums[cat] += amt
print(dict(sums))                          # {'food': 130, 'cafe': 50}

dq = deque(maxlen=3)                       # 가장 최근 3개만 유지
for i in range(5):
    dq.append(i)
print(list(dq))                            # [2, 3, 4]
```

```python
import itertools as it
import functools as ft

print(list(it.islice(it.count(1), 3)))     # [1, 2, 3]  무한 수열에서 앞 3개
print(list(it.accumulate([1, 2, 3, 4])))   # [1, 3, 6, 10]  누적합 (잔액 추이!)
print(list(it.pairwise([1, 2, 3])))        # [(1, 2), (2, 3)]  (3.10+)

rows = sorted([("food", 1), ("cafe", 2), ("food", 3)])
for key, group in it.groupby(rows, key=lambda r: r[0]):
    print(key, [v for _, v in group])      # cafe [2] / food [1, 3]

@ft.lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(50))                             # 12586269025 (캐시가 없으면 몇 분이 걸리는 계산)
```

`groupby`는 이미 정렬된 데이터에서 이웃한 같은 키만 묶으므로 반드시 키로 먼저 정렬해야 합니다. 정렬 없이 쓰면 같은 카테고리가 여러 번 나뉘어 나오는 것이 가장 흔한 실수입니다. 정렬이 번거로우면 `defaultdict`가 더 안전합니다.

```python
import re
from enum import Enum

m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", "2026-10-27")
print(m.groups() if m else None)           # ('2026', '10', '27')
print(re.fullmatch(r"\d{4}-\d{2}", "2026-1"))   # None (월은 2자리여야 함)
print(re.findall(r"#(\w+)", "점심 #식비 #회사"))   # ['식비', '회사']
print(re.sub(r"\s+", " ", "a   b \n c"))   # a b c

class Kind(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"

print(Kind("income"), Kind.EXPENSE.value)   # Kind.INCOME expense
print(Kind.INCOME == "income")             # True  (str을 상속했기 때문)
try:
    Kind("x")
except ValueError as e:
    print("ValueError:", e)                # 'x' is not a valid Kind
print([k.value for k in Kind])             # ['income', 'expense']  허용값 안내 메시지에 활용
```

정규표현식은 날짜 검증에 쓰지 마세요. `2026-02-30`은 모양이 맞아도 존재하지 않는 날짜이므로, 모양 검사는 `re`, 존재 검사는 `date`로 역할을 나눕니다. `Enum`을 쓰면 `"expnse"` 같은 오타가 조용히 저장되는 대신 즉시 `ValueError`가 나고, 그 목록을 힌트에 넣을 수 있습니다.

### 연습문제

1. 오늘로부터 100일 뒤 날짜와, 2026-12-25까지 남은 일수를 구하세요. (`date.today()`를 씁니다)
2. `"2026-02-29"`와 `"2028-02-29"`가 각각 유효한 날짜인지 `True/False`를 돌려주는 함수 `is_valid_date(text)`를 만드세요.
3. 월(`2026-10`)과 일수를 받아, 그 달의 모든 날짜를 `YYYY-MM-DD` 문자열로 만드는 제너레이터를 만드세요.
4. 카테고리 리스트 `["food","cafe","food","food","bus","cafe"]`에서 가장 많이 쓴 카테고리 1위와 횟수를 구하세요.
5. 거래 금액 `[5000, -1200, 3000, -800]`의 누적 잔액 리스트를 `itertools.accumulate`로 만드세요.
6. 메모 `"점심 #식비 #회사 저녁 #식비"`에서 태그를 중복 없이, 처음 나온 순서대로 뽑으세요.
7. `Enum`으로 `Kind`를 만들고, 입력 `"expnse"`가 들어오면 `허용값: income, expense`가 포함된 메시지로 에러를 내는 함수 `parse_kind(text)`를 만드세요.
8. (도전) 문자열 `"12,500원"`, `"-3,000"`, `"+7000"`, `"abc"`를 정수로 바꾸는 `parse_amount`를 정규표현식으로 만들고, 마지막은 `ValueError`가 나게 하세요.

힌트: 2번은 `try/except ValueError`, 3번은 `calendar.monthrange`와 `yield`, 6번은 `dict.fromkeys`가 순서를 보존하는 성질을 이용합니다.

### 정답과 해설

```python
from datetime import date, timedelta
import calendar, re, itertools as it
from collections import Counter
from enum import Enum

# 1
today = date.today()
print(today + timedelta(days=100), (date(2026, 12, 25) - today).days)

# 2
def is_valid_date(text: str) -> bool:
    try:
        date.fromisoformat(text)
        return True
    except ValueError:
        return False
print(is_valid_date("2026-02-29"), is_valid_date("2028-02-29"))   # False True

# 3
def days_of_month(ym: str):
    y, m = map(int, ym.split("-"))
    for d in range(1, calendar.monthrange(y, m)[1] + 1):
        yield f"{y:04d}-{m:02d}-{d:02d}"
print(list(days_of_month("2026-02"))[-1])                         # 2026-02-28

# 4
print(Counter(["food", "cafe", "food", "food", "bus", "cafe"]).most_common(1))   # [('food', 3)]

# 5
print(list(it.accumulate([5000, -1200, 3000, -800])))             # [5000, 3800, 6800, 6000]

# 6
tags = re.findall(r"#(\w+)", "점심 #식비 #회사 저녁 #식비")
print(list(dict.fromkeys(tags)))                                  # ['식비', '회사']

# 7
class Kind(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"

def parse_kind(text: str) -> Kind:
    try:
        return Kind(text)
    except ValueError:
        allowed = ", ".join(k.value for k in Kind)
        raise ValueError(f"알 수 없는 종류 '{text}' (허용값: {allowed})") from None

# 8
def parse_amount(text: str) -> int:
    m = re.fullmatch(r"([+-]?)([\d,]+)원?", text.strip())
    if not m:
        raise ValueError(f"금액 형식이 아닙니다: {text!r}")
    value = int(m.group(2).replace(",", ""))
    return -value if m.group(1) == "-" else value
for t in ["12,500원", "-3,000", "+7000"]:
    print(parse_amount(t))                                        # 12500 / -3000 / 7000
```

- 3번: 제너레이터라서 한 번에 한 날짜씩만 만들어 냅니다. `list(...)`로 감싼 것은 확인용입니다.
- 6번: `set`을 쓰면 순서가 사라집니다. `dict.fromkeys`는 중복을 지우면서 순서를 유지하는 관용구입니다.
- 7번: `from None`은 원래 예외의 긴 연쇄를 숨기고 우리 메시지만 남깁니다(7장). 사용자 화면에 스택 트레이스를 노출하지 않는 미션 요구와 맞닿아 있습니다.
- 8번: 정규식 `[\d,]+`는 `1,,2`처럼 이상한 콤마도 통과시킵니다. 엄격하게 하려면 `\d{1,3}(,\d{3})*|\d+`처럼 더 좁혀야 하는데, 이처럼 정규식은 쉽게 복잡해지므로 미션에서는 "콤마 제거 후 `int()`"를 쓰는 편이 더 낫습니다.

### 미션 연결

날짜 검증(`date`), 월별 집계(`defaultdict`), 최신 N건(`deque`/`heapq`), 수입·지출 종류 검증(`Enum`), 태그 추출(`re`)이 모두 이 장에서 나온 도구입니다. 도구를 많이 쓰는 것보다 "어디에 무엇을 쓸지 설명할 수 있는 것"이 동료 평가에서 더 중요합니다.

## 15장. 명령줄 프로그램 만들기 (argparse)

`python -m budget_app add --date ... --amount 12500`처럼 쓰는 방식을 만드는 장입니다. 명령줄 인자를 직접 파싱하면 도움말, 오류 메시지, 타입 변환을 전부 내가 만들어야 하지만, 표준 라이브러리 `argparse`는 이것을 선언만으로 해결합니다.

### 핵심 개념

- `add_argument("--date", ...)`은 옵션, `add_argument("tx_id")`처럼 `--` 없이 쓰면 위치 인자입니다.
- `type=int`처럼 타입을 주면 변환과 검사를 자동으로 합니다. 직접 만든 함수를 넣어도 됩니다.
- `choices=[...]`는 허용값 검사, `required=True`는 필수, `action="store_true"`는 스위치, `action="append"`는 반복 지정입니다.
- 서브커맨드(`add_subparsers`): `add`, `list`, `summary`처럼 명령마다 자기 옵션을 가집니다.
- `parents=[common]`으로 공통 옵션(`--data-dir`)을 모든 명령에 재사용합니다.
- `set_defaults(func=cmd_add)`로 명령과 함수를 연결하면 `if/elif` 분기가 사라집니다.
- `--from`은 파이썬 예약어라 `args.from`으로 못 쓰므로 `dest="date_from"`으로 이름을 바꿔 줍니다.

### 따라 하기

`cli15.py`로 저장합니다. 실제 작업은 하지 않고 인자가 제대로 파싱되는지만 보여 주는 뼈대입니다.

```python
import argparse
import sys
from pathlib import Path


def cmd_add(args: argparse.Namespace) -> int:
    print(f"추가: {args.date} {args.type} {args.category} {args.amount:,}원 태그={args.tag}")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    print(f"조회: month={args.month} from={args.date_from} limit={args.limit} dir={args.data_dir}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--data-dir", type=Path, default=Path("./data"),
                        help="데이터 폴더 (기본: ./data)")

    parser = argparse.ArgumentParser(prog="budget_app", description="나만의 용돈 기입장")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", parents=[common], help="거래 추가")
    p_add.add_argument("--date", required=True, help="YYYY-MM-DD")
    p_add.add_argument("--type", choices=["income", "expense"], required=True)
    p_add.add_argument("--category", required=True)
    p_add.add_argument("--amount", type=int, required=True)
    p_add.add_argument("--tag", action="append", default=[], help="여러 번 지정 가능")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", parents=[common], help="거래 조회")
    p_list.add_argument("--month", help="YYYY-MM")
    p_list.add_argument("--from", dest="date_from", help="시작일")
    p_list.add_argument("--limit", type=int, default=10)
    p_list.set_defaults(func=cmd_list)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
```

실행해 보세요.

```bash
python cli15.py add --date 2026-10-27 --type expense --category food --amount 12500 --tag lunch --tag work
# 추가: 2026-10-27 expense food 12,500원 태그=['lunch', 'work']

python cli15.py list --from 2026-10-01 --limit 3 --data-dir /tmp/x
# 조회: month=None from=2026-10-01 limit=3 dir=/tmp/x

python cli15.py add --type spend
# budget_app add: error: argument --type: invalid choice: 'spend' (choose from 'income', 'expense')

python cli15.py add --help      # 옵션 목록과 도움말이 자동으로 나옴
```

잘못된 인자를 주면 `argparse`가 스택 트레이스 없이 사용법과 원인만 출력하고 종료 코드 2로 끝냅니다. 미션의 "실패 시 0이 아닌 종료 코드"가 이 경로로도 이미 만족됩니다. 종료 코드는 실행 직후 `echo $?`(macOS/Linux), `echo $LASTEXITCODE`(PowerShell)로 확인합니다. `| tail`처럼 파이프를 붙이면 마지막 명령의 코드가 찍히니 주의하세요.

`main(argv)`가 인자를 받고 `int`를 돌려주도록 만들어 둔 이유는 테스트입니다. 터미널 없이 `main(["list", "--month", "2026-10"])`처럼 부르고 반환값을 `assert`하면 됩니다(16장).

### 연습문제

위 `cli15.py`를 복사해 `ex15.py`를 만들고 고쳐 나가세요.

1. `--help`와 잘못된 인자(영어 대신 이상한 `--type`)로 실행해 종료 코드를 확인하세요.
2. `delete` 서브커맨드를 추가하세요. 위치 인자 `tx_id`와 스위치 `--yes`를 받습니다.
3. `--amount`가 `12,500`도 받고, 0 이하면 오류가 나게 `positive_int` 타입 함수를 만드세요.
4. `summary --month`를 필수로 하고, `2026-13` 같은 존재하지 않는 달은 거부하는 `year_month` 타입 함수를 만드세요.
5. 공통 옵션 `--verbose`/`-v`를 추가해 모든 명령에서 쓸 수 있게 하세요.
6. 대화형 입력 헬퍼 `ask(prompt, parse)`를 만드세요. 변환에 실패하면 이유를 보여 주고 다시 묻습니다.
7. (도전) 인자 없이 실행하면 도움말 대신 1) 추가 2) 조회 3) 종료 메뉴가 나오도록 하세요. 작동하는 최소 버전이면 충분합니다.

힌트: 3·4번은 `type=` 함수에서 `argparse.ArgumentTypeError`를 던집니다. 6번은 `while True` + `try/except` + `return`입니다(7장 연습 7번과 같은 패턴).

### 정답과 해설

```python
import argparse
import re
from datetime import date

# 3
def positive_int(text: str) -> int:
    try:
        value = int(text.replace(",", ""))
    except ValueError:
        raise argparse.ArgumentTypeError(f"정수가 아닙니다: {text!r} (예: 12500 또는 12,500)")
    if value <= 0:
        raise argparse.ArgumentTypeError(f"0보다 커야 합니다: {value}")
    return value

# 4
def year_month(text: str) -> str:
    if not re.fullmatch(r"\d{4}-\d{2}", text):
        raise argparse.ArgumentTypeError(f"YYYY-MM 형식이어야 합니다: {text!r} (예: 2026-10)")
    try:
        date.fromisoformat(text + "-01")
    except ValueError:
        raise argparse.ArgumentTypeError(f"존재하지 않는 달입니다: {text!r}") from None
    return text

# 2, 4, 5  (build_parser 안에 추가)
common.add_argument("--verbose", "-v", action="store_true")           # 5

p_del = sub.add_parser("delete", parents=[common], help="거래 삭제")   # 2
p_del.add_argument("tx_id")
p_del.add_argument("--yes", action="store_true")
p_del.set_defaults(func=cmd_delete)

p_sum = sub.add_parser("summary", parents=[common], help="월 요약")    # 4
p_sum.add_argument("--month", type=year_month, required=True)
p_sum.set_defaults(func=cmd_summary)
# 기존 add의 --amount는 type=positive_int 로 바꾼다                       # 3

# 6
def ask(prompt, parse, *, input_fn=input):
    while True:
        raw = input_fn(prompt).strip()
        try:
            return parse(raw)
        except (ValueError, argparse.ArgumentTypeError) as e:
            print(f"  다시 입력하세요: {e}")
```

실행 결과는 다음과 같아야 합니다.

```text
$ python ex15.py summary --month 2026-13
budget_app summary: error: argument --month: 존재하지 않는 달입니다: '2026-13'      (종료 코드 2)
$ python ex15.py amt --amount 12,500
12500
```

- 6번의 `input_fn=input`은 테스트를 위한 훅입니다. 실제 실행에서는 기본값 `input`을 쓰고, 테스트에서는 `lambda p: next(it)`를 넣으면 키보드 없이 검증할 수 있습니다. 같은 입력 `abc`, `-3`, `12,500`을 순서대로 넣으면 두 번 다시 묻고 12500을 돌려줍니다.
- 4번: 모양(`re`)과 존재(`date`)를 나눠 검사하는 것이 14장의 원칙입니다.
- 7번 정답은 문서에 두지 않습니다. 도전 과제는 스스로 설계하는 것이 목적입니다. `main`에서 `argv`가 비어 있을 때만 대화형 모드로 분기하는 것이 힌트입니다.

### 미션 연결

필수 요구사항의 커맨드 10개, `--data-dir`, "원인 + 힌트" 오류, 비정상 종료 코드가 모두 이 장에서 합쳐집니다. 특히 `type=` 함수의 오류 메시지에 예시(`예: 2026-10`)를 넣는 것이 "힌트"를 내는 가장 쉽고 자연스러운 방법입니다.

## 16장. 테스트, 로깅, 디버깅

테스트는 “내 코드가 맞다”를 사람이 눈으로 확인하는 대신 프로그램에게 시키는 일입니다. 용돈 기입장은 파일을 건드리는 프로그램이라, 고치다가 다른 곳이 깨지는 일이 흔합니다. 테스트가 있으면 고칠 때마다 몇 초 만에 확인할 수 있고, 동료 평가에서 “어떻게 검증했나요?”라는 질문에도 답이 됩니다.

### 핵심 개념

- `unittest`는 표준 라이브러리 테스트 도구입니다. `TestCase`를 상속하고 `test_`로 시작하는 메서드를 만듭니다.
- 검증은 `assertEqual`, `assertIsNone`, `assertRaises`, `assertAlmostEqual`, `assertIn`으로 합니다.
- 같은 검증을 입력만 바꿔 반복할 때는 `subTest`를 씁니다. 실패한 입력이 어느 것인지 알려 줍니다.
- 파일 테스트는 `tempfile.TemporaryDirectory()`에서 합니다. 진짜 `data/`를 건드리면 안 됩니다.
- `input()` 같은 외부 입력은 `unittest.mock.patch`로 가짜 값을 넣고, `print` 출력은 `redirect_stdout`으로 잡습니다.
- `logging`은 `print`보다 한 단계 정돈된 기록 도구입니다. 수준(DEBUG, INFO, WARNING, ERROR)으로 걸러 볼 수 있습니다.

### 따라 하기

`t16` 폴더를 만들고 파일 4개를 둡니다. 먼저 테스트할 대상입니다.

```python
# calc.py
def usage_rate(budget: int, used: int) -> float | None:
    if budget <= 0:
        return None
    return used / budget * 100


def parse_amount(text: str) -> int:
    cleaned = text.replace(",", "").strip()
    try:
        value = int(cleaned)
    except ValueError:
        raise ValueError(f"금액은 정수여야 합니다: {text!r} (예: 12500)") from None
    if value <= 0:
        raise ValueError(f"금액은 1 이상이어야 합니다: {value}")
    return value
```

```python
# store.py
import json
from pathlib import Path


def save(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def load(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]
```

```python
# ask.py
from calc import parse_amount


def ask_amount() -> int:
    while True:
        raw = input("금액: ")
        try:
            return parse_amount(raw)
        except ValueError as e:
            print(f"오류: {e}")
```

이제 테스트입니다.

```python
# test_all.py
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from ask import ask_amount
from calc import parse_amount, usage_rate
from store import load, save


class UsageRateTest(unittest.TestCase):
    def test_normal(self):
        self.assertAlmostEqual(usage_rate(300000, 187500), 62.5)

    def test_zero_budget_is_none(self):
        self.assertIsNone(usage_rate(0, 100))


class ParseAmountTest(unittest.TestCase):
    def test_valid(self):
        for text, want in [("12500", 12500), ("12,500", 12500), (" 7 ", 7)]:
            with self.subTest(text=text):
                self.assertEqual(parse_amount(text), want)

    def test_invalid(self):
        for text in ["abc", "", "0", "-5", "12.5"]:
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    parse_amount(text)


class StoreTest(unittest.TestCase):
    def test_roundtrip(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "tx.jsonl"
            rows = [{"id": "TX-000001", "memo": "점심"}]
            save(p, rows)
            self.assertEqual(load(p), rows)

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(load(Path(d) / "nope.jsonl"), [])


class AskTest(unittest.TestCase):
    def test_retry_then_ok(self):
        buf = io.StringIO()
        with patch("builtins.input", side_effect=["abc", "12,500"]), redirect_stdout(buf):
            self.assertEqual(ask_amount(), 12500)
        self.assertIn("오류", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
```

같은 폴더에서 실행합니다.

```bash
python -m unittest -v
```

```text
test_retry_then_ok (test_all.AskTest.test_retry_then_ok) ... ok
test_invalid (test_all.ParseAmountTest.test_invalid) ... ok
test_valid (test_all.ParseAmountTest.test_valid) ... ok
test_missing_file (test_all.StoreTest.test_missing_file) ... ok
test_roundtrip (test_all.StoreTest.test_roundtrip) ... ok
test_normal (test_all.UsageRateTest.test_normal) ... ok
test_zero_budget_is_none (test_all.UsageRateTest.test_zero_budget_is_none) ... ok

Ran 7 tests in 0.004s

OK
```

`AskTest`가 핵심입니다. `side_effect=["abc", "12,500"]`는 `input()`이 첫 번째엔 `abc`, 두 번째엔 `12,500`을 돌려주게 합니다. 사람이 키보드를 치지 않아도 “틀리게 입력하면 오류를 보여 주고 다시 묻는다”를 검증합니다.

### 오류 읽는 법

테스트가 실패하거나 프로그램이 죽으면 스택 트레이스가 나옵니다. 아래 `bug.py`로 읽는 연습을 합니다.

```python
from calc import usage_rate
rate = usage_rate(0, 100)
print(f"{rate:.1f}%")
```

```text
Traceback (most recent call last):
  File "bug.py", line 3, in <module>
    print(f"{rate:.1f}%")
            ^^^^^^^^^^
TypeError: unsupported format string passed to NoneType.__format__
```

1. 맨 아래 줄부터 읽습니다. `TypeError`이고 `NoneType`이라는 말이 핵심 단서입니다.
2. 그 위의 줄이 죽은 위치(`bug.py`의 3번째 줄)입니다.
3. `rate`가 `None`일 것이라고 추리합니다. 예산이 0이면 `usage_rate`가 `None`을 돌려주기 때문입니다.
4. 해결은 부르는 쪽에서 `None`을 처리하는 것입니다. `if rate is None: ...`

디버깅의 기본 도구는 세 가지입니다. 의심 지점에 `print(repr(값))`를 넣어 실제 값을 보는 것, `breakpoint()`로 그 줄에서 멈춰 변수를 조회하는 것(`p 변수`, `n` 다음 줄, `c` 계속, `q` 종료), 그리고 마지막으로 문제를 가장 작은 입력으로 줄여 재현하는 것입니다. 마지막이 가장 효과가 큽니다.

### 로깅

```python
import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
log = logging.getLogger("budget")
log.debug("보이지 않음")                      # INFO보다 낮아서 숨김
log.info("거래 %s건 로드", 3)
log.warning("깨진 줄 건너뜀: line=%d", 7)
try:
    int("x")
except ValueError:
    log.exception("변환 실패")                # ERROR + 스택 트레이스
```

```text
INFO budget: 거래 3건 로드
WARNING budget: 깨진 줄 건너뜀: line=7
ERROR budget: 변환 실패
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: 'x'
```

- 로그 메시지는 `f"..."` 대신 `"... %s", 값` 형태가 관례입니다. 해당 수준이 꺼져 있을 때 문자열 조립을 아끼기 때문입니다.
- 사용자에게 보이는 오류 문장은 `print(..., file=sys.stderr)`로, 개발자용 상세 기록은 `log`로 나눕니다. 미션은 사용자에게 스택 트레이스를 보이지 말라고 했으므로, `log.exception`은 로그 파일이나 `--verbose` 옵션일 때만 쓰는 것이 안전합니다.

### 연습문제

위 `calc.py`, `store.py`, `ask.py`, `test_all.py`를 그대로 두고 확장합니다.

1. `parse_amount("1,000,000")`이 1000000을 돌려주는지 확인하는 테스트를 추가하세요.
2. `usage_rate(100, 250)`이 250.0이 되는지, 예산 초과도 정상으로 취급하는지 테스트하세요.
3. `store.load`가 빈 줄이 섞인 파일도 읽는지 테스트하세요. 임시 파일에 `{"a": 1}\n\n{"a": 2}\n`을 직접 쓴 뒤 `[{"a": 1}, {"a": 2}]`와 비교합니다.
4. `parse_amount`가 오류 메시지에 입력값을 포함하는지(`"abc"`가 메시지 안에 있는지) `assertRaises`의 `as cm`와 `str(cm.exception)`으로 검증하세요.
5. `ask_amount`가 세 번 틀린 뒤 맞아도 동작하는지 테스트하세요. `side_effect`에 `["x", "-1", "", "500"]`을 넣고 오류 줄이 3번 출력되는지 `count`로 확인합니다.
6. 일부러 `parse_amount`의 `<= 0`을 `< 0`으로 바꿔 어떤 테스트가 실패하는지 보고 원래대로 되돌리세요. (테스트가 버그를 잡아 주는 경험입니다.)
7. `logging`으로 `store.load`가 불러온 행 수를 INFO로 기록하게 하고, 파일이 없을 때는 WARNING을 남기게 고치세요.

힌트: 3번은 `Path.write_text(..., encoding="utf-8")`, 4번은 `with self.assertRaises(ValueError) as cm:` 다음 줄에서 `cm.exception`을 씁니다, 5번은 `buf.getvalue().count("오류")`입니다.

### 정답과 해설

```python
# test_extra.py
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from ask import ask_amount
from calc import parse_amount, usage_rate
from store import load


class Extra(unittest.TestCase):
    def test_1_big_number(self):                       # 1
        self.assertEqual(parse_amount("1,000,000"), 1000000)

    def test_2_over_budget(self):                      # 2
        self.assertEqual(usage_rate(100, 250), 250.0)

    def test_3_blank_lines(self):                      # 3
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "a.jsonl"
            p.write_text('{"a": 1}\n\n{"a": 2}\n', encoding="utf-8")
            self.assertEqual(load(p), [{"a": 1}, {"a": 2}])

    def test_4_message_has_input(self):                # 4
        with self.assertRaises(ValueError) as cm:
            parse_amount("abc")
        self.assertIn("abc", str(cm.exception))

    def test_5_three_failures(self):                   # 5
        buf = io.StringIO()
        with patch("builtins.input", side_effect=["x", "-1", "", "500"]), redirect_stdout(buf):
            self.assertEqual(ask_amount(), 500)
        self.assertEqual(buf.getvalue().count("오류"), 3)


if __name__ == "__main__":
    unittest.main()
```

```python
# 7  store.py의 load만 고친 모습
import logging
log = logging.getLogger("budget")

def load(path):
    if not path.exists():
        log.warning("저장 파일이 없어 빈 목록으로 시작: %s", path)
        return []
    with path.open(encoding="utf-8") as f:
        rows = [json.loads(line) for line in f if line.strip()]
    log.info("%s에서 %d건 로드", path.name, len(rows))
    return rows
```

- 1\~5번: 테스트 이름은 `test_`로 시작해야 실행됩니다. 이름을 `check_...`로 쓰면 조용히 무시되니 주의하세요.
- 4번: `assertRaises`를 `with`로 쓰면 예외 객체를 `cm.exception`으로 받아 메시지까지 검사할 수 있습니다.
- 5번: `side_effect` 리스트의 값이 다 소진된 뒤에도 `input()`이 불리면 `StopIteration`이 나서 테스트가 실패합니다. 이것은 “프로그램이 예상보다 더 많이 물었다”는 신호입니다.
- 6번: 경계값(0)에 대한 테스트가 있어야 `<`와 `<=`의 차이가 잡힙니다. 위 `test_invalid`가 `"0"`을 포함해 두었기 때문에 실패합니다. 테스트 입력에 경계값을 꼭 넣으세요.

### 미션 연결

미션은 테스트를 필수로 요구하지는 않지만, 동료 평가에서 “검증했는가”는 늘 나오는 질문입니다. 최소 권장은 날짜·금액 검증 함수 테스트, 저장소의 임시 폴더 왕복 테스트, `main([...])`을 불러 종료 코드를 확인하는 테스트 세 묶음입니다. `main(argv)`가 `int`를 돌려주도록 만든 15장의 설계가 여기서 빛을 발합니다.

## 17장. 가상환경과 Git

미션 제목이 “Python과 Git 심화”인 만큼 Git은 평가 대상입니다. 이 장의 목표는 “내 프로젝트를 남에게 넘겨도 그대로 돌아가고, 변경 이력이 읽히는 상태”입니다. 아래 명령은 실제로 실행해 확인한 결과입니다.

### 핵심 개념

- 가상환경(`venv`)은 프로젝트마다 독립된 파이썬 패키지 공간입니다. 이 미션은 표준 라이브러리만 쓰지만, 습관으로 만들어 두면 좋습니다.
- `.gitignore`는 Git이 추적하지 말아야 할 파일(가상환경, 캐시, 내 실제 거래 데이터)을 적는 파일입니다.
- 커밋은 “하나의 의미 있는 변경” 단위입니다. 메시지만 읽어도 무슨 변경인지 알아야 합니다.
- 브랜치는 기능 하나를 따로 작업하는 갈래입니다. 작업이 끝나면 `merge`로 합칩니다.
- 두 브랜치가 같은 줄을 다르게 고치면 충돌이 나고, 사람이 직접 해결합니다. 충돌은 사고가 아니라 정상적인 상황입니다.

### 따라 하기: 가상환경

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\Activate.ps1       # Windows PowerShell
```

활성화하면 터미널 앞에 `(.venv)`가 붙습니다. 가상환경의 파이썬을 쓰고 있는지 확인하는 방법은 다음과 같습니다.

```bash
python -c "import sys; print(sys.prefix != sys.base_prefix)"   # True 이면 가상환경 안
```

끄려면 `deactivate`입니다. 폴더를 통째로 지우면 환경이 사라지므로 망가져도 부담 없이 다시 만들 수 있습니다.

### 따라 하기: 첫 커밋과 .gitignore

```bash
git init
printf '.venv/\n__pycache__/\n*.pyc\ndata/\n' > .gitignore
echo 'print("hi")' > app.py
mkdir data && echo x > data/tx.jsonl
git status --short
```

```text
?? .gitignore
?? app.py
```

`.venv/`와 `data/`가 목록에 없는 것이 포인트입니다. 무시되었기 때문입니다. 내 가계 데이터를 실수로 공개 저장소에 올리지 않으려면 `data/`를 무시하는 편이 안전합니다. 다만 예시용 샘플 데이터를 제출해야 한다면 `examples/` 같은 다른 폴더에 따로 두세요.

```bash
git add .
git commit -m "feat: 첫 커밋"
git log --oneline
```

커밋 메시지는 `종류: 요약` 형태로 씁니다. `feat`(기능), `fix`(버그), `docs`(문서), `test`, `refactor`가 널리 쓰이는 관례입니다. 요약은 “무엇을 했다”를 한 줄로 씁니다.

### 따라 하기: 브랜치와 충돌 해결

일부러 충돌을 만들어 봅니다. 이미 `main`에 커밋이 있다고 보고 진행합니다.

```bash
git switch -c feature/list                  # 새 브랜치로 이동
echo 'print("list")' >> app.py
git commit -am "feat: list 명령 추가"

git switch main                             # 다시 main으로
echo 'print("main change")' >> app.py     # 같은 위치를 다르게 수정
git commit -am "docs: 메인 수정"

git merge feature/list
```

```text
Auto-merging app.py
CONFLICT (content): Merge conflict in app.py
Automatic merge failed; fix conflicts and then commit the result.
```

`app.py`를 열면 다음과 같이 표시가 들어 있습니다.

```text
print("hi")
<<<<<<< HEAD
print("main change")
=======
print("list")
>>>>>>> feature/list
```

`<<<<<<< HEAD`와 `=======` 사이가 현재 브랜치(main)의 내용이고, `=======`와 `>>>>>>>` 사이가 합치려는 브랜치의 내용입니다. 해결은 세 단계입니다.

1. 남길 내용을 정합니다. 둘 다 필요하면 두 줄을 모두 남기고, 표시 줄 세 중(`<<<<<<<`, `=======`, `>>>>>>>`)을 지웁니다.
2. 파일을 저장하고 `git add app.py`로 “해결했다”고 알립니다.
3. `git commit`으로 병합을 마무리합니다.

충돌 중 길을 잃으면 `git status`로 현재 상태를 보고, 포기하고 처음으로 되돌리려면 `git merge --abort`를 씁니다. 이 명령은 안전합니다.

### 자주 쓰는 명령 정리

| 하고 싶은 일 | 명령 |
| --- | --- |
| 현재 상태 보기 | `git status` |
| 어떤 줄을 고쳤는지 보기 | `git diff` |
| 커밋에 담기 | `git add 파일` → `git commit -m "메시지"` |
| 이력 한 줄씩 보기 | `git log --oneline` |
| 브랜치 만들어 이동 | `git switch -c 이름` |
| 브랜치 합치기 | `git switch main` 후 `git merge 이름` |
| 최근 커밋 메시지 고치기 | `git commit --amend` (아직 push 전일 때만) |

### 연습문제

연습용 빈 폴더를 하나 만들고 진행합니다. 연습이므로 실제 프로젝트 저장소는 건드리지 마세요.

1. `python -m venv .venv`로 환경을 만들고 활성화한 뒤, 위의 한 줄 명령으로 가상환경 안인지 확인하세요.
2. `.gitignore`를 만들고 `.venv/`, `__pycache__/`, `data/`를 넣은 뒤 `git status --short`에 이것들이 나타나지 않는 것을 확인하세요.
3. `app.py` 하나로 커밋 3개를 만드세요. 각각 다른 의미의 변경이어야 하고 메시지는 `feat:`, `fix:`, `docs:` 중 알맞은 것을 붙이세요.
4. `git diff`로 커밋 전 변경 내용을 한 번 확인하는 습관을 들이세요. 일부러 오타를 하나 내고 잡아 보세요.
5. 위의 충돌 실습을 직접 재현하고, 두 줄을 모두 남기는 방식으로 해결하세요. 해결 후 `git log --oneline --graph`로 합쳐진 모양을 보세요.
6. 충돌을 한 번 더 만들고 이번에는 `git merge --abort`로 취소해 보세요. 취소 후 `git status`가 깨끗한지 확인합니다.
7. 미션 저장소를 가정하고, 세 단계(저장소·서비스·CLI)를 각각 브랜치 하나씨으로 나눠 작업하는 계획을 브랜치 이름과 커밋 메시지 예시로 써 보세요.

### 정답과 해설

```bash
# 1
python -m venv .venv
source .venv/bin/activate
python -c "import sys; print(sys.prefix != sys.base_prefix)"   # True

# 2
printf '.venv/\n__pycache__/\ndata/\n' > .gitignore
git status --short        # .gitignore 와 수정한 소스만 나온다

# 3  예시
git commit -m "feat: add_tx 함수 추가"
git commit -m "fix: 금액 0 입력 검사 추가"
git commit -m "docs: README 실행 방법 추가"

# 5  충돌 해결 후 app.py 내용
#   print("hi")
#   print("main change")
#   print("list")
git add app.py
git commit -m "merge: feature/list 병합"
git log --oneline --graph

# 6
git merge feature/list
git merge --abort
git status                 # nothing to commit, working tree clean

# 7  예시
# feature/repository  -> "feat: JSONL 저장소와 원자적 저장 추가"
# feature/service     -> "feat: 월별 요약 집계 추가"
# feature/cli         -> "feat: argparse 서브커맨드 추가"
```

- 2번: 이미 추적 중인 파일은 나중에 `.gitignore`에 적어도 계속 추적됩니다. 이때는 `git rm -r --cached data/`로 추적만 끊습니다(파일은 지워지지 않습니다).
- 5번: 충돌 표시 줄을 지우지 않고 커밋하면 표시가 그대로 소스에 남아 문법 오류가 납니다. 커밋 전에 `<<<<<<<`를 검색하는 습관을 들이세요.
- 7번: 라벨은 타인이 읽었을 때 “무엇을 했는지” 드러나면 충분합니다.

### 미션 연결

미션은 작은 개발 단위마다 커밋하는 것을 기대합니다. 동료 평가자가 `git log --oneline`만 봐도 개발 순서(모델 → 저장소 → 서비스 → CLI → README)가 보이도록 커밋하세요. 18장의 Step별 종료 시점에 커밋하는 것이 좋습니다.

## 18장. 용돈 기입장 단계별 구현

이 장은 앞에서 배운 것을 하나의 프로그램으로 합칩니다. 아래 코드는 전부 실제로 실행해 모든 명령과 오류 경로, 테스트 9개가 통과한 것입니다(Python 3.13에서 확인, 문법은 3.10 이상 기준). 복사해 붙이지 말고 한 단계씩 직접 친 뒤, 막히면 이 코드와 비교하세요. 반드시 내 설계대로 바꿔 보는 연습(19장)까지 해야 내 것이 됩니다.

### 폴더 구조와 역할

```text
pylab/
├── budget_app/
│   ├── __init__.py
│   ├── __main__.py     # python -m budget_app 진입점
│   ├── errors.py       # BudgetError 계층 (원인 + 힌트)
│   ├── models.py       # Transaction, Budget, 입력 검증 함수
│   ├── storage.py      # JSONL 읽기(제너레이터)/쓰기(원자적)
│   ├── services.py     # 업무 규칙 (추가/검색/수정/요약/CSV)
│   ├── decorators.py   # @handle_errors, @timed
│   └── cli.py          # argparse, 화면 출력
└── tests/
    ├── __init__.py
    └── test_app.py
```

의존 방향은 `cli → services → storage → models`입니다. 화살표가 가리키는 쪽은 위쪽을 알지 못합니다. 예를 들어 `storage.py`는 `print`나 `argparse`를 모르고, `models.py`는 파일을 모릅니다. 이 규칙이 “계층의 책임 분리”의 실체입니다.

저장 파일은 `data/` 아래 3개입니다: `transactions.jsonl`, `categories.jsonl`, `budgets.jsonl`.

정책 결정(설계 선택)은 다음과 같습니다. 내 설계를 달리 해도 되지만 기준을 말로 설명할 수 있어야 합니다.

| 결정 | 내용 | 이유 |
| --- | --- | --- |
| 금액 | 원 단위 정수 | float 오차 회피 (1장) |
| 날짜 | `YYYY-MM-DD` 문자열로 저장 | 문자열 비교로 정렬·기간 검색이 가능 |
| 카테고리 | 등록된 것만 사용 | 오타로 인한 집계 분산 방지 |
| 저장 | 매번 전체를 임시 파일에 쓰고 `os.replace` | 중간에 꾸어진다고 해도 원본 보존 |
| 읽기 | 한 줄씩 제너레이터 | 큰 파일도 메모리 사용량 일정 |
| 최신 N건 | `heapq.nlargest` | 전체 정렬 없이 N개만 유지 |
| CSV 가져오기 | 잘못된 행은 건너뛰고 줄 번호와 이유 보고 | 한 줄 때문에 전체가 실패하지 않게 |

### Step 1. 오류와 모델 (errors.py, models.py)

가장 아래 계층부터 만듭니다. 먼저 `pylab/budget_app/` 폴더를 만들고 빈 `__init__.py`에 한 줄 docstring을 씁니다.

```python
# budget_app/__init__.py
"""나만의 용돈 기입장 (표준 라이브러리만 사용)."""
```

```python
# budget_app/errors.py
class BudgetError(Exception):
    """원인(cause)과 해결 힌트(hint)를 함께 가지는 앱 전용 예외."""

    def __init__(self, cause: str, hint: str = "") -> None:
        super().__init__(cause)
        self.cause = cause
        self.hint = hint

    def __str__(self) -> str:
        return f"{self.cause} (힌트: {self.hint})" if self.hint else self.cause


class ValidationError(BudgetError):
    """사용자 입력이 규칙에 맞지 않을 때."""


class NotFoundError(BudgetError):
    """찾는 거래/카테고리가 없을 때."""


class StorageError(BudgetError):
    """파일을 읽거나 쓸 수 없을 때."""
```

```python
# budget_app/models.py
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date

from .errors import ValidationError

TYPES = ("income", "expense")


def parse_date(text: str) -> str:
    """'2026-1-5' 같은 입력도 받아 'YYYY-MM-DD'로 통일한다."""
    try:
        y, m, d = (int(p) for p in text.strip().split("-"))
        return date(y, m, d).isoformat()
    except (ValueError, TypeError):
        raise ValidationError(
            f"날짜 형식이 올바르지 않습니다: {text!r}",
            "YYYY-MM-DD 형식의 실제 존재하는 날짜를 입력하세요 (예: 2026-10-27)",
        ) from None


def parse_amount(text: str | int) -> int:
    try:
        value = int(str(text).replace(",", "").strip())
    except ValueError:
        raise ValidationError(
            f"금액이 정수가 아닙니다: {text!r}", "숫자만 입력하세요 (예: 12500 또는 12,500)"
        ) from None
    if value <= 0:
        raise ValidationError(f"금액은 1 이상이어야 합니다: {value}", "0보다 큰 정수를 입력하세요")
    return value


def parse_month(text: str) -> str:
    try:
        y, m = (int(p) for p in text.strip().split("-"))
        return date(y, m, 1).strftime("%Y-%m")
    except (ValueError, TypeError):
        raise ValidationError(
            f"월 형식이 올바르지 않습니다: {text!r}", "YYYY-MM 형식으로 입력하세요 (예: 2026-10)"
        ) from None


@dataclass
class Transaction:
    id: str
    date: str
    type: str
    category: str
    amount: int
    memo: str = ""
    tags: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.type not in TYPES:
            raise ValidationError(
                f"거래 종류가 올바르지 않습니다: {self.type!r}", "income 또는 expense 중 하나를 쓰세요"
            )

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, raw: dict) -> "Transaction":
        return cls(
            id=raw["id"],
            date=raw["date"],
            type=raw["type"],
            category=raw["category"],
            amount=int(raw["amount"]),
            memo=raw.get("memo", ""),
            tags=list(raw.get("tags", [])),
        )

    @property
    def signed_amount(self) -> int:
        return self.amount if self.type == "income" else -self.amount


@dataclass(frozen=True)
class Budget:
    month: str
    category: str
    limit: int
```

`from None`은 원래 `ValueError`의 긴 에러 연결 기록을 숨기고 우리 메시지만 남깁니다. `signed_amount`는 `@property`라 괄호 없이 `tx.signed_amount`로 씁니다.

확인(폴더 `pylab`에서 실행):

```python
from budget_app.models import Transaction, parse_date, parse_amount
from budget_app.errors import BudgetError
tx = Transaction("TX-000001", parse_date("2026-1-5"), "expense", "식비", parse_amount("12,500"), "점심", ["학교"])
print(tx)
print(tx.to_dict())
try:
    parse_date("2026-02-30")
except BudgetError as e:
    print(e)
```

```text
Transaction(id='TX-000001', date='2026-01-05', type='expense', category='식비', amount=12500, memo='점심', tags=['학교'])
{'id': 'TX-000001', 'date': '2026-01-05', 'type': 'expense', 'category': '식비', 'amount': 12500, 'memo': '점심', 'tags': ['학교']}
날짜 형식이 올바르지 않습니다: '2026-02-30' (힌트: YYYY-MM-DD 형식의 실제 존재하는 날짜를 입력하세요 (예: 2026-10-27))
```

커밋할 시점입니다. `git commit -m "feat: 오류 계층과 거래 모델 추가"`

### Step 2. 저장소 (storage.py)

파일을 읽고 쓰는 일만 합니다. 핵심 포인트는 세 가지입니다. `read_jsonl`은 제너레이터(한 줄씩), `atomic_write`는 컨텍스트 매니저(임시 파일 → 교체), `Storage`는 3개 파일을 묶는 클래스입니다.

```python
# budget_app/storage.py
from __future__ import annotations

import json
import os
import tempfile
from collections.abc import Iterable, Iterator
from contextlib import contextmanager
from pathlib import Path

from .errors import StorageError
from .models import Budget, Transaction


@contextmanager
def atomic_write(path: Path) -> Iterator:
    """임시 파일에 먼저 쓰고, 성공하면 os.replace로 한 번에 교체한다."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            yield f
        os.replace(tmp_name, path)
    except BaseException:
        Path(tmp_name).unlink(missing_ok=True)
        raise


def read_jsonl(path: Path) -> Iterator[dict]:
    """한 줄씩 읽어 dict를 내보내는 제너레이터. 파일이 없으면 아무것도 내보내지 않는다."""
    if not path.exists():
        return
    with path.open(encoding="utf-8") as f:
        for no, line in enumerate(f, start=1):
            if not line.strip():
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                raise StorageError(
                    f"{path.name} {no}번째 줄을 읽을 수 없습니다",
                    "그 줄의 JSON 형식을 고치거나 줄을 삭제하세요",
                ) from None


def write_jsonl(path: Path, rows: Iterable[dict]) -> None:
    try:
        with atomic_write(path) as f:
            for row in rows:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
    except OSError as e:
        raise StorageError(f"{path} 에 저장할 수 없습니다: {e.strerror}", "경로와 쓰기 권한을 확인하세요") from None


class Storage:
    """data_dir 아래 3개 파일(transactions/categories/budgets .jsonl)을 다룬다."""

    def __init__(self, data_dir: Path) -> None:
        self.data_dir = Path(data_dir)
        self.tx_path = self.data_dir / "transactions.jsonl"
        self.cat_path = self.data_dir / "categories.jsonl"
        self.budget_path = self.data_dir / "budgets.jsonl"

    # 거래
    def iter_transactions(self) -> Iterator[Transaction]:
        for raw in read_jsonl(self.tx_path):
            yield Transaction.from_dict(raw)

    def save_transactions(self, txs: Iterable[Transaction]) -> None:
        write_jsonl(self.tx_path, (t.to_dict() for t in txs))

    def next_id(self) -> str:
        biggest = 0
        for tx in self.iter_transactions():
            biggest = max(biggest, int(tx.id.split("-")[1]))
        return f"TX-{biggest + 1:06d}"

    # 카테고리
    def load_categories(self) -> list[str]:
        return [r["name"] for r in read_jsonl(self.cat_path)]

    def save_categories(self, names: Iterable[str]) -> None:
        write_jsonl(self.cat_path, ({"name": n} for n in sorted(set(names))))

    # 예산
    def load_budgets(self) -> list[Budget]:
        return [Budget(r["month"], r["category"], int(r["limit"])) for r in read_jsonl(self.budget_path)]

    def save_budgets(self, budgets: Iterable[Budget]) -> None:
        write_jsonl(
            self.budget_path,
            ({"month": b.month, "category": b.category, "limit": b.limit} for b in budgets),
        )
```

시선이 머물러야 할 곳이 두 군데 있습니다. 첫째, `iter_transactions`는 `yield`를 쓰는 제너레이터 함수입니다. 호출해도 파일을 읽지 않고, 마지막 `for`가 돌아갈 때만 한 줄씩 읽힙니다. 둘째, `save_transactions`가 리스트 대신 제너레이터를 받아도 되는 이유는 “읽으면서 바로 쓴다”는 구조가 가능해서입니다. 임시 파일에 쓰는 동안 원본은 그대로 있고, 끝난 뒤에만 교체되기 때문에 안전합니다.

확인:

```python
import tempfile
from pathlib import Path
from budget_app.storage import Storage
from budget_app.models import Transaction
with tempfile.TemporaryDirectory() as d:
    st = Storage(Path(d))
    print(st.next_id())                     # 파일이 없으면 1번부터
    st.save_transactions([Transaction("TX-000001", "2026-10-01", "expense", "식비", 1000)])
    print(st.next_id())
    gen = st.iter_transactions()
    print(type(gen).__name__)               # generator
    print(next(gen))
    print(sorted(p.name for p in Path(d).iterdir()))   # 임시 파일이 남지 않는다
```

```text
TX-000001
TX-000002
generator
Transaction(id='TX-000001', date='2026-10-01', type='expense', category='식비', amount=1000, memo='', tags=[])
['transactions.jsonl']
```

커밋: `git commit -m "feat: JSONL 저장소와 원자적 저장 추가"`

### Step 3. 서비스 계층 (services.py)

업무 규칙이 모여 있는 파일입니다. “등록되지 않은 카테고리는 거부한다”, “사용 중인 카테고리는 삭제할 수 없다”, “월 합계는 이렇게 계산한다” 같은 규칙입니다. 화면 출력(`print`)이 하나도 없는 것이 포인트입니다.

```python
# budget_app/services.py
from __future__ import annotations

import csv
import heapq
from collections import defaultdict
from collections.abc import Iterator
from dataclasses import dataclass, field
from itertools import chain
from pathlib import Path

from .errors import NotFoundError, ValidationError
from .models import (
    Budget,
    Transaction,
    parse_amount,
    parse_date,
    parse_month,
)
from .storage import Storage

CSV_COLUMNS = ["date", "type", "category", "amount", "memo", "tags"]


@dataclass
class MonthSummary:
    month: str
    income: int = 0
    expense: int = 0
    by_category: dict[str, int] = field(default_factory=dict)
    budgets: dict[str, int] = field(default_factory=dict)

    @property
    def balance(self) -> int:
        return self.income - self.expense

    def usage_rate(self, category: str) -> float | None:
        limit = self.budgets.get(category)
        if not limit:
            return None
        return self.by_category.get(category, 0) / limit * 100


@dataclass
class ImportResult:
    imported: int = 0
    skipped: list[tuple[int, str]] = field(default_factory=list)


def split_tags(text: str) -> list[str]:
    return [t.strip() for t in text.replace(";", ",").split(",") if t.strip()]


class BudgetService:
    def __init__(self, storage: Storage) -> None:
        self.storage = storage

    # ---- 카테고리 ----
    def list_categories(self) -> list[str]:
        return sorted(self.storage.load_categories())

    def add_category(self, name: str) -> None:
        name = name.strip()
        if not name:
            raise ValidationError("카테고리 이름이 비어 있습니다", "공백이 아닌 이름을 입력하세요")
        cats = self.storage.load_categories()
        if name in cats:
            raise ValidationError(f"이미 있는 카테고리입니다: {name}", "category list 로 목록을 확인하세요")
        self.storage.save_categories([*cats, name])

    def remove_category(self, name: str) -> None:
        cats = self.storage.load_categories()
        if name not in cats:
            raise NotFoundError(f"없는 카테고리입니다: {name}", "category list 로 목록을 확인하세요")
        if any(t.category == name for t in self.storage.iter_transactions()):
            raise ValidationError(
                f"'{name}' 카테고리를 쓰는 거래가 있어 삭제할 수 없습니다",
                "해당 거래의 카테고리를 먼저 update 로 바꾸거나 거래를 delete 하세요",
            )
        self.storage.save_categories(c for c in cats if c != name)

    def _require_category(self, name: str) -> None:
        if name not in self.storage.load_categories():
            raise ValidationError(
                f"등록되지 않은 카테고리입니다: {name!r}",
                f"먼저 'category add {name}' 명령으로 등록하세요",
            )

    # ---- 거래 ----
    def add(self, date: str, type_: str, category: str, amount: str | int, memo: str = "",
            tags: list[str] | None = None) -> Transaction:
        self._require_category(category)
        tx = Transaction(
            id=self.storage.next_id(),
            date=parse_date(date),
            type=type_,
            category=category,
            amount=parse_amount(amount),
            memo=memo,
            tags=tags or [],
        )
        self.storage.save_transactions(chain(self.storage.iter_transactions(), [tx]))
        return tx

    def latest(self, limit: int = 10) -> list[Transaction]:
        """전체를 메모리에 올리지 않고 최신 limit건만 유지한다."""
        return heapq.nlargest(limit, self.storage.iter_transactions(), key=lambda t: (t.date, t.id))

    def search(self, keyword: str | None = None, category: str | None = None,
               type_: str | None = None, date_from: str | None = None, date_to: str | None = None,
               min_amount: int | None = None, max_amount: int | None = None,
               tag: str | None = None) -> Iterator[Transaction]:
        d_from = parse_date(date_from) if date_from else None
        d_to = parse_date(date_to) if date_to else None
        for tx in self.storage.iter_transactions():
            if keyword and keyword not in tx.memo and keyword not in tx.category:
                continue
            if category and tx.category != category:
                continue
            if type_ and tx.type != type_:
                continue
            if d_from and tx.date < d_from:
                continue
            if d_to and tx.date > d_to:
                continue
            if min_amount is not None and tx.amount < min_amount:
                continue
            if max_amount is not None and tx.amount > max_amount:
                continue
            if tag and tag not in tx.tags:
                continue
            yield tx

    def update(self, tx_id: str, **changes) -> Transaction:
        found: list[Transaction] = []

        def rewritten() -> Iterator[Transaction]:
            for tx in self.storage.iter_transactions():
                if tx.id == tx_id:
                    tx = self._apply(tx, changes)
                    found.append(tx)
                yield tx

        self.storage.save_transactions(rewritten())
        if not found:
            raise NotFoundError(f"거래를 찾을 수 없습니다: {tx_id}", "list 또는 search 로 ID를 확인하세요")
        return found[0]

    def _apply(self, tx: Transaction, changes: dict) -> Transaction:
        values = tx.to_dict()
        for key, val in changes.items():
            if val is None:
                continue
            if key == "date":
                val = parse_date(val)
            elif key == "amount":
                val = parse_amount(val)
            elif key == "category":
                self._require_category(val)
            elif key == "tags":
                val = split_tags(val) if isinstance(val, str) else val
            values[key] = val
        return Transaction.from_dict(values)

    def delete(self, tx_id: str) -> Transaction:
        removed: list[Transaction] = []

        def kept() -> Iterator[Transaction]:
            for tx in self.storage.iter_transactions():
                if tx.id == tx_id:
                    removed.append(tx)
                else:
                    yield tx

        self.storage.save_transactions(kept())
        if not removed:
            raise NotFoundError(f"거래를 찾을 수 없습니다: {tx_id}", "list 또는 search 로 ID를 확인하세요")
        return removed[0]

    # ---- 예산·요약 ----
    def set_budget(self, month: str, category: str, limit: str | int) -> Budget:
        self._require_category(category)
        new = Budget(parse_month(month), category, parse_amount(limit))
        others = [b for b in self.storage.load_budgets() if (b.month, b.category) != (new.month, new.category)]
        self.storage.save_budgets([*others, new])
        return new

    def budgets_for(self, month: str) -> list[Budget]:
        month = parse_month(month)
        return sorted((b for b in self.storage.load_budgets() if b.month == month), key=lambda b: b.category)

    def summary(self, month: str) -> MonthSummary:
        month = parse_month(month)
        result = MonthSummary(month)
        spent: defaultdict[str, int] = defaultdict(int)
        for tx in self.storage.iter_transactions():
            if not tx.date.startswith(month):
                continue
            if tx.type == "income":
                result.income += tx.amount
            else:
                result.expense += tx.amount
                spent[tx.category] += tx.amount
        result.by_category = dict(sorted(spent.items(), key=lambda kv: kv[1], reverse=True))
        result.budgets = {b.category: b.limit for b in self.budgets_for(month)}
        return result

    # ---- CSV ----
    def export_csv(self, path: Path, month: str | None = None) -> int:
        month = parse_month(month) if month else None
        count = 0
        with Path(path).open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_COLUMNS)
            for tx in self.storage.iter_transactions():
                if month and not tx.date.startswith(month):
                    continue
                writer.writerow([tx.date, tx.type, tx.category, tx.amount, tx.memo, ";".join(tx.tags)])
                count += 1
        return count

    def import_csv(self, path: Path) -> ImportResult:
        path = Path(path)
        if not path.exists():
            raise NotFoundError(f"파일이 없습니다: {path}", "경로를 확인하세요")
        result = ImportResult()
        known = set(self.storage.load_categories())
        base = int(self.storage.next_id().split("-")[1])
        new: list[Transaction] = []
        with path.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None or [c.strip() for c in reader.fieldnames] != CSV_COLUMNS:
                raise ValidationError(
                    f"CSV 헤더가 맞지 않습니다: {reader.fieldnames}",
                    "첫 줄을 date,type,category,amount,memo,tags 로 맞추세요",
                )
            for line_no, row in enumerate(reader, start=2):
                try:
                    if row["category"] not in known:
                        raise ValidationError(f"등록되지 않은 카테고리: {row['category']!r}")
                    new.append(Transaction(
                        id=f"TX-{base + len(new):06d}",
                        date=parse_date(row["date"]),
                        type=row["type"].strip(),
                        category=row["category"],
                        amount=parse_amount(row["amount"]),
                        memo=row["memo"] or "",
                        tags=split_tags(row["tags"] or ""),
                    ))
                    result.imported += 1
                except ValidationError as e:
                    result.skipped.append((line_no, e.cause))
        if new:
            self.storage.save_transactions(chain(self.storage.iter_transactions(), new))
        return result
```

이 파일에서 배울 점을 번호로 정리합니다.

1. `latest`는 `heapq.nlargest`로 전체를 정렬하지 않고 N건만 유지합니다. 정렬 기준 `(t.date, t.id)`는 날짜가 같을 때 ID로 순서를 정하는 튜플 비교입니다.
2. `search`는 `yield`를 쓰는 제너레이터라 조건에 맞는 거래를 하나씩 내보냅니다. 호출하는 쪽이 `list(...)`로 감쌀지, `for`로 돌지 정합니다.
3. `update`/`delete` 안쪽의 `rewritten()`/`kept()`는 파일을 읽으면서 바로 내보내는 제너레이터이고, 바깥 리스트 `found`/`removed`가 “찾았는가”를 기억합니다. 파일을 다 쓴 뒤에도 비어 있으면 `NotFoundError`를 던집니다. 이 경우 파일은 내용이 똑같은 채로 다시 저장되므로 데이터가 변하지 않습니다.
4. `import_csv`는 행 단위 오류(`ValidationError`)만 잡아 건너뛰고, 헤더가 틀리거나 파일이 없는 것같은 전체 실패는 그대로 위로 올립니다. 에러를 어느 단계에서 잡는가는 설계 결정입니다.

커밋: `git commit -m "feat: 거래·카테고리·예산·요약·CSV 서비스 추가"`

### Step 4. 데코레이터와 명령줄 (decorators.py, cli.py, 진입점 `__main__.py`)

이제 사용자가 만나는 계층입니다. `@handle_errors`는 모든 명령 함수에 붙어 오류를 “원인 + 힌트” 한 줄로 바꾸고 종료 코드를 돌려줍니다. 예상하지 못한 오류는 코드 2로 구분합니다.

```python
# budget_app/decorators.py
from __future__ import annotations

import functools
import logging
import sys
import time
from collections.abc import Callable
from typing import ParamSpec, TypeVar

from .errors import BudgetError

P = ParamSpec("P")
R = TypeVar("R")
log = logging.getLogger("budget")


def handle_errors(func: Callable[P, int]) -> Callable[P, int]:
    """BudgetError를 '원인 + 힌트' 한 줄로 바꾸고 종료 코드를 돌려준다. 스택 트레이스는 숨긴다."""

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> int:
        try:
            return func(*args, **kwargs)
        except BudgetError as e:
            print(f"오류: {e}", file=sys.stderr)
            return 1
        except KeyboardInterrupt:
            print("중단했습니다.", file=sys.stderr)
            return 130
        except Exception as e:  # 예상 못 한 오류도 스택 트레이스 대신 안내만 보여 준다
            log.debug("unexpected error", exc_info=True)
            print(f"오류: 예상하지 못한 문제가 발생했습니다 ({type(e).__name__}) "
                  "(힌트: --verbose 로 다시 실행하면 자세한 기록을 볼 수 있습니다)", file=sys.stderr)
            return 2

    return wrapper


def timed(func: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            log.debug("%s 실행 시간 %.1f ms", func.__name__, (time.perf_counter() - start) * 1000)

    return wrapper
```

```python
# budget_app/__main__.py
import sys

from .cli import main

if __name__ == "__main__":
    sys.exit(main())
```

```python
# budget_app/cli.py
from __future__ import annotations

import argparse
import logging
import sys
import unicodedata
from collections.abc import Callable, Sequence
from datetime import date
from pathlib import Path

from .decorators import handle_errors, timed
from .errors import ValidationError
from .models import Transaction
from .services import BudgetService, split_tags
from .storage import Storage

COMMANDS: dict[str, Callable[[argparse.Namespace], int]] = {}


def command(name: str):
    """명령 함수를 이름으로 등록하는 데코레이터."""

    def deco(func):
        COMMANDS[name] = func
        return func

    return deco


def width(text: str) -> int:
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in text)


def pad(text: str, w: int, right: bool = False) -> str:
    gap = " " * (w - width(text))
    return gap + text if right else text + gap


def print_table(headers: list[str], rows: list[list[str]], right_cols: set[int] = frozenset()) -> None:
    widths = [max(width(str(x)) for x in col) for col in zip(headers, *rows)] if rows else [width(h) for h in headers]
    def line(cells):
        return "  ".join(pad(str(c), widths[i], i in right_cols) for i, c in enumerate(cells)).rstrip()
    print(line(headers))
    print("  ".join("-" * w for w in widths))
    for r in rows:
        print(line(r))


def tx_rows(txs: Sequence[Transaction]) -> list[list[str]]:
    return [[t.id, t.date, "수입" if t.type == "income" else "지출", t.category,
             f"{t.amount:,}", t.memo, ",".join(t.tags)] for t in txs]


TX_HEADERS = ["ID", "날짜", "구분", "카테고리", "금액", "메모", "태그"]


def make_service(args: argparse.Namespace) -> BudgetService:
    return BudgetService(Storage(Path(args.data_dir)))


@command("add")
@handle_errors
@timed
def cmd_add(args: argparse.Namespace) -> int:
    tx = make_service(args).add(args.date, args.type, args.category, args.amount,
                                args.memo, split_tags(args.tags))
    print(f"추가했습니다: {tx.id} {tx.date} {tx.category} {tx.amount:,}원")
    return 0


@command("list")
@handle_errors
@timed
def cmd_list(args: argparse.Namespace) -> int:
    txs = make_service(args).latest(args.limit)
    if not txs:
        print("거래가 없습니다. add 명령으로 첫 거래를 추가해 보세요.")
        return 0
    print_table(TX_HEADERS, tx_rows(txs), right_cols={4})
    return 0


@command("search")
@handle_errors
@timed
def cmd_search(args: argparse.Namespace) -> int:
    found = list(make_service(args).search(
        keyword=args.keyword, category=args.category, type_=args.type,
        date_from=args.date_from, date_to=args.date_to,
        min_amount=args.min, max_amount=args.max, tag=args.tag))
    if not found:
        print("조건에 맞는 거래가 없습니다.")
        return 0
    print_table(TX_HEADERS, tx_rows(found), right_cols={4})
    print(f"\n{len(found)}건, 합계 {sum(t.signed_amount for t in found):,}원 (수입 +, 지출 -)")
    return 0


@command("summary")
@handle_errors
@timed
def cmd_summary(args: argparse.Namespace) -> int:
    month = args.month or date.today().strftime("%Y-%m")
    s = make_service(args).summary(month)
    print(f"[{s.month}] 수입 {s.income:,}원 / 지출 {s.expense:,}원 / 잔액 {s.balance:,}원")
    if not s.by_category:
        print("이 달의 지출이 없습니다.")
        return 0
    rows = []
    for cat, spent in s.by_category.items():
        rate = s.usage_rate(cat)
        limit = s.budgets.get(cat)
        rows.append([cat, f"{spent:,}", f"{limit:,}" if limit else "-",
                     f"{rate:.1f}%" if rate is not None else "-",
                     "초과" if rate is not None and rate > 100 else ""])
    print()
    print_table(["카테고리", "지출", "예산", "사용률", "상태"], rows, right_cols={1, 2, 3})
    return 0


@command("budget")
@handle_errors
@timed
def cmd_budget(args: argparse.Namespace) -> int:
    svc = make_service(args)
    if args.action == "set":
        if not (args.month and args.category and args.limit):
            raise ValidationError("budget set 에는 --month, --category, --limit 가 모두 필요합니다",
                                  "예: budget set --month 2026-10 --category 식비 --limit 300000")
        b = svc.set_budget(args.month, args.category, args.limit)
        print(f"예산을 설정했습니다: {b.month} {b.category} {b.limit:,}원")
    else:
        month = args.month or date.today().strftime("%Y-%m")
        budgets = svc.budgets_for(month)
        if not budgets:
            print(f"{month} 에 설정된 예산이 없습니다.")
        for b in budgets:
            print(f"{b.month} {b.category} {b.limit:,}원")
    return 0


@command("category")
@handle_errors
@timed
def cmd_category(args: argparse.Namespace) -> int:
    svc = make_service(args)
    if args.action == "add":
        svc.add_category(args.name)
        print(f"카테고리를 추가했습니다: {args.name}")
    elif args.action == "remove":
        svc.remove_category(args.name)
        print(f"카테고리를 삭제했습니다: {args.name}")
    else:
        cats = svc.list_categories()
        print(", ".join(cats) if cats else "등록된 카테고리가 없습니다. category add 로 추가하세요.")
    return 0


@command("update")
@handle_errors
@timed
def cmd_update(args: argparse.Namespace) -> int:
    tx = make_service(args).update(args.id, date=args.date, type=args.type, category=args.category,
                                   amount=args.amount, memo=args.memo, tags=args.tags)
    print(f"수정했습니다: {tx.id} {tx.date} {tx.category} {tx.amount:,}원 {tx.memo}")
    return 0


@command("delete")
@handle_errors
@timed
def cmd_delete(args: argparse.Namespace) -> int:
    tx = make_service(args).delete(args.id)
    print(f"삭제했습니다: {tx.id} {tx.date} {tx.category} {tx.amount:,}원")
    return 0


@command("import")
@handle_errors
@timed
def cmd_import(args: argparse.Namespace) -> int:
    result = make_service(args).import_csv(Path(args.file))
    print(f"가져오기 완료: {result.imported}건 추가, {len(result.skipped)}건 건너뜀")
    for line_no, reason in result.skipped:
        print(f"  - {line_no}번째 줄: {reason}", file=sys.stderr)
    return 0


@command("export")
@handle_errors
@timed
def cmd_export(args: argparse.Namespace) -> int:
    n = make_service(args).export_csv(Path(args.file), args.month)
    print(f"내보내기 완료: {n}건 -> {args.file}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--data-dir", default="data", help="데이터 폴더 (기본: ./data)")
    common.add_argument("--verbose", action="store_true", help="자세한 기록 출력")

    parser = argparse.ArgumentParser(prog="budget_app", description="나만의 용돈 기입장")
    sub = parser.add_subparsers(dest="command", required=True, metavar="명령")

    p = sub.add_parser("add", parents=[common], help="거래 추가")
    p.add_argument("--date", default=date.today().isoformat(), help="YYYY-MM-DD (기본: 오늘)")
    p.add_argument("--type", choices=["income", "expense"], default="expense")
    p.add_argument("--category", required=True)
    p.add_argument("--amount", required=True, help="정수 (콤마 허용)")
    p.add_argument("--memo", default="")
    p.add_argument("--tags", default="", help="쉼표 또는 ; 로 구분")

    p = sub.add_parser("list", parents=[common], help="최근 거래 보기")
    p.add_argument("--limit", type=int, default=10)

    p = sub.add_parser("search", parents=[common], help="거래 검색")
    p.add_argument("keyword", nargs="?")
    p.add_argument("--category")
    p.add_argument("--type", choices=["income", "expense"])
    p.add_argument("--from", dest="date_from", metavar="날짜")
    p.add_argument("--to", dest="date_to", metavar="날짜")
    p.add_argument("--min", type=int)
    p.add_argument("--max", type=int)
    p.add_argument("--tag")

    p = sub.add_parser("summary", parents=[common], help="월 요약")
    p.add_argument("--month", help="YYYY-MM (기본: 이번 달)")

    p = sub.add_parser("budget", parents=[common], help="월별 카테고리 예산")
    p.add_argument("action", choices=["set", "show"])
    p.add_argument("--month")
    p.add_argument("--category")
    p.add_argument("--limit")

    p = sub.add_parser("category", parents=[common], help="카테고리 관리")
    p.add_argument("action", choices=["add", "list", "remove"])
    p.add_argument("name", nargs="?", default="")

    p = sub.add_parser("update", parents=[common], help="거래 수정")
    p.add_argument("id")
    p.add_argument("--date")
    p.add_argument("--type", choices=["income", "expense"])
    p.add_argument("--category")
    p.add_argument("--amount")
    p.add_argument("--memo")
    p.add_argument("--tags")

    p = sub.add_parser("delete", parents=[common], help="거래 삭제")
    p.add_argument("id")

    p = sub.add_parser("import", parents=[common], help="CSV 가져오기")
    p.add_argument("file")

    p = sub.add_parser("export", parents=[common], help="CSV 내보내기")
    p.add_argument("file")
    p.add_argument("--month")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.WARNING,
                        format="%(levelname)s %(message)s")
    return COMMANDS[args.command](args)
```

데코레이터 쌓는 순서가 중요합니다. `@command(...)`, `@handle_errors`, `@timed`를 위에서 아래로 작성하면 실제 적용은 아래에서 위로(`@timed` 먼저) 일어납니다. `cmd_add`를 부르면 `handle_errors`가 오류를 잡아 주고, 그 안쪽에서 `timed`가 시간을 재습니다. `@command`는 가장 바깥에 두어 이미 오류 처리가 감싼 함수를 등록합니다.

`--date`, `--amount`처럼 날짜·금액이 문자열로 넘어오는 입력은 `argparse`가 검사하지 않고 서비스의 `parse_date`/`parse_amount`가 검사합니다. 그래서 잘못된 값은 `argparse` 오류(종료 코드 2)가 아니라 우리 오류 메시지(종료 코드 1)로 나옵니다. 입력 검사를 한 곳에 모으는 설계입니다.

커밋: `git commit -m "feat: argparse 서브커맨드와 오류 처리 데코레이터 추가"`

### Step 5. 추가, 조회, 검색, 요약 시연

이제 `pylab` 폴더에서 실제로 쓰습니다. 메모에 공백이 있으면 큰따옴표로 감싼다는 점을 기억하세요. 안 감싼면 쉘이 단어를 나눠 `unrecognized arguments` 오류가 납니다. 아래는 모두 실제 실행 결과입니다(날짜를 직접 넣어 결과가 날마다 달라지지 않게 했습니다).

```bash
python -m budget_app category add 식비
python -m budget_app category add 교통
python -m budget_app category add 용돈
python -m budget_app category list
```

```text
카테고리를 추가했습니다: 식비
카테고리를 추가했습니다: 교통
카테고리를 추가했습니다: 용돈
교통, 식비, 용돈
```

```bash
python -m budget_app add --date 2026-10-01 --type income --category 용돈 --amount 100,000 --memo "10월 용돈"
python -m budget_app add --date 2026-10-02 --category 식비 --amount 6500 --memo 점심 --tags 학교,점심
python -m budget_app add --date 2026-10-05 --category 교통 --amount 1450 --memo 지하철
python -m budget_app add --date 2026-10-07 --category 식비 --amount 21000 --memo "저녁 치킨"
python -m budget_app budget set --month 2026-10 --category 식비 --limit 25000
```

```text
추가했습니다: TX-000001 2026-10-01 용돈 100,000원
추가했습니다: TX-000002 2026-10-02 식비 6,500원
추가했습니다: TX-000003 2026-10-05 교통 1,450원
추가했습니다: TX-000004 2026-10-07 식비 21,000원
예산을 설정했습니다: 2026-10 식비 25,000원
```

```bash
python -m budget_app list
```

```text
ID         날짜        구분  카테고리     금액  메모       태그
---------  ----------  ----  --------  -------  ---------  ---------
TX-000004  2026-10-07  지출  식비       21,000  저녁 치킨
TX-000003  2026-10-05  지출  교통        1,450  지하철
TX-000002  2026-10-02  지출  식비        6,500  점심       학교,점심
TX-000001  2026-10-01  수입  용돈      100,000  10월 용돈
```

금액 열은 오른쪽 정렬이고, 한글이 섞여도 열이 맞습니다. 2장에서 본 `width()`로 한글 글자 폭을 2로 계산했기 때문입니다.

```bash
python -m budget_app search 점심
python -m budget_app search --category 식비 --min 10000
python -m budget_app summary --month 2026-10
```

```text
ID         날짜        구분  카테고리   금액  메모  태그
---------  ----------  ----  --------  -----  ----  ---------
TX-000002  2026-10-02  지출  식비      6,500  점심  학교,점심

1건, 합계 -6,500원 (수입 +, 지출 -)

ID         날짜        구분  카테고리    금액  메모       태그
---------  ----------  ----  --------  ------  ---------  ----
TX-000004  2026-10-07  지출  식비      21,000  저녁 치킨

1건, 합계 -21,000원 (수입 +, 지출 -)

[2026-10] 수입 100,000원 / 지출 28,950원 / 잔액 71,050원

카테고리    지출    예산  사용률  상태
--------  ------  ------  ------  ----
식비      27,500  25,000  110.0%  초과
교통       1,450       -       -
```

직접 계산해 확인해 보세요. 식비 6,500 + 21,000 = 27,500이고, 예산 25,000 대비 110.0%입니다. 테스트 결과를 눈으로 검산하는 습관이 동료 평가에서 시연할 때도 큰 도움이 됩니다.

커밋: `git commit -m "feat: 거래 추가·조회·검색·월 요약 명령 완성"`

### Step 6. 수정, 삭제, 오류 경로 점검

```bash
python -m budget_app update TX-000004 --amount 18,000 --memo "저녁 치킨(반마리)"
python -m budget_app delete TX-000003
python -m budget_app list --limit 3
```

```text
수정했습니다: TX-000004 2026-10-07 식비 18,000원 저녁 치킨(반마리)
삭제했습니다: TX-000003 2026-10-05 교통 1,450원
ID         날짜        구분  카테고리     금액  메모               태그
---------  ----------  ----  --------  -------  -----------------  ---------
TX-000004  2026-10-07  지출  식비       18,000  저녁 치킨(반마리)
TX-000002  2026-10-02  지출  식비        6,500  점심               학교,점심
TX-000001  2026-10-01  수입  용돈      100,000  10월 용돈
```

이제 일부러 틀린 입력을 넣어 오류 메시지와 종료 코드를 확인합니다. Windows PowerShell에서는 `echo $LASTEXITCODE`, macOS/Linux에서는 `echo $?`로 종료 코드를 봅니다.

```bash
python -m budget_app add --date 2026-02-30 --category 식비 --amount 100
python -m budget_app add --category 게임 --amount 100
python -m budget_app delete TX-999999
python -m budget_app category remove 식비
python -m budget_app list --bogus
```

```text
오류: 날짜 형식이 올바르지 않습니다: '2026-02-30' (힌트: YYYY-MM-DD 형식의 실제 존재하는 날짜를 입력하세요 (예: 2026-10-27))     # 종료 코드 1
오류: 등록되지 않은 카테고리입니다: '게임' (힌트: 먼저 'category add 게임' 명령으로 등록하세요)              # 종료 코드 1
오류: 거래를 찾을 수 없습니다: TX-999999 (힌트: list 또는 search 로 ID를 확인하세요)                           # 종료 코드 1
오류: '식비' 카테고리를 쓰는 거래가 있어 삭제할 수 없습니다 (힌트: 해당 거래의 카테고리를 먼저 update 로 바꾸거나 거래를 delete 하세요)  # 종료 코드 1
usage: budget_app [-h] 명령 ...
budget_app: error: unrecognized arguments: --bogus                                                           # 종료 코드 2
```

여기서 볼 점이 세 가지 있습니다. 하나, 모든 오류에 스택 트레이스가 없습니다. 둘, 우리가 만든 오류는 종료 코드 1이고, `argparse`가 직접 내는 사용법 오류는 2입니다. 셋, 모든 메시지가 “무엇이 문제인지 + 다음에 무엇을 할지”를 담고 있습니다. 미션이 요구한 “원인 + 힌트” 형식입니다.

커밋: `git commit -m "feat: 거래 수정·삭제와 오류 메시지 정리"`

### Step 7. CSV 내보내기와 가져오기

CSV는 `date,type,category,amount,memo,tags` 헤더를 가진 UTF-8 파일입니다. 여러 태그는 `;`로 이어 한 칸에 넣습니다. 먼저 내보내기입니다.

```bash
python -m budget_app export out.csv --month 2026-10
```

```text
내보내기 완료: 3건 -> out.csv
```

```text
date,type,category,amount,memo,tags
2026-10-01,income,용돈,100000,10월 용돈,
2026-10-02,expense,식비,6500,점심,학교;점심
2026-10-07,expense,식비,18000,저녁 치킨(반마리),
```

이제 일부러 문제가 있는 파일을 가져옵니다. `in.csv`를 아래 내용으로 만듭니다. 두 번째 데이터 행은 없는 카테고리, 세 번째는 존재하지 않는 날짜, 네 번째는 음수 금액입니다.

```text
date,type,category,amount,memo,tags
2026-10-10,expense,식비,4500,"김밥, 라면",점심;학교
2026-10-11,expense,게임,3000,스킨,
2026-13-01,expense,식비,1000,x,
2026-10-12,expense,식비,-5,y,
```

```bash
python -m budget_app import in.csv
python -m budget_app import nope.csv
```

```text
가져오기 완료: 1건 추가, 3건 건너뜀
  - 3번째 줄: 등록되지 않은 카테고리: '게임'
  - 4번째 줄: 날짜 형식이 올바르지 않습니다: '2026-13-01'
  - 5번째 줄: 금액은 1 이상이어야 합니다: -5
오류: 파일이 없습니다: nope.csv (힌트: 경로를 확인하세요)
```

줄 번호는 헤더를 1번째로 세기 때문에 데이터 첫 행이 2번째입니다. 엑셀에서 보이는 행 번호와 같아서 고치기 쉽습니다. 파일 전체 형식 문제(헤더 불일치)는 종료 코드 1로 멈춘니다.

```bash
printf 'a,b\n1,2\n' > bad.csv
python -m budget_app import bad.csv
```

```text
오류: CSV 헤더가 맞지 않습니다: ['a', 'b'] (힌트: 첫 줄을 date,type,category,amount,memo,tags 로 맞추세요)
```

이 결정들을 말로 설명할 수 있어야 합니다. 엑셀에서 저장한 CSV는 UTF-8 BOM이 붙을 수 있어 읽을 때는 `utf-8-sig`로 열어 BOM을 자동으로 버립니다. `newline=""`는 `csv` 모듈이 줄바꿈을 직접 처리하게 하는 표준 설정이며, 메모 안의 쉼표와 따옴표는 `csv`가 알아서 처리합니다.

커밋: `git commit -m "feat: CSV 가져오기·내보내기 추가"`

### Step 8. 테스트와 README

테스트는 `pylab/tests/test_app.py`에 둡니다. `tests/__init__.py`는 빈 파일입니다.

```python
import io
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

from budget_app.cli import main
from budget_app.errors import NotFoundError, ValidationError
from budget_app.models import parse_amount, parse_date
from budget_app.services import BudgetService
from budget_app.storage import Storage


class ParseTest(unittest.TestCase):
    def test_date(self):
        self.assertEqual(parse_date("2026-1-5"), "2026-01-05")
        for bad in ["2026-02-30", "abc", "2026-13-01", ""]:
            with self.subTest(bad=bad), self.assertRaises(ValidationError):
                parse_date(bad)

    def test_amount(self):
        self.assertEqual(parse_amount("12,500"), 12500)
        for bad in ["0", "-1", "x", "1.5"]:
            with self.subTest(bad=bad), self.assertRaises(ValidationError):
                parse_amount(bad)


class ServiceTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.svc = BudgetService(Storage(Path(self._tmp.name)))
        self.svc.add_category("식비")

    def test_add_and_latest(self):
        self.svc.add("2026-10-01", "expense", "식비", 1000)
        self.svc.add("2026-10-03", "expense", "식비", 2000)
        self.assertEqual([t.amount for t in self.svc.latest(1)], [2000])

    def test_unknown_category(self):
        with self.assertRaises(ValidationError):
            self.svc.add("2026-10-01", "expense", "게임", 1000)

    def test_update_delete(self):
        tx = self.svc.add("2026-10-01", "expense", "식비", 1000)
        self.assertEqual(self.svc.update(tx.id, amount="3,000").amount, 3000)
        self.svc.delete(tx.id)
        with self.assertRaises(NotFoundError):
            self.svc.delete(tx.id)

    def test_summary(self):
        self.svc.add("2026-10-01", "income", "식비", 5000)
        self.svc.add("2026-10-02", "expense", "식비", 2000)
        self.svc.set_budget("2026-10", "식비", 4000)
        s = self.svc.summary("2026-10")
        self.assertEqual((s.income, s.expense, s.balance), (5000, 2000, 3000))
        self.assertEqual(s.usage_rate("식비"), 50.0)

    def test_no_tmp_left(self):
        self.svc.add("2026-10-01", "expense", "식비", 1000)
        names = [p.name for p in Path(self._tmp.name).iterdir()]
        self.assertFalse([n for n in names if n.endswith(".tmp")])


class CliTest(unittest.TestCase):
    def run_cli(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = main(list(argv))
        return code, out.getvalue(), err.getvalue()

    def test_error_has_exit_code_and_no_traceback(self):
        with tempfile.TemporaryDirectory() as d:
            code, _, err = self.run_cli("add", "--data-dir", d, "--category", "없음", "--amount", "100")
        self.assertEqual(code, 1)
        self.assertIn("힌트", err)
        self.assertNotIn("Traceback", err)

    def test_happy_path(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(self.run_cli("category", "add", "식비", "--data-dir", d)[0], 0)
            code, out, _ = self.run_cli("add", "--data-dir", d, "--category", "식비",
                                        "--amount", "12,500", "--date", "2026-10-27")
            self.assertEqual(code, 0)
            self.assertIn("12,500원", out)


if __name__ == "__main__":
    unittest.main()
```

```bash
python -m unittest discover -v
```

```text
(중략)
Ran 9 tests in 0.019s

OK
```

`CliTest`는 `main(argv)`가 `int`를 돌려주는 설계 덕분에 종료 코드를 직접 검사합니다(`sys.exit`는 `__main__.py`만 호출). `test_no_tmp_left`는 원자적 저장 후 임시 파일이 남지 않는지 확인합니다. 이 테스트들은 `tempfile`의 임시 폴더만 쓰기 때문에 진짜 `data/`는 건드리지 않습니다.

README는 미션이 요구하는 네 가지(실행 방법, 저장 위치와 형식, 명령 예시, CSV 스키마)를 빠뜨리지 않았는지 확인합니다. 아래 템플릿을 그대로 출발점으로 쓰세요.

```markdown
# 나만의 용돈 기입장

표준 라이브러리만 쓰는 콘솔 용돈 기입장입니다. Python 3.10 이상이 필요합니다.

## 실행 방법

    python -m budget_app <명령> [옵션]
    python -m budget_app --help

공통 옵션: `--data-dir 폴더` (기본 `./data`), `--verbose`

## 저장 위치와 형식

`--data-dir` 폴더(기본 `./data`) 아래에 JSON Lines(한 줄 = JSON 하나, UTF-8) 파일 3개가 생깁니다.

| 파일 | 내용 | 한 줄 예 |
| --- | --- | --- |
| transactions.jsonl | 거래 | {"id": "TX-000001", "date": "2026-10-01", "type": "income", "category": "용돈", "amount": 100000, "memo": "10월 용돈", "tags": []} |
| categories.jsonl | 카테고리 | {"name": "식비"} |
| budgets.jsonl | 월별 예산 | {"month": "2026-10", "category": "식비", "limit": 25000} |

저장은 임시 파일에 쓴 뒤 교체하는 방식이라 도중에 중단되어도 원본이 깨지지 않습니다.

## 명령 예시

    python -m budget_app category add 식비
    python -m budget_app add --date 2026-10-02 --category 식비 --amount 6500 --memo 점심 --tags 학교,점심
    python -m budget_app list --limit 5
    python -m budget_app search 점심 --min 1000
    python -m budget_app budget set --month 2026-10 --category 식비 --limit 25000
    python -m budget_app summary --month 2026-10
    python -m budget_app update TX-000001 --amount 7000
    python -m budget_app delete TX-000001
    python -m budget_app export out.csv --month 2026-10
    python -m budget_app import in.csv

## CSV 스키마

UTF-8, 첫 줄 헤더: `date,type,category,amount,memo,tags`

- date: YYYY-MM-DD, type: income 또는 expense, amount: 1 이상 정수
- tags: `;` 로 연결 (예: `점심;학교`)
- 가져올 때 잘못된 행은 건너뛰고 줄 번호와 이유를 보고합니다.

## 오류와 종료 코드

오류는 `원인 (힌트: …)` 한 줄로 출력하고 스택 트레이스는 보이지 않습니다. 0 = 성공, 1 = 입력/데이터 문제, 2 = 사용법 오류 또는 예상하지 못한 문제.

## 테스트

    python -m unittest discover -v
```

### Step 8 체크리스트: 미션 요구사항이 어디에 있는지

| 미션 요구 | 이 구현의 위치 |
| --- | --- |
| 표준 라이브러리만 사용 | `argparse`, `csv`, `json`, `heapq`, `dataclasses` 등만 import |
| 10개 기능 | add, list, search, summary, budget, category, update, delete, import, export |
| 파일 3개 이상 저장 | `Storage`의 transactions/categories/budgets |
| 제너레이터 스트리밍 | `read_jsonl`, `Storage.iter_transactions`, `search` |
| 데코레이터 1개 이상 | `handle_errors`, `timed`, `command` |
| 타입 힌트 | 모든 함수 시그니처 |
| dataclass, 클래스 2개 이상 | `Transaction`, `Budget`, `MonthSummary`, `Storage`, `BudgetService` |
| 모듈 3개 이상 | errors, models, storage, services, decorators, cli |
| 원인 + 힌트 에러, 스택 트레이스 없음, 실패 시 비정상 종료 코드 | `BudgetError.__str__`, `@handle_errors` |
| 보너스: 표 정렬 | `print_table`의 `width()`/`pad()` |
| 보너스: 원자적 저장 | `atomic_write` |
| 보너스: 백업, 반복 거래 | 미구현 → 19장 확장 과제 |

마지막 점검입니다. 미션 요구를 빠짐없이 맞췄는지는 본인이 미션 문서의 항목과 이 표를 대조해 보세요. 이 표는 제가 정리한 매핑이라, 미션 원문의 정확한 문구와 차이가 있을 수 있습니다.

커밋: `git commit -m "test: 단위 테스트와 README 추가"`

## 19장. 종합 문제와 확장 과제

앞에서 배운 것을 섮어 쓰는 연습입니다. 이 장을 정답 없이 절반 이상 풀 수 있다면 미션을 혹은 작은 파이썬 프로젝트를 혼자 끝낼 수 있는 수준입니다. 아래 문제는 모두 한 파일(`ch19.py`)에 독립된 함수로 작성합니다.

### A. 숙련도 점검 문제 10개

아래 데이터를 파일 맨 위에 둡니다.

```python
txs = [
    {"date": "2026-10-01", "category": "용돈", "amount": 100000, "type": "income", "memo": "10월 용돈"},
    {"date": "2026-10-02", "category": "식비", "amount": 6500, "type": "expense", "memo": "점심 #학교"},
    {"date": "2026-10-05", "category": "교통", "amount": 1450, "type": "expense", "memo": "지하철"},
    {"date": "2026-10-07", "category": "식비", "amount": 21000, "type": "expense", "memo": "저녁 #치킨 #친구"},
    {"date": "2026-11-01", "category": "식비", "amount": 9000, "type": "expense", "memo": ""},
]
```

1. `by_category(rows)`: 지출만 카테고리별로 합계해 “합계가 큰 순”의 `(카테고리, 합계)` 리스트를 돌려주세요. 타입 힌트를 붙이세요.
2. `lines_in_month(lines, month)`: 문자열 줄들 중 `month`(예 `"2026-10"`)로 시작하는 줄만 하나씩 내보내는 제너레이터를 만드세요. 리스트를 만들면 안 됩니다.
3. `count_calls`: 감싼 함수가 몇 번 호출됐는지 `함수이름.calls`로 알 수 있는 데코레이터를 만드세요. 원래 함수의 `__name__`이 유지되어야 합니다.
4. `top_category(rows)`: 지출이 가장 큰 카테고리 이름을 돌려주고, 지출이 없으면 `None`을 돌려주세요. 1번을 다시 쓰세요.
5. `safe_int(text, default=None)`: `"1,200"`처럼 콤마가 있어도 정수로 바꾸고, 실패하면 `default`를 돌려주세요.
6. `Wallet` 클래스: `deposit(n)`, `withdraw(n)`을 가지고 잔액이 부족하면 “원인 + 힌트”가 들어 있는 `InsufficientFunds` 예외를 던지세요.
7. `timer(label)`: `with timer("작업"):` 블록이 끝날 때 걸린 시간을 밀리초로 출력하는 컨텍스트 매니저를 만드세요. 블록 안에서 예외가 나도 출력되어야 합니다.
8. `hashtags(memo)`: `"저녁 #치킨 #친구"`에서 `['치킨', '친구']`를 뽑으세요(정규표현식).
9. `last_day(y, m)`: 그 달의 마지막 날(숫자)을 돌려주세요. 윤년도 맞아야 합니다. 직접 계산하지 말고 표준 라이브러리를 쓰세요.
10. `moving_avg(values, n=3)`: 최근 `n`개의 이동평균을 하나씩 내보내는 제너레이터를 만드세요. 앞부분은 있는 만큼만 평균합니다.

힌트: 1·4번은 `defaultdict`와 `sorted(..., key=lambda kv: kv[1], reverse=True)`, 3번은 함수에 속성을 붙일 수 있습니다, 7번은 `@contextmanager` + `try/finally`, 9번은 `calendar.monthrange`, 10번은 `collections.deque(maxlen=n)`입니다.

### 정답과 해설

아래 코드 전체를 한 파일로 실행해 확인한 결과입니다.

```python
import calendar
import functools
import re
import time
from collections import defaultdict, deque
from collections.abc import Iterable, Iterator
from contextlib import contextmanager


# 1
def by_category(rows: Iterable[dict]) -> list[tuple[str, int]]:
    total: defaultdict[str, int] = defaultdict(int)
    for r in rows:
        if r["type"] == "expense":
            total[r["category"]] += r["amount"]
    return sorted(total.items(), key=lambda kv: kv[1], reverse=True)

print(by_category(txs))          # [('식비', 36500), ('교통', 1450)]


# 2
def lines_in_month(lines: Iterable[str], month: str) -> Iterator[str]:
    for line in lines:
        if line.startswith(month):
            yield line

g = lines_in_month(["2026-10-01 a", "2026-11-02 b", "2026-10-09 c"], "2026-10")
print(type(g).__name__, sum(1 for _ in g))     # generator 2


# 3
def count_calls(func):
    @functools.wraps(func)
    def wrapper(*a, **k):
        wrapper.calls += 1
        return func(*a, **k)
    wrapper.calls = 0
    return wrapper

@count_calls
def hello():
    return "hi"

hello(); hello(); hello()
print(hello.calls, hello.__name__)             # 3 hello


# 4
def top_category(rows: Iterable[dict]) -> str | None:
    ranked = by_category(rows)
    return ranked[0][0] if ranked else None

print(top_category(txs), top_category([]))     # 식비 None


# 5
def safe_int(text: str, default: int | None = None) -> int | None:
    try:
        return int(text.replace(",", ""))
    except ValueError:
        return default

print(safe_int("1,200"), safe_int("x"), safe_int("x", 0))   # 1200 None 0


# 6
class InsufficientFunds(Exception):
    def __init__(self, need: int, have: int):
        super().__init__(f"잔액이 부족합니다: 필요 {need:,}원, 보유 {have:,}원 (힌트: 입금하거나 금액을 줄이세요)")

class Wallet:
    def __init__(self, balance: int = 0) -> None:
        self.balance = balance

    def deposit(self, n: int) -> None:
        if n <= 0:
            raise ValueError("입금액은 1 이상이어야 합니다")
        self.balance += n

    def withdraw(self, n: int) -> None:
        if n > self.balance:
            raise InsufficientFunds(n, self.balance)
        self.balance -= n

w = Wallet(1000)
w.deposit(500)
w.withdraw(300)
print(w.balance)                               # 1200
try:
    w.withdraw(5000)
except InsufficientFunds as e:
    print(e)   # 잔액이 부족합니다: 필요 5,000원, 보유 1,200원 (힌트: 입금하거나 금액을 줄이세요)


# 7
@contextmanager
def timer(label: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label}: {(time.perf_counter() - start) * 1000:.1f} ms")   # 숫자는 실행마다 다릅니다

with timer("작업"):
    sum(range(1000))


# 8
def hashtags(memo: str) -> list[str]:
    return re.findall(r"#(\w+)", memo)

print(hashtags("저녁 #치킨 #친구"), hashtags("없음"))   # ['치킨', '친구'] []


# 9
def last_day(y: int, m: int) -> int:
    return calendar.monthrange(y, m)[1]

print(last_day(2026, 2), last_day(2028, 2), last_day(2026, 10))   # 28 29 31


# 10
def moving_avg(values: Iterable[int], n: int = 3) -> Iterator[float]:
    window: deque[int] = deque(maxlen=n)
    for v in values:
        window.append(v)
        yield sum(window) / len(window)

print([round(x, 1) for x in moving_avg([1000, 2000, 3000, 6000])])   # [1000.0, 1500.0, 2000.0, 3666.7]
```

- 1번: 수입(용돈)이 집계에서 빠지는 이유는 `type == "expense"` 조건이 있어서입니다. 이 조건을 빼먹으면 용돈 100,000원이 맨 앞에 나옵니다.
- 3번: `wrapper.calls`는 함수 객체에 붙이는 속성입니다. 파이썬의 함수는 객체라서 속성을 붙일 수 있습니다. `@functools.wraps`를 빼면 `hello.__name__`이 `wrapper`가 됩니다.
- 4번: `ranked[0][0]`은 첫 튜플의 첫 값(카테고리 이름)입니다. 빈 리스트를 미리 검사하지 않으면 `IndexError`가 납니다.
- 6번: 예외 클래스가 메시지를 스스로 조립하면 호출하는 쪽이 늘 같은 형식의 메시지를 내게 됩니다.
- 7번: `finally` 덕분에 블록 안에서 예외가 나도 시간이 출력됩니다. `yield`는 “여기서 `with` 블록을 실행하라”는 자리입니다.
- 8번: `\w`는 한글도 포함합니다. 그래서 `#치킨`이 잡힙니다.
- 10번: `deque(maxlen=n)`는 새 값을 넣으면 가장 오래된 값이 자동으로 밀려나가서, 원래 데이터가 크더라도 메모리를 n개만 씁니다.

### B. 확장 과제 (미션 보너스 + 연습)

18장의 `budget_app`를 그대로 두고 기능을 하나씩 더합니다. 난이도는 낮은 순입니다. 반드시 새 브랜치에서 작업하고 새 기능마다 테스트를 하나 이상 추가하세요.

| 번호 | 과제 | 배우는 것 | 난이도 |
| --- | --- | --- | --- |
| B1 | `list --all`: 전체 목록을 최신순으로, 그러나 메모리에 모두 올리지 않고 페이지(`--page`)로 | 제너레이터, `itertools.islice` | 하 |
| B2 | `summary --by-tag`: 태그별 지출 합계 | 태그 1개에 거래가 여러 번 집계되는 상황 다루기 | 하 |
| B3 | `export --format jsonl`: 형식 선택지 추가 | `choices`, 함수 디스패치 딕셔너리 | 하 |
| B4 | `backup` 명령: 데이터 폴더를 시각 폴더로 복사, 최근 N개만 유지 | `shutil`, `pathlib`, 파일 정리 | 중 |
| B5 | 반복 거래(매월 N일 통신비 등) 등록과 월별 적용 | 월 말일 처리, 중복 방지(멈등성) | 중 |
| B6 | 저장소를 SQLite(`sqlite3`)로 교체해 보기. `services.py`는 한 줄도 고치지 않아야 함 | 계층 분리의 진짜 가치, Protocol | 상 |
| B7 | 동시 실행 방지 잠금 파일 | 파일 잠금, 경쟁 상태 | 상 |

B1\~B3은 힌트만, B4·B5는 완성 코드가 아래에 있습니다. B6·B7은 방향만 잡습니다.

- B1 힌트: 최신순 N페이지는 "최신순 정렬 결과의 (N-1)×크기 번째부터 크기개"입니다. 가장 쉬운 방법은 `heapq.nlargest(page*size, ...)`로 필요한 만큼만 뽑아 뒤쪽 `size`개를 자르는 것입니다(메모리는 `page*size`개). 파일을 한 건씩 흘려보내면서 최신순 페이지를 만들기 어려운 이유(최신순을 알려면 끝까지 읽어야 함)를 한 문장으로 써 보는 것이 학습 포인트입니다.
- B2 힌트: `for tag in tx.tags: total[tag] += tx.amount`. 한 거래에 태그가 여러 개면 여러 번 집계되므로 태그 합계의 총합이 지출 총합보다 커질 수 있다는 점을 화면에 설명하세요.
- B3 힌트: `FORMATS = {"csv": export_csv, "jsonl": export_jsonl}`처럼 함수를 딕셔너리에 넣고 `FORMATS[args.format](...)`를 부릅니다.

### B4, B5 완성 코드

새 파일 `budget_app/extras.py`입니다. 실제로 돌려 다음을 확인했습니다: 정기 거래는 두 번 적용해도 한 번만 추가되고, 31일로 등록한 것이 2월에는 28일로 들어가며, 백업은 최근 3개만 남습니다.

```python
# budget_app/extras.py
from __future__ import annotations

import calendar
import shutil
from datetime import datetime
from pathlib import Path

from .models import parse_amount, parse_month
from .services import BudgetService
from .storage import Storage, read_jsonl, write_jsonl


def backup(storage: Storage, keep: int = 5, now: datetime | None = None) -> Path:
    """data 폴더의 .jsonl 파일을 backups/타임스탬프/ 로 복사하고 오래된 백업은 keep개만 남긴다."""
    stamp = (now or datetime.now()).strftime("%Y%m%d-%H%M%S")
    root = storage.data_dir / "backups"
    dest = root / stamp
    dest.mkdir(parents=True, exist_ok=True)
    for src in storage.data_dir.glob("*.jsonl"):
        shutil.copy2(src, dest / src.name)
    old = sorted(p for p in root.iterdir() if p.is_dir())[:-keep]
    for p in old:
        shutil.rmtree(p)
    return dest


def add_recurring(storage: Storage, category: str, amount: str | int, day: int, memo: str = "") -> None:
    path = storage.data_dir / "recurring.jsonl"
    rows = list(read_jsonl(path))
    rows.append({"category": category, "amount": parse_amount(amount), "day": day, "memo": memo})
    write_jsonl(path, rows)


def apply_recurring(service: BudgetService, month: str) -> int:
    """해당 월에 반복 거래를 넣는다. 이미 넣은 것은 건너뛰므로 여러 번 실행해도 안전하다."""
    month = parse_month(month)
    year, mon = (int(p) for p in month.split("-"))
    last = calendar.monthrange(year, mon)[1]
    path = service.storage.data_dir / "recurring.jsonl"
    done = {(t.memo, t.date) for t in service.storage.iter_transactions()}
    added = 0
    for rule in read_jsonl(path):
        date = f"{month}-{min(rule['day'], last):02d}"
        memo = rule["memo"] or "정기 지출"
        if (memo, date) in done:
            continue
        service.add(date, "expense", rule["category"], rule["amount"], memo, ["정기"])
        added += 1
    return added
```

사용 예시입니다(반복 거래 등록 명령은 CLI에 연결하는 것까지가 과제입니다).

```python
st = Storage(Path("data")); svc = BudgetService(st)
svc.add_category("통신")
add_recurring(st, "통신", 55000, 31, "휴대폰 요금")
print(apply_recurring(svc, "2026-02"), apply_recurring(svc, "2026-02"))   # 1 0
# 추가된 거래: ('2026-02-28', '휴대폰 요금', 55000)
```

설계 선택을 설명할 수 있어야 합니다. 중복 적용 방지는 “같은 메모 + 같은 날짜”로 판단하므로 메모를 바꾸면 다시 들어가는 한계가 있습니다. 더 튼튼하게 만들려면 적용한 규칙 ID를 거래에 기록해 두는 방법이 있습니다.

### C. 스스로 평가하는 숙련도 체크리스트

- [ ] 빈 파일에서 `dataclass` 하나와 `to_dict/from_dict`를 기억으로 쓸 수 있다.
- [ ] `yield`와 `return`의 차이를, 메모리 관점에서 예시와 함께 설명할 수 있다.
- [ ] `@wraps`를 빼면 어떤 문제가 생기는지 시연할 수 있다.
- [ ] 타입 힌트가 실행을 막지 않는다는 것과 `mypy`가 잡아 주는 것을 구분할 수 있다.
- [ ] 오류 메시지를 읽고 원인 줄을 찾아 고칠 수 있다(16장).
- [ ] `python -m 패키지`가 동작하는 이유를 `__main__.py`로 설명할 수 있다.
- [ ] 파일 저장이 도중에 중단되어도 원본이 안 깨지는 이유를 설명할 수 있다.
- [ ] 새 기능 하나를 브랜치 → 테스트 → 커밋 → 병합 순서로 추가할 수 있다.

체크가 안 되는 항목이 있으면 해당 장으로 돌아가 연습문제만 다시 풉니다: 데이터 모델 9장, 파일 8장, 패키지 10장, 제너레이터 11장, 데코레이터 12장, 타입 힌트 13장, 디버깅 16장, Git 17장.

## 20장. 동료 평가 준비

미션 문서는 마친 뒤 스스로 설명할 수 있어야 할 것으로 계층 책임, 제너레이터 스트리밍, 데코레이터, 타입 힌트 이점을 꼽습니다. 동료 평가는 결국 "내 코드를 내가 설명할 수 있는가"를 확인하는 자리이므로, 아래 답변을 외우지 말고 18장 코드를 열어 놓고 자기 말로 바꿔 보세요. 평가 항목의 정확한 문구는 미션 문서를 직접 대조하세요.

### 설명 목표별 답변 뼈대

| 설명할 것 | 한 줄 답 | 보여 줄 코드 |
| --- | --- | --- |
| 저장 방식 | JSONL 3개 파일(거래·카테고리·예산). 한 줄이 JSON 하나라 한 줄씩 읽을 수 있고, 저장은 임시 파일에 쓴 뒤 `os.replace`로 교체해 중간에 끊겨도 원본이 안전합니다. | `storage.py`의 `atomic_write`, `read_jsonl` |
| 계층 책임 | models는 데이터와 입력 검증, storage는 파일 읽기/쓰기, services는 업무 규칙, cli는 인자 해석과 화면 출력입니다. 의존은 한 방향(cli → services → storage → models)입니다. | 폴더 구조, `services.py`에 `print`가 없다는 점 |
| 제너레이터 | 파일 전체를 리스트로 올리지 않고 `yield`로 한 줄씩 내보내서 거래가 아주 많아져도 메모리가 일정합니다. 최신 N건은 `heapq.nlargest`로 N개만 유지합니다. | `read_jsonl`, `search`, `latest`, 11장의 `tracemalloc` 측정 |
| 데코레이터 | 오류 처리와 시간 측정은 모든 명령에 공통이라 명령 함수마다 복사하지 않고 `@handle_errors`, `@timed`로 한 번만 작성했습니다. 명령 본문은 핵심 로직만 남습니다. | `decorators.py`, `cli.py`의 `@command`, `@handle_errors`, `@timed` |
| 타입 힌트 이점 | 함수의 입력/출력 계약이 코드에 드러나고, `mypy` 같은 도구가 실행 전에 `None` 처리 누락 같은 실수를 잡습니다. 실행을 막지는 않습니다. | 13장의 `bad13.py`와 `mypy` 결과 |

### 예상 질문과 답 방향

| 질문 | 답 방향 |
| --- | --- |
| 왜 금액을 `int`로 저장했나요? | `float`은 0.1+0.2처럼 오차가 생겨 돈 계산에 부적합하기 때문입니다(1장). 원 단위라 소수가 필요 없습니다. |
| 저장할 때마다 전체 파일을 다시 쓰면 비효율 아닌가요? | 맞습니다. 대신 구현이 단순하고 원자적 교체로 안전합니다. 거래가 매우 많아지면 추가 전용(append)이나 SQLite로 바꿀 수 있고, 계층을 나눠 두었기 때문에 `services.py`는 고치지 않아도 됩니다(19장 B6). |
| 제너레이터를 쓰면 정말 메모리가 줄었나요? | 리스트로 읽을 때와 제너레이터로 읽을 때의 `tracemalloc` 측정 결과를 보여 줍니다(11장). 추측으로 말하지 말고 숫자로 보여 주세요. |
| `@wraps`를 왜 썼나요? | 안 쓰면 감싼 함수의 `__name__`이 `wrapper`가 되어 로그와 도움말이 헷갈리기 때문입니다(12장). |
| 잘못된 CSV 행이 있으면 전체가 실패하나요? | 행 단위 오류는 건너뛰고 줄 번호와 이유를 보고합니다. 헤더가 틀렸거나 파일이 없으면 전체를 중단합니다. |
| 스택 트레이스를 왜 숨기나요? | 사용자에게는 원인과 해결 방법이 필요하기 때문입니다. 예상 못한 오류도 `--verbose`로 자세한 기록을 볼 수 있습니다. |
| 테스트는 어떻게 했나요? | `unittest`와 임시 폴더로 파싱, 서비스, 종료 코드를 검증했습니다(16장). |

### 시연 순서 (5분)

1. `python -m budget_app --help`로 명령 목록 보여 주기
2. `category add` → `add` 3건 → `list`(표 정렬과 천 단위 콤마)
3. `budget set` → `summary --month`(예산 초과 표시)
4. `search`로 키워드·금액·태그 필터
5. `update`, `delete`
6. 일부러 잘못된 날짜로 `add` 실행: 원인 + 힌트 메시지와 종료 코드 1, 스택 트레이스가 없다는 점
7. `export` 후 `import`: 잘못된 행을 건너뛰고 줄 번호로 보고
8. `python -m unittest discover -v` 통과 화면
9. 코드 두 곳 열어 보기: `read_jsonl`(제너레이터), `handle_errors`(데코레이터)

시연 전 `data/` 폴더를 비운 새 폴더에서 한 번 처음부터 끝까지 따라 해 보세요. 데이터가 남아 있으면 ID와 합계가 예상과 달라 당황하기 쉽습니다.

### 제출 전 점검

- [ ] README에 실행 방법, 저장 위치와 형식, 명령 예시, CSV 스키마가 있다
- [ ] 새 폴더에서 README만 보고 따라 했을 때 막힘이 없다
- [ ] 모든 명령이 실패 시 0이 아닌 종료 코드를 반환한다
- [ ] 어떤 오류에서도 스택 트레이스가 보이지 않는다
- [ ] `.gitignore`에 `data/`, `.venv/`, `__pycache__/`가 있고 개인 데이터가 저장소에 없다
- [ ] `git log --oneline`만 읽어도 개발 순서가 보인다
- [ ] 위 5가지 설명을 코드를 보며 말로 할 수 있다
- [ ] 평가자가 물어볼 것 같은 약점(전체 재작성, 동시 실행 미지원 등)을 알고 한 문장으로 답할 수 있다

## 심화편. 파이썬 전문가 과정 (21\~29장)

18\~20장까지가 미션 수행용이고, 여기서부터는 미션 이후에 파이썬 전반을 숙련하기 위한 심화 과정입니다. 21\~29장은 서로 독립적이라 필요한 장부터 읽어도 되지만, 처음 읽는다면 순서대로 보세요. 모든 예제는 `python 파일이름.py`로 실행해 출력을 확인한 것입니다.

## 21장. 클래스 심화: 변수 종류, 메서드 3종, 상속, 추상 클래스

9장에서 클래스의 기본을 다뤘다면, 이 장은 “클래스를 설계하는 법”입니다. `@classmethod`와 `@staticmethod`가 언제 필요한지, 상속을 언제 쓰고 언제 쓰지 말아야 하는지를 익힙니다.

### 핵심 개념

- 인스턴스 변수는 `self.x`로 만들며 객체마다 따로 있습니다. 클래스 변수는 클래스 본문에 적으며 모든 객체가 공유합니다.
- 객체에서 `a.x = 값`을 하면 클래스 변수를 바꾸는 게 아니라 그 객체에만 새 인스턴스 변수가 생깁니다(가려짐). 클래스 변수를 바꾸려면 `클래스이름.x = 값`으로 씁니다.
- 인스턴스 메서드는 첫 인자가 `self`이고 객체의 데이터를 다룹니다.
- `@classmethod`는 첫 인자가 `cls`(클래스 자신)입니다. 주로 `parse`, `from_dict`처럼 다른 재료로 객체를 만드는 대체 생성자에 씁니다. 자식 클래스에서 호출하면 `cls`가 자식이라서 자식 객체가 만들어집니다.
- `@staticmethod`는 `self`도 `cls`도 받지 않는 보통 함수를 클래스 안에 넣은 것입니다. 클래스와 관련은 있지만 객체 데이터는 안 쓰는 검증·변환 함수에 씁니다. 모듈 함수로 둬도 되는지 먼저 생각하세요. 대개는 모듈 함수가 더 단순합니다.
- 상속(`class 자식(부모)`)은 “자식은 부모의 한 종류다(is-a)”일 때만 씁니다. 단순히 코드를 재사용하려는 목적이면 합성(has-a, 객체를 속성으로 가지기)이 더 안전합니다.
- `super()`는 “MRO에서 다음 클래스”를 가리킵니다. 부모 하나만 있을 때는 “부모”와 같지만, 다중 상속에서는 아닙니다.
- MRO(Method Resolution Order)는 메서드를 찾는 순서이며 `클래스.__mro__`로 볼 수 있습니다.
- 추상 클래스(`ABC` + `@abstractmethod`)는 “이 메서드는 자식이 꼭 구현해야 한다”는 약속입니다. 구현하지 않으면 객체를 만들 때 `TypeError`가 납니다.

### 따라 하기

`ch21a.py`: 변수 종류.

```python
# 인스턴스 변수 vs 클래스 변수
class Account:
    bank = "코디은행"          # 클래스 변수: 모든 객체가 공유
    count = 0

    def __init__(self, owner: str, balance: int = 0) -> None:
        self.owner = owner      # 인스턴스 변수: 객체마다 따로
        self.balance = balance
        Account.count += 1

a = Account("안흥", 1000)
b = Account("민수")
print(a.bank, b.bank, Account.count)   # 코디은행 코디은행 2
a.bank = "내은행"                      # a에만 새 인스턴스 변수가 생김(그림자)
print(a.bank, b.bank, Account.bank)    # 내은행 코디은행 코디은행
print(a.__dict__)                      # {'owner': '안흥', 'balance': 1000, 'bank': '내은행'}
```

`ch21b.py`: 메서드 3종. 마지막 두 줄이 `@classmethod`의 핵심입니다. `Won.parse`를 부르면 `Money`가 아니라 `Won` 객체가 나옵니다.

```python
# 메서드 3종
class Money:
    UNIT = "원"

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def add(self, other: "Money") -> "Money":        # 인스턴스 메서드: self 필요
        return Money(self.amount + other.amount)

    @classmethod
    def parse(cls, text: str) -> "Money":            # 대체 생성자: cls로 자기 클래스를 받는다
        digits = text.replace(",", "").replace(cls.UNIT, "").strip()
        return cls(int(digits))

    @staticmethod
    def is_valid(text: str) -> bool:                 # self도 cls도 안 쓰는 보조 함수
        digits = text.replace(",", "").replace("원", "").strip()
        return digits.isdigit()

    def __repr__(self) -> str:
        return f"Money({self.amount})"

print(Money.parse("12,500원"))          # Money(12500)
print(Money.is_valid("12,5oo"))         # False
print(Money(100).add(Money(50)))        # Money(150)
m = Money(1)
print(m.is_valid("77"))                 # 인스턴스로도 호출은 되지만 의미는 같다

class Won(Money):
    UNIT = "₩"
print(type(Won.parse("₩3,000")).__name__)   # Won  ← classmethod는 상속받은 클래스를 돌려준다
```

`ch21c.py`: 상속과 다형성. `Income`과 `Expense`는 `signed()`를 따로 구현하지 않았지만 부모의 `sign` 값만 다르게 줘서 같은 코드가 다르게 동작합니다. `issubclass(Expense, Income)`이 `False`인 점도 확인하세요. 둘은 형제이지 부모-자식이 아닙니다.

```python
# 상속, super, 오버라이딩, 다형성
class Transaction:
    sign = 0
    def __init__(self, amount: int, category: str) -> None:
        self.amount = amount
        self.category = category
    def signed(self) -> int:
        return self.sign * self.amount
    def describe(self) -> str:
        return f"{self.category} {self.amount:,}원"

class Income(Transaction):
    sign = +1

class Expense(Transaction):
    sign = -1
    def __init__(self, amount: int, category: str, memo: str = "") -> None:
        super().__init__(amount, category)   # 부모 초기화를 먼저
        self.memo = memo
    def describe(self) -> str:
        base = super().describe()
        return f"{base} ({self.memo})" if self.memo else base

items = [Income(50000, "용돈"), Expense(12000, "식비", "치킨"), Expense(3000, "교통")]
for t in items:                      # 다형성: 같은 호출, 클래스마다 다른 동작
    print(type(t).__name__, t.describe(), t.signed())
print(isinstance(items[0], Transaction), issubclass(Expense, Income))
print(sum(t.signed() for t in items))
```

```text
Income 용돈 50,000원 50000
Expense 식비 12,000원 (치킨) -12000
Expense 교통 3,000원 -3000
True False
35000
```

`ch21d.py`: 다중 상속과 MRO. `D → B → C → A` 순서로 `super()`가 이어집니다. B의 `super()`가 부모 A가 아니라 C로 갔다는 점이 중요합니다. 믹스인(`JsonMixin`)은 단독으로 쓰지 않고 기능 하나를 덧붙이는 작은 클래스입니다.

```python
# MRO와 다중 상속
class A:
    def hello(self): return "A"
class B(A):
    def hello(self): return "B>" + super().hello()
class C(A):
    def hello(self): return "C>" + super().hello()
class D(B, C):
    def hello(self): return "D>" + super().hello()
print(D().hello())                      # D>B>C>A
print([k.__name__ for k in D.__mro__])  # ['D', 'B', 'C', 'A', 'object']

# 믹스인: 작은 기능 조각
import json
class JsonMixin:
    def to_json(self) -> str:
        return json.dumps(self.__dict__, ensure_ascii=False)
class Tx(JsonMixin):
    def __init__(self, amount, category):
        self.amount, self.category = amount, category
print(Tx(1200, "간식").to_json())
```

```text
D>B>C>A
['D', 'B', 'C', 'A', 'object']
{"amount": 1200, "category": "간식"}
```

`ch21e.py`: 추상 클래스와 합성. `Exporter`는 “공통 흐름은 부모가, 달라지는 부분은 자식이” 맡는 템플릿 메서드 패턴입니다. `Ledger`는 상속 대신 `Exporter`를 속성으로 가집니다. 내보내기 방식을 바꾸고 싶으면 객체만 갈아 끼우면 됩니다.

```python
# 합성(has-a) vs 상속(is-a), ABC
from abc import ABC, abstractmethod

class Exporter(ABC):
    @abstractmethod
    def export(self, rows: list[dict]) -> str: ...
    def run(self, rows):                       # 템플릿 메서드: 공통 흐름은 부모가
        return self.export(sorted(rows, key=lambda r: r["date"]))

class CsvExporter(Exporter):
    def export(self, rows):
        return "\n".join(f'{r["date"]},{r["amount"]}' for r in rows)

class JsonlExporter(Exporter):
    def export(self, rows):
        import json
        return "\n".join(json.dumps(r, ensure_ascii=False) for r in rows)

try:
    Exporter()
except TypeError as e:
    print("추상 클래스는 만들 수 없다:", e)

rows = [{"date": "2026-10-02", "amount": 300}, {"date": "2026-10-01", "amount": 900}]
for ex in (CsvExporter(), JsonlExporter()):
    print(type(ex).__name__)
    print(ex.run(rows))

class Ledger:                                   # 합성: Ledger는 Exporter를 '가진다'
    def __init__(self, exporter: Exporter) -> None:
        self.exporter = exporter
        self.rows: list[dict] = []
    def dump(self) -> str:
        return self.exporter.run(self.rows)
l = Ledger(CsvExporter()); l.rows = rows
print(l.dump())
```

```text
추상 클래스는 만들 수 없다: Can't instantiate abstract class Exporter without an implementation for abstract method 'export'
CsvExporter
2026-10-01,900
2026-10-02,300
JsonlExporter
{"date": "2026-10-01", "amount": 900}
{"date": "2026-10-02", "amount": 300}
2026-10-01,900
2026-10-02,300
```

### 연습문제

`ex21.py`에 풀어 보세요.

1. 객체가 만들어질 때마다 클래스 변수 `total`이 1 늘어나는 `Counter` 클래스를 만들고, 객체 3개를 만든 뒤 `Counter.total`을 출력하세요.
2. `Category` 클래스에 `@classmethod from_text(cls, text)`를 만들어 공백을 없애고 소문자로 바꾼 이름으로 객체를 만드세요. `"  식비 "`, `" FOOD"`로 확인하세요.
3. `@staticmethod c_to_f(c)`(섭씨→화씨)를 가진 `Temp` 클래스를 만들고 100도를 변환하세요.
4. `area()`를 가진 부모 `Shape`(호출하면 `NotImplementedError`)와 자식 `Rect(w, h)`, `Circle(r)`을 만들고, 리스트에 담아 컴프리헨션으로 면적 목록을 출력하세요.
5. `A`, `B(A)`, `C(A)`, `D(B, C)`가 있고 `C`만 `who()`를 오버라이드합니다. `D().who()`의 결과와 `D.__mro__`를 예상한 뒤 확인하세요.
6. 추상 클래스 `Rule`에 `check(amount) -> bool`을 추상 메서드로 두고, `Positive`(0보다 큼)와 `Limit(cap)`(cap 이하)을 구현하세요. 5000원과 200000원(cap 100000)이 두 규칙을 모두 통과하는지 `all()`로 확인하세요.
7. `Base → Mid → Leaf`에서 각 `__init__`이 `super().__init__()`을 부르고 자기 이름을 `self.log` 리스트에 붙입니다. `Leaf().log`가 어떻게 나올지 예상하세요.

힌트: 1번은 `Counter.total += 1`을 `__init__` 안에서, 4번은 `[s.area() for s in ...]`, 7번은 부모 `__init__`이 먼저 실행되므로 `Base`부터 쌓입니다.

### 정답과 해설

```python
# 1
class Counter:
    total = 0
    def __init__(self):
        Counter.total += 1
a, b, c = Counter(), Counter(), Counter()
print(Counter.total)  # 3
# 2
class Category:
    def __init__(self, name): self.name = name
    @classmethod
    def from_text(cls, text):
        return cls(text.strip().lower())
print(Category.from_text("  식비 ").name, Category.from_text(" FOOD").name)
# 3
class Temp:
    @staticmethod
    def c_to_f(c): return c * 9 / 5 + 32
print(Temp.c_to_f(100))
# 4
class Shape:
    def area(self): raise NotImplementedError
class Rect(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return round(3.14159 * self.r ** 2, 2)
print([s.area() for s in (Rect(2, 3), Circle(1))])
# 5
class A:
    def who(self): return "A"
class B(A): pass
class C(A):
    def who(self): return "C"
class D(B, C): pass
print(D().who(), [k.__name__ for k in D.__mro__])
# 6
from abc import ABC, abstractmethod
class Rule(ABC):
    @abstractmethod
    def check(self, amount: int) -> bool: ...
class Positive(Rule):
    def check(self, amount): return amount > 0
class Limit(Rule):
    def __init__(self, cap): self.cap = cap
    def check(self, amount): return amount <= self.cap
rules = [Positive(), Limit(100000)]
print(all(r.check(5000) for r in rules), all(r.check(200000) for r in rules))
# 7
class Base:
    def __init__(self): self.log = ["Base"]
class Mid(Base):
    def __init__(self):
        super().__init__(); self.log.append("Mid")
class Leaf(Mid):
    def __init__(self):
        super().__init__(); self.log.append("Leaf")
print(Leaf().log)
```

```text
3
식비 food
212.0
[6, 3.14]
C ['D', 'B', 'C', 'A', 'object']
True False
['Base', 'Mid', 'Leaf']
```

- 1번에서 `self.total += 1`이라고 쓰면 읽은 값은 클래스 변수이지만 대입은 인스턴스 변수가 만들어져서 합계가 늘지 않습니다. 반드시 `Counter.total`로 씁니다.
- 5번의 결과가 `C`인 이유는 MRO가 `D, B, C, A`이고 `B`에는 `who`가 없어서 다음인 `C`에서 찾기 때문입니다. `A`까지 가지 않습니다.
- 6번의 `all(...)`은 하나라도 `False`이면 `False`입니다. `any(...)`와 구별하세요.

### 이 장의 판단 기준

| 상황 | 선택 |
| --- | --- |
| 다른 재료(문자열, dict)로 객체를 만들고 싶다 | `@classmethod` 대체 생성자 |
| 클래스와 관련 있지만 객체 데이터는 안 쓰는 함수 | 모듈 함수 먼저, 클래스 묶음이 꼭 필요하면 `@staticmethod` |
| “A는 B의 한 종류다” | 상속 |
| “A는 B를 사용한다/가진다” | 합성 |
| 자식이 반드시 구현해야 하는 메서드가 있다 | `ABC` + `@abstractmethod` |

## 22장. 특수 메서드(던더 메서드): 내 클래스를 파이썬답게

`len(x)`, `x + y`, `x == y`, `for a in x`, `with x`는 모두 객체의 특수 메서드를 부르는 문법입니다. 양쪽에 밑줄 두 개가 붙어서 던더(double underscore) 메서드라고 부릅니다. 특수 메서드를 구현하면 내가 만든 클래스가 리스트나 숫자처럼 자연스럽게 동작합니다. 지금까지 본 `__init__`, `__repr__`, `__enter__`도 모두 여기에 속합니다.

### 핵심 개념

| 문법 | 부르는 메서드 | 용도 |
| --- | --- | --- |
| `repr(x)`, 디버그 출력 | `__repr__` | 개발자용 표현. 가능하면 `Money(1200)`처럼 코드로 다시 만들 수 있게 |
| `str(x)`, `print(x)` | `__str__` | 사용자용 표현. 없으면 `__repr__`을 씀 |
| `x == y` | `__eq__` | 같은지 비교 |
| `hash(x)`, set/dict 키 | `__hash__` | `__eq__`를 정의하면 `__hash__`도 같이 정의해야 함 |
| `<`, `>` 등 | `__lt__` 등 | `@total_ordering`을 쓰면 `__eq__`와 `__lt__` 하나만 써도 나머지가 생김 |
| `x + y` | `__add__`, `__radd__` | `__radd__`는 왼쪽이 모르는 타입일 때 오른쪽이 처리 |
| `len(x)` | `__len__` | 길이 |
| `x[i]`, `x[1:3]` | `__getitem__` | 인덱싱과 슬라이싱 |
| `for a in x` | `__iter__` | 반복. 이터레이터는 `__next__`도 필요 |
| `a in x` | `__contains__` | 포함 여부 |
| `if x:` | `__bool__`(없으면 `__len__`) | 참/거짓 |
| `x(...)` | `__call__` | 객체를 함수처럼 호출 |
| `with x:` | `__enter__`, `__exit__` | 컨텍스트 매니저 |

규칙 세 가지만 기억하세요.

- 모르는 타입과 연산할 때는 예외를 던지지 말고 `NotImplemented`를 반환합니다. 그러면 파이썬이 반대쪽 객체의 메서드를 시도하고, 그것도 안 되면 알아서 `TypeError`를 냅니다.
- `__eq__`만 정의하고 `__hash__`를 빼면 그 클래스의 객체는 set과 dict 키로 쓸 수 없습니다(해시 불가능이 됩니다).
- 특수 메서드는 직접 `x.__len__()`처럼 부르지 말고 `len(x)`처럼 내장 함수와 연산자로 호출합니다.

### 따라 하기

`ch22a.py`: 금액 객체. `sum()`이 동작하려면 `__radd__`가 필요합니다. `sum`이 `0 + 첫 객체`부터 시작하기 때문입니다.

```python
from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, amount: int) -> None:
        self.amount = amount
    def __repr__(self) -> str:           # 개발자용: 디버깅/로그
        return f"Money({self.amount})"
    def __str__(self) -> str:            # 사용자용: print
        return f"{self.amount:,}원"
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount
    def __lt__(self, other: "Money") -> bool:
        return self.amount < other.amount
    def __hash__(self) -> int:           # __eq__를 정의하면 hash도 함께 정의해야 set/dict 키로 쓴다
        return hash(self.amount)
    def __add__(self, other: "Money") -> "Money":
        return Money(self.amount + other.amount)
    def __radd__(self, other):           # sum()이 0 + Money 를 시도하므로 필요
        return self if other == 0 else NotImplemented
    def __bool__(self) -> bool:
        return self.amount != 0

a, b = Money(1200), Money(800)
print(a, repr(a), [a, b])           # 1,200원 Money(1200) [Money(1200), Money(800)]
print(a == Money(1200), a != b, a > b, a >= b, b <= a)
print(sorted([a, b]), max(a, b))
print(a + b, sum([a, b, Money(100)]))
print({Money(5), Money(5), Money(7)})
print(bool(Money(0)), bool(a))
print(a == 1200)                     # False (다른 타입과는 같지 않다)
```

```text
1,200원 Money(1200) [Money(1200), Money(800)]
True True True True True
[Money(800), Money(1200)] 1,200원
2,000원 2,100원
{Money(5), Money(7)}
False True
False
```

`ch22b.py`: 장부를 리스트처럼, 함수처럼, `with`처럼 쓰기. `__getitem__`에서 슬라이스(`L[1:]`)가 오면 `slice` 객체가 들어오므로 따로 처리했습니다.

```python
class Ledger:
    def __init__(self, items=None) -> None:
        self._items = list(items or [])
    def __len__(self) -> int:
        return len(self._items)
    def __getitem__(self, i):                 # ledger[0], ledger[1:3], 그리고 for 반복도 가능
        if isinstance(i, slice):
            return Ledger(self._items[i])
        return self._items[i]
    def __iter__(self):
        return iter(self._items)
    def __contains__(self, x) -> bool:
        return x in self._items
    def __repr__(self) -> str:
        return f"Ledger({self._items!r})"
    def __call__(self, category: str):        # 객체를 함수처럼 호출
        return [x for x in self._items if x["category"] == category]
    def __enter__(self):
        print("장부 열기"); return self
    def __exit__(self, exc_type, exc, tb):
        print("장부 닫기", "(오류 발생)" if exc_type else ""); return False

L = Ledger([{"category": "식비", "amount": 900}, {"category": "교통", "amount": 1250}, {"category": "식비", "amount": 4000}])
print(len(L), L[0]["amount"], len(L[1:]))
print([t["amount"] for t in L])
print({"category": "교통", "amount": 1250} in L)
print(L("식비"))
with L as ledger:
    print("안에서 사용:", len(ledger))
```

```text
3 900 2
[900, 1250, 4000]
True
[{'category': '식비', 'amount': 900}, {'category': '식비', 'amount': 4000}]
장부 열기
안에서 사용: 3
장부 닫기 
```

`ch22c.py`: 이터레이터 프로토콜을 직접 구현하면 11장의 제너레이터가 무엇을 대신해 주는지 보입니다. 그리고 `NotImplemented`가 어떻게 `TypeError`로 이어지는지 확인합니다.

```python
class Countdown:
    def __init__(self, n): self.n = n
    def __iter__(self): return self
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1
print(list(Countdown(3)))

class V:
    def __init__(self, x): self.x = x
    def __add__(self, o):
        if not isinstance(o, V): return NotImplemented
        return V(self.x + o.x)
    def __repr__(self): return f"V({self.x})"
print(V(1) + V(2))
try:
    V(1) + 5
except TypeError as e:
    print("TypeError:", e)
```

```text
[3, 2, 1]
V(3)
TypeError: unsupported operand type(s) for +: 'V' and 'int'
```

### 연습문제

`ex22.py`에 풀어 보세요.

1. `Tag(name)` 클래스를 만들어 `print(t)`는 `#식비`, `repr(t)`는 `Tag('식비')`로 나오게 하고, 이름이 같으면 같은 태그로 취급해 set에 한 번만 들어가게 하세요.
2. `Stack` 클래스에 `push`, `pop`을 만들고, `len(s)`, `bool(s)`(비었으면 False), `list(s)`(나중에 넣은 것부터)가 동작하게 하세요.
3. `Poly(1, 2, 3)`이 `1 + 2x + 3x²`를 뜻하고 `p(2)`로 값을 계산하게 `__call__`을 구현하세요.
4. `Vec(x, y)`에 덧셈, 숫자 곱(`v * 3`과 `3 * v` 모두)을 구현하세요.
5. 코드 블록의 실행 시간을 재는 `Timer` 컨텍스트 매니저를 만들어 `with Timer() as t:` 뒤에 `t.elapsed`로 읽게 하세요.
6. 리스트를 `size`개씩 나눠 주는 `Page(data, size)`를 만들어 `len`, `page[i]`, `for chunk in page`가 모두 되게 하세요. (`__getitem__`만으로 `for`가 되는 이유도 설명해 보세요.)

힌트: 1번은 `__eq__`와 `__hash__`를 함께, 3번은 `enumerate`, 4번은 `__rmul__`에서 `self * k`를 재사용, 6번은 범위를 벗어나면 `IndexError`를 일으킵니다.

### 정답과 해설

```python
# 1
class Tag:
    def __init__(self, name): self.name = name
    def __repr__(self): return f"Tag({self.name!r})"
    def __str__(self): return f"#{self.name}"
    def __eq__(self, o): return isinstance(o, Tag) and self.name == o.name
    def __hash__(self): return hash(self.name)
t = Tag("식비"); print(t, repr(t), t == Tag("식비"), len({t, Tag("식비")}))
# 2
class Stack:
    def __init__(self): self._d = []
    def push(self, x): self._d.append(x)
    def pop(self): return self._d.pop()
    def __len__(self): return len(self._d)
    def __bool__(self): return bool(self._d)
    def __iter__(self): return reversed(self._d)
s = Stack(); s.push(1); s.push(2); s.push(3)
print(len(s), bool(s), list(s), bool(Stack()))
# 3
class Poly:
    def __init__(self, *c): self.c = c
    def __call__(self, x): return sum(k * x ** i for i, k in enumerate(self.c))
p = Poly(1, 2, 3)   # 1 + 2x + 3x^2
print(p(2))
# 4
class Vec:
    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, o): return Vec(self.x + o.x, self.y + o.y)
    def __mul__(self, k): return Vec(self.x * k, self.y * k)
    def __rmul__(self, k): return self * k
    def __repr__(self): return f"Vec({self.x}, {self.y})"
print(Vec(1, 2) + Vec(3, 4), Vec(1, 2) * 3, 3 * Vec(1, 2))
# 5
class Timer:
    def __enter__(self):
        import time; self.t0 = time.perf_counter(); return self
    def __exit__(self, *exc):
        import time; self.elapsed = time.perf_counter() - self.t0; return False
with Timer() as tm:
    sum(range(100000))
print(tm.elapsed < 1)
# 6
class Page:
    def __init__(self, data, size): self.data, self.size = data, size
    def __len__(self): return (len(self.data) + self.size - 1) // self.size
    def __getitem__(self, i):
        if not 0 <= i < len(self): raise IndexError(i)
        return self.data[i * self.size:(i + 1) * self.size]
pg = Page(list(range(7)), 3)
print(len(pg), pg[2], list(pg))   # __getitem__만 있어도 for가 IndexError까지 돈다
```

```text
#식비 Tag('식비') True 1
3 True [3, 2, 1] False
17
Vec(4, 6) Vec(3, 6) Vec(3, 6)
True
3 [6] [[0, 1, 2], [3, 4, 5], [6]]
```

- 6번 설명: `__iter__`가 없으면 파이썬은 `__getitem__`에 0, 1, 2…를 차례로 넣어 보고 `IndexError`가 나면 반복을 끝냅니다. 오래된 반복 프로토콜이 남아 있는 것이며, 직접 만들 때는 `__iter__`를 쓰는 편이 명확합니다.
- 4번에서 `3 * v`가 되려면 `int.__mul__(3, v)`가 `NotImplemented`를 내고, 파이썬이 `v.__rmul__(3)`을 부르기 때문입니다. 이 흐름이 `__radd__`와 같습니다.
- 5번의 `__exit__`가 `False`를 반환하는 것은 “예외를 삼키지 않고 그대로 전파하겠다”는 뜻입니다. `True`를 반환하면 `with` 안의 예외가 사라지므로 신중하게 쓰세요.

## 23장. 데이터클래스 심화

9장에서 `@dataclass`의 기본을 다뤘습니다. 이 장은 실무에서 자주 막히는 부분인 가변 기본값, 불변 객체, 정렬, 검증, 메모리 절약, 대안 도구(NamedTuple, TypedDict)를 정리합니다.

### 핵심 개념

- `@dataclass`는 타입 힌트가 붙은 필드 목록을 보고 `__init__`, `__repr__`, `__eq__`를 자동으로 만듭니다.
- 리스트·dict·set처럼 가변인 기본값은 `field(default_factory=list)`로 줍니다. `= []`라고 쓰면 모든 객체가 같은 리스트를 공유하게 되므로 파이썬이 아예 `ValueError`로 막습니다.
- `frozen=True`는 만든 뒤에 값을 바꿀 수 없게 합니다(`FrozenInstanceError`). `eq`와 함께 쓰면 `__hash__`도 생겨서 dict 키로 쓸 수 있습니다. 금액, 좌표처럼 값 자체인 객체에 적합합니다.
- `order=True`는 `<`, `>` 비교를 만들어 줍니다. 필드가 선언된 순서대로 비교합니다.
- `__post_init__`은 `__init__`이 끝난 직후 자동 호출됩니다. 값 검증과 파생 값 계산에 씁니다.
- `field(init=False)`는 생성자 인자에서 빼고, `InitVar`는 생성자에서만 받고 저장하지 않습니다.
- `slots=True`(3.10+)는 `__dict__` 대신 고정 슬롯을 써서 메모리를 아끼고 오타로 새 속성을 만드는 실수를 막습니다. `kw_only=True`(3.10+)는 모든 인자를 이름을 붙여서만 넘기게 합니다.
- 도구: `asdict`, `astuple`(변환), `replace`(일부만 바꾼 복사본), `fields`(필드 목록).

### 따라 하기

`ch23a.py`: 기본 기능.

```python
from dataclasses import dataclass, field, asdict, astuple, replace, fields, InitVar

@dataclass
class Transaction:
    date: str
    amount: int
    category: str = "기타"
    tags: list[str] = field(default_factory=list)   # 가변 기본값은 반드시 default_factory
    memo: str = ""

t = Transaction("2026-10-29", 12000, "식비")
print(t)                       # __repr__ 자동
print(t == Transaction("2026-10-29", 12000, "식비"))   # __eq__ 자동: 필드 값 비교
print(asdict(t))               # dict로
print(astuple(t))
t2 = replace(t, amount=15000)  # 일부만 바꾼 복사본
print(t2.amount, t.amount)
print([f.name for f in fields(Transaction)])

try:
    @dataclass
    class Bad:
        items: list = []       # 허용되지 않음
except ValueError as e:
    print("ValueError:", e)
```

```text
Transaction(date='2026-10-29', amount=12000, category='식비', tags=[], memo='')
True
{'date': '2026-10-29', 'amount': 12000, 'category': '식비', 'tags': [], 'memo': ''}
('2026-10-29', 12000, '식비', [], '')
15000 12000
['date', 'amount', 'category', 'tags', 'memo']
ValueError: mutable default <class 'list'> for field items is not allowed: use default_factory
```

`ch23b.py`: 불변, 정렬, 검증. `Task`의 `sort_key`는 정렬 기준만 따로 만든 필드입니다. 선언 순서대로 비교하므로 맨 앞에 둡니다.

```python
from dataclasses import dataclass, field

@dataclass(frozen=True, order=True)
class Money:
    amount: int
    currency: str = "KRW"

a, b = Money(100), Money(250)
print(a < b, sorted([b, a]))
try:
    a.amount = 5
except Exception as e:
    print(type(e).__name__)    # FrozenInstanceError
print({a: "키로 쓸 수 있다"})       # frozen + eq → __hash__ 자동 생성

@dataclass(order=True)
class Task:
    sort_key: int = field(init=False, repr=False)   # 비교 기준 필드를 따로 만든다
    name: str = ""
    priority: int = 0
    def __post_init__(self):                         # __init__ 직후에 실행: 검증/파생값
        if self.priority < 0:
            raise ValueError("priority는 0 이상이어야 합니다")
        self.sort_key = -self.priority               # 우선순위 높은 것이 먼저
tasks = [Task("청소", 1), Task("과제", 5), Task("운동", 3)]
print([t.name for t in sorted(tasks)])
try:
    Task("x", -1)
except ValueError as e:
    print("오류:", e)
```

```text
True [Money(amount=100, currency='KRW'), Money(amount=250, currency='KRW')]
FrozenInstanceError
{Money(amount=100, currency='KRW'): '키로 쓸 수 있다'}
['과제', '운동', '청소']
오류: priority는 0 이상이어야 합니다
```

`ch23c.py`: `slots`, `kw_only`, `InitVar`.

```python
from dataclasses import dataclass, field, InitVar

@dataclass(slots=True, kw_only=True)
class Budget:
    category: str
    limit: int
    used: int = 0
    def rate(self) -> float:
        return self.used / self.limit

b = Budget(category="식비", limit=300000, used=120000)
print(b, f"{b.rate():.0%}")
try:
    Budget("식비", 300000)          # kw_only=True: 이름 없이는 못 넘긴다
except TypeError as e:
    print("TypeError:", e)
try:
    b.extra = 1                      # slots=True: 새 속성 금지
except AttributeError as e:
    print("AttributeError")

@dataclass
class User:
    name: str
    password: InitVar[str]           # __init__에만 받고 저장은 안 함
    hashed: str = field(init=False)
    def __post_init__(self, password: str):
        self.hashed = str(hash(password) % 1000)
u = User("안흥", "secret")
print(u.name, hasattr(u, "password"))

@dataclass
class P1: x: int; y: int
@dataclass(slots=True)
class P2: x: int; y: int
print(hasattr(P1(1, 2), "__dict__"), hasattr(P2(1, 2), "__dict__"))
```

```text
Budget(category='식비', limit=300000, used=120000) 40%
TypeError: Budget.__init__() takes 1 positional argument but 3 were given
AttributeError
안흥 False
True False
```

`ch23d.py`: 상속과 대안. 데이터클래스를 상속할 때는 기본값 없는 필드가 기본값 있는 필드보다 앞에 와야 합니다. 대안 선택 기준은 아래 표를 보세요.

```python
from dataclasses import dataclass
from typing import NamedTuple, TypedDict

@dataclass
class Base:
    id: str
    amount: int
@dataclass
class Expense(Base):
    category: str = "기타"      # 기본값 있는 필드는 기본값 없는 필드 뒤에
print(Expense("TX-1", 100, "식비"))

class Point(NamedTuple):         # 불변, 튜플처럼 언패킹 가능
    x: int
    y: int
p = Point(1, 2); x, y = p
print(p, x + y, p._replace(x=10))

class TxDict(TypedDict):         # 타입 검사기만 보는 dict 모양 (실행 중엔 그냥 dict)
    id: str
    amount: int
d: TxDict = {"id": "TX-1", "amount": 100}
print(type(d).__name__, d["amount"])
```

```text
Expense(id='TX-1', amount=100, category='식비')
Point(x=1, y=2) 3 Point(x=10, y=2)
dict 100
```

| 도구 | 바꿀 수 있나 | 메서드 | 언제 |
| --- | --- | --- | --- |
| 일반 클래스 | 예 | 직접 작성 | 동작이 복잡하고 데이터는 부수적일 때 |
| `@dataclass` | 예(`frozen`으로 막기 가능) | 가능 | 데이터 중심 객체(거래, 예산) |
| `NamedTuple` | 아니오 | 가능 | 좌표처럼 작고 불변인 값, 튜플 언패킹이 필요할 때 |
| `TypedDict` | 예 | 없음 | JSON/dict 모양을 타입 검사기에 알려 줄 때 |

### 연습문제

`ex23.py`에 풀어 보세요.

1. `Item(name, price, qty=1)` 데이터클래스에 `total()` 메서드(가격×수량)를 추가하고 `Item("펜", 1200, 3)`을 출력하세요.
2. `Cart` 데이터클래스에 `items: list[Item]`(기본값 빈 리스트)을 두고 `add`, `total`을 만드세요. 카트 두 개가 리스트를 공유하지 않는지 확인하세요.
3. `frozen=True`인 `Coord(lat, lng)`을 만들고 값을 바꾸려 하면 어떤 예외가 나는지 확인한 뒤, `replace`로 lat만 바꾼 새 객체를 만드세요.
4. `Range(lo, hi)`에서 `lo > hi`이면 `__post_init__`이 `ValueError`를 내게 하세요.
5. `order=True`인 `Ver(major, minor=0)`을 만들어 `Ver(1, 10)`, `Ver(1, 2)`, `Ver(0, 9)`를 정렬하고, `asdict`로 dict도 출력하세요.
6. `Tx(id, amount)`에 CSV 한 줄(dict, amount는 문자열)로 만드는 `@classmethod from_row`를 추가하세요. (21장의 대체 생성자입니다.)

힌트: 2번은 `field(default_factory=list)`, 4번은 `raise ValueError(f"...")`, 6번은 `cls(row["id"], int(row["amount"]))`.

### 정답과 해설

```python
# 1
from dataclasses import dataclass, field, asdict, replace
@dataclass
class Item:
    name: str
    price: int
    qty: int = 1
    def total(self): return self.price * self.qty
i = Item("펜", 1200, 3); print(i, i.total())
# 2
@dataclass
class Cart:
    items: list[Item] = field(default_factory=list)
    def add(self, it): self.items.append(it)
    def total(self): return sum(x.total() for x in self.items)
c1, c2 = Cart(), Cart(); c1.add(i); print(c1.total(), c2.items)
# 3
@dataclass(frozen=True)
class Coord:
    lat: float
    lng: float
c = Coord(37.5, 127.0)
try: c.lat = 0
except Exception as e: print(type(e).__name__)
print(replace(c, lat=35.1))
# 4
@dataclass
class Range:
    lo: int
    hi: int
    def __post_init__(self):
        if self.lo > self.hi: raise ValueError(f"lo({self.lo})가 hi({self.hi})보다 큽니다")
try: Range(5, 1)
except ValueError as e: print(e)
# 5
@dataclass(order=True)
class Ver:
    major: int
    minor: int = 0
print(sorted([Ver(1, 10), Ver(1, 2), Ver(0, 9)]))
print(asdict(Ver(2, 1)))
# 6
@dataclass
class Tx:
    id: str
    amount: int
    @classmethod
    def from_row(cls, row: dict): return cls(row["id"], int(row["amount"]))
print(Tx.from_row({"id": "TX-1", "amount": "500"}))
```

```text
Item(name='펜', price=1200, qty=3) 3600
3600 []
FrozenInstanceError
Coord(lat=35.1, lng=127.0)
lo(5)가 hi(1)보다 큽니다
[Ver(major=0, minor=9), Ver(major=1, minor=2), Ver(major=1, minor=10)]
{'major': 2, 'minor': 1}
Tx(id='TX-1', amount=500)
```

- 5번에서 `Ver(1, 2) < Ver(1, 10)`인 이유는 `(major, minor)` 튜플처럼 앞 필드부터 비교하기 때문입니다. 문자열 `"1.2"`와 `"1.10"`을 비교하면 틀리는 문제를 이렇게 피합니다.
- 3번의 `replace`는 `frozen` 객체를 “고치는” 표준 방법입니다. 원본은 그대로이고 새 객체가 나옵니다.

## 24장. 객체 모델: 참조, 가변성, 얕은/깊은 복사

파이썬 버그의 상당수는 “이 변수가 가리키는 객체가 누구와 공유되는가”를 놓쳐서 생깁니다. 이 장은 그 감각을 만듭니다.

### 핵심 개념

- 파이썬의 변수는 값을 담는 상자가 아니라 객체에 붙인 이름표입니다. `b = a`는 객체를 복사하지 않고 이름표를 하나 더 붙입니다.
- `==`는 값이 같은지, `is`는 같은 객체인지 묻습니다. 값 비교는 `==`로 하고, `is`는 `None` 확인(`x is None`)에만 씁니다.
- 불변 객체: `int`, `float`, `str`, `tuple`, `frozenset`, `bytes`. 가변 객체: `list`, `dict`, `set`, 직접 만든 클래스 객체.
- 함수에 가변 객체를 넘기면 함수 안의 수정이 호출한 쪽에도 보입니다. 원본을 보호하려면 함수 안에서 새 객체를 만들어 반환하세요.
- 복사 세 종류: 대입(복사 아님), 얕은 복사(`copy`, `[:]`, `list()`, `dict.copy()`: 바깥만 새로 만들고 안쪽 객체는 공유), 깊은 복사(`copy.deepcopy`: 전부 새로).
- 해시 가능한 것은 대체로 불변 객체이고, dict 키와 set 원소가 될 수 있습니다.
- `x += y`는 리스트에서는 제자리 변경이고, `x = x + y`는 새 객체입니다. 둘의 차이가 `b = a`로 공유 중일 때 드러납니다.
- 객체는 아무도 가리키지 않으면(참조 횟수 0) 사라집니다. `weakref`는 사라지는 걸 막지 않는 참조입니다.

### 따라 하기

`ch24a.py`: 이름표와 가변성.

```python
# 변수는 상자가 아니라 이름표
a = [1, 2, 3]
b = a                  # 같은 리스트에 이름표 하나 더
b.append(4)
print(a, a is b, id(a) == id(b))
c = [1, 2, 3, 4]
print(a == c, a is c)  # 값은 같지만 서로 다른 객체

def add_tag(tags, t):
    tags.append(t)     # 호출자의 리스트가 바뀐다
    return tags
mine = ["식비"]
add_tag(mine, "외식")
print(mine)

# 불변 vs 가변
s = "abc"; s2 = s
s += "d"
print(s, s2)           # 문자열은 불변: += 는 새 객체를 만든다
t = (1, [2, 3])
t[1].append(4)         # 튜플 안의 리스트는 바뀐다
print(t)

# is는 None 비교에만
x = None
print(x is None)
```

```text
[1, 2, 3, 4] True True
True False
['식비', '외식']
abcd abc
(1, [2, 3, 4])
True
```

`ch24b.py`: 복사. 얕은 복사본 안의 `tags`가 원본의 수정에 따라 바뀌는 줄을 눈여겨보세요.

```python
import copy
rows = [{"id": 1, "tags": ["a"]}, {"id": 2, "tags": ["b"]}]

alias = rows                    # 복사가 아님
shallow = rows.copy()           # 얕은 복사: 바깥 리스트만 새로, 안쪽 dict는 공유
deep = copy.deepcopy(rows)      # 깊은 복사: 전부 새로

rows[0]["tags"].append("NEW")
print(shallow[0]["tags"])       # ['a', 'NEW']  ← 공유되어 따라 바뀜
print(deep[0]["tags"])          # ['a']
rows.append({"id": 3})
print(len(alias), len(shallow), len(deep))   # 3 2 2

# 2차원 리스트 함정
bad = [[0] * 3] * 2
bad[0][0] = 9
print(bad)                      # [[9, 0, 0], [9, 0, 0]]
good = [[0] * 3 for _ in range(2)]
good[0][0] = 9
print(good)

# 슬라이스와 list(), dict.copy()도 얕은 복사
orig = [[1], [2]]
cp = orig[:]
cp[0].append(99)
print(orig)
```

```text
['a', 'NEW']
['a']
3 2 2
[[9, 0, 0], [9, 0, 0]]
[[9, 0, 0], [0, 0, 0]]
[[1, 99], [2]]
```

`ch24c.py`: 기본 인자, 해시, 참조 횟수. 첫 줄 `[1, 2] [1, 2]`는 `add(1)`과 `add(2)`가 같은 기본 리스트를 돌려주기 때문에 둘 다 최종 상태로 보이는 것입니다.

```python
def add(x, bucket=[]):
    bucket.append(x); return bucket
print(add(1), add(2))
print(add.__defaults__)

d = {(1, 2): "튜플은 가능"}
try:
    d[[1, 2]] = "x"
except TypeError as e:
    print("TypeError:", e)

n1, n2 = 10 ** 6, 10 ** 6
print(n1 == n2)                 # True: 값 비교는 항상 이것을 쓴다

import sys, weakref
class Node: pass
o = Node()
print(sys.getrefcount(o) >= 2)
w = weakref.ref(o)
print(w() is o)
del o
print(w())                      # None: 더 이상 아무도 붙잡지 않아 사라짐
```

```text
[1, 2] [1, 2]
([1, 2],)
TypeError: unhashable type: 'list'
True
True
True
None
```

### 연습문제

`ex24.py`에 풀어 보세요.

1. `a = [1, 2]; b = a; b.append(3)` 뒤에 `a`와 `a is b`를 예상하고 확인하세요.
2. 호출할 때마다 새 리스트를 만드는 `append_to(x, lst=None)`을 작성해 `append_to(1)`, `append_to(2)`가 `[1]`, `[2]`가 나오게 하세요.
3. `cfg = {"db": {"host": "x"}, "tags": ["a"]}`를 `cfg.copy()`와 `copy.deepcopy(cfg)`로 복사한 뒤 `cfg["db"]["host"] = "y"`를 하면 각 복사본의 host는 무엇일까요?
4. 2×2 격자를 안전하게 만들고 `grid[0][1] = 5`로 한 칸만 바꾸세요.
5. 튜플의 요소를 바꾸려 하면 어떤 예외가 나는지 확인하고, 같은 값 튜플의 `hash`가 같은지 비교하세요.
6. 입력 리스트를 바꾸지 않고 각 요소에 `"!"`를 붙인 새 리스트를 반환하는 `tag_all(items)`를 작성하세요.
7. `x = [1,2,3]; y = x; x = x + [4]`와 `x2 = [1,2,3]; y2 = x2; x2 += [4]`에서 각각 `y`, `y2`는 어떻게 될까요?

힌트: 3번은 얕은 복사가 안쪽 dict를 공유하는지, 7번은 `+`가 새 객체를 만드는지 `+=`가 제자리 변경인지 생각하세요.

### 정답과 해설

```python
# 1
a = [1, 2]; b = a; b.append(3); print(a, a is b)
# 2
def append_to(x, lst=None):
    if lst is None: lst = []
    lst.append(x); return lst
print(append_to(1), append_to(2))
# 3
import copy
cfg = {"db": {"host": "x"}, "tags": ["a"]}
s = cfg.copy(); d = copy.deepcopy(cfg)
cfg["db"]["host"] = "y"
print(s["db"]["host"], d["db"]["host"])
# 4
grid = [[0] * 2 for _ in range(2)]; grid[0][1] = 5; print(grid)
# 5
t = (1, 2)
try: t[0] = 9
except TypeError as e: print("TypeError")
print(hash(t) == hash((1, 2)))
# 6
def tag_all(items):
    return [i + "!" for i in items]        # 원본을 바꾸지 않고 새 리스트
src = ["a", "b"]; out = tag_all(src); print(src, out)
# 7
x = [1, 2, 3]
y = x
x = x + [4]       # + 는 새 리스트
print(x, y)
x2 = [1, 2, 3]; y2 = x2
x2 += [4]         # += 는 제자리 변경
print(x2, y2)
```

```text
[1, 2, 3] True
[1] [2]
y x
[[0, 5], [0, 0]]
TypeError
True
['a', 'b'] ['a!', 'b!']
[1, 2, 3, 4] [1, 2, 3]
[1, 2, 3, 4] [1, 2, 3, 4]
```

- 3번: 얕은 복사본 `s`의 host가 `y`로 바뀝니다(안쪽 dict를 공유). 깊은 복사본 `d`는 `x`로 그대로입니다.
- 7번: `x = x + [4]`는 `x`가 새 리스트를 가리키게 하므로 `y`는 그대로입니다. `x2 += [4]`는 같은 리스트를 바꾸므로 `y2`도 따라 바뀝니다. 같은 모양의 코드가 다르게 동작하는 대표적인 예입니다.
- 2번의 `None` 기본값 패턴은 5장의 함정 해결법과 같은 것입니다.

## 부록

### A. 자주 만나는 오류 사전

오류는 맨 아래 줄의 종류를 먼저 봅니다. 메시지 문구는 파이썬 버전에 따라 약간 다를 수 있습니다.

| 오류 종류 | 흔한 원인 | 확인할 것 |
| --- | --- | --- |
| `SyntaxError` | 괄호·따옴표·콜론(`:`) 빠짐 | 오류가 가리키는 줄과 그 바로 위 줄 |
| `IndentationError` | 들여쓰기 불일치, 탭과 스페이스 혼용 | 한 블록은 스페이스 4칸으로 통일 |
| `NameError` | 정의 전에 사용, 오타 | 변수·함수 이름 철자, 위치 |
| `TypeError` | 타입이 다른 값을 섮음, `None`에 연산, 인자 개수 불일치 | 값의 실제 타입 `print(type(x), repr(x))` |
| `ValueError` | 타입은 맞지만 값이 부적절(`int("abc")`) | 입력값 자체 |
| `KeyError` | 딕셔너리에 없는 키 | `d.get(key)` 또는 `key in d`로 사전 확인 |
| `IndexError` | 리스트 범위 밖 인덱스, 빈 리스트 `[0]` | `len()`을 먼저 찍어 보기 |
| `AttributeError` | `None` 또는 다른 타입의 객체에 없는 속성 사용 | 함수가 `None`을 돌려줬는지(`return` 빠짐) |
| `ZeroDivisionError` | 0으로 나눔 | 분모(예산)가 0인 경우 처리 |
| `FileNotFoundError` | 경로 오타, 실행 위치 차이 | 상대 경로는 실행한 폴더 기준. `Path.cwd()` 출력 |
| `UnicodeDecodeError` | 인코딩 불일치(Windows 기본값 등) | `open(..., encoding="utf-8")` 명시 |
| `json.JSONDecodeError` | JSON 형식 오류, 빈 줄, 끝 콤마 | 오류가 나는 줄 번호와 그 줄 내용 |
| `ModuleNotFoundError` | 모듈 이름 오타, 패키지 미설치, 실행 위치 | `pylab` 폴더에서 `python -m budget_app`로 실행했는지 |
| `ImportError: attempted relative import...` | 패키지 안 파일을 `python 파일.py`로 직접 실행 | `python -m 패키지.모듈`로 실행 (10장) |
| `unrecognized arguments` | 공백 있는 값을 따옴표 없이 입력 | `--memo "저녁 치킨"` |

### B. 문법 치트시트

```python
# 자료형
x = 3; y = 3.0; s = "hi"; ok = True; nothing = None
xs = [1, 2]; t = (1, 2); d = {"a": 1}; st = {1, 2}

# 문자열
f"{n:,}"  f"{x:.1f}"  f"{s:<8}"  f"{n:>10,}"  f"{n:06d}"
s.strip()  s.split(",")  ",".join(xs)  s.replace(a, b)  s.startswith(a)

# 제어문
if a: ... elif b: ... else: ...
for i, v in enumerate(xs, start=1): ...
while cond: ...      # break, continue

# 컨테이너
xs.append(v)  xs.sort(key=...)  sorted(xs, key=lambda v: v, reverse=True)
d.get(k, 0)  d.items()  d.setdefault(k, [])
[f(v) for v in xs if cond]   {k: v for ...}   (v for v in xs)   # 마지막은 제너레이터 표현식

# 함수는 타입 힌트와 함께
def f(a: int, b: str = "x", *args: int, **kw: str) -> int | None: ...

# 예외
try: ...
except (ValueError, KeyError) as e: ...
else: ...
finally: ...
raise MyError("원인", "힌트") from None

# 클래스
@dataclass
class A:
    x: int
    tags: list[str] = field(default_factory=list)

# 제너레이터·데코레이터·컨텍스트 매니저
def gen(): yield 1
def deco(fn):
    @functools.wraps(fn)
    def wrapper(*a, **k): return fn(*a, **k)
    return wrapper
@contextmanager
def cm(): yield

# 파일
with open(p, encoding="utf-8") as f: ...
Path(p).read_text(encoding="utf-8")
json.dumps(obj, ensure_ascii=False)
csv.writer(f)    # open(..., newline="")
```

### C. 추천 교재와 읽는 순서

이 가이드만으로도 미션을 할 수 있게 만들었지만, 더 깊이 파고 싶을 때는 아래 순서를 추천합니다. 아래는 일반적으로 알려진 성격에 대한 설명이며, 책마다 판본에 따라 장 구성이 다를 수 있어 장 번호는 적지 않았습니다.

| 순서 | 자료 | 언제 읽는가 |
| --- | --- | --- |
| 1 | 이 가이드 1\~10장 | 파이썬을 처음 배울 때 |
| 2 | 입문용 한국어 파이썬 책이나 공식 튜토리얼(docs.python.org) | 문법을 다시 정리하고 싶을 때 |
| 3 | 이 가이드 11\~16장 | 미션의 핵심(제너레이터·데코레이터·타입 힌트)을 한 번 익힌 뒤 |
| 4 | 파이썬 코딩의 기술 (Effective Python) | 자주 쓰는 관용구와 좋은 습관을 항목 단위로 익히고 싶을 때 |
| 5 | 전문가를 위한 파이썬 (Fluent Python) | 데이터 모델, 제너레이터, 데코레이터를 깊이 이해하고 싶을 때(초보자에게는 다소 단단함) |

학습이 문제를 푸는 데서 끝나지 않고 내 코드를 남에게 설명하는 단계까지 가야 실력이 고정됩니다. 그래서 마지막 연습을 20장의 시연으로 두었습니다.
