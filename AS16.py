import turtle, math

turtle.speed(0)

def draw_square():
    turtle.down()
    for _ in range(4):
        turtle.right(90)
        turtle.forward(20)
    turtle.up()
    turtle.forward(40)

for _ in range(5):
    draw_square()

def draw_square(side_length: int, flag: bool = True):
    if flag:
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.right(90)
    turtle.down()
    for _ in range(4):
        turtle.right(90)
        turtle.forward(side_length)
    turtle.up()

for size in range(20, 101, 20):
    draw_square(size)

def draw_poly(t, n, sz):
    t.pendown()

    for _ in range(n):
        t.fd(sz)
        t.rt(360/n)

    t.penup()

tess = turtle.Turtle()
draw_poly(tess, 8, 50)

for _ in range(10):
    turtle.left(18)
    for _ in range(4):
        draw_square(100, False)
        turtle.left(90)

def draw_spiral_1(t, size: int = 100):
    for sz in range(size, 5, -5):
        t.forward(sz)
        t.right(90)
        t.forward(sz)
        t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(5)
    t.right(90)

def draw_spiral_2(t, size: int = 360):
    for sz in range(size, 1, -1):
        t.forward(sz)
        t.right(90)
        t.forward(sz)
        t.right(90)
        t.right(1)

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t2.up()
t2.goto(-300, 300)

draw_spiral_1(t1)
t2.down()
turtle.tracer(False)
draw_spiral_2(t2)

turtle.tracer(True)

def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)

def sum_to(n: int) -> int:
    return sum(range(1, n+1))

def area_of_circle(r: int) -> float:
    return math.pi*r*r

def star():
    for _ in range(5):
        turtle.forward(100)
        turtle.right(144)

for _ in range(5):
    star()
    turtle.up()
    turtle.forward(350)
    turtle.right(144)
    turtle.down()

turtle.mainloop()
