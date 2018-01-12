# import modules
import turtle as t
import time as w
import random as ran


def setp(x,y):
    t.bk(0+x)
    t.setx(0+y)


def ss(n, v, z, j):
    t.write(n, True, align="center", font=("Oswald", 30, "normal"))
    t.rt(90)
    t.fd(j)
    t.pd()
    for i in range(v):
        t.fd(z)
        t.lt(360 / v)
    t.lt(90)
    t.pu()
    w.sleep(.25)


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
    w.sleep(.25)
    setp(30, 0)
    t.write("(Control in Terminal)",
            True, align="center", font=("Oswald", 20, "normal"))
    w.sleep(.25)
    setp(60, 0)
    t.write("Select a shape.",
            True, align="center", font=("Oswald", 30, "normal"))
    w.sleep(.25)
    # triangle
    setp(200, -400)
    t.color("blue")
    ss("1.", 3, 200, 15)
    # square
    setp(0, -100)
    t.color("green")
    ss("2.", 4, 175, 15)
    # pentagon
    setp(0, 200)
    t.color("orange")
    ss("3.", 5, 120, 15)
    # hexagon
    setp(300, -400)
    t.color("yellow")
    ss("4.", 6, 110, 60)
    # heptagon
    setp(0, -100)
    t.color("purple")
    ss("5.", 7, 90, 55)
    # octagon
    setp(0,200)
    t.color("red")
    ss("6.", 8, 80, 55)



def selectcolor():
    t.clear()
    t.pu()
    t.setx(0)
    t.sety(0)
    t.fd(300)
    t.write("Select a color.",
            True, align="center", font=("Oswald", 40, "normal"))
    w.sleep(.25)
    setp(30, 0)
    t.write("(Control in Terminal)",
            True, align="center", font=("Oswald", 20, "normal"))
    w.sleep(.25)
    if sides == 3:
        ui = 200
    elif sides == 4:
        ui = 175
    elif sides == 5:
        ui = 120
    elif sides == 6:
        ui = 110
    elif sides == 7:
        ui = 90
    elif sides == 8:
        ui = 80
    # red blue yellow green purple orange black random assorted
    # red
    setp(200, -400)
    t.color("blue")
    ss("1.", sides, ui, 15)
    # blue
    setp(0, -100)
    t.color("green")
    ss("2.", sides, ui, 15)
    # yellow
    setp(0, 200)
    t.color("orange")
    ss("3.", sides, ui, 15)
    # green
    setp(300, -400)
    t.color("yellow")
    ss("4.", sides, ui, 15)
    # purple
    setp(0, -100)
    t.color("purple")
    ss("5.", sides, ui, 15)
    # orange
    setp(0, 200)
    t.color("red")
    ss("6.", sides, ui, 15)
    # black
    setp(0, 200)
    t.color("red")
    ss("6.", sides, ui, 15)
    # random
    setp(0, 200)
    t.color("red")
    ss("6.", sides, ui, 15)
    # assorted
    setp(0, 200)
    t.color("red")
    ss("6.", sides, ui, 15)


def selectsize():
    t.clear()
    t.pu()
    t.setx(0)
    t.sety(0)
    t.fd(300)
    t.write("Select a size.",
            True, align="center", font=("Oswald", 40, "normal"))
    w.sleep(.25)
    setp(30, 0)
    t.write("(Control in Terminal)",
            True, align="center", font=("Oswald", 20, "normal"))
    w.sleep(.25)
    setp(60, -100)
    t.write("25",True, align="center", font=("Oswald", 20, "normal"))
    t.pd()
    t.rt(90)
    # draw triangle
    t.fd(25)
    t.lt(120)
    t.fd(25)
    t.lt(120)
    t.fd(25)
    t.lt(120)
    t.lt(90)
    # continue
    t.pu()
    w.sleep(.25)
    setp(60, -100)
    t.write("50", True, align="center", font=("Oswald", 20, "normal"))
    t.pd()
    t.rt(90)
    # draw triangle
    t.fd(50)
    t.lt(120)
    t.fd(50)
    t.lt(120)
    t.fd(50)
    t.lt(120)
    t.lt(90)
    # continue
    t.pu()
    w.sleep(.25)
    setp(80, -100)
    t.write("75", True, align="center", font=("Oswald", 20, "normal"))
    t.pd()
    t.rt(90)
    # draw triangle
    t.fd(75)
    t.lt(120)
    t.fd(75)
    t.lt(120)
    t.fd(75)
    t.lt(120)
    t.lt(90)
    # continue
    t.pu()
    w.sleep(.25)
    setp(100, -100)
    t.write("100", True, align="center", font=("Oswald", 20, "normal"))
    t.pd()
    t.rt(90)
    # draw triangle
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.lt(90)
    # continue
    t.pu()
    w.sleep(.25)
    setp(120, -100)
    t.write("125", True, align="center", font=("Oswald", 20, "normal"))
    t.pd()
    t.rt(90)
    # draw triangle
    t.fd(125)
    t.lt(120)
    t.fd(125)
    t.lt(120)
    t.fd(125)
    t.lt(120)
    t.lt(90)
    # continue
    t.pu()
    w.sleep(.25)
    setp(140, -100)
    t.write("150", True, align="center", font=("Oswald", 20, "normal"))
    t.pd()
    t.rt(90)
    # draw triangle
    t.fd(150)
    t.lt(120)
    t.fd(150)
    t.lt(120)
    t.fd(150)
    t.lt(120)
    t.lt(90)
    # continue
    t.pu()


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
        cheese = input("How many sides does your shape have?.\n")
        try:
            float(cheese)
        except ValueError:
            print("This is not a valid input.\n")
            select()
        sides = int(cheese)
    else:
        print("Invalid input.\n")
        select()


def selects():
    print("Select your size.")
    print("\033[31m(Note: This is the size of each side.")
    print("Sizes over 100 for shapes with 4 or")
    print("more sides may not fit on the screen.)\033[0m")
    choose = input("\n")
    try:
        float(choose)
    except ValueError:
        print("This is not a valid input.\n")
        selects()
    global size
    if choose == "25":
        size = 25
    elif choose == "50":
        size = 50
    elif choose == "75":
        size = 75
    elif choose == "100":
        size = 100
    elif choose == "125":
        size = 125
    elif choose == "150":
        size = 150
    else:
        print("This is not a valid option.\n")
        selects()


def selectc():
    choose = input("Select your color.\n")
    global sides
    global size
    if choose == "1" or choose == "red":
        color = "#D33825"
        draw(sides, color, size)
    elif choose == "2" or choose == "blue":
        color = "#1B74F6"
        draw(sides, color, size)
    elif choose == "3" or choose == "yellow":
        color = "#DCBB16"
        draw(sides, color, size)
    elif choose == "4" or choose == "green":
        color = "#26B553"
        draw(sides, color, size)
    elif choose == "5" or choose == "purple":
        color = "#8326B5"
        draw(sides, color, size)
    elif choose == "6" or choose == "orange":
        color = "#F6891B"
        draw(sides, color, size)
    elif choose == "7" or choose == "black":
        color = "#000000"
        draw(sides, color, size)
    elif choose == "8" or choose == "random":
        color = "#%06x" % ran.randint(0, 0xFFFFFF)
        draw(sides, color, size)
    elif choose == "9" or choose == "assorted":
        draw2(sides, size)
    else:
        print("Invalid input.")
        selectc()


def draw(sides, color, size):
    t.clear()
    t.pu()
    t.setx(0)
    t.sety(0)
    t.rt(90)
    t.pd()

    d = 25
    h = 25
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

    t.lt(sha)
    t.fd(y)
    for i in range(sides):
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


def draw2(sides, size):
    t.clear()
    t.pu()
    t.setx(0)
    t.sety(0)
    t.rt(90)
    t.pd()

    d = 25
    h = 25
    y = size
    v = .75
    sha = -360 / sides
    t.pu()
    t.setx(d)
    t.sety(h)
    t.pd()
    y /= v
    t.speed(0)

    t.lt(sha)
    t.fd(y)
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

selectscreen()
select()
selectsize()
selects()
selectcolor()
selectc()