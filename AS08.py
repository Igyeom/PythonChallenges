from random import choice

move = choice(["rock", "paper", "scissors"])
outcomes = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
player = input().lower()

if player == move.lower():
    print("It's a draw!")
    exit()
elif outcomes[player] == move.lower():
    print(move[0].upper() + move[1:] + " beats " + player[0].upper() + player[1:] + "!")
