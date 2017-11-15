import turtle as t
import time as w

sides = 4
size = 50
color = "#D33825"

t.clear()
t.pu()
t.setx(0)
t.sety(0)
t.pd()

d = 200
h = 100
for i in range(sides):
    y = size
    v = y
    sha = -360 / sides
    t.pu()
    t.setx(d)
    t.sety(h)
    t.pd()
    t.color(color)
    y /= .5
    for i in range(sides):
        t.bk(y)
        t.rt(sha)
    for i in range(5 * sides):
        y *= .5
        for i in range(sides):
            t.fd(y)
            t.rt(sha)
        t.fd(y)
        t.rt(sha)
        t.fd(y)
        t.rt(sha)
        y *= .5
        for i in range(sides):
            t.bk(y)
            t.rt(sha)
        t.bk(y)
        t.rt(sha)
        t.bk(y)
        t.rt(sha)

t.exitonclick()
