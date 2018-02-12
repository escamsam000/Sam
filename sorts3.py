import random as ran
import time as t


def bint():
    print("How many integers would you like to sort?")
    boi = input("Type your selection: ").lower()
    try:
        val = int(boi)
    except ValueError:
        print("\033[31mThat's not a number.\033[0m\n")
        t.sleep(2)
        bint()
    val = int(boi)
    d = val - 1
    e = val

    print("Calculating integers...")
    global no
    no = ran.randint(10**d, (10**e)-1)
    global na
    na = ran.randint(10**d, (10**e)-1)
    global ni
    ni = ran.randint(10**d, (10**e)-1)
    t.sleep(2)
    global one
    one = list(str(no))
    print("\033[31m" + str(len(one)), "integers calculated.\033[0m\n")
    t.sleep(2)
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
    name = ""
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
    print("Time:\033[31m", pom, "seconds\033[0m\n")
    t.sleep(1)


def listing():
    print("Would you like to view the list of integers?")
    bih = input("").lower()
    if bih == "yes":
        print(no)
    elif bih == "no":
        exit()
    else:
        print("\033[31mThat's not an option.\033[0m\n")
        listing()

bint()
run(2)
listing()
