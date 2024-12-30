import turtle

t = turtle.Turtle()

def regular_polygon(sides, side_length):
    t.pendown()

    for i in range(sides):
        t.fd(side_length)
        t.rt(360/sides)

    t.penup()
t.begin_fill()
regular_polygon(8, 50)
t.end_fill()
