import random as ran
import time as t


def bint():
    print("How many integers would you like to sort?")
    t.sleep(2)
    print("A: 10")
    t.sleep(1)
    print("B: 100")
    t.sleep(1)
    print("C: 1000")
    t.sleep(1)
    print("D: 10000")
    t.sleep(1)
    print("E: 100000")
    boi = input("Type your selection: ").lower()
    if boi == "10" or boi == "ten" or boi == "a":
        d = 9
        e = 10
    elif boi == "100" or boi == "one hundred" or boi == "b":
        d = 99
        e = 100
    elif boi == "1000" or boi == "one thousand" or boi == "c":
        d = 999
        e = 1000
    elif boi == "10000" or boi == "ten thousand" or boi == "d":
        d = 9999
        e = 10000
    elif boi == "100000" or boi == "one hundred thousand" or boi == "e":
        d = 99999
        e = 100000
    else:
        print("\033[31mInvalid input.\033[0m")
        bint()

    print("Calculating integers...")
    n = ran.randint(10**d, (10**e)-1)
    t.sleep(1)
    print(n)
    t.sleep(2)
    global x
    x = list(str(n))


def insertion(x):
    for index in range(1, len(x)):
        current = x[index]
        position = index

        while position > 0 and x[position-1] > current:
            x[position] = x[position-1]
            position -= 1

        x[position] = current


def bubble(x):
    for num in range(len(x)-1, 0, -1):
        for i in range(num):
            if x[i] > x[i+1]:
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp


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
#
bint()
print("Sorting with Insertion Sort...")
start = t.time()
insertion(x)
end = t.time()
print(x)
pom = round(end - start, 5)
print("\033[31mTime:", pom, "seconds\033[0m")
t.sleep(1)
#
print("Sorting with Bubble Sort...")
start = t.time()
bubble(x)
end = t.time()
print(x)
pon = round(end - start, 5)
print("\033[31mTime:", pon, "seconds\033[0m")
t.sleep(1)
#
print("Sorting with Merge Sort...")
start = t.time()
merge(x)
end = t.time()
print(x)
poq = round(end - start, 5)
print("\033[31mTime:", poq, "seconds\033[0m")
