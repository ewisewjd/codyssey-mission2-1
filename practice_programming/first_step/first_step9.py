
balance = 20000
expense = 5000
memo = ""

if not memo:
    print("거래 메모를 입력하세요.")
elif expense <= 0:
    print("지출 금액은 0보다 커야 합니다.")

else:
    balance-=expense