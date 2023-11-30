from sty import fg
from random import choice

balance = 50000
bet = 0
value_dict = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

def unique(array):
    seen = []
    for i in array:
        if i in seen:
            return False
        seen.append(i)
    return True

def get_total(hand):
    result = []
    for card in hand:
        result.append(value_dict[card["value"]])
    while True:
        for i in range(len(result)):
            if result[i] == 1:
                result[i] = 11
                break
        else:
            return sum(result)
        if sum(result) > 21:
            return sum(result) - 10

def random_card():
    suit = choice(["♠", "♥", "♣", "♦"])
    reds = ["♥", "♦"]
    value = choice(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])
    return {"suit": suit, "value": value, "display": f"{fg.rs}{fg.red * (suit in reds)}{value}{suit}{fg.rs}"}

print("\033c", end="\033]A")
print(f"{fg.rs}Black{fg.red}jack{fg.rs}")
input(f"Press {fg.li_green}Enter{fg.rs} to play...")

while True:
    print("\033c", end="\033]A")
    print(f"{fg.rs}Black{fg.red}jack{fg.rs}")
    print(f"Balance: {fg.li_green}${balance}{fg.rs}")

    dealer_total = choice([17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 21, 21])

    bet = input(f"{fg.rs}Bet how much? {fg.li_green}$")
    if bet.lower() == "q":
        print("\033c", end="\033]A")
        print(f"{fg.red}QUIT{fg.rs}")
        break
    bet = int(bet)
    if bet < 500:
        print(f"{fg.rs}Bet at least {fg.li_green}$500{fg.rs}, or go play a game you can afford.")
        while bet < 500:
            bet = int(input(f"{fg.rs}Bet how much? {fg.li_green}$"))
            print(f"{fg.rs}Bet at least {fg.li_green}$500{fg.rs}, or go play a game you can afford.")
    elif bet > balance:
        print(f"{fg.red}Your balance may be too low.")
        while bet > balance:
            bet = int(input(f"{fg.rs}Bet how much? {fg.li_green}$"))
            print(f"{fg.red}Your balance may be too low.")

    balance -= bet

    cards = [random_card(), random_card()]
    game_loop = True

    while not unique(cards):
        cards = [random_card(), random_card()]


    while game_loop:
        print("\033c", end="\033]A")
        print(f"{fg.rs}Black{fg.red}jack{fg.rs}")
        print(f"Balance: {fg.li_green}${balance}{fg.rs}")
        print(f"{fg.rs}Bet: {fg.li_green}${bet}{fg.rs}")
        print(" ".join([card["display"] for card in cards]))
        print(f"Total: {fg.li_green}{get_total(cards)}{fg.rs}")

        action = input()

        print("\033c", end="\033]A")
        print(f"{fg.rs}Black{fg.red}jack{fg.rs}")
        print(f"Balance: {fg.li_green}${balance}{fg.rs}")
        print(f"{fg.rs}Bet: {fg.li_green}${bet}{fg.rs}")
        if action == "h":
            print(f"{fg.rs}Previous Action: {fg.red}HIT{fg.rs}")
            old_cards = list(cards)
            cards.append(random_card())

            while not unique(cards):
                cards.pop()
                cards.append(random_card())
            print(" ".join([card["display"] for card in cards]))
            print(f"Total: {fg.li_green}{get_total(cards)}{fg.rs}")
            if get_total(cards) > 21:
                print(f"{fg.red}BUST{fg.rs}")
                print(f"{fg.rs}Dealer Score: {fg.li_yellow}{dealer_total}{fg.rs}")
                input(f"Press {fg.li_green}Enter{fg.rs} to continue...")
                game_loop = False
        elif action == "s":
            print(f"{fg.rs}Previous Action: {fg.li_green}STAND{fg.rs}")
            print(" ".join([card["display"] for card in cards]))
            print(f"Total: {fg.li_green}{get_total(cards)}{fg.rs}")
            if get_total(cards) > dealer_total:
                print(f"{fg.li_green}VICTORY{fg.rs}")
                print(f"{fg.rs}Dealer Score: {fg.li_yellow}{dealer_total}{fg.rs}")
                balance += bet * 2
            elif get_total(cards) == dealer_total:
                print(f"{fg.rs}DRAW")
                print(f"{fg.rs}Dealer Score: {fg.li_yellow}{dealer_total}{fg.rs}")
                balance += bet
            else:
                print(f"{fg.red}LOSS{fg.rs}")
                print(f"{fg.rs}Dealer Score: {fg.li_yellow}{dealer_total}{fg.rs}")
            input(f"Press {fg.li_green}Enter{fg.rs} to continue...")
            game_loop = False
    if balance <= 0:
        print("\033c", end="\033]A")
        print(f"{fg.red}BANKRUPT{fg.rs}")
        break
