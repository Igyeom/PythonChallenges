# Exercise 1
expression = "1 2 + 3 *".split()
stk = []
for i in expression:
    if i == "+":
        stk.append(stk.pop()+stk.pop())
    elif i == "*":
        stk.append(stk.pop()*stk.pop())
    else:
        stk.append(int(i))
print(stk)

# Exercise 2
# 2 3 * 1 +
