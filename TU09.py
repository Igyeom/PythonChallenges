# Exercise 1
cnt = 0
while True:
    MyNumber = input("Please enter a number: ")
    try:
        valid_number = int(MyNumber)
        break
    except ValueError:
        cnt += 1
        print(f"Seriously, don't you read the instructions. \nI asked for a number...\nYou haven't listened {cnt} time(s) now.")
 
print(valid_number)

# technically floats are also numbers but the base program only accepts integers lol
# please enter a "number" is crazy
