import turtle as t
import time as u


x = 50
y = 200
t.pu()
t.setx(450)
t.sety(-375)
t.pd()

tri = -120
squ = -90
pen = -72
hex = -60
sep = -51.42857142857143
oct = -45
non = -40
dec = -36


def draw(sha):
    for i in range(x):
        t.bk(y)
        t.lt(sha)
        t.bk(y)
        t.lt(sha)
        t.bk(y)
        t.lt(sha)
        y = y * .5
        t.bk(y)
        t.lt(sha)
        t.bk(y)
        t.rt(sha)
        t.bk(y)
        t.rt(sha)

print("1. Triangle")
print("2. Square")
print("3. Pentagon")
print("4. Hexagon")
print("5. Septagon")
print("1. Triangle")
print("1. Triangle")

pick = input("Shape:")
if pick == "1":
    sha = 360 / 3
elif pick == "2":
    sha = 360 / 4
elif pick == "3":
    sha = 360 / 5
elif pick == "4":
    sha = 360 / 6
elif pick == "5":
    sha = 360 / 7
elif pick == "6":
    sha = 360 / 8
elif pick == "7":
    sha = 360 / 9
elif pick == "8":
    sha = 360 / 10
else:
    exit()








