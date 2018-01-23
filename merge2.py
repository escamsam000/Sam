import random as ran
import time as t

print("Calculating...")
n = ran.randint(10**100000, (10**100001)-1)
t.sleep(1)
print(n)
x = list(str(n))


def mergeSort(x):
    if len(x) > 1:
        mid = len(x)//2
        lefthalf = x[:mid]
        righthalf = x[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                x[k] = lefthalf[i]
                i += 1
            else:
                x[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            x[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            x[k] = righthalf[j]
            j += 1
            k += 1


mergeSort(x)
print(x)