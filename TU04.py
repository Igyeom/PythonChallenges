def run():
    userBirthYear = int(input("Enter your birthdate to find how much older/younger someone is compared to you!\n"))
    comparingBirthYear = int(input("Now enter someone else's birthday (the one that you wanna compare ages with)\n"))
    if userBirthYear == comparingBirthYear:
        print("Y'all are the same age! (assuming both of you had either passed your birthday this year, or both haven't this year.)")
    elif userBirthYear < comparingBirthYear:
        print(f'You are {abs(comparingBirthYear - userBirthYear)} years older!')
    else:
        print(f'You are {abs(comparingBirthYear - userBirthYear)} years younger!')