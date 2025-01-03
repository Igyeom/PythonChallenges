def day_name(day_number: int) -> str:
    return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][day_number]

def returning_day(starting_day_number: int, length_of_stay: int) -> int:
    return (starting_day_number+length_of_stay) % 7

# a <= b
# a < b
# a < 18 or day != 3
# a < 18 or day == 3

print(3 == 3) # True
print(3 != 3) # False
print(3 >= 4) # False
print(not (3 < 4)) # False

# pqr not(p and q) or r
# FFF T
# FFT T
# FTF T
# FTT T
# TFF T
# TFT T
# TTF F
# TTT T

def mark_to_grade(mark: int | float) -> str:
    if mark >= 75: return "First"
    if mark >= 70: return "Upper Second"
    if mark >= 60: return "Second"
    if mark >= 50: return "Third"
    if mark >= 45: return "F1 Supp"
    if mark >= 40: return "F2"
    return "F3"

for i in [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]:
    print(mark_to_grade(i))

import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    if height >= 0:
        t.begin_fill()           # Added this line
        t.left(90)
        t.forward(height)
        t.write("  "+ str(height))
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill()             # Added this line
    if height < 0:
        t.write("  "+ str(height))
    t.up()
    if height < 0:
        t.forward(50)
    else:
        t.forward(10)
    t.down()

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("blue", "red")
tess.pensize(3)

xs = [48,117,200,240,160,260,220]

for a in xs:
    if a >= 200: tess.color("blue", "red")
    elif a >= 100: tess.color("blue", "yellow")
    else: tess.color("blue", "green")
    draw_bar(tess, a)

wn.clear()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(3)


xs = [48,-117,-200,240,-160,260,220]

for a in xs:
    if a >= 200: tess.color("blue", "red")
    elif a >= 100: tess.color("blue", "yellow")
    else: tess.color("blue", "green")
    draw_bar(tess, a)

def find_hypot(a: int | float, b: int | float) -> float:
    return (a*a+b*b)**0.5

def is_rightangled(a: int | float, b: int | float, hypot: int | float) -> float:
    return abs(a*a+b*b-hypot*hypot)<= 10**-9 # check that the difference is at most 1e-9 to account for floating point error

def is_rightangled_unordered(a: int | float, b: int | float, c: int | float) -> float:
    p, q, r = sorted([a, b, c])
    return abs(p*p+q*q-r*r)<= 10**-9 # check that the difference is at most 1e-9 to account for floating point error

import math
a = math.sqrt(2.0)
print(a, a*a)
print(a*a == 2.0)

wn.mainloop()
