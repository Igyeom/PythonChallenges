def sumDigits(n: int) -> int:
    if len(str(n)) == 1: return n
    else:
        s = 0
        for c in str(n):
            s += sumDigits(int(c))
        return s

print(sumDigits(int(input())))
