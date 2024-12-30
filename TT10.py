import turtle

def triangle_draw(x,y,sz):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(3):
        turtle.forward(sz)
        turtle.right(120)
        
turtle.speed(0)
for y in range (-100,100,10):
    for x in range (-100,100,10):
        triangle_draw(x,y,10)
        turtle.left(60)

turtle.done()
