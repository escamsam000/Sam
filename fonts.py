import turtle as t
t.Screen()

def drawW():
    t.pu()
    t.backward(60)
    t.right(90)
    t.backward(120)
    # make left diagonal line
    t.pd()
    tilt = 14
    t.left(tilt)
    t.forward(124)
    t.left(90)
    t.lt(50)
    t.forward(68)
    t.lt(52)
    t.backward(68)
    t.lt(-40)
    t.forward(124)


def drawX():
    t.pu()
    #go to bottom left
    t.backward(60)
    t.pd()
    #make first line
    tilt = 45
    t.left(tilt)
    t.forward(170)
    t.left(90)
    t.left(tilt)
    #go to top left
    t.pu()
    t.forward(120)
    t.pd()
    #make second line
    tilt = 45
    t.right(tilt)
    t.backward(170)
    t.right(90)
    t.right(tilt)


def drawY():
    #go to top right
    t.pu()
    t.fd(60)
    t.lt(90)
    t.fd(120)
    #make right diagonal line
    t.pd()
    tilt = 45
    t.right(tilt)
    t.backward(85)
    t.right(90)
    #make left diagonal line
    t.left(0)
    t.backward(85)
    t.forward(85)
    #make vertical line
    t.right(45)
    t.forward(60)


def drawZ():
    #make bottom line
    t.pd()
    t.fd(60)
    t.bk(120)
    #make diagonal line
    tilt = 45
    t.lt(tilt)
    t.fd(170)
    t.lt(90)
    #make top line
    t.lt(tilt)
    t.fd(120)

drawY()
t.exitonclick()
