import turtle as t
import time as s
import random as ran

t.setup (width=800, height=800, startx=0, starty=0)

x = 20
n = input("How many sides does your shape have?: ")
try:
    float(n)
except ValueError:
    print("This is not a number")
sides = int(n)

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

sha = -360 / sides


def draw():
    class c:
        r = "\033[1;31m"
        g = "\033[1;32m"
        y = "\033[1;33m"
        b = "\033[1;34m"
        m = "\033[1;35m"
        c = "\033[1;36m"
        e = "\033[1;m"

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

    if c == "1" or c == "red":
        y = 300
        t.color("#E90A0A")
        for i in range(sides):
            t.bk(y)
            t.lt(sha)

        for i in range(x):
            y = y * .5
            t.bk(y)
            t.lt(sha)
            t.bk(y)
            t.rt(sha)
            t.bk(y)
            t.rt(sha)

    elif c == "2" or c == "blue":
        y = 300
        t.color("#0A6AE9")
        for i in range(sides):
            t.bk(y)
            t.lt(sha)

        for i in range(x):
            y = y * .5
            t.bk(y)
            t.lt(sha)
            t.bk(y)
            t.rt(sha)
            t.bk(y)
            t.rt(sha)

    elif c == "3" or c == "yellow":
        y = 300
        t.color("#EDE421")
        for i in range(sides):
            t.bk(y)
            t.lt(sha)

        for i in range(x):
            y = y * .5
            t.bk(y)
            t.lt(sha)
            t.bk(y)
            t.rt(sha)
            t.bk(y)
            t.rt(sha)

    elif c == "4" or c == "green":
        y = 300
        t.color("#1CB245")
        for i in range(sides):
            t.bk(y)
            t.lt(sha)

        for i in range(x):
            y = y * .5
            t.bk(y)
            t.lt(sha)
            t.bk(y)
            t.rt(sha)
            t.bk(y)
            t.rt(sha)

    elif c == "5" or c == "magenta":
        y = 300
        t.color("#F449E7")
        for i in range(sides):
            t.bk(y)
            t.lt(sha)

        for i in range(x):
            y = y * .5
            t.bk(y)
            t.lt(sha)
            t.bk(y)
            t.rt(sha)
            t.bk(y)
            t.rt(sha)

    elif c == "6" or c == "cyan":
        y = 300
        t.color("#32E7F3")
        for i in range(sides):
            t.bk(y)
            t.lt(sha)

        for i in range(x):
            y = y * .5
            t.bk(y)
            t.lt(sha)
            t.bk(y)
            t.rt(sha)
            t.bk(y)
            t.rt(sha)

    elif c == "7" or c == "black":
        y = 300
        for i in range(sides):
            t.bk(y)
            t.lt(sha)

        for i in range(x):
            y = y * .5
            t.bk(y)
            t.lt(sha)
            t.bk(y)
            t.rt(sha)
            t.bk(y)
            t.rt(sha)

    elif c == "8" or c == "random":
        y = 300
        for i in range(sides):
            t.color("#%06x" % ran.randint(0, 0xFFFFFF))
            t.bk(y)
            t.lt(sha)

        for i in range(x):
            t.color("#%06x" % ran.randint(0, 0xFFFFFF))
            y = y * .5
            t.bk(y)
            t.lt(sha)
            t.bk(y)
            t.rt(sha)
            t.bk(y)
            t.rt(sha)


draw()

