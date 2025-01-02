from random import choice

with open("words_alpha.txt", "r") as f:
    words = f.read().splitlines()

word = choice(words)
while len(word) != 5:
    word = choice(words)

while True:
    guess = input("Guess: ")
    ans = 0
    for i in range(len(word)):
        if guess[i] == word[i]:
            ans += 1
    print(f"Likeness: {ans}")
    if ans == 5:
        print("You win!")
        break
