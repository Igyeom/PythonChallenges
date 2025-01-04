from sympy import *
x, y, z = symbols('x y z') # use symbols x, y, z to enter the expression
print(str(expand(eval(input().replace("^", "**")))).replace("**", "^"))
