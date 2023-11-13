n, m = map(int,input().split())
arr = [['*' for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        if j%2==i%2:
            arr[i][j] = '.'

print('\n'.join([''.join(i) for i in arr]))
