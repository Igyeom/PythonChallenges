def run():
    print("I can tell you we got an indentation error for exercise 1a, but if that error existed in the code while interpreting, the program won't continue! So here I am.\n")

    test1 = input("Is it raining? y/n (this time type in a capital 'Y' to see what happens)\n")
    if test1 == "y":
        print("Oh dear, no football today!")

    test2 = input("Is it raining? y/n (again, type in a capital 'Y' to see what happens)\n")
    if test2 == "Y":
        print("Oh dear, no football today!")

    test3 = input("Is it raining? y/n/yes/no (this time you may type in any case you'd like. I have not used the code given because it is inefficient. We could've just used either .upper() or .lower())\n")
    if test3.upper() == "YES" or test3.upper() == "Y":
        print("Oh dear, no football today!")
    elif test3.upper() == "NO" or test3.upper() == "N":
        print("Great, we can play!")
    else:
        print("You didn't answer the question properly.")
    
    print("\nNote for Exercise 3: if we add an else statement to say 'great, we can play', it would also apply to any other answer in the world (well, at least in the scope of strings that python can handle, obviously) so just put an elif block. In my code, I've added an else block as well for handling other answers.")