from random import choice

with open("words_alpha.txt", "r") as f:
    words = f.read().splitlines()

word = choice(words)
while len(word) <= 1:
    word = choice(words)
l = ["_" for _ in range(len(word))]
i = 7

while True:
    print("\033c", end="\033[A")
    if i == 1:
        print("1 chance left")
    else:
        print(f"{i} chances left")
    for j in l:
        print(f"{j}", end=' ')
    guess = input("Guess a letter or the word (you are only given 1 chance to guess the word): ")
    if len(guess) > 1:
        if guess == word:
            print("\033c", end="\033[A")
            print("You win!")
            break
        else:
            print("\033c", end="\033[A")
            print("You lose.")
            break
    if guess in word:
        for j in range(len(word)):
            if word[j] == guess:
                l[j] = guess
    else:
        i -= 1
        if i <= 0: break

print("\033c", end="\033[A")
print("You lose.")
