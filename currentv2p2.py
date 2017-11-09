# import modules
import turtle as t
import time as w


def setp(x,y):
    t.bk(0+x)
    t.setx(0+y)


def selectscreen():
    t.bgcolor("#DBDBDB")
    t.pu()
    t.lt(90)
    t.fd(300)
    t.write("Fractal Generator",
            True, align="center", font=("Oswald", 40, "normal"))
    w.sleep(1)
    setp(30,0)
    t.write("(Control in Terminal)",
            True, align="center", font=("Oswald", 20, "normal"))
    w.sleep(1)
    setp(60,0)
    t.write("Select a shape.",
            True, align="center", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60,-200)
    t.color("#21B921")
    t.write("1. Triangle",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60,-200)
    t.color("#173BCF")
    t.write("2. Square",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60,-200)
    t.color("#E60000")
    t.write("3. Pentagon",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -200)
    t.color("#E60000")
    t.write("4. Hexagon",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -200)
    t.color("#E60000")
    t.write("5. Heptagon",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -200)
    t.color("#E60000")
    t.write("6. Octagon",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -200)
    t.color("#E60000")
    t.write("7. Other",
            True, align="left", font=("Oswald", 30, "normal"))

selectscreen()


def selectcolor():
    t.bgcolor("#DBDBDB")
    t.pu()
    t.lt(90)
    t.fd(300)
    setp(60,0)
    t.write("Select a color.",
            True, align="center", font=("Oswald", 40, "normal"))
    w.sleep(1)
    setp(30, 0)
    t.write("(Control in Terminal)",
            True, align="center", font=("Oswald", 20, "normal"))
    w.sleep(1)
    setp(60,-200)
    t.color("#21B921")
    t.write("1. Triangle",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60,-200)
    t.color("#173BCF")
    t.write("2. Square",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60,-200)
    t.color("#E60000")
    t.write("3. Pentagon",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -200)
    t.color("#E60000")
    t.write("4. Hexagon",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -200)
    t.color("#E60000")
    t.write("5. Heptagon",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -200)
    t.color("#E60000")
    t.write("6. Octagon",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -200)
    t.color("#E60000")
    t.write("7. Other",
            True, align="left", font=("Oswald", 30, "normal"))

selectcolor()

t.clear()
t.pu()
t.setx(0)
t.sety(0)
t.lt(-90)
t.pd()
sides = 3
y = 500
v = y
d = 300
sha = -360 / sides
g = 0
x = sides
t.pu()
t.setx(d)
t.sety(-d)
t.pd()

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

y = v
t.pu()
t.setx(d-y)
t.sety(-d)
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

y = v
t.pu()
t.setx(d-y)
t.sety(-d)
t.pd()

# fix
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

t.exitonclick()
print(sides)
