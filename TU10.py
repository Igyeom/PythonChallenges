# exercise 1
mynumber = random.uniform(0.1, 9.9)

# exercise 2
import random
Choose_Name = ["James","John","Mark","Rick"]
for i in range(1,5):
    chosen = random.choice(Choose_Name)
    print(chosen)
    if input("Remove from list? (Y/n)").lower() == "y":
      Choose_Name.remove(chosen)
