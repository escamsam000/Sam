import turtle as t

# t.Screen()
t.speed(1)
t.pu()


# Draw a box with dimensions 120x160px with vertical divisions every 40px
def box(size):
    # Setup
    t.pd()
    x = 90
    t.fd(size * 60)
    # Draw the box
    for i in range(2):
        t.lt(x)
        t.fd(size * 120)
        t.lt(x)
        t.fd(size * 120)
    t.lt(x)
    # Draw each horizontal 40px
    t.fd(size * 40)
    t.lt(x)
    t.fd(size * 120)
    t.rt(x)
    t.fd(size * 40)
    t.rt(x)
    t.fd(size * 120)
    t.lt(x)
    t.bk(80)
    t.rt(90)
    t.bk(60)
    # Reset the pen
    t.pu()


def drawSpace():
    t.rt(360)


def drawA(size):
    # Draws an uppercase A
    a = 26.565
    x = 134.164
    # Setup
    t.pu()
    t.bk(size * 60)
    # Draw first leg
    t.pd()
    t.lt(90 - a)
    t.fd(size * x)
    # Draw second leg
    t.rt(180 - 2 * a)
    t.fd(size * x)
    # Draw center stem
    t.rt(180)
    t.fd(size * (x / 3))
    t.lt(90 - a)
    t.fd(size * 80)
    # Reset from A
    t.pu()
    t.lt(180)
    t.fd(size * 40)
    t.rt(90)
    t.fd(size * 40)
    t.lt(90)


def drawB(size):
    # Draws an uppercase B
    # Draw low horizontal stem
    t.pd()
    t.lt(180)
    t.fd(size * 60)
    # Draw vertical stem
    t.rt(90)
    t.fd(size * 120)
    # Draw high horizontal stem
    t.rt(90)
    t.fd(size * 60)
    # Draw the upper hump
    for i in range(180):
        t.fd(size * 0.524)
        t.rt(1)
    # Draw the lowerhump
    t.rt(180)
    for i in range(180):
        t.fd(size * 0.524)
        t.rt(1)
    # Finalize
    t.rt(180)
    t.pu()


def drawC(size):
    # draws uppercase C
    # go to center right
    t.fd(size * 60)
    t.lt(90)
    t.fd(size * 60)
    t.rt(180)
    # Draw c
    for i in range(360):
        if i < 45 or i > 315:
            t.pu()
        else:
            t.pd()
        t.fd(size * 1.048)
        t.rt(1)
    # finalize
    t.fd(size * 60)
    t.lt(90)
    t.bk(60)


def drawD(size):
    # Draws an uppercase D
    # Go to bottom corner
    t.bk(60)
    # Draw stem of D
    t.lt(90)
    t.pd()
    t.fd(size * 120)
    # Draw D
    t.rt(90)
    t.fd(size * 60)
    for i in range(180):
        t.fd(size * 1.047)
        t.rt(1)
    t.fd(size * 60)
    # Finalize
    t.rt(180)
    t.fd(size * 60)


def drawE(size):
    # Draws an uppercase E
    # Draw bottom stem
    t.pd()
    t.fd(size * 60)
    t.bk(120)
    # Draw middle stem
    t.lt(90)
    t.fd(size * 60)
    t.rt(90)
    t.fd(size * 120)
    t.bk(120)
    # Draw top stem
    t.lt(90)
    t.fd(size * 60)
    t.rt(90)
    t.fd(size * 120)
    # Finalize
    t.pu()
    t.bk(60)
    t.rt(90)
    t.fd(size * 120)
    t.lt(90)


def drawF(size):
    # Draws an uppercase F
    # Go to initial point
    t.bk(size * 60)
    # Draw first stem
    t.pd()
    t.lt(90)
    t.fd(size * 60)
    t.rt(90)
    t.fd(size * 120)
    t.bk(size * 120)
    # Draw top stem
    t.lt(90)
    t.fd(size * 60)
    t.rt(90)
    t.fd(size * 120)
    # Finalize
    t.pu()
    t.bk(size * 60)
    t.rt(90)
    t.fd(size * 120)
    t.lt(90)


def drawG(size):
    # Draws an uppercase G
    # Go to initial point
    t.fd(size * 60)
    t.lt(90)
    t.fd(size * 120)
    t.lt(90)
    # Draw the circle
    t.pd()
    t.fd(size * 60)
    for i in range(270):
        t.fd(size * 1.048)
        t.lt(1)
    # Draw stem
    t.lt(90)
    t.fd(size * 60)
    # Finalize
    t.pu()
    t.lt(90)
    t.fd(size * 60)
    t.lt(size * 90)


def drawH(size):
    # Draws an uppercase H
    # Go to initial point
    t.bk(size * 60)
    t.lt(90)
    # Draw first vertical
    t.pd()
    t.fd(size * 120)
    t.bk(size * 60)
    # Draw center
    t.rt(90)
    t.fd(size * 120)
    # Draw second vertical
    t.lt(90)
    t.fd(size * 60)
    t.bk(size * 120)
    # Finalize
    t.pu()
    t.rt(90)
    t.bk(size * 60)
    t.rt(180)


def drawI(size):
    # You get the pattern
    # Draw first horizontal
    t.pd()
    t.fd(size * 60)
    t.bk(size * 120)
    t.fd(size * 60)
    # Draw center
    t.rt(90)
    t.fd(size * 120)
    # Draw second horizontal
    t.lt(90)
    t.fd(size * 60)
    t.bk(size * 120)
    # Finalize
    t.pu()
    t.fd(size * 60)


def drawJ(size):
    # go to initial point
    t.bk(size * 60)
    t.lt(90)
    t.fd(size * 120)
    t.rt(90)
    # draw the straight parts
    t.pd()
    t.fd(size * 120)
    t.rt(90)
    t.fd(size * 60)
    # draw the curve
    for i in range(180):
        t.fd(size * 1.048)
        t.rt(1)
    # finalize
    t.pu()
    t.bk(size * 60)
    t.rt(90)
    t.fd(size * 60)


def drawK(size):
    x = 26.565
    d = 134.164
    # go to initial
    t.fd(size * 60)
    # draw diagonals
    t.pd()
    t.rt(180 + x)
    t.fd(size * d)
    t.rt(180 - 2 * x)
    t.fd(size * d)
    # get to stem
    t.lt(180)
    t.fd(size * d)
    t.lt(90 - x)
    t.fd(size * 60)
    t.bk(size * 120)
    # finalize
    t.pu()
    t.fd(size * 120)
    t.lt(90)
    t.fd(size * 60)


def drawL(size):
    # draw bottom stem
    t.pd()
    t.fd(size * 60)
    t.bk(size * 120)
    # draw vertical stem
    t.lt(90)
    t.fd(size * 120)
    # finalize
    t.bk(size * 120)
    t.rt(90)
    t.fd(size * 60)
    t.pu()


def drawM(size):
    x = 72.111
    b = 33.69
    # go to initial
    t.bk(size * 60)
    t.pd()
    # draw left stem
    t.lt(90)
    t.fd(size * 120)
    # draw center stem 1
    t.rt(90 + b)
    t.fd(size * x)
    # draw center stem 2
    t.lt(2 * b)
    t.fd(size * x)
    # draw right stem
    t.rt(b + 90)
    t.fd(size * 120)
    # finalize
    t.pu()
    t.lt(90)
    t.bk(size * 60)


def drawN(size):
    x = 169.706
    # go to initial
    t.bk(size * 60)
    # draw first stem
    t.pd()
    t.lt(90)
    t.fd(size * 120)
    # draw center stem
    t.rt(90 + 45)
    t.fd(size * x)
    # draw final stem
    t.lt(90 + 45)
    t.fd(size * 120)
    # finalize
    t.pu()
    t.bk(size * 120)
    t.rt(90)
    t.bk(size * 60)


def drawO(size):
    # draw o
    t.pd()
    for i in range(360):
        t.fd(size * 1.048)
        t.lt(1)
    t.pu()


def drawP(size):
    # Draws an uppercase B
    # Draw low horizontal stem
    t.lt(180)
    t.fd(size * 60)
    # Draw vertical stem
    t.pd()
    t.rt(90)
    t.fd(size * 120)
    # Draw high horizontal stem
    t.rt(90)
    t.fd(size * 60)
    # Draw the upper hump
    for i in range(180):
        t.fd(size * 0.524)
        t.rt(1)
    t.fd(size * 60)
    # finalize
    t.pu()
    t.lt(90)
    t.fd(size * 60)
    t.lt(90)
    t.fd(size * 60)


def drawQ(size):
    x = 84.853
    # draw o
    t.pd()
    for i in range(360):
        t.fd(size * 1.048)
        t.lt(1)
    # draw stem
    t.pu()
    t.fd(size * 60)
    t.pd()
    t.lt(180 - 45)
    t.fd(size * x)
    # finalize
    t.pu()
    t.rt(45)
    t.bk(size * 60)
    t.rt(90)


def drawR(size):
    x = 84.853
    # go to initial
    t.lt(180)
    t.fd(size * 60)
    # Draw vertical stem
    t.pd()
    t.rt(90)
    t.fd(size * 120)
    # Draw high horizontal stem
    t.rt(90)
    t.fd(size * 30)
    # Draw the hump
    for i in range(180):
        t.fd(size * 0.524)
        t.rt(1)
    t.fd(size * 30)
    # draw the diagonal stem
    t.rt(180)
    t.rt(45)
    t.fd(size * x)
    # finalize
    t.pu()
    t.lt(45)


def drawS(size):
    x = 0.524
    # initial position
    t.fd(size * 60)
    t.lt(90)
    t.fd(size * 120)
    t.fd(size * 30)
    t.pd()
    # draw top bar
    t.lt(90)
    t.fd(size * 30)
    # draw first hump
    for i in range(180):
        t.fd(size * x)
        t.lt(1)
    # draw second hump
    for i in range(180):
        t.fd(size * x)
        t.rt(1)
    t.fd(size * 30)
    # finalize
    t.pu()
    t.rt(180)
    t.fd(size * 30)


def drawT(size):
    # draw t
    t.pd()
    t.lt(90)
    t.fd(size * 120)
    t.rt(90)
    t.fd(size * 60)
    t.bk(size * 120)
    # finalize
    t.pu()
    t.fd(size * 60)
    t.rt(90)
    t.fd(size * 120)
    t.lt(90)


def drawU(size):
    x = 1.048
    # go to initial
    t.bk(size * 60)
    t.rt(90)
    t.bk(size * 60)
    # draw vertical stem
    t.pd()
    t.bk(size * 60)
    # draw curve
    t.fd(size * 60)
    for i in range(180):
        t.fd(size * x)
        t.lt(1)
    # draw vertical stem
    t.fd(size * 60)
    # finalize
    t.pu()
    t.bk(size * 120)
    t.rt(90)
    t.bk(size * 60)


def drawV(size):
    # Draws an uppercase A
    a = 26.565
    d = 134.164
    # Draw first leg
    t.pd()
    t.lt(90 - a)
    t.fd(size * d)
    # Draw second leg
    t.lt(180)
    t.fd(size * d)
    # Draw center stem
    t.rt(180 - 2 * a)
    t.fd(size * d)
    # finalize
    t.pu()
    t.rt(180)
    t.fd(size * d)
    t.rt(a - 90)


def drawW(size):
    t.pu()
    t.bk(60*size)
    t.rt(90)
    t.bk(120*size)
    # make left diagonal line
    t.pd()
    tilt = 14
    t.lt(tilt)
    t.fd(124*size)
    t.lt(90)
    t.lt(50)
    t.fd(68*size)
    t.lt(52)
    t.bk(68*size)
    t.lt(-40)
    t.fd(124*size)
    # reset (needs fixing)
    t.pu()
    t.rt(-12)
    t.bk(120*size)
    t.lt(90)
    t.fd(60*size)
    t.rt(90)


def drawX(size):
    t.pu()
    #go to bottom left
    t.bk(60*size)
    t.pd()
    #make first line
    tilt = 45
    t.lt(tilt)
    t.fd(170*size)
    t.lt(90)
    t.lt(tilt)
    #go to top left
    t.pu()
    t.fd(120*size)
    t.pd()
    #make second line
    tilt = 45
    t.rt(tilt)
    t.bk(170*size)
    t.rt(90)
    t.rt(tilt)
    # reset
    t.pu()
    t.bk(60 * size)
    t.rt(-90)


def drawY(size):
    #go to top right
    t.pu()
    t.fd(60*size)
    t.lt(90)
    t.fd(120*size)
    #make right diagonal line
    t.pd()
    tilt = 45
    t.rt(tilt)
    t.bk(85*size)
    t.rt(90)
    #make left diagonal line
    t.lt(0)
    t.bk(85*size)
    t.fd(85*size)
    #make vertical line
    t.rt(45)
    t.fd(60*size)
    #reset
    t.rt(180)


def drawZ(size):
    #make bottom line
    t.pd()
    t.fd(60*size)
    t.bk(120*size)
    #make diagonal line
    tilt = 45
    t.lt(tilt)
    t.fd(170*size)
    t.lt(90*size)
    #make top line
    t.lt(tilt)
    t.fd(120*size)
    #reset
    t.bk(60*size)
    t.pu()
    t.rt(90)
    t.bk(120*size)


def Draw(size, letter):
    let = str(letter)
    l = list(let)
    for x in l:
        if x == "A":
            drawA(size)
        if x == "B":
            drawB(size)
        if x == "C":
            drawC(size)
        if x == "D":
            drawD(size)
        if x == "E":
            drawE(size)
        if x == "F":
            drawF(size)
        if x == "G":
            drawG(size)
        if x == "H":
            drawH(size)
        if x == "I":
            drawI(size)
        if x == "J":
            drawJ(size)
        if x == "K":
            drawK(size)
        if x == "L":
            drawL(size)
        if x == "M":
            drawM(size)
        if x == "N":
            drawN(size)
        if x == "O":
            drawO(size)
        if x == "P":
            drawP(size)
        if x == "Q":
            drawQ(size)
        if x == "R":
            drawR(size)
        if x == "S":
            drawS(size)
        if x == "T":
            drawT(size)
        if x == "U":
            drawU(size)
        if x == "V":
            drawV(size)
        if x == "W":
            drawW(size)
        if x == "X":
            drawX(size)
        if x == "Y":
            drawY(size)
        if x == "Z":
            drawZ(size)
        if x == ' ':
            drawSpace()

def drawAll():
    w = input("Input Font Size(1-8): ")
    x = 0
    if w == "1":
        x = .25
    elif w == "2":
        x = .5
    elif w == "3":
        x = .75
    elif w == "4":
        x = 1
    elif w == "5":
        x = 1.25
    elif w == "6":
        x = 1.5
    elif w == "7":
        x = 1.75
    elif w == "8":
        x = 2
    else:
        print("This number is invalid.")
        drawAll()
    y = input("Input Message: ")
    z = y.upper()
    Draw(x,z)

drawZ(1)

