l = [*map(int,input("ISBN "))]
m = [*range(10,1,-1)]
for i in range(len(l)):
    l[i] *= m[i%len(m)]
res = 11-(sum(l)%11)
if res == 11: res = 0
if res == 10: res = "X"
print(f"Check digit: {res}")
