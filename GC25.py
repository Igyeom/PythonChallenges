print("Vending Machine\nNote: Product n costs n coins.\n")
product = int(input("SELECT PRODUCT (1~9) "))
coins = int(input("INSERT COIN (0~100) "))
change = coins-product
if change < 0: print("NOT ENOUGH COINS")
else:
    print(f"Product: {product}")
    print(f"Change: {change}")
