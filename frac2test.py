import turtle as t
import time as w
import math
import random as ran


def setp(x,y):
    t.bk(0+x)
    t.setx(0+y)


def ss(n, v):
    t.write(n, True, align="center", font=("Oswald", 30, "normal"))
    t.rt(90)
    t.fd(3)
    t.pd()
    for i in range(v):
        j = math.degrees(math.sin(math.pi/v))
        t.fd(2 * j)
        t.lt(360 / v)
    t.lt(90)
    t.pu()
    w.sleep(.25)


def selectscreen():
    t.speed(3)
    t.clear()
    t.pu()
    t.setx(0)
    t.sety(0)
    t.bgcolor("#F8F8F8")
    t.pu()
    t.lt(90)
    t.fd(300)
    t.write("Fractal Generator",
            True, align="center", font=("Oswald", 40, "normal"))
    w.sleep(.25)
    setp(30, 0)
    t.write("(Control in Terminal)",
            True, align="center", font=("Oswald", 20, "normal"))
    w.sleep(.25)
    setp(60, 0)
    t.write("Select a shape.",
            True, align="center", font=("Oswald", 30, "normal"))
    t.speed(8)
    w.sleep(.25)
    # triangle
    setp(200, -400)
    ss("1.", 3)
    # square
    setp(0, -100)
    ss("2.", 4)
    # pentagon
    setp(0, 200)
    ss("3.", 5)
    # hexagon
    setp(300, -400)
    ss("4.", 6)
    # heptagon
    setp(0, -100)
    ss("5.", 7)
    # octagon
    setp(0,200)
    ss("6.", 8)
    t.exitonclick()

selectscreen()