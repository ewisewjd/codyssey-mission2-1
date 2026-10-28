transactions = [
    {
        "amount": 3000,
        "category": "식비",
        "memo": "점심"
    },
    {
        "amount": 1500,
        "category": "교통비",
        "memo": "버스"
    },
    {
    "amount": 2000,
    "category": "식비",
    "memo": "커피"
}
]

# for transaction in transactions:
#     print(transaction["memo"])

# total = 0
# for transaction in transactions:
#     if transaction["category"] == "식비":
#         total+= transaction["amount"]

# print(total)

totals={}

for transaction in transactions:
    category= transaction["category"]
    amount=  transaction["amount"]

    totals[category] = totals.get(category,0)+amount
# print(totals)
for category, total in totals.items():
    print(f"{category}: {total}원")