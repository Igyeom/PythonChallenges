from random import randint

p1 = [randint(1, 9)*10**randint(0, 9) for _ in range(5)]
p2 = [randint(1, 9)*10**randint(0, 9) for _ in range(5)]

print("Draw" if max(p1) == max(p2) else "Player 1 wins" if max(p1) > max(p2) else "Player 2 wins")
