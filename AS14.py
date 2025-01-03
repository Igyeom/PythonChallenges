s = input("Enter a string with brackets: ")
stk = []
for i in range(len(s)):
    stk.append(s[i])
    if len(stk) > 1:
        if stk[-2] == '(' and stk[-1] == ')':
            stk.pop()
            stk.pop()
if len(stk) > 0: print("NO")
else: print("YES")
