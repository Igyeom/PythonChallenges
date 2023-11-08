import roman

print("1) Arabic -> Roman")
print("2) Roman -> Arabic")

if int(input("1 or 2: ")) == 1:
    number = int(input('> '))
    print(roman.toRoman(number))
else:
    number = input('> ')
    print(roman.fromRoman(number))