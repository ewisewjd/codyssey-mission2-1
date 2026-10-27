"""Core regression tests for the budget ledger (stdlib unittest only)."""
import csv
import tempfile
import unittest
from pathlib import Path

from budget_app.models import Transaction
from budget_app.service import BudgetService
from budget_app.storage import JsonlStore


class BudgetServiceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.store = JsonlStore(str(Path(self.temp.name) / "data"))
        self.service = BudgetService(self.store)

    def test_add_persists_and_assigns_unique_ids(self):
        first = self.service.add("expense", "2026-10-27", 4500, "food", "점심", ["meal"])
        second = self.service.add("income", "2026-10-27", 10000, "salary")
        self.assertEqual(first.id, "TX-000001")
        self.assertEqual(second.id, "TX-000002")
        self.assertEqual(list(self.store.iter_transactions())[0].memo, "점심")

    def test_rejects_invalid_transaction(self):
        with self.assertRaises(ValueError):
            self.service.add("expense", "2026-02-30", 100, "food")
        with self.assertRaises(ValueError):
            self.service.add("expense", "2026-10-27", 0, "food")
        with self.assertRaises(ValueError):
            self.service.add("expense", "2026-10-27", 100, "not-a-category")

    def test_update_delete_and_missing_id(self):
        item = self.service.add("expense", "2026-10-27", 4500, "food")
        updated = self.service.update(item.id, amount=5000, memo="저녁")
        self.assertEqual(updated.amount, 5000)
        self.assertEqual(updated.memo, "저녁")
        self.service.delete(item.id)
        self.assertEqual(list(self.store.iter_transactions()), [])
        with self.assertRaises(ValueError):
            self.service.delete(item.id)

    def test_search_and_month_summary(self):
        self.service.add("income", "2026-10-01", 100000, "salary")
        self.service.add("expense", "2026-10-02", 12000, "food", "점심", ["meal"])
        self.service.add("expense", "2026-09-02", 3000, "transport")
        found = self.service.search(start="2026-10-01", end="2026-10-31", tag="meal")
        self.assertEqual(len(found), 1)
        summary = self.service.summary("2026-10")
        self.assertEqual(summary["income"], 100000)
        self.assertEqual(summary["expense"], 12000)
        self.assertEqual(summary["balance"], 88000)

    def test_budget_and_category_safety(self):
        self.service.set_budget("2026-10", 10000)
        self.assertEqual(self.store.budgets()["2026-10"], 10000)
        self.service.add("expense", "2026-10-02", 1200, "food")
        with self.assertRaises(ValueError):
            self.service.remove_category("food")
        self.service.add_category("books")
        self.service.remove_category("books")
        self.assertNotIn("books", self.store.categories())

    def test_csv_round_trip_and_month_end(self):
        self.service.add("expense", "2026-02-28", 1234, "food", "국밥, 특", ["lunch", "korean"])
        output = Path(self.temp.name) / "february.csv"
        count = self.service.export_csv(str(output), month="2026-02")
        self.assertEqual(count, 1)
        with output.open(encoding="utf-8", newline="") as file:
            row = next(csv.DictReader(file))
        self.assertEqual(row["memo"], "국밥, 특")
        self.assertEqual(row["tags"], "lunch,korean")

    def test_all_three_data_files_exist(self):
        self.assertTrue(self.store.transactions_path.exists())
        self.assertTrue(self.store.categories_path.exists())
        self.assertTrue(self.store.budgets_path.exists())


if __name__ == "__main__":
    unittest.main()
