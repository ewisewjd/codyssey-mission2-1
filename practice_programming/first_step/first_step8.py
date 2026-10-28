balance=int(input("잔액 저장:"))
expense=int(input("지출 금액:"))
memo= input("할일 저장:")

if expense <= 0:
    print("지출 금액은 0보다 커야 합니다.")
elif balance == 0:
    print("잔액이 없습니다.")
elif balance < expense:
    print("잔액이 부족합니다.")
else:
    balance -= expense
    print("지출이 완료되었습니다.")