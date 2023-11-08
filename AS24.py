print(str(abs(__import__("datetime").datetime.strptime(input("First Date: "), "%d/%m/%y")-__import__("datetime").datetime.strptime(input("Second Date: "), "%d/%m/%y"))).replace(", 0:00:00", ""))
# one-liner lol
