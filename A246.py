possible = [*range(1,112)]
i = 0
while True:
    print(possible[len(possible)//2])
    feedback = input()
    if feedback == 'h':
        possible = possible[len(possible)//2+1:]
    elif feedback == 'l':
        possible = possible[:len(possible)//2]
    elif feedback == 'c':
        print(f"The computer guessed the number within {i} tries!")
        break
    else:
        print("Type 'h' for higher and 'l' for lower, 'c' to admit that the computer got it correct.")
        i -= 1
    i += 1
