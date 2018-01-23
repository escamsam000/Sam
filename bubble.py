import random as ran
import time as t

print("Calculating...")
n = ran.randint(10**10000, 20**10000)
t.sleep(1)
print(n)
x = list(str(n))


def bubbleSort(x):
    for passnum in range(len(x)-1,0,-1):
        for i in range(passnum):
            if x[i] > x[i+1]:
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp
print("Calculating...")
bubbleSort(x)
print(x)