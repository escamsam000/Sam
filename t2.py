import turtle as t
import time as s
import random as ran

t.setup (width=800, height=800, startx=0, starty=0)

x = 20
sides = 5
t.pu()
t.setx(375)
t.sety(-375)
t.pd()


sha = -360 / sides
def draw(sha):
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


draw(sha)















