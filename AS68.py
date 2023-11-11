# This UNO game may require a terminal that supports 8-bit colour formatting. Use a VSCode terminal, which guarantees 24-bit colour formatting.

from sty import fg
from random import choice, randint
from time import sleep

print("\033c", end="\033]A")
print(f"{fg.red}U{fg.li_green}NO{fg.rs}.{fg.li_blue}p{fg.li_yellow}y{fg.rs}")
input(f"Press {fg.li_green}Enter{fg.rs} to play...")

def random_card():
    colour = choice(["blue", "red", "green", "yellow"])
    sty_colour = eval(f"fg.{colour}")
    value = choice(["0"] + ["1", "2", "3", "4", "5", "6", "7", "8", "9", "B", "R", "W", "+2", "+4"]*2)
    return {"colour": colour, "value": value, "display": f"{sty_colour}{value}{fg.rs}"}

turn = randint(0, 3)
top_card = random_card()
cards = [[random_card(), random_card(), random_card(), random_card(), random_card(), random_card(), random_card()], [random_card(), random_card(), random_card(), random_card(), random_card(), random_card(), random_card()], [random_card(), random_card(), random_card(), random_card(), random_card(), random_card(), random_card()], [random_card(), random_card(), random_card(), random_card(), random_card(), random_card(), random_card()]]
direction = 1

while True:
    print("\033c", end="\033]A")
    print(f"{fg.red}U{fg.li_green}NO{fg.rs}.{fg.li_blue}p{fg.li_yellow}y{fg.rs}")
    print(f"{fg.rs}Card Counts: {fg.red}{len(cards[0])}{fg.rs}, {len(cards[1])}, {len(cards[2])}, {len(cards[3])}")
    print(f"{fg.rs}Your Deck: {' '.join([card['display'] for card in sorted(cards[0], key=lambda x: (x['colour'], x['value']))])}")
    print(f"{fg.rs}Top Card: {top_card['display']}")
    
    if turn == 0:
        while True:
            move = input("Card to play (indexed form, leave blank to draw 1 card): ")
            if move == '':
                cards[0].append(random_card())
                break
            else:
                played = sorted(cards[0], key=lambda x: (x['colour'], x['value']))[int(move)]
                if played["value"] == top_card["value"] or played["colour"] == top_card["colour"]:
                    cards[0].remove(played)
                    top_card = played

                    if played["value"] == "B":
                        turn += direction
                        turn %= 4
                    if played["value"] == "+2":
                        turn += direction
                        turn %= 4
                        cards[turn].append(random_card())
                        cards[turn].append(random_card())
                    if played["value"] == "+4":
                        turn += direction
                        turn %= 4
                        cards[turn].append(random_card())
                        cards[turn].append(random_card())
                        cards[turn].append(random_card())
                        cards[turn].append(random_card())
                        top_card["colour"] = input("Wildcard Colour [red/yellow/green/blue]: ")
                        top_card["display"] = f"{eval('fg.' + top_card["colour"])}{top_card["value"]}{fg.rs}"
                    if played["value"] == "W":
                        turn += direction
                        turn %= 4
                        top_card["colour"] = input("Wildcard Colour [red/yellow/green/blue]: ")
                        top_card["display"] = f"{eval('fg.' + top_card["colour"])}{top_card["value"]}{fg.rs}"
                    if played["value"] == "R":
                        direction = -1
                    break
                else:
                    print(f"{fg.red}Play a legal card.{fg.rs}")
    else:
        for card in cards[turn]:
            if card["value"] == top_card["value"] or card["colour"] == top_card["colour"]:
                top_card = cards[turn].pop(randint(0, len(cards[turn])-1))
                if top_card["value"] == "B":
                    turn += direction
                    turn %= 4
                if top_card["value"] == "+2":
                    turn += direction
                    turn %= 4
                    cards[turn].append(random_card())
                    cards[turn].append(random_card())
                if top_card["value"] == "+4":
                    turn += direction
                    turn %= 4
                    cards[turn].append(random_card())
                    cards[turn].append(random_card())
                    cards[turn].append(random_card())
                    cards[turn].append(random_card())
                    top_card["colour"] = choice(["blue", "red", "green", "yellow"])
                    top_card["display"] = f"{eval('fg.' + top_card["colour"])}{top_card["value"]}{fg.rs}"
                if top_card["value"] == "W":
                    turn += direction
                    turn %= 4
                    top_card["colour"] = choice(["blue", "red", "green", "yellow"])
                    top_card["display"] = f"{eval('fg.' + top_card["colour"])}{top_card["value"]}{fg.rs}"
                if top_card["value"] == "R":
                    direction = -1
                break
        else:
            cards[turn].append(random_card())
        sleep(0.2)

    turn += direction
    turn %= 4

    if len(cards[0]) == 0:
        print("\033c", end="\033]A")
        print(f"{fg.li_yellow}YOU WIN!{fg.rs}")
        break
