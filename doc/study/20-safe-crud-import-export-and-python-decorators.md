# 20. 코드 해설: 안전한 수정·삭제·CSV 입출력과 Python 장식 문법

이 문서는 Mission 2-1의 실제 구현을 읽고 동료평가에서 설명할 수 있도록 정리한 자료다. 소스 코드의 실행 로직은 바꾸지 않고, 주요 함수에 설명 주석을 추가했다.

## 1. 먼저 전체 흐름 보기

```text
사용자 명령
  ↓
cli.py: argparse로 명령/옵션 해석
  ↓
cli.py: run()이 명령 분기
  ↓
service.py: 업무 규칙·검증·수정할 데이터 구성
  ↓
storage.py: JSONL 파일 읽기/쓰기
  ↓
main()의 종료 코드 → __main__.py의 SystemExit
```

- `cli.py`: 입력과 출력, 명령 선택
- `service.py`: 거래 규칙, CRUD, CSV 변환
- `storage.py`: 저장 파일을 읽고 쓰는 책임
- `models.py`: Transaction 데이터 형태와 검증
- `decorators.py`: 실행 시간 같은 공통 기능

## 2. Update: 거래 수정은 어떻게 안전하게 처리하나?

관련 코드: `budget_app/service.py`의 `BudgetService.update()`, `budget_app/storage.py`의 `replace_transactions()`와 `_atomic_write()`.

1. 수정할 필드가 하나 이상인지, 허용된 필드인지 확인한다.
2. 기존 거래를 하나씩 읽는다.
3. ID가 일치하는 거래의 새 값을 구성한다. 지정하지 않은 필드는 기존 값을 유지한다.
4. 날짜·유형·금액·카테고리를 검증하고, 카테고리가 실제 등록되어 있는지 확인한다.
5. 대상 ID를 찾지 못하면 오류를 발생시킨다.
6. 모든 검증을 통과하고 대상을 찾은 경우에만 새 거래 목록을 저장소에 전달한다.
7. 저장소는 원본 파일을 직접 비우지 않는다. 같은 폴더에 임시 파일을 만들고 새 JSONL 전체를 쓴 뒤 `os.replace()`로 최종 파일과 교체한다.

**왜 이렇게 하나?** 검증이 중간에 실패했을 때 원본 파일을 이미 수정한 상태가 되지 않게 하기 위해서다. 다만 수정 대상과 남길 거래를 `list`에 모으므로, 파일 크기만큼 메모리를 사용한다.

## 3. Delete: 삭제도 파일을 직접 편집하지 않는다

관련 코드: `BudgetService.delete()`.

1. 전체 거래를 읽으면서 삭제 대상 ID와 일치하는 거래는 새 목록에 넣지 않는다.
2. 나머지 거래만 새 목록에 모은다.
3. 대상 ID가 없으면 오류를 내고 저장하지 않는다.
4. 대상이 확인되면 `replace_transactions()` → `_atomic_write()`로 새 파일을 만든 뒤 교체한다.

즉, 삭제는 파일 중간의 한 줄을 물리적으로 지우는 작업이 아니라 **삭제 대상만 제외한 새 파일을 만들어 바꾸는 작업**이다.

## 4. `_atomic_write()`: 임시 파일을 쓰는 이유

관련 코드: `budget_app/storage.py`.

- `NamedTemporaryFile(..., dir=path.parent, delete=False)`: 목적 파일과 같은 폴더에 임시 파일을 만든다. 같은 파일 시스템에 두면 교체 작업에 유리하다.
- `json.dumps(...)+"\\n"`: 각 레코드를 JSON 한 줄로 기록한다.
- `flush()`: Python 파일 버퍼에 남은 데이터를 운영체제로 보낸다.
- `os.fsync(file.fileno())`: 가능한 범위에서 파일 데이터를 저장 장치에 기록하도록 요청한다.
- 파일을 닫은 뒤 `os.replace(temp_name, path)`: 완성된 임시 파일을 최종 경로로 교체한다.
- `finally`: 교체 전에 오류가 발생해 임시 파일이 남았다면 정리한다.

**보장 범위도 정확히 설명하자.** 원본을 직접 덮어쓰다가 중간 실패로 파일이 비거나 일부만 기록되는 위험을 줄인다. 하지만 이것만으로 동시 실행하는 두 프로세스의 수정 충돌까지 해결하지는 않는다. 파일 잠금이나 충돌 감지는 별도 구현이 필요하다.

## 5. CSV Export: 기존 출력 파일을 어떻게 보호하나?

관련 코드: `BudgetService.export_csv()`.

1. `--month` 또는 `--from`과 `--to`가 함께 지정됐는지 먼저 확인한다.
2. 월/날짜 형식과 시작일·종료일 순서를 검증한다.
3. 검증이 끝난 뒤 결과를 임시 CSV 파일에 쓴다.
4. 헤더와 데이터 행을 모두 기록하고 `flush()`, `fsync()`를 실행한다.
5. 쓰기가 끝나면 `os.replace()`로 목적 파일을 교체한다.
6. 실패하면 `finally`에서 임시 파일을 정리한다.

특히 날짜 필터 검증을 파일 열기 전에 하는 것이 중요하다. `filtered()`는 제너레이터이므로 함수 호출 시점이 아니라 실제로 순회할 때 검증 코드가 실행된다. 검증을 제너레이터 안에만 두고 목적 파일부터 열면, 잘못된 날짜를 발견하기 전에 기존 출력 파일을 건드릴 위험이 있다.

## 6. CSV Import: 행 단위 검증과 부분 성공

관련 코드: `BudgetService.import_csv()`.

1. `utf-8-sig`로 열어 UTF-8 BOM이 있는 CSV도 읽을 수 있게 한다.
2. `csv.DictReader`가 헤더를 기준으로 각 행을 딕셔너리처럼 제공한다.
3. 필수 헤더 `date,type,category,amount`가 있는지 확인한다.
4. 각 행의 금액을 양의 정수로 검사하고 태그 문자열을 쉼표 기준 리스트로 바꾼다.
5. 각 행을 `self.add()`에 전달해 일반 거래 추가와 같은 검증을 재사용한다.
6. 성공한 행은 imported를 증가시킨다. `ValueError`나 `TypeError`가 난 행은 skipped와 오류 메시지를 기록하고 다음 행을 계속 처리한다.
7. 건너뛴 행이 있으면 CLI가 종료 코드 1을 반환한다.

**중요한 한계:** 이 import는 전체 CSV를 하나의 트랜잭션처럼 처리하지 않는다. 앞 행에서 유효한 거래가 저장된 뒤 뒤쪽 행이 실패하면, 앞서 저장된 거래는 그대로 남는다. 즉, “행 단위 부분 성공” 정책이다. 잘못된 행이 하나라도 있으면 전부 되돌리는 all-or-nothing 방식은 아니다.

## 7. `@dataclass`: 거래 데이터 틀을 간단히 선언하기

관련 코드: `budget_app/models.py`.

```python
@dataclass
class Transaction:
    id: str
    type: str
    date: str
    amount: int
    category: str
    memo: str = ""
    tags: list[str] = field(default_factory=list)
```

- 클래스는 데이터와 동작을 묶는 설계도, 인스턴스는 그 설계도로 만든 개별 객체다.
- `@dataclass`는 필드 선언을 보고 `__init__()`와 `__repr__()` 같은 반복 코드를 자동 생성한다.
- `memo: str = ""`는 생략했을 때 빈 문자열을 기본값으로 쓴다.
- `field(default_factory=list)`는 각 Transaction마다 새 리스트를 만든다. `tags=[]`를 모든 인스턴스의 기본 리스트로 공유하는 문제를 피한다.
- `amount: int`는 타입 힌트일 뿐, 잘못된 값을 자동으로 막는 검증기는 아니다. 그래서 별도 검증 함수가 필요하다.

## 8. `@staticmethod`: 왜 self가 없나?

관련 코드: `budget_app/storage.py`의 `append_json()`, `iter_json()`, `_atomic_write()`.

일반 인스턴스 메서드는 첫 매개변수 `self`를 통해 특정 객체의 상태에 접근한다. 반면 이 정적 메서드들은 `self.data_dir` 같은 인스턴스 상태를 사용하지 않고, 전달받은 경로와 데이터만 처리한다. 그래서 `@staticmethod`로 표시할 수 있다.

```python
JsonlStore.append_json(path, data)
```

이 호출에서는 Python이 `self`를 자동으로 끼워 넣지 않는다. 반대로 `@staticmethod`가 없는 일반 인스턴스 메서드는 보통 `store.method(...)`로 호출하며, `store` 객체가 `self`로 전달된다.

## 9. `@classmethod`와 `@staticmethod`는 다르다

관련 코드: `Transaction.from_dict()`.

- `@classmethod`: 첫 인수로 클래스 `cls`를 자동으로 받는다. 여기서는 `cls(...)`로 Transaction 객체를 만든다. 상속받은 하위 클래스에서 호출해도 해당 클래스의 객체를 만들 수 있다는 장점이 있다.
- `@staticmethod`: `self`도 `cls`도 자동으로 받지 않는다. 전달받은 인수만으로 동작한다.
- `@dataclass`: 클래스 선언을 바탕으로 데이터 보관용 반복 메서드를 생성한다.

세 가지는 모두 `@` 문법을 사용하지만 역할이 서로 다르다.

## 10. `@timed`: 매개변수가 있는 데코레이터

관련 코드: `budget_app/decorators.py`, `budget_app/cli.py`.

```python
@timed("명령 실행")
def run(args):
    ...
```

개념적으로 `run = timed("명령 실행")(run)`과 비슷하다.

- `timed("명령 실행")`: 표시할 라벨을 받아 실제 데코레이터를 돌려준다.
- `decorate(function)`: 원래 함수를 받아 감쌀 준비를 한다.
- `wrapper(*args, **kwargs)`: 원래 인수를 그대로 전달해 함수를 실행한다.
- `@wraps(function)`: wrapper가 원래 함수의 이름·문서 등 메타데이터를 보존하도록 돕는다.
- 반환값은 `result`에 담아 그대로 돌려준다.
- 환경 변수 `BUDGET_APP_SHOW_TIMING=1`일 때만 실행 시간을 출력한다.

현재 구현에서는 원래 함수가 예외를 발생시키면 시간 출력 줄까지 도달하지 않는다. 항상 예외 발생 여부와 관계없이 시간을 출력하려면 `try/finally` 같은 별도 설계가 필요하다.

## 11. 제너레이터, 타입 힌트, 종료 코드

- `yield`: 값을 한 번에 전부 만들지 않고 하나씩 제공한다. `iter_json()`과 `iter_transactions()`가 이 방식을 사용한다.
- `Iterator[Transaction]`: Transaction 객체를 하나씩 제공하는 반복 가능한 흐름임을 나타내는 타입 힌트다. 타입 힌트만으로 실행 시 검증이 되지는 않는다.
- `return 0`: 일반적으로 명령이 성공했다는 뜻이다.
- `return 1`: 앱이 오류 또는 부분 실패를 보고한다.
- `raise SystemExit(main())`: `main()`이 반환한 정수를 프로세스 종료 코드로 전달한다.
- `except`: 예상한 오류를 사용자 메시지로 바꾸어 처리한다. 모든 예외를 무조건 잡으면 실제 버그를 감출 수 있다.

## 12. 동료평가용 30초 설명

> 거래 수정과 삭제는 원본 JSONL 파일을 직접 편집하지 않습니다. 서비스 계층에서 거래를 읽고 수정하거나 삭제한 새 목록을 만든 다음, 저장소 계층이 같은 폴더에 임시 파일을 완성하고 `os.replace`로 교체합니다. 그래서 쓰기 도중 실패했을 때 원본이 부분적으로 덮어써질 위험을 줄입니다. CSV export도 날짜 조건을 먼저 검증하고 임시 파일을 완성한 후 교체합니다. CSV import는 각 행을 검증해 유효한 행은 저장하고 잘못된 행은 건너뛰므로, 현재 구현은 전체 롤백이 아니라 부분 성공 방식입니다. 다만 임시 파일 교체만으로 동시 수정 충돌까지 해결되는 것은 아닙니다.

## 13. 스스로 설명해 보기

1. 수정할 ID가 없을 때 왜 파일 교체를 실행하지 않을까?
2. 임시 파일을 원본과 같은 폴더에 만드는 이유는 무엇일까?
3. `os.replace()` 직전에 오류가 나면 원본 파일은 어떤 상태일까?
4. CSV import에서 5번째 행이 잘못되면 앞서 성공한 1~4번째 행은 어떻게 될까?
5. `@dataclass`, `@classmethod`, `@staticmethod`는 각각 무엇을 하는가?
6. `@timed("명령 실행")`은 왜 매개변수를 받는 데코레이터인가?
7. 이 구현이 해결하지 못하는 동시 실행 문제는 무엇인가?
