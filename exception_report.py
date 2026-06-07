transactions = [5000, 12000, 800, 15000]

for amount in transactions:
    if amount > 10000:
        print("Review Required:", amount)
    else:
        print("OK:", amount)
