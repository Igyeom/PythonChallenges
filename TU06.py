from math import floor

def run():
    height = int(input("What's your height? (in cm. Sorry, imperial users.) "))
    if height > 144.3:
        print("Oh my, you're taller than 11.75 year old me!")
    elif floor(height) == 144:
        print("Ooh, 11.75 year old me was the same height as you! What are the odds?")
    else:
        print("Turns out 11.75 year old me was taller as you!")