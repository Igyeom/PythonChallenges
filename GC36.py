from random import randint
import time

timer = time.time()
score = 0
while timer-time.time() <= 60.0:
    print("\033c", end="\033[A")
    print(f"{60.0+timer-time.time():.3f}")
    print(f"Score: {score}")
    a = randint(0, 12)
    b = randint(0, 12)
    ans = a*b
    attempt = input(f"{a} x {b} = ")
    if ans == int(attempt):
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print(ans)
        time.sleep(1)
print(score)
