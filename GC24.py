try:
    print(float(input()), "is a valid float!")
except ValueError:
    raise ValueError("The entered value was an invalid float.")
