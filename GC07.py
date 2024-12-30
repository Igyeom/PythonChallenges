balance = int(input("Current account balance: $"))
x = int(input("Withdrawal amount: $"))
if x%5==0:
    if x+0.50 <= balance:
        print("Transaction accepted.")
        balance -= x+0.50
    else:
        print("Transaction declined. (Not enough money in balance)")
else:
    print("Transaction declined. (Amount must be a multiple of $5)")

print(f"Final account balance: ${balance:.2f}")
