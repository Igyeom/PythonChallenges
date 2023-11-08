for number in range(101, 1001):
    if number % sum(map(int, str(number))) == 0:
        print(number)