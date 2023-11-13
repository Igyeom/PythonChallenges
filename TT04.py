import turtle

t = turtle.Turtle()

def regular_polygon(sides, side_length):
    t.pendown()

    for i in range(sides):
        t.fd(side_length)
        t.rt(360/sides)

    t.penup()

regular_polygon(4, 50)
regular_polygon(3, 50)
regular_polygon(6, 50)
regular_polygon(int(input("Custom Side Length: ")), 50)
