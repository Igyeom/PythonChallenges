from random import randint
l = [randint(1, 100) for _ in range(50)]
print(min(l), max(l), sum(l)/50)
