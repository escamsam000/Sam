import random as ran
import time as t

print("Calculating...")
n = ran.randint(10**10000, 20**10000)
t.sleep(1)
print(n)
x = list(str(n))


def insertionSort(x):
    for index in range(1,len(x)):
        currentvalue = x[index]
        position = index

        while position > 0 and x[position-1] > currentvalue:
            x[position] = x[position-1]
            position -= 1

        x[position] = currentvalue
print("Calculating...")
insertionSort(x)
print(x)