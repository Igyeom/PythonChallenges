from random import randint

number = randint(1, 100)
while True:
    guess = int(input("Guess: "))
    if guess > number:
        print("Lower")
    elif guess < number:
        print("Higher")
    else:
        print("Correct!")
        break
