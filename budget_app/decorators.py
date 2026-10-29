"""Reusable decorators for command execution."""
import os
from functools import wraps
from time import perf_counter
from typing import Callable, TypeVar, Any

# F는 함수 타입을 나타내는 타입 변수다. 데코레이터가 함수 형태를 최대한 보존함을 표시한다.
F = TypeVar("F", bound=Callable[..., Any])


# @timed("명령 실행")처럼 라벨을 먼저 받는 매개변수형 데코레이터다.
def timed(label: str) -> Callable[[F], F]:
    """Optionally print elapsed time when BUDGET_APP_SHOW_TIMING=1."""
    # decorate는 실제로 감쌀 원본 함수를 받는다.
    def decorate(function: F) -> F:
        # wraps는 wrapper가 원본 함수의 이름/문서 등 메타데이터를 보존하게 돕는다.
        @wraps(function)
        # *args/**kwargs로 원본 함수가 받던 위치/키워드 인수를 그대로 전달한다.
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            started = perf_counter()
            # 먼저 원본 함수를 실행하고, 그 반환값을 보관한다.
            result = function(*args, **kwargs)
            # 환경 변수가 1일 때만 시간 정보를 출력해 기본 화면은 조용히 유지한다.
            if os.environ.get("BUDGET_APP_SHOW_TIMING") == "1":
                elapsed = perf_counter() - started
                print(f"[실행 시간] {label}: {elapsed:.4f}초")
            return result
        return wrapper  # type: ignore[return-value]
    return decorate
