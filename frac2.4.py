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


def ssa(n, v, z, j):
    t.write(n, True, align="center", font=("Oswald", 30, "normal"))
    t.rt(90)
    t.fd(j)
    t.pd()
    for i in range(v):
        t.color("#%06x" % ran.randint(0, 0xFFFFFF))
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
    ss("1.", 3, 200, 15)
    # square
    setp(0, -100)
    ss("2.", 4, 175, 15)
    # pentagon
    setp(0, 200)
    ss("3.", 5, 120, 15)
    # hexagon
    setp(300, -400)
    ss("4.", 6, 110, 60)
    # heptagon
    setp(0, -100)
    ss("5.", 7, 90, 55)
    # octagon
    setp(0,200)
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
        ui = 175
    elif sides == 4:
        ui = 125
    elif sides == 5:
        ui = 120
    elif sides == 6:
        ui = 90
    elif sides == 7:
        ui = 70
    elif sides == 8:
        ui = 60

    if sides == 3:
        iu = 15
    elif sides == 4:
        iu = 15
    elif sides == 5:
        iu = 15
    elif sides == 6:
        iu = 30
    elif sides == 7:
        iu = 25
    elif sides == 8:
        iu = 40

    # red
    setp(200, -400)
    t.color("blue")
    ss("1.", sides, ui, iu)
    # blue
    setp(0, -100)
    t.color("green")
    ss("2.", sides, ui, iu)
    # yellow
    setp(0, 200)
    t.color("orange")
    ss("3.", sides, ui, iu)
    # green
    setp(200, -400)
    t.color("yellow")
    ss("4.", sides, ui, iu)
    # purple
    setp(0, -100)
    t.color("purple")
    ss("5.", sides, ui, iu)
    # orange
    setp(0, 200)
    t.color("red")
    ss("6.", sides, ui, iu)
    # black
    setp(200, -400)
    t.color("black")
    ss("7.", sides, ui, iu)
    # random
    setp(0, -100)
    t.color("#%06x" % ran.randint(0, 0xFFFFFF))
    ss("8.", sides, ui, iu)
    # assorted
    setp(0, 200)
    t.color("#%06x" % ran.randint(0, 0xFFFFFF))
    ssa("9.", sides, ui, iu)


def selectsize():
    t.clear()
    t.color("black")
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

    if sides == 3:
        w.sleep(.25)
        # 25
        setp(100, -425)
        ss("1.", sides, 25, 15)
        # 50
        setp(0, -125)
        ss("2.", sides, 50, 15)
        # 75
        setp(0, 175)
        ss("3.", sides, 75, 15)
        # 100
        setp(200, -425)
        ss("4.", sides, 100, 15)
        # 125
        setp(0, -125)
        ss("5.", sides, 125, 15)
        # 150
        setp(0, 175)
        ss("6.", sides, 150, 15)
        # 200
        setp(300, -425)
        ss("7.", sides, 200, 15)
        # 225
        setp(0, -125)
        ss("8.", sides, 225, 15)
        # 250
        setp(0, 175)
        ss("9.", sides, 250, 15)
    elif sides == 4:
        w.sleep(.25)
        # 25
        setp(100, -425)
        ss("1.", sides, 25, 15)
        # 50
        setp(0, -125)
        ss("2.", sides, 50, 15)
        # 75
        setp(0, 175)
        ss("3.", sides, 75, 15)
        # 100
        setp(200, -425)
        ss("4.", sides, 100, 15)
        # 125
        setp(0, -125)
        ss("5.", sides, 125, 15)
        # 150
        setp(0, 175)
        ss("6.", sides, 150, 15)
        # 200
        setp(300, -425)
        ss("7.", sides, 200, 15)
        # 225
        setp(0, -125)
        ss("8.", sides, 225, 15)
        # 250
        setp(0, 175)
        ss("9.", sides, 250, 15)
    elif sides == 5:
        w.sleep(.25)
        # 25
        setp(200, -400)
        ss("1.", sides, 25, 15)
        # 50
        setp(0, -100)
        ss("2.", sides, 50, 15)
        # 75
        setp(0, 200)
        ss("3.", sides, 75, 15)
        # 100
        setp(300, -400)
        ss("4.", sides, 100, 15)
        # 125
        setp(0, -100)
        ss("5.", sides, 125, 15)
        # 150
        setp(0, 200)
        ss("6.", sides, 150, 15)
    elif sides == 6:
        w.sleep(.25)
        # 25
        setp(200, -425)
        ss("1.", sides, 25, 15)
        # 50
        setp(0, -125)
        ss("2.", sides, 50, 20)
        # 75
        setp(0, 175)
        ss("3.", sides, 75, 20)
        # 100
        setp(400, -425)
        ss("4.", sides, 100, 20)
        # 125
        setp(0, -125)
        ss("5.", sides, 125, 20)
        # 150
        setp(0, 175)
        ss("6.", sides, 150, 30)
    elif sides == 7:
        w.sleep(.25)
        # 25
        setp(200, -425)
        ss("1.", sides, 25, 15)
        # 50
        setp(0, -125)
        ss("2.", sides, 50, 20)
        # 75
        setp(0, 175)
        ss("3.", sides, 75, 20)
        # 100
        setp(350, -425)
        ss("4.", sides, 100, 20)
        # 125
        setp(0, -125)
        ss("5.", sides, 125, 20)
        # 150
        setp(0, 175)
        ss("6.", sides, 150, 30)
    elif sides == 8:
        w.sleep(.25)
        # 25
        setp(200, -425)
        ss("1.", sides, 25, 30)
        # 50
        setp(0, -125)
        ss("2.", sides, 50, 40)
        # 75
        setp(0, 175)
        ss("3.", sides, 75, 50)
        # 100
        setp(350, -425)
        ss("4.", sides, 100, 60)
        # 125
        setp(0, -125)
        ss("5.", sides, 125, 70)





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
    choose = input("Select your size.\n")
    try:
        float(choose)
    except ValueError:
        print("This is not a valid input.\n")
        selects()
    global size
    if choose == "1":
        size = 25
    elif choose == "2":
        size = 50
    elif choose == "3":
        size = 75
    elif choose == "4":
        size = 100
    elif choose == "5":
        size = 125
    elif choose == "6":
        size = 150
    elif choose == "7":
        size = 200
    elif choose == "8":
        size = 225
    elif choose == "9":
        size = 250
    else:
        print("This is not a valid option.\n")
        selects()


def selectc():
    print("Select your color.")
    print("\033[31m(Note: 8 and 9 are random colors.)\033[0m")
    choose = input("\n")
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
