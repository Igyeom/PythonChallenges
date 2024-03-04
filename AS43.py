s = input()
d = []
for i in set(s): d.append([i, s.count(i)])
d.sort(key=lambda x: x[1])
print(d[0][0], f"occurs {d[0][1]} times")
print(d[1][0], f"occurs {d[1][1]} times")
print(d[2][0], f"occurs {d[2][1]} times")
print(d[-1][0], f"occurs {d[-1][1]} times")
print(d[-2][0], f"occurs {d[-2][1]} times")
print(d[-3][0], f"occurs {d[-3][1]} times")
# assumes s consists of at least 3 unique characters
