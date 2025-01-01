while True:
    try:
        recommended_calories = int(input("Check the recommended amount of calories for you and type it here: "))
    except ValueError:
        continue
    break
consumed_calories = input("Calories consumed: ")
while consumed_calories.lower() != "end day":
    try:
        recommended_calories -= int(consumed_calories)
    except ValueError:
        print("Invalid Input!")
        consumed_calories = input("Calories consumed: ")
        continue
    consumed_calories = input("Calories consumed: ")
if recommended_calories < 0:
    print(f"You consumed {-recommended_calories} calories over your recommended amount!")
elif recommended_calories > 0:
    print(f"You consumed {recommended_calories} calories unde your recommended amount!")
else:
    print("You consumed exactly the amount of calories recommended to you! Impressive.")
