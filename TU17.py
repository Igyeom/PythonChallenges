l = [*map(int,input("Number: "))]
m = [*map(int,input("Multipliers: "))]
for i in range(len(l)):
    l[i] *= m[i%len(m)]
print(f"Checksum: {11-(sum(l)%11)}")
