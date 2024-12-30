import tkinter # imports main library
import random # For random functions

# Exercise 1
window = tkinter.Tk() #so that there's less confusing brackets

def RandomNumber():
    dice_thrown = tkinter.Label(window, font="Helvetica 16 bold")
    MyRandom = random.choice(["Alice", "Bob", "Cheryl", "Daniel"])
    dice_thrown.configure(text="Name picked: " + str(MyRandom))
    dice_thrown.pack()

MyTitle = tkinter.Label(window, text="Random Name Picker\n",font="Helvetica 16 bold")
MyTitle.pack()

MyButton = tkinter.Button(window, text="Generate Name", command=RandomNumber)
MyButton.pack()

dice_thrown = tkinter.Label(window, font="Helvetica 16 bold")
dice_thrown.pack()
window.mainloop()
