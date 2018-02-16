import time


# introduction to concepts
def intro():
    time.sleep(1)
    print("This program is meant to demonstrate how sorting algorithms")
    print("work; in general and within python code.\n")
    time.sleep(2)
    print("Now the program will demonstrate examples of sorting algorithms.\n")
    text()


# begin demonstration
def text():
    print("To begin, you need to type in 10 numbers.\n")
    time.sleep(2)
    main()


# main function
def main():
    global boi
    boi = input("Type your selection:\n").lower()
    try:
        int(boi)
    except ValueError:
        print("\033[31mYou need to type in numbers.\033[0m\n")
        time.sleep(2)
        main()
    if len(boi) < 10:
        z = (10 - len(boi))
        print("\033[31mYou need to have", z, "more numbers.\033[0m\n")
        time.sleep(2)
        main()
    elif len(boi) > 10:
        z = (len(boi) - 10)
        print("\033[31mYou need to have", z, "less numbers.\033[0m\n")
        time.sleep(2)
        main()


def main2(boi):
    global a
    a = list(str(boi))
    global b
    b = list(str(boi))
    global c
    c = list(str(boi))
    print("Now the program will sort your numbers in order.\n")
    time.sleep(2)
    print("To do this, the program will use three different sorting")
    print("algorithms, Insertion Sort, Bubble Sort, and Merge Sort.")


def insertion(a):
    for index in range(1, len(a)):
        current = a[index]
        position = index

        while position > 0 and a[position-1] > current:
            a[position] = a[position-1]
            position -= 1

            a[position] = current

        print(a)
    print("Insertion Sort Finished.")
    time.sleep(2)


def bubble(b):
    for num in range(len(b)-1, 0, -1):
        for i in range(num):
            if b[i] > b[i+1]:
                temp = b[i]
                b[i] = b[i+1]
                b[i+1] = temp
        print(b)
    print("Bubble Sort Finished.")
    time.sleep(2)


def merge(c):
    if len(c) > 1:
        mid = len(c)//2
        left = c[:mid]
        right = c[mid:]

        merge(left)
        merge(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                c[k] = left[i]
                i += 1
            else:
                c[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            c[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            c[k] = right[j]
            j += 1
            k += 1
        print(c)


def done():
    print("Merge Sort Finished.")
    time.sleep(2)


def skip():
    y = input("Would you like to skip the intro? \033[31m(Yes/No)\033[0m\n").lower()
    if y == "yes":
        text()
    elif y == "no":
        intro()

skip()
main2(boi)
insertion(a)
bubble(b)
merge(c)
done()
