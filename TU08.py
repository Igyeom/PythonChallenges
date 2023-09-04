def run():
    while True:
        if input("What's your favourite subject?\n").lower() == "computer science":
            print("Me too!")
            break

    number = 0.0

    while number < 0.1 or number > 2.0:
        print("Please enter a number between 0.1 and 2")
        number = float(input("enter a number: "))