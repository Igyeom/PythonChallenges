# Exercise 1

l = [45, 65, 76, 7]
print(", ".join(map(str,l)))

# Exercise 2
v = []
while True:
    character = input("Enter video game character (terminate via Ctrl-C, type 'view' to view list)")
    if character.lower().strip() == "view": print(", ".join(v))
    else: v.append(character)
