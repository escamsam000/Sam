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
    no = ran.randint(10**d, (10**e)-1)
    na = ran.randint(10**d, (10**e)-1)
    ni = ran.randint(10**d, (10**e)-1)
    t.sleep(2)
    global one
    one = list(str(no))
    print(len(one), "integers calculated.")
    global two
    two = list(str(na))
    global three
    three = list(str(ni))


def insertion(one):
    for index in range(1, len(one)):
        current = one[index]
        position = index

        while position > 0 and one[position-1] > current:
            one[position] = one[position-1]
            position -= 1

            one[position] = current


def bubble(three):
    for num in range(len(three)-1, 0, -1):
        for i in range(num):
            if three[i] > three[i+1]:
                temp = three[i]
                three[i] = three[i+1]
                three[i+1] = temp


def merge(two):
    if len(two) > 1:
        mid = len(two)//2
        left = two[:mid]
        right = two[mid:]

        merge(left)
        merge(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                two[k] = left[i]
                i += 1
            else:
                two[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            two[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            two[k] = right[j]
            j += 1
            k += 1


def run(funk):
    if funk == 1:
        name = "Insertion"
    elif funk == 2:
        name = "Merge"
    elif funk == 3:
        name = "Bubble"
    print("Sorting with\033[31m", name, "\033[0mSort...")
    start = t.time()
    if funk == 1:
        insertion(one)
        print(one)
    elif funk == 2:
        merge(two)
        print(two)
    elif funk == 3:
        bubble(three)
        print(three)
    end = t.time()
    pom = round(end - start, 5)
    print("\033[31mTime:", pom, "seconds\033[0m")
    t.sleep(1)

bint()
run(2)
run(3)
run(1)
