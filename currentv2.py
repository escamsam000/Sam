# import modules
import turtle as t
import time as s

sides = 3
y = 300
sha = -360 / sides
g = 0
x = sides

for i in range(sides):
    t.bk(y)
    t.lt(sha)

for i in range(5 * sides):
    t.speed(0)
    y *= .5
    t.bk(y)

    t.lt(sha)
    t.bk(y)

    t.rt(sha)
    t.bk(y)

    t.rt(sha)
    t.bk(y)

    t.lt(sha)

y = 300
t.pu()
t.setx(-y)
t.sety(0)
t.pd()


for i in range(5 * sides):
    t.speed(0)
    y *= .5
    t.fd(y)

    t.lt(sha)
    t.bk(y)

    t.rt(sha)
    t.bk(y)

    t.rt(sha)
    t.bk(y)

    t.lt(sha)

y = 300
t.pu()
t.setx(-y)
t.sety(0)
t.pd()

t.color("red")
t.fd(y / 2)

t.lt(sha)
t.bk(y / 2)
t.lt(sha)
t.fd(y / 4)
y /= 2

#fix
for i in range(5 * sides):
    t.speed(1)
    y *= .5
    t.fd(y)

    t.lt(sha)
    t.bk(y)

    t.rt(sha)
    t.bk(y)

    t.rt(sha)
    t.bk(y)

    t.lt(sha)


print(sides)
