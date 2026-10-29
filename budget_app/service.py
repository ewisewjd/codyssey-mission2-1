"""Business rules for transactions, categories, budgets and CSV."""
import calendar
import csv
import heapq
import os
import tempfile
from collections import Counter
from pathlib import Path
from typing import Iterator

from .models import Transaction, validate_date, validate_month, validate_transaction_fields
from .storage import JsonlStore


# 업무 규칙 계층: 입력 검증, 거래 규칙, CSV 정책을 저장소 세부 구현과 분리한다.
class BudgetService:
    def __init__(self, store: JsonlStore) -> None:
        self.store = store

    def add(self, transaction_type: str, transaction_date: str, amount: int, category: str,
            memo: str = "", tags: list[str] | None = None) -> Transaction:
        validate_transaction_fields(transaction_type, transaction_date, amount, category)
        if category not in self.store.categories():
            raise ValueError(f"등록되지 않은 카테고리입니다: {category}. 'category add'로 먼저 등록하세요.")
        transaction = Transaction(
            id=self.store.next_transaction_id(), type=transaction_type, date=transaction_date,
            amount=amount, category=category, memo=memo.strip(), tags=tags or []
        )
        self.store.add_transaction(transaction)
        return transaction

    def filtered(self, start: str | None = None, end: str | None = None,
                 category: str | None = None, transaction_type: str | None = None,
                 query: str | None = None, tag: str | None = None) -> Iterator[Transaction]:
        # Validate before reading any records so invalid filters fail immediately.
        if start:
            validate_date(start)
        if end:
            validate_date(end)
        if start and end and start > end:
            raise ValueError("--from 날짜는 --to 날짜보다 늦을 수 없습니다.")
        if transaction_type and transaction_type not in {"income", "expense"}:
            raise ValueError("--type은 income 또는 expense여야 합니다.")
        if category and category not in self.store.categories():
            raise ValueError(f"등록되지 않은 카테고리입니다: {category}")
        for item in self.store.iter_transactions():
            if start and item.date < start:
                continue
            if end and item.date > end:
                continue
            if category and item.category != category:
                continue
            if transaction_type and item.type != transaction_type:
                continue
            if query and query.casefold() not in item.memo.casefold():
                continue
            if tag and tag not in item.tags:
                continue
            yield item

    def list_transactions(self, limit: int = 20) -> list[Transaction]:
        if limit < 1:
            raise ValueError("--limit은 1 이상의 정수여야 합니다.")
        # nlargest iterates over the generator and retains only the newest `limit` records.
        return heapq.nlargest(
            limit,
            self.store.iter_transactions(),
            key=lambda item: (item.date, item.id),
        )

    def search(self, **filters: str | None) -> list[Transaction]:
        # Sorting newest-first requires retaining all matches in memory.
        return sorted(self.filtered(**filters), key=lambda item: (item.date, item.id), reverse=True)

    # 수정할 거래만 바꾼 새 목록을 만든 뒤, 전체 파일을 안전 교체한다.
    # 검증 중 오류가 나면 replace_transactions까지 도달하지 않으므로 원본 파일을 건드리지 않는다.
    def update(self, transaction_id: str, **changes: object) -> Transaction:
        allowed = {"date", "type", "amount", "category", "memo", "tags"}
        if not changes or not set(changes).issubset(allowed):
            raise ValueError("수정할 필드를 하나 이상 지정하세요: --date, --type, --amount, --category, --memo, --tags")
        found: Transaction | None = None
        rows: list[Transaction] = []
        categories = self.store.categories()
        for item in self.store.iter_transactions():
            if item.id == transaction_id:
                values = {
                    "date": str(changes.get("date", item.date)),
                    "type": str(changes.get("type", item.type)),
                    "amount": int(changes.get("amount", item.amount)),
                    "category": str(changes.get("category", item.category)),
                    "memo": str(changes.get("memo", item.memo)),
                    "tags": changes.get("tags", item.tags),
                }
                if not isinstance(values["tags"], list):
                    values["tags"] = [part.strip() for part in str(values["tags"]).split(",") if part.strip()]
                validate_transaction_fields(values["type"], values["date"], values["amount"], values["category"])
                if values["category"] not in categories:
                    raise ValueError(f"등록되지 않은 카테고리입니다: {values['category']}")
                found = Transaction(id=item.id, **values)  # type: ignore[arg-type]
                rows.append(found)
            else:
                rows.append(item)
        if found is None:
            raise ValueError(f"거래 ID를 찾을 수 없습니다: {transaction_id}")
        # 모든 검증과 대상 존재 확인이 끝난 뒤에만 파일 교체를 요청한다.
        self.store.replace_transactions(iter(rows))
        return found

    # 삭제도 원본을 직접 줄 단위 수정하지 않고, 남길 거래를 모아 파일 전체를 교체한다.
    def delete(self, transaction_id: str) -> None:
        rows: list[Transaction] = []
        found = False
        for item in self.store.iter_transactions():
            if item.id == transaction_id:
                found = True
            else:
                rows.append(item)
        if not found:
            raise ValueError(f"거래 ID를 찾을 수 없습니다: {transaction_id}")
        self.store.replace_transactions(iter(rows))

    def summary(self, month: str, top: int = 3) -> dict[str, object]:
        month = validate_month(month)
        if top < 1:
            raise ValueError("--top은 1 이상의 정수여야 합니다.")
        income = expense = 0
        categories: Counter[str] = Counter()
        count = 0
        for item in self.store.iter_transactions():
            if item.date.startswith(month):
                count += 1
                if item.type == "income":
                    income += item.amount
                else:
                    expense += item.amount
                    categories[item.category] += item.amount
        budget = self.store.budgets().get(month)
        return {"month": month, "count": count, "income": income, "expense": expense,
                "balance": income - expense, "top": categories.most_common(top), "budget": budget}

    def set_budget(self, month: str, amount: int) -> None:
        month = validate_month(month)
        if amount <= 0:
            raise ValueError("예산은 0보다 큰 정수여야 합니다.")
        self.store.set_budget(month, amount)

    def add_category(self, name: str) -> None:
        name = name.strip()
        if not name:
            raise ValueError("카테고리명을 입력하세요.")
        if name in self.store.categories():
            raise ValueError(f"이미 등록된 카테고리입니다: {name}")
        self.store.add_category(name)

    def remove_category(self, name: str) -> None:
        if name not in self.store.categories():
            raise ValueError(f"등록되지 않은 카테고리입니다: {name}")
        if any(item.category == name for item in self.store.iter_transactions()):
            raise ValueError(f"{name} 카테고리는 거래에서 사용 중이므로 삭제할 수 없습니다.")
        self.store.replace_categories([item for item in self.store.categories() if item != name])

    # CSV를 행 단위로 읽는다. 한 행이 잘못되어도 전체 작업을 중단하지 않고 그 행을 건너뛴다.
    def import_csv(self, source: str) -> tuple[int, int, list[str]]:
        """Import valid rows and return counts plus row-specific skip reasons."""
        imported = skipped = 0
        errors: list[str] = []
        with Path(source).open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            required = {"date", "type", "category", "amount"}
            if not required.issubset(set(reader.fieldnames or [])):
                raise ValueError("CSV 필수 헤더는 date,type,category,amount 입니다.")
            # 헤더가 1행이므로 데이터 행 번호는 2부터 센다.
            for row_number, row in enumerate(reader, start=2):
                try:
                    amount_text = (row.get("amount") or "").strip()
                    if not amount_text.isdigit() or int(amount_text) <= 0:
                        raise ValueError("amount는 0보다 큰 정수여야 합니다.")
                    tags = [part.strip() for part in (row.get("tags") or "").split(",") if part.strip()]
                    self.add(row.get("type") or "", (row.get("date") or "").strip(), int(amount_text),
                             (row.get("category") or "").strip(), row.get("memo") or "", tags)
                    imported += 1
                except (ValueError, TypeError) as exc:
                    skipped += 1
                    errors.append(f"행 {row_number}: {exc}")
        return imported, skipped, errors

    # 기존 출력 파일 보호: 필터를 먼저 검증하고 임시 CSV를 완성한 뒤 마지막에 교체한다.
    def export_csv(self, target: str, month: str | None = None, start: str | None = None,
                   end: str | None = None) -> int:
        """Export atomically: an invalid filter or write error must not damage an existing file."""
        if not month and not (start and end):
            raise ValueError("export에는 --month 또는 --from과 --to를 함께 지정해야 합니다.")

        if month:
            month = validate_month(month)
            last_day = calendar.monthrange(int(month[:4]), int(month[5:7]))[1]
            start, end = f"{month}-01", f"{month}-{last_day:02d}"
        else:
            # filtered() is a generator, so its validation would otherwise run only after
            # the output file had already been opened. Validate eagerly before touching it.
            if start:
                validate_date(start)
            if end:
                validate_date(end)
            if start and end and start > end:
                raise ValueError("--from 날짜는 --to 날짜보다 늦을 수 없습니다.")

        records = self.filtered(start=start, end=end)
        target_path = Path(target)
        temp_name: str | None = None
        count = 0
        try:
            with tempfile.NamedTemporaryFile(
                "w", encoding="utf-8", newline="", dir=target_path.parent,
                prefix=f".{target_path.name}.", suffix=".tmp", delete=False
            ) as file:
                temp_name = file.name
                writer = csv.DictWriter(file, fieldnames=["date", "type", "category", "amount", "memo", "tags"])
                writer.writeheader()
                for item in records:
                    writer.writerow({"date": item.date, "type": item.type, "category": item.category,
                                     "amount": item.amount, "memo": item.memo, "tags": ",".join(item.tags)})
                    count += 1
                file.flush()
                os.fsync(file.fileno())
            os.replace(temp_name, target_path)  # 성공한 임시 파일만 최종 경로에 반영한다.
            temp_name = None  # finally에서 이미 교체한 임시 파일을 지우지 않도록 표시한다.
        finally:
            if temp_name and os.path.exists(temp_name):
                os.unlink(temp_name)
        return count
