number = None
while number == None:
    try:
        number = int(input())
    except ValueError:
        print("Please enter a whole number.")
