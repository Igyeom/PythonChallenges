from random import randint, choice

print("How many random IP addresses do you need in your life?")

for _ in range(int(input())):
    print(randint(0,255), randint(0,255), randint(0,255), randint(0,255), sep=".")
    print(choice("0123456789abcdef"), choice("0123456789abcdef"), choice("0123456789abcdef"), choice("0123456789abcdef"), ":", choice("0123456789abcdef"), choice("0123456789abcdef"), choice("0123456789abcdef"), choice("0123456789abcdef"), ":", choice("0123456789abcdef"), choice("0123456789abcdef"), choice("0123456789abcdef"), choice("0123456789abcdef"), ":", choice("0123456789abcdef"), choice("0123456789abcdef"), choice("0123456789abcdef"), choice("0123456789abcdef"), ":", choice("0123456789abcdef"), choice("0123456789abcdef"), choice("0123456789abcdef"), choice("0123456789abcdef"), ":", choice("0123456789abcdef"), choice("0123456789abcdef"), choice("0123456789abcdef"), choice("0123456789abcdef"), ":", choice("0123456789abcdef"), choice("0123456789abcdef"), choice("0123456789abcdef"), choice("0123456789abcdef"), ":", choice("0123456789abcdef"), choice("0123456789abcdef"), choice("0123456789abcdef"), choice("0123456789abcdef"), sep="")