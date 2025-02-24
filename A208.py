import math
expression = input().split()
stk = []
for i in expression:
    if i == "+":
        stk.append(stk.pop()+stk.pop())
    elif i == "*":
        stk.append(stk.pop()*stk.pop())
    elif i == "-":
        stk.append(stk.pop()-stk.pop())
    elif i == "/":
        stk.append(stk.pop()/stk.pop())
    elif i == "^":
        stk.append(stk.pop()**stk.pop())
    elif i == "sin":
        stk.append(math.sin(stk.pop()))
    elif i == "cos":
        stk.append(math.cos(stk.pop()))
    elif i == "tan":
        stk.append(math.tan(stk.pop()))
    elif i == "pi":
        stk.append(math.pi)
    else:
        stk.append(int(i))
print(stk)
