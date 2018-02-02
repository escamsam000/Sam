import random as ran
import time as t

print("Calculating...")
n = ran.randint(10**99999, (10**100000)-1)
t.sleep(1)
print(n)
x = list(str(n))


def insertion(x):
    for index in range(1, len(x)):
        current = x[index]
        position = index

        while position > 0 and x[position-1] > current:
            x[position] = x[position-1]
            position -= 1

        x[position] = current

print("Calculating...")
start = t.time()
insertion(x)
end = t.time()
print(x)
print(end - start)
