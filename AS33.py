import random
q = int(input("How many questions? "))
for i in range(1,q+1):
    if random.randint(0,1):
        print(f"{i}. Convert the following to hexadecimal:")
        print(bin(random.randint(0,255))[2:])
    else:
        print(f"{i}. Convert the following to binary:")
        print(hex(random.randint(0,255))[2:].upper())
