import turtle as t
import random as r

r


a = t.Pen()
a.shape("turtle")
b = t.Pen()
b.shape("turtle")
c = t.Pen()
c.shape("turtle")
d = t.Pen()
d.shape("turtle")
s = t.Pen()

s.shape("blank")
s.color("white")
s.pu()
s.pd()

t.bgcolor("#2BB220")

tw = 300
tl = 750


def track():
    s.speed(0)
    s.pu()
    s.goto(-tw/2, -tl/2)
    s.pd()
    s.fillcolor("#CB6750")
    s.begin_fill()
    for i in range(2):
        s.fd(tw)
        s.lt(90)
        s.fd(tl)
        s.lt(90)
    s.end_fill()
    for i in range(3):
        s.fd(tw/4)
        s.lt(90)
        s.fd(tl)
        s.bk(tl)
        s.rt(90)
    s.fd(tw/4)
    s.lt(90)
    s.fd(tl/14)
    s.lt(90)
    s.fd(tw)

    a.goto(-tw/2, -tl/2)
    b.goto(-tw/2, -tl/2)
    c.goto(-tw/2, -tl/2)
    d.goto(-tw/2, -tl/2)


track()
t.exitonclick()
