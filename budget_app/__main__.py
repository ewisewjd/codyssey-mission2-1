"""Allow running the app with: python -m budget_app."""
import sys

from .cli import main


if __name__ == "__main__":
    raise SystemExit(main())
