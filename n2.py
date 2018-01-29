import turtle as t
import random as r

a = t.Pen()
a.shape("blank")
a.color("#%06x" % r.randint(0, 0xFFFFFF))
b = t.Pen()
b.shape("blank")
b.color("#%06x" % r.randint(0, 0xFFFFFF))
c = t.Pen()
c.shape("blank")
c.color("#%06x" % r.randint(0, 0xFFFFFF))
d = t.Pen()
d.shape("blank")
d.color("#%06x" % r.randint(0, 0xFFFFFF))
s = t.Pen()
s.shape("blank")
s.color("white")
s.pu()
s.pd()
t.bgcolor("#46C626")

tw = 350
tl = 775
hw = tw/2
ew = tw/8
hl = tl/2
hf = tl/28


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

    a.pu()
    b.pu()
    c.pu()
    d.pu()
    a.goto(-hw + ew, -hl + hf)
    b.goto(-hw + 3*ew, -hl + hf)
    c.goto(hw - 3*ew, -hl + hf)
    d.goto(hw - ew, -hl + hf)
    a.pd()
    b.pd()
    c.pd()
    d.pd()
    a.lt(90)
    b.lt(90)
    c.lt(90)
    d.lt(90)
    a.shape("turtle")
    b.shape("turtle")
    c.shape("turtle")
    d.shape("turtle")

    for i in range(200):
        w = r.randint(0, 10)
        x = r.randint(0, 10)
        y = r.randint(0, 10)
        z = r.randint(0, 10)
        w2 = r.randint(-7, 7)
        x2 = r.randint(-7, 7)
        y2 = r.randint(-7, 7)
        z2 = r.randint(-7, 7)
        a.speed(w)
        b.speed(x)
        c.speed(y)
        d.speed(z)
        a.fd(w)
        b.fd(x)
        c.fd(y)
        d.fd(z)
        a.lt(w2)
        b.lt(x2)
        c.lt(y2)
        d.lt(z2)
        l = int(a.xcor())
        m = int(b.xcor())
        n = int(c.xcor())
        o = int(d.xcor())
        if l <= -hw:
            a.rt(7)
            a.fd(w)
        if l >= -hw+(2*ew):
            a.lt(7)
            a.fd(w)
        #
        if m <= -hw+(2*ew):
            b.rt(7)
            b.fd(w)
        if m >= 0:
            b.lt(7)
            b.fd(w)
        #
        if n <= 0:
            c.rt(7)
            c.fd(w)
        if n >= hw-(2*ew):
            c.lt(7)
            c.fd(w)
        #
        if o <= hw-(2*ew):
            d.rt(7)
            d.fd(w)
        if o >= hw:
            d.lt(7)
            d.fd(w)

        h = int(a.ycor())
        i = int(b.ycor())
        j = int(c.ycor())
        k = int(d.ycor())
        if h >= hl:
            print("A wins!")
            break
        if i >= hl:
            print("B wins!")
            break
        if j >= hl:
            print("C wins!")
            break
        if k >= hl:
            print("D wins!")
            break

track()
t.exitonclick()

