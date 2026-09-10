from turtle import Turtle, Screen
import turtle

sides = 6
length = int(input("Side length of regular polygon: "))

t = Turtle()
t.speed(0)

screen = Screen()

for k in range(50):
    for j in range(8):
        for i in range(sides):
            t.forward(length*20)
            t.right(360//sides)
        t.right(180*(sides-2)//sides)
        # t.forward(length*20)
        for i in range(j):
            t.forward(length*20)
            t.right(360//sides)
    for _ in range(k+1):
        t.forward(length*20)
        t.right(360//sides)
turtle.done()
