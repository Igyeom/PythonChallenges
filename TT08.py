import turtle
turtle.bgcolor("blue")
turtle.speed(0)
for i in range(300,-300,-10):
    turtle.penup()
    turtle.goto(-400,i)
    turtle.pendown()
    turtle.forward(600)
turtle.right(90)
for i in range(200,-410,-10):
    turtle.penup()
    turtle.goto(i,300)
    turtle.pendown()
    turtle.forward(600)
turtle.done()
