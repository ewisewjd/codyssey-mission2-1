balance=int(input("잔액 저장:"))
memo= input("할일 저장:")
expense=int(input("지출 금액:"))

balance-=expense


print(f"거래 내역 : {memo}")
print(f"지출 금액: {expense}원")
print(f"남은 잔약: {balance}원")

