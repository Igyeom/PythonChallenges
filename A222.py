base_s = int(input("Starting Base (e.g. 2, 10, 16): "))
number = input("Number to Convert: ")
base_e = int(input("Ending Base (e.g. 2, 10, 16): "))
if base_e == 2:
    print(bin(int(number, base_s)))
if base_e == 10:
    print(int(number, base_s))
if base_e == 16:
    print(hex(int(number, base_s)))
