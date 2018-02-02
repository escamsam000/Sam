import random as ran
import time as t

print("Calculating...")
n = ran.randint(10**99999, (10**100000)-1)
t.sleep(1)
print(n)
x = list(str(n))


def bubble(x):
    for num in range(len(x)-1, 0, -1):
        for i in range(num):
            if x[i] > x[i+1]:
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp

print("Calculating...")
start = t.time()
bubble(x)
end = t.time()
print(x)
print(end - start)
