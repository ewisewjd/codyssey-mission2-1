"""Allow running the app with: python -m budget_app."""
import sys

from .cli import main


# python -m budget_app로 실행했을 때만 main을 호출한다.
# main의 정수 반환값을 프로세스 종료 코드로 전달한다.
if __name__ == "__main__":
    raise SystemExit(main())
