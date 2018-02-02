import random as ran
import time as t

print("Calculating...")
n = ran.randint(10**99999, (10**100000)-1)
t.sleep(1)
print(n)
x = list(str(n))


def merge(x):
    if len(x) > 1:
        mid = len(x)//2
        left = x[:mid]
        right = x[mid:]

        merge(left)
        merge(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                x[k] = left[i]
                i += 1
            else:
                x[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            x[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            x[k] = right[j]
            j += 1
            k += 1

print("Calculating...")
start = t.time()
merge(x)
end = t.time()
print(x)
print("Time:", end - start)
