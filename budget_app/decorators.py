"""Reusable decorators for command execution."""
import os
from functools import wraps
from time import perf_counter
from typing import Callable, TypeVar, Any

F = TypeVar("F", bound=Callable[..., Any])


def timed(label: str) -> Callable[[F], F]:
    """Optionally print elapsed time when BUDGET_APP_SHOW_TIMING=1."""
    def decorate(function: F) -> F:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            started = perf_counter()
            result = function(*args, **kwargs)
            if os.environ.get("BUDGET_APP_SHOW_TIMING") == "1":
                elapsed = perf_counter() - started
                print(f"[실행 시간] {label}: {elapsed:.4f}초")
            return result
        return wrapper  # type: ignore[return-value]
    return decorate
