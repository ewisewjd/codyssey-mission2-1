balance=int(input("잔액 저장:"))
memo= input("할일 저장:")
expense=int(input("지출 금액:"))

if balance== 0:
        print("잔액이 없습니다.")
elif balance< expense:
      print("잔액이 부족합니다. ")
else:
    balance-=expense
    print("지출이 완료 되었습니다. ")


print(f"거래 내역 : {memo}")
print(f"지출 금액: {expense}원")
print(f"남은 잔약: {balance}원")

