import turtle as t
import time as w
import random as ran

sides = 6
size = 50
color = "#D33825"

t.clear()
t.pu()
t.setx(0)
t.sety(0)
t.pd()

d = 200
h = 100
y = size
v = .75
sha = -360 / sides
t.pu()
t.setx(d)
t.sety(h)
t.pd()
t.color(color)
y /= v
t.speed(0)

for i in range(sides):
    t.color("#%06x" % ran.randint(0, 0xFFFFFF))
    t.lt(sha)
    t.fd(y)
    for i in range(sides):
        t.bk(y)
        t.rt(sha)
    for i in range(5 * sides):
        y *= v
        for i in range(sides):
            t.fd(y)
            t.rt(sha)
            t.fd(y)
            t.rt(sha)
        t.fd(y)
        t.rt(sha)
        t.fd(y)
        t.rt(sha)
        y *= v
        for i in range(sides):
            t.bk(y)
            t.rt(sha)
        t.bk(y)
        t.rt(sha)
        t.bk(y)
        t.rt(sha)
    y = size
    t.pu()
    t.setx(d)
    t.sety(h)
    t.pd()
    y /= v
    t.lt(sha)
    t.fd(y)




t.exitonclick()
