m, n = map(int,input().split())
l = []
for _ in range(m):
    l.append([*map(int, input().split())])

for i in range(m):
    for j in range(n):
        if max(map(max, l)) == l[i][j]:
            print(i, j)
            quit()
