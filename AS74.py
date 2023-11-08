def AND(a, b):
    return int(a & b)

def OR(a, b):
    return int(a | b)

def NOR(a, b):
    return int(not (a | b))

def XOR(a, b):
    return int(a ^ b)

print(XOR(1, 0)) # outputs 1
print(NOR(1, 1)) # outputs 0
print(OR(0, 0)) # outputs 0