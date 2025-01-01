from random import choice
name = input("What's their name? ")
l = ["lmao &1 did you know no one asked", "&1 better sleep with three eyes open tonight", "wow so funny &1, everyone laughed"]
print(choice(l).replace("&1", name))
