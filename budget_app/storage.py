"""JSONL persistence. Read operations iterate line-by-line."""
import json
import os
import tempfile
from pathlib import Path
from typing import Any, Iterator

from .models import Transaction


DEFAULT_CATEGORIES = ["food", "transport", "rent", "salary", "shopping", "health", "etc"]


# 저장소(Repository): JSONL 파일을 읽고 쓰는 책임을 CLI/서비스에서 분리한다.
class JsonlStore:
    def __init__(self, data_dir: str = "data") -> None:
        self.data_dir = Path(data_dir)
        self.transactions_path = self.data_dir / "transactions.jsonl"
        self.categories_path = self.data_dir / "categories.jsonl"
        self.budgets_path = self.data_dir / "budgets.jsonl"
        # Keep a high-water mark so deleting the latest transaction cannot recycle its ID.
        self.transaction_sequence_path = self.data_dir / "transaction_sequence.json"
        self.ensure_files()

    # 데이터 폴더와 필수 파일이 없으면 만들고, 카테고리 파일이 비어 있으면 기본값을 채운다.
    def ensure_files(self) -> None:
        self.data_dir.mkdir(parents=True, exist_ok=True)
        for path in (self.transactions_path, self.categories_path, self.budgets_path):
            if not path.exists():
                path.touch()
        if self.categories_path.stat().st_size == 0:
            for name in DEFAULT_CATEGORIES:
                self.append_json(self.categories_path, {"name": name})

    # 인스턴스의 self를 쓰지 않는 파일 유틸리티이므로 @staticmethod로 선언한다.
    @staticmethod
    def append_json(path: Path, data: dict[str, Any]) -> None:
        with path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(data, ensure_ascii=False) + "\n")

    # 파일을 한 번에 통째로 읽지 않고 한 줄씩 JSON 객체로 바꾸어 제공한다(yield).
    # 경로만 사용하고 self 상태에는 의존하지 않아 정적 메서드로 둔다.
    @staticmethod
    def iter_json(path: Path) -> Iterator[dict[str, Any]]:
        if not path.exists():
            return
        with path.open("r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue
                try:
                    yield json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"{path}의 {line_number}번째 줄이 올바른 JSON이 아닙니다. 파일을 확인하세요.") from exc

    def iter_transactions(self) -> Iterator[Transaction]:
        for row in self.iter_json(self.transactions_path):
            try:
                yield Transaction.from_dict(row)
            except (KeyError, TypeError, ValueError) as exc:
                raise ValueError(f"거래 데이터 형식이 잘못되었습니다: {exc}") from exc

    def categories(self) -> list[str]:
        return [str(row["name"]) for row in self.iter_json(self.categories_path) if row.get("name")]

    def budgets(self) -> dict[str, int]:
        result: dict[str, int] = {}
        for row in self.iter_json(self.budgets_path):
            if row.get("month") is not None:
                result[str(row["month"])] = int(row["amount"])
        return result

    # 마지막으로 예약한 번호를 별도 파일에 보관해, 최신 거래 삭제 후에도 ID를 재사용하지 않는다.
    def next_transaction_id(self) -> str:
        """Reserve and persist the next ID before returning it."""
        if self.transaction_sequence_path.exists():
            try:
                state = json.loads(self.transaction_sequence_path.read_text(encoding="utf-8"))
                highest = int(state["last_id"])
            except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
                raise ValueError(
                    f"{self.transaction_sequence_path}의 ID 기록이 손상되었습니다. 파일을 확인하세요."
                ) from exc
        else:
            # Upgrade existing data directories that predate the sequence file.
            highest = 0
            for transaction in self.iter_transactions():
                try:
                    highest = max(highest, int(transaction.id.removeprefix("TX-")))
                except ValueError:
                    continue

        next_number = highest + 1
        self._atomic_write(
            self.transaction_sequence_path,
            iter([{"last_id": next_number}]),
        )
        return f"TX-{next_number:06d}"

    def add_transaction(self, transaction: Transaction) -> None:
        self.append_json(self.transactions_path, transaction.to_dict())

    def replace_transactions(self, transactions: Iterator[Transaction]) -> None:
        self._atomic_write(self.transactions_path, (item.to_dict() for item in transactions))

    def add_category(self, name: str) -> None:
        self.append_json(self.categories_path, {"name": name})

    def replace_categories(self, categories: list[str]) -> None:
        self._atomic_write(self.categories_path, ({"name": name} for name in categories))

    def set_budget(self, month: str, amount: int) -> None:
        budgets = self.budgets()
        budgets[month] = amount
        self._atomic_write(self.budgets_path, ({"month": m, "amount": a} for m, a in sorted(budgets.items())))

    # 원본을 바로 덮어쓰지 않고 같은 폴더의 임시 파일을 완성한 다음 교체한다.
    # self 상태를 쓰지 않는 공통 쓰기 도구라 @staticmethod로 선언한다.
    @staticmethod
    def _atomic_write(path: Path, rows: Iterator[dict[str, Any]]) -> None:
        temp_name: str | None = None
        try:
            with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as file:
                temp_name = file.name
                for row in rows:
                    file.write(json.dumps(row, ensure_ascii=False) + "\n")
                file.flush()  # Python 버퍼에 남은 내용을 운영체제로 밀어낸다.
                os.fsync(file.fileno())  # 가능한 범위에서 저장 장치에 기록되도록 요청한다.
            os.replace(temp_name, path)  # 같은 파일 시스템 안에서 완성된 파일로 교체한다.
            temp_name = None
        finally:
            # Clean up after any failure, not only OSError.
            if temp_name and os.path.exists(temp_name):
                os.unlink(temp_name)
