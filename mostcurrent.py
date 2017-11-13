# import modules
import turtle as t
import time as w
import random as ran


def setp(x,y):
    t.bk(0+x)
    t.setx(0+y)


def selectscreen():
    t.clear()
    t.pu()
    t.setx(0)
    t.sety(0)
    t.bgcolor("#DBDBDB")
    t.pu()
    t.lt(90)
    t.fd(300)
    t.write("Fractal Generator",
            True, align="center", font=("Oswald", 40, "normal"))
    w.sleep(1)
    setp(30, 0)
    t.write("(Control in Terminal)",
            True, align="center", font=("Oswald", 20, "normal"))
    w.sleep(1)
    setp(60, 0)
    t.write("Select a shape.",
            True, align="center", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -100)
    t.color("#26B553")
    t.write("1. Triangle",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -100)
    t.color("#EE23BB")
    t.write("2. Square",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -100)
    t.color("#2FC4CE")
    t.write("3. Pentagon",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -100)
    t.color("#8326B5")
    t.write("4. Hexagon",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -100)
    t.color("#EE7723")
    t.write("5. Heptagon",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -100)
    t.color("#D33825")
    t.write("6. Octagon",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -100)
    t.color("#000000")
    t.write("7. Other",
            True, align="left", font=("Oswald", 30, "normal"))


def selectcolor():
    t.clear()
    t.pu()
    t.setx(0)
    t.sety(0)
    t.fd(300)
    t.write("Select a color.",
            True, align="center", font=("Oswald", 40, "normal"))
    w.sleep(1)
    setp(30, 0)
    t.write("(Control in Terminal)",
            True, align="center", font=("Oswald", 20, "normal"))
    w.sleep(1)
    setp(60, -100)
    t.color("#D33825")
    t.write("1. Red",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -100)
    t.color("#1B74F6")
    t.write("2. Blue",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -100)
    t.color("#DCBB16")
    t.write("3. Yellow",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -100)
    t.color("#26B553")
    t.write("4. Green",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -100)
    t.color("#8326B5")
    t.write("5. Purple",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -100)
    t.color("#F6891B")
    t.write("6. Orange",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -100)
    t.color("#000000")
    t.write("7. Black",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -100)
    t.color("#%06x" % ran.randint(0, 0xFFFFFF))
    t.write("8. Random",
            True, align="left", font=("Oswald", 30, "normal"))
    w.sleep(1)
    setp(60, -100)
    t.color("#%06x" % ran.randint(0, 0xFFFFFF))
    t.write("9. ",
            True, align="left", font=("Oswald", 30, "normal"))
    t.color("#%06x" % ran.randint(0, 0xFFFFFF))
    t.write("A",
            True, align="left", font=("Oswald", 30, "normal"))
    t.color("#%06x" % ran.randint(0, 0xFFFFFF))
    t.write("s",
            True, align="left", font=("Oswald", 30, "normal"))
    t.color("#%06x" % ran.randint(0, 0xFFFFFF))
    t.write("s",
            True, align="left", font=("Oswald", 30, "normal"))
    t.color("#%06x" % ran.randint(0, 0xFFFFFF))
    t.write("o",
            True, align="left", font=("Oswald", 30, "normal"))
    t.color("#%06x" % ran.randint(0, 0xFFFFFF))
    t.write("r",
            True, align="left", font=("Oswald", 30, "normal"))
    t.color("#%06x" % ran.randint(0, 0xFFFFFF))
    t.write("t",
            True, align="left", font=("Oswald", 30, "normal"))
    t.color("#%06x" % ran.randint(0, 0xFFFFFF))
    t.write("e",
            True, align="left", font=("Oswald", 30, "normal"))
    t.color("#%06x" % ran.randint(0, 0xFFFFFF))
    t.write("d",
            True, align="left", font=("Oswald", 30, "normal"))


def select():
    choose = input("Select your shape.\n")
    global sides
    if choose == "1" or choose == "triangle":
        sides = 3
    elif choose == "2" or choose == "square":
        sides = 4
    elif choose == "3" or choose == "pentagon":
        sides = 5
    elif choose == "4" or choose == "hexagon":
        sides = 6
    elif choose == "5" or choose == "heptagon":
        sides = 7
    elif choose == "6" or choose == "octagon":
        sides = 8
    elif choose == "7" or choose == "other":
        sides = 9
    else:
        print("Invalid input.")
        select()


def selectc():
    choose = input("Select your color.\n")
    global sides
    if choose == "1" or choose == "red":
        color = "#D33825"
        draw(sides, color)
    elif choose == "2" or choose == "blue":
        color = "#1B74F6"
        draw(sides, color)
    elif choose == "3" or choose == "yellow":
        color = "#DCBB16"
        draw(sides, color)
    elif choose == "4" or choose == "green":
        color = "#26B553"
        draw(sides, color)
    elif choose == "5" or choose == "purple":
        color = "#8326B5"
        draw(sides, color)
    elif choose == "6" or choose == "orange":
        color = "#F6891B"
        draw(sides, color)
    elif choose == "7" or choose == "black":
        color = "#000000"
        draw(sides, color)
    elif choose == "8" or choose == "random":
        color = "#%06x" % ran.randint(0, 0xFFFFFF)
        draw(sides, color)
    elif choose == "9" or choose == "assorted":
        draw2(sides)
    else:
        print("Invalid input.")
        selectc()


def draw(sides, color):
    t.clear()
    t.pu()
    t.setx(0)
    t.sety(0)
    t.lt(-90)
    w.sleep(8)
    t.pd()
    y = 500
    v = y
    d = 300
    sha = -360 / sides
    t.pu()
    t.setx(d)
    t.sety(-d)
    t.pd()
    t.color(color)
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
    t.setx(d - y)
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
    t.setx(d - y)
    t.sety(-d)
    t.pd()
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


def draw2(sides):
    t.clear()
    t.pu()
    t.setx(0)
    t.sety(0)
    t.lt(-90)
    w.sleep(8)
    t.pd()
    y = 500
    v = y
    d = 300
    sha = -360 / sides
    t.pu()
    t.setx(d)
    t.sety(-d)
    t.pd()
    for i in range(sides):
        t.color("#%06x" % ran.randint(0, 0xFFFFFF))
        t.bk(y)
        t.lt(sha)
    for i in range(5 * sides):
        t.color("#%06x" % ran.randint(0, 0xFFFFFF))
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
    t.setx(d - y)
    t.sety(-d)
    t.pd()
    for i in range(5 * sides):
        t.color("#%06x" % ran.randint(0, 0xFFFFFF))
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
    t.setx(d - y)
    t.sety(-d)
    t.pd()
    t.lt(sha)
    for i in range(5 * sides):
        t.color("#%06x" % ran.randint(0, 0xFFFFFF))
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


def restart():
    selectscreen()
    select()
    selectcolor()
    selectc()


def res():
    chooz = input("Would you like to draw something else? (Yes/No)\n")
    choose = chooz.lower()
    if choose == "yes":
        restart()
    elif choose == "no":
        exit()
    else:
        print("Invalid input.\n\n")
        res()


selectscreen()
select()
selectcolor()
selectc()

