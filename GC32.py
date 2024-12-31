from random import randint
a = int(input("Confess? (1 for Yes, 0 for No)"))
b = randint(0, 1)
if a and b:print("You are sentenced to 5 years in prison.")
elif not a and not b:print("You are sentenced to 1 year in prison.")
elif a:print("You are released from prison.")
else:print("You are sentenced to 20 years in prison.")
