"""Command-line interface for the budget ledger."""
import argparse
import sys
from typing import Sequence

from .decorators import timed
from .models import validate_date
from .service import BudgetService
from .storage import JsonlStore


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m budget_app", description="JSONL 기반 개인 가계부")
    parser.add_argument("--data-dir", default="data", help="데이터 디렉터리 (기본값: ./data)")
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("add", help="거래 추가")
    listing = commands.add_parser("list", help="최신 거래 목록")
    listing.add_argument("--limit", type=int, default=20)

    search = commands.add_parser("search", help="조건으로 거래 검색")
    search.add_argument("--from", dest="start")
    search.add_argument("--to", dest="end")
    search.add_argument("--category")
    search.add_argument("--type", dest="transaction_type", choices=["income", "expense"])
    search.add_argument("--q", dest="query")
    search.add_argument("--tag")

    summary = commands.add_parser("summary", help="월별 수입·지출 요약")
    summary.add_argument("--month", required=True)
    summary.add_argument("--top", type=int, default=3)

    budget = commands.add_parser("budget", help="월 예산 설정")
    budget_sub = budget.add_subparsers(dest="budget_action", required=True)
    set_budget = budget_sub.add_parser("set", help="월 예산 저장")
    set_budget.add_argument("--month", required=True)
    set_budget.add_argument("--amount", type=int, required=True)

    category = commands.add_parser("category", help="카테고리 관리")
    category_sub = category.add_subparsers(dest="category_action", required=True)
    category_sub.add_parser("add", help="카테고리 추가")
    category_sub.add_parser("list", help="카테고리 목록")
    remove = category_sub.add_parser("remove", help="카테고리 삭제")
    remove.add_argument("--name", help="삭제할 카테고리명")

    update = commands.add_parser("update", help="거래 수정 (옵션 방식)")
    update.add_argument("--id", required=True)
    update.add_argument("--date")
    update.add_argument("--type", dest="transaction_type", choices=["income", "expense"])
    update.add_argument("--amount", type=int)
    update.add_argument("--category")
    update.add_argument("--memo")
    update.add_argument("--tags", help="쉼표로 구분")

    delete = commands.add_parser("delete", help="거래 삭제")
    delete.add_argument("--id", required=True)

    imp = commands.add_parser("import", help="CSV 거래 가져오기")
    imp.add_argument("--from", dest="source", required=True)

    exp = commands.add_parser("export", help="CSV 거래 내보내기")
    exp.add_argument("--out", required=True)
    exp.add_argument("--month")
    exp.add_argument("--from", dest="start")
    exp.add_argument("--to", dest="end")
    return parser


def print_transactions(items: list) -> None:
    if not items:
        print("거래 내역이 없습니다.")
        return
    for item in items:
        print(f"{item.id} | {item.date} | {item.type:<7} | {item.category} | {item.amount}원 | {item.memo} | 태그: {','.join(item.tags)}")


@timed("명령 실행")
def run(args: argparse.Namespace) -> int:
    store = JsonlStore(args.data_dir)
    service = BudgetService(store)

    if args.command == "add":
        categories = store.categories()
        print("등록된 카테고리:", ", ".join(categories))
        transaction_date = input("날짜(YYYY-MM-DD, 기본값 오늘): ").strip() or __import__("datetime").date.today().isoformat()
        transaction_type = input("타입(income/expense): ").strip()
        category_name = input("카테고리: ").strip()
        amount_text = input("금액(양수 정수): ").strip()
        memo = input("메모(선택): ").strip()
        tags_text = input("태그(쉼표로 구분, 선택): ").strip()
        if not amount_text.isdigit():
            raise ValueError("금액은 0보다 큰 정수여야 합니다.")
        transaction = service.add(transaction_type, transaction_date, int(amount_text), category_name,
                                  memo, [tag.strip() for tag in tags_text.split(",") if tag.strip()])
        print(f"[저장 완료] id={transaction.id}")
    elif args.command == "list":
        print_transactions(service.list_transactions(args.limit))
    elif args.command == "search":
        print_transactions(service.search(start=args.start, end=args.end, category=args.category,
                                          transaction_type=args.transaction_type, query=args.query, tag=args.tag))
    elif args.command == "summary":
        result = service.summary(args.month, args.top)
        if result["count"] == 0:
            print(f"{result['month']}: 데이터 없음")
        print(f"월: {result['month']}")
        print(f"총 수입: {result['income']}원")
        print(f"총 지출: {result['expense']}원")
        print(f"잔액: {result['balance']}원")
        if result["budget"] is not None:
            budget_amount = result["budget"]
            used = result["expense"]
            rate = used / budget_amount * 100
            print(f"예산: {budget_amount}원 (사용률 {rate:.1f}%)")
            if used > budget_amount:
                print("[경고] 월 예산을 초과했습니다.")
        print(f"지출 TOP {args.top}")
        if result["top"]:
            for index, (name, amount) in enumerate(result["top"], start=1):
                print(f"{index}) {name} {amount}원")
        else:
            print("지출 내역 없음")
    elif args.command == "budget":
        service.set_budget(args.month, args.amount)
        print(f"[저장 완료] {args.month} 예산 {args.amount}원")
    elif args.command == "category":
        if args.category_action == "add":
            name = input("카테고리명: ").strip()
            service.add_category(name)
            print(f"[저장 완료] category={name}")
        elif args.category_action == "list":
            for name in store.categories():
                print(f"- {name}")
        else:
            name = args.name or input("삭제할 카테고리명: ").strip()
            service.remove_category(name)
            print(f"[삭제 완료] category={name}")
    elif args.command == "update":
        changes = {}
        for key, value in (("date", args.date), ("type", args.transaction_type), ("amount", args.amount),
                           ("category", args.category), ("memo", args.memo), ("tags", args.tags)):
            if value is not None:
                changes[key] = value
        if "tags" in changes:
            changes["tags"] = [tag.strip() for tag in changes["tags"].split(",") if tag.strip()]
        item = service.update(args.id, **changes)
        print(f"[수정 완료] id={item.id}")
    elif args.command == "delete":
        service.delete(args.id)
        print(f"[삭제 완료] id={args.id}")
    elif args.command == "import":
        imported, skipped = service.import_csv(args.source)
        print(f"[완료] imported={imported}, skipped={skipped}")
    elif args.command == "export":
        count = service.export_csv(args.out, month=args.month, start=args.start, end=args.end)
        print(f"[완료] {args.out} ({count} records)")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return run(args)
    except (ValueError, OSError, KeyError) as exc:
        print(f"[오류] {exc}", file=sys.stderr)
        print("[힌트] 명령의 --help를 확인하고 입력값과 데이터 파일을 점검하세요.", file=sys.stderr)
        return 1
