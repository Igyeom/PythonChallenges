from random import randint

while True:
    l = []
    ans = 0
    mode = randint(0, 1)
    if mode:
        print("Odd Parity")
    else:
        print("Even Parity")
    
    s = 0

    for _ in range(7):
        l.append(x:=randint(0, 1))
        s += x
        print(x, end='')
    print("X")
    check = input("What's the parity bit labelled X? (type 'q' to stop)| ")

    if check == "0":
        check = 0
    elif check == "1":
        check = 1
    elif check == "q":
        break
    else:
        print("Invalid input!")
        continue

    if (s+check)%2^mode:
        print("Incorrect!")
        print("The correct answer is", s%2^mode)
    else:
        print("Correct!")
