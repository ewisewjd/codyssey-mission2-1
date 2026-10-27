# 09. 클래스, dataclass, 타입 힌트

## 공부할 개념
- 클래스와 인스턴스
- 속성과 메서드, `self`, `__init__`
- `@dataclass`
- 타입 힌트: `str`, `int`, `list[str]`, `dict`, `str | None`
- 반환 타입과 선택 필드
- 타입 힌트는 런타임 입력을 자동 검증하지 않는다는 점
- 데이터 검증과 타입 힌트의 차이
- 객체와 JSON 자료형 사이 변환

## 미션 적용
- Transaction dataclass
- 최소 두 개 이상의 클래스
- 함수 계약을 타입 힌트로 표현
- amount가 int로 표기되어도 입력 검증을 별도로 수행

## 확인 과제
Transaction을 만들고 잘못된 amount가 들어왔을 때 타입 힌트만으로 막히는지 직접 확인한다.
