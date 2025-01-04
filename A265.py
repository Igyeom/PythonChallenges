def solve(n, s, m, e):
    if n == 1:
        print(s, e)
        return
    solve(n-1, s, e, m)
    print(s, e)
    solve(n-1, m, s, e)

n = int(input()) # enter 3 for three discs

print(2**n-1)
if n <= 20: solve(n, 1, 2, 3)
