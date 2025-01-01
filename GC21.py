# Exercise 1

for _ in range(1000):print("We like Python's turtles!")


# Exercise 2

# Phone number
# Region
# Brand

# call(number)
# startup()
# shutdown()


# Exercise 3

for i in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
    print(f"One of the months of the year is {i}")


# Exercise 4

# Rotates 3645 degrees to the left
print(360-(3645%360)) # Final heading


# Exercise 5

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in xs:print(i)
for i in xs:print(i, i*i)
total=0
for i in xs:total+=i
print(total)
total=1
for i in xs:total*=i
print(total)


# Exercise 6

import turtle

t = turtle.Turtle()

def regular_polygon(sides, side_length):
    t.pendown()

    for i in range(sides):
        t.fd(side_length)
        t.rt(360/sides)

    t.penup()
regular_polygon(3, 50)
regular_polygon(4, 50)
regular_polygon(6, 50)
regular_polygon(8, 50)


# Exercise 7

import turtle

for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    turtle.left(i)
    turtle.forward(100)


# Exercise 8

print(turtle.heading())


# Exercise 9
print(180-(360//18))


# Exercise 10

# 11 points


# Exercise 11

star = turtle.Turtle()
for i in range(5):
    star.right(180-36)
    star.forward(100)

# Exercise 12

clock = turtle.Turtle()

for i in range(12):
    clock.right(30)

    clock.penup()
    clock.forward(100)

    clock.pendown()
    clock.forward(20)

    clock.penup()
    clock.forward(15)

    clock.pendown()
    clock.stamp()

    clock.penup()
    clock.backward(135)
turtle.done()


# Exercise 13

print(type(star))


# Exercise 14

# Bale, Nest, Turn, Dole


# Exercise 15

# Non-venomous, no collective noun
