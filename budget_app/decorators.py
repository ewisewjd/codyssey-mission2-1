"""Reusable decorators for command execution."""
from functools import wraps
from time import perf_counter
from typing import Callable, TypeVar, Any

F = TypeVar("F", bound=Callable[..., Any])


def timed(label: str) -> Callable[[F], F]:
    """Print elapsed time after a successful operation."""
    def decorate(function: F) -> F:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            started = perf_counter()
            result = function(*args, **kwargs)
            elapsed = perf_counter() - started
            print(f"[실행 시간] {label}: {elapsed:.4f}초")
            return result
        return wrapper  # type: ignore[return-value]
    return decorate
