# fractal generator by Sam Escamilla

# import modules
import turtle as t
import time as s
import random as ran

# set screen size
t.setup (width=800, height=800, startx=0, starty=0)

# ask user for shape
n = input("How many sides does your shape have?: ")
try:
    float(n)
except ValueError:
    print("This is not a number")

# convert input to integer and set x equal to it
sides = int(n)

# decide starting coordinates based on shape
if sides == 3:
    t.pu()
    t.setx(375)
    t.sety(-375)
    t.pd()

elif sides == 4:
    t.pu()
    t.setx(300)
    t.sety(-300)
    t.pd()

elif sides == 5:
    t.pu()
    t.setx(375)
    t.sety(-375)
    t.pd()

elif sides == 6:
    t.pu()
    t.setx(375)
    t.sety(-375)
    t.pd()

elif sides == 7:
    t.pu()
    t.setx(375)
    t.sety(-375)
    t.pd()

elif sides == 8:
    t.pu()
    t.setx(375)
    t.sety(-375)
    t.pd()

elif sides == 9:
    t.pu()
    t.setx(375)
    t.sety(-375)
    t.pd()

elif sides >= 10:
    t.pu()
    t.setx(375)
    t.sety(-375)
    t.pd()

# equation for shape angles
sha = -360 / sides


def draw():
    # set text colors
    class c:
        r = "\033[1;31m"
        g = "\033[1;32m"
        y = "\033[1;33m"
        b = "\033[1;34m"
        m = "\033[1;35m"
        c = "\033[1;36m"
        e = "\033[1;m"

    # list of options for user
    print(c.r + "1. Red" + c.e)
    print(c.b + "2. Blue" + c.e)
    print(c.y + "3. Yellow" + c.e)
    print(c.g + "4. Green" + c.e)
    print(c.m + "5. Magenta" + c.e)
    print(c.c + "6. Cyan" + c.e)
    print("7. Black")
    print(c.y+"8"+c.g+"."+c.r+" Ra"+c.b+"n"+c.c+"do"+c.m+"m"+c.e)
    z = input("What color do you want?: ")
    c = z.lower()

    # decide color based on user input
    if c == "1" or c == "red":
        t.color("#E90A0A")
    elif c == "2" or c == "blue":
        t.color("#0A6AE9")
    elif c == "3" or c == "yellow":
        t.color("#EDE421")
    elif c == "4" or c == "green":
        t.color("#1CB245")
    elif c == "5" or c == "magenta":
        t.color("#F449E7")
    elif c == "6" or c == "cyan":
        t.color("#32E7F3")
    elif c == "7" or c == "black":
        t.color("#000000")
    elif c == "8" or c == "random":
        y = 300
        sides = int(n)
        x = sides
        for i in range(sides):
            # randomizes color of each line
            t.color("#%06x" % ran.randint(0, 0xFFFFFF))
            t.bk(y)
            t.lt(sha)
        for i in range(sides):
            sides *= x
            for i in range(sides):
                g = 0
                t.speed(2 + g)
                y *= .5
                t.bk(y)
                t.lt(sha)
                t.bk(y)
                t.rt(sha)
                t.bk(y)
                t.rt(sha)
                t.bk(y)
                t.rt(sha)
                g += 1
    else:
        print("That is not a valid color.")
        draw()

    y = 300
    sides = int(n)
    x = sides
    g = 0

    # fix
    for i in range(sides):
        t.bk(y)
        t.lt(sha)

    for i in range(sides):
        sides *= x
        for i in range(sides):
            t.speed(1 + g)
            y *= .5
            t.bk(y)
            t.lt(sha)
            t.bk(y)
            t.rt(sha)
            t.bk(y)
            t.rt(sha)
            t.bk(y)
            t.rt(sha)
            g += 1

    print(sides)


draw()
