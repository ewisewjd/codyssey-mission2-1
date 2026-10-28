"""Regression tests for the budget ledger using only the standard library."""
import csv
import io
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

from budget_app.cli import main
from budget_app.service import BudgetService
from budget_app.storage import JsonlStore


class BudgetServiceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = JsonlStore(str(self.root / "data"))
        self.service = BudgetService(self.store)

    def test_add_persists_and_assigns_unique_ids(self):
        first = self.service.add("expense", "2026-10-27", 4500, "food", "점심", ["meal"])
        second = self.service.add("income", "2026-10-27", 10000, "salary")
        self.assertEqual(first.id, "TX-000001")
        self.assertEqual(second.id, "TX-000002")
        self.assertEqual(list(self.store.iter_transactions())[0].memo, "점심")

    def test_id_is_not_reused_after_deleting_latest_transaction(self):
        first = self.service.add("expense", "2026-10-27", 1000, "food")
        latest = self.service.add("expense", "2026-10-27", 2000, "food")
        self.service.delete(latest.id)
        next_item = self.service.add("expense", "2026-10-27", 3000, "food")
        self.assertEqual(first.id, "TX-000001")
        self.assertEqual(latest.id, "TX-000002")
        self.assertEqual(next_item.id, "TX-000003")

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

    def test_export_preserves_existing_file_when_date_is_invalid(self):
        output = self.root / "existing.csv"
        output.write_text("do not destroy this data\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.service.export_csv(str(output), start="2026-13-01", end="2026-13-31")
        self.assertEqual(output.read_text(encoding="utf-8"), "do not destroy this data\n")

    def test_export_preserves_existing_file_when_range_is_reversed(self):
        output = self.root / "existing.csv"
        output.write_text("keep me\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.service.export_csv(str(output), start="2026-10-20", end="2026-10-01")
        self.assertEqual(output.read_text(encoding="utf-8"), "keep me\n")

    def test_csv_round_trip_and_month_end(self):
        self.service.add("expense", "2026-02-28", 1234, "food", "국밥, 특", ["lunch", "korean"])
        output = self.root / "february.csv"
        count = self.service.export_csv(str(output), month="2026-02")
        self.assertEqual(count, 1)
        with output.open(encoding="utf-8", newline="") as file:
            row = next(csv.DictReader(file))
        self.assertEqual(row["memo"], "국밥, 특")
        self.assertEqual(row["tags"], "lunch,korean")

        second_store = JsonlStore(str(self.root / "imported-data"))
        second_service = BudgetService(second_store)
        imported, skipped, errors = second_service.import_csv(str(output))
        self.assertEqual((imported, skipped, errors), (1, 0, []))
        imported_row = list(second_store.iter_transactions())[0]
        self.assertEqual(imported_row.memo, "국밥, 특")
        self.assertEqual(imported_row.tags, ["lunch", "korean"])
        self.assertEqual(imported_row.amount, 1234)

    def test_import_reports_each_skipped_row_reason(self):
        source = self.root / "bad.csv"
        source.write_text(
            "date,type,category,amount,memo\n"
            "2026-10-01,expense,food,100,valid\n"
            "2026-13-01,expense,food,100,bad date\n"
            "2026-10-03,expense,food,0,zero amount\n",
            encoding="utf-8",
        )
        imported, skipped, errors = self.service.import_csv(str(source))
        self.assertEqual((imported, skipped), (1, 2))
        self.assertEqual(len(errors), 2)
        self.assertIn("행 3:", errors[0])
        self.assertIn("행 4:", errors[1])

    def test_all_three_data_files_exist(self):
        self.assertTrue(self.store.transactions_path.exists())
        self.assertTrue(self.store.categories_path.exists())
        self.assertTrue(self.store.budgets_path.exists())

    def test_add_handles_end_of_input_without_traceback(self):
        stderr = io.StringIO()
        with patch("builtins.input", side_effect=EOFError), redirect_stderr(stderr):
            code = main(["--data-dir", str(self.root / "cli-data"), "add"])
        self.assertEqual(code, 1)
        self.assertIn("입력 종료", stderr.getvalue())
        self.assertNotIn("Traceback", stderr.getvalue())

    def test_add_handles_keyboard_interrupt_without_traceback(self):
        stderr = io.StringIO()
        with patch("builtins.input", side_effect=KeyboardInterrupt), redirect_stderr(stderr):
            code = main(["--data-dir", str(self.root / "cli-data"), "add"])
        self.assertEqual(code, 130)
        self.assertIn("취소", stderr.getvalue())
        self.assertNotIn("Traceback", stderr.getvalue())

    def test_empty_summary_does_not_print_zero_totals(self):
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = main(["--data-dir", str(self.root / "cli-data"), "summary", "--month", "2026-10"])
        self.assertEqual(code, 0)
        self.assertIn("거래 데이터 없음", stdout.getvalue())
        self.assertNotIn("총 수입: 0원", stdout.getvalue())
        self.assertNotIn("총 지출: 0원", stdout.getvalue())

    def test_import_with_skipped_rows_returns_nonzero_and_explains_them(self):
        source = self.root / "all-bad.csv"
        source.write_text(
            "date,type,category,amount\n"
            "2026-13-01,expense,food,100\n",
            encoding="utf-8",
        )
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            code = main(["--data-dir", str(self.root / "cli-data"), "import", "--from", str(source)])
        self.assertEqual(code, 1)
        self.assertIn("skipped=1", stdout.getvalue())
        self.assertIn("행 2:", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
