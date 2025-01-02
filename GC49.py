from sty import fg
from time import sleep
from random import randrange

print(fg(200, 200, 200) + "Arithmetic Practice")
print(fg.rs + "Choose an option from below (type the number)\n")
print(fg.li_blue + "[1] Addition")
print(fg(255, 50, 0) + "[2] Subtraction")
print(fg(255, 0, 255) + "[3] Times Tables")
print(fg.li_green + "[4] Division")

def start():
    if option == 1:
        ans = ""
        print("To stop the practice session, type " + fg.li_yellow + "'stop'" + fg.rs + ".")
        while str(ans).lower() != "stop":
            try:
                num1 = randrange(100, 999)
                num2 = randrange(10, 99)
                ans = input("What is " + str(num1) + " + " + str(num2) + "?\n")
                if ans.lower() != "stop":
                    if num1 + num2 == int(ans):
                        print("Correct!")
                    else:
                        print("Incorrect. Better luck next time!")
            except:
                print("Please enter an integer.")
    elif option == 2:
        ans = ""
        print("To stop the practice session, type " + fg.li_yellow + "'stop'" + fg.rs + ".")
        while str(ans).lower() != "stop":
            try:
                num1 = randrange(100, 999)
                num2 = randrange(10, 99)
                ans = input("What is " + str(num1) + " - " + str(num2) + "?\n")
                if ans.lower() != "stop":
                    if num1 - num2 == int(ans):
                        print("Correct!")
                    else:
                        print("Incorrect. Better luck next time!")
            except:
                print("Please enter an integer.")
    elif option == 3:
        ans = ""
        print("To stop the practice session, type " + fg.li_yellow + "'stop'" + fg.rs + ".")
        while str(ans).lower() != "stop":
            try:
                num1 = randrange(1, 12)
                num2 = randrange(1, 12)
                ans = input("What is " + str(num1) + " x " + str(num2) + "?\n")
                if ans.lower() != "stop":
                    if num1 * num2 == int(ans):
                        print("Correct!")
                    else:
                        print("Incorrect. Better luck next time!")
            except:
                print("Please enter an integer.")
    elif option == 4:
        ans = ""
        print("To stop the practice session, type " + fg.li_yellow + "'stop'" + fg.rs + ".")
        while str(ans).lower() != "stop":
            try:
                num2 = randrange(1, 12)
                num1 = num2 * randrange(1, 12)
                ans = input("What is " + str(num1) + " ÷ " + str(num2) + "?\n")
                if ans.lower() != "stop":
                    if num1 / num2 == int(ans):
                        print("Correct!")
                    else:
                        print("Incorrect. Better luck next time!")
            except:
                print("Please enter an integer.")

while 1:
    try:
        option = int(input(fg.rs + "Type the corresponding number (e.g. 1 for addition): "))
        if option <= 4:
            start()
            break
        else:
            print("\nPlease type a valid option.")
    except:
        print(fg.rs + "\nPlease type a valid option.")
