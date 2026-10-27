"""Data models and validation for the budget ledger."""
from dataclasses import asdict, dataclass, field
from datetime import date
from typing import Any


@dataclass
class Transaction:
    id: str
    type: str
    date: str
    amount: int
    category: str
    memo: str = ""
    tags: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Transaction":
        return cls(
            id=str(data["id"]),
            type=str(data["type"]),
            date=str(data["date"]),
            amount=int(data["amount"]),
            category=str(data["category"]),
            memo=str(data.get("memo", "")),
            tags=[str(tag) for tag in data.get("tags", [])],
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def validate_date(value: str) -> str:
    try:
        parsed = date.fromisoformat(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 입력하세요. 예: 2026-10-27") from exc
    if parsed.isoformat() != value:
        raise ValueError("날짜는 YYYY-MM-DD 형식이어야 합니다. 예: 2026-10-27")
    return value


def validate_month(value: str) -> str:
    try:
        year_text, month_text = value.split("-")
        year, month = int(year_text), int(month_text)
        if len(year_text) != 4 or len(month_text) != 2 or not 1 <= month <= 12:
            raise ValueError
    except (ValueError, AttributeError) as exc:
        raise ValueError("월은 YYYY-MM 형식이어야 합니다. 예: 2026-10") from exc
    return f"{year:04d}-{month:02d}"


def validate_transaction_fields(
    transaction_type: str, transaction_date: str, amount: int, category: str
) -> None:
    if transaction_type not in {"income", "expense"}:
        raise ValueError("타입은 income 또는 expense만 가능합니다.")
    validate_date(transaction_date)
    if isinstance(amount, bool) or amount <= 0:
        raise ValueError("금액은 0보다 큰 정수여야 합니다.")
    if not category.strip():
        raise ValueError("카테고리를 입력하세요.")
