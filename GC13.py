s = [*map(int,input("Enter ISBN | "))]
for i in range(len(s)):
    if i%2:
        s[i] *= 3
    else:
        s[i] *= 1
print("The check digit is", 10-sum(s)%10)
