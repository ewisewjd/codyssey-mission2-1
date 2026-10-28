transaction={
"amount":3000,
"category": "식비",
"memo": "점심"
}


transaction["amount"] = 5000
transaction["payment"] = "카드"

del transaction["payment"]

print(transaction["amount"])
print(transaction["category"])
print(transaction["memo"])
print(transaction)