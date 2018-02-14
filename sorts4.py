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
    print("To begin, you need to type in 20 numbers.\n")
    time.sleep(2)
    main()


# main function
def main():
    boi = input("Type your selection:\n").lower()
    try:
        int(boi)
    except ValueError:
        print("\033[31mYou need to type in numbers.\033[0m\n")
        time.sleep(2)
        main()
    if len(boi) < 20:
        z = (20 - len(boi))
        print("\033[31mYou need to have", z, "more numbers.\033[0m\n")
        time.sleep(2)
        main()
    elif len(boi) > 20:
        z = (len(boi) - 20)
        print("\033[31mYou need to have", z, "less numbers.\033[0m\n")
        time.sleep(2)
        main()
    a = list(str(boi))
    b = list(str(boi))
    c = list(str(boi))
    print("Now the program will sort your numbers in order.\n")
    time.sleep(2)
    print("To do this, the program will use three different sorting")
    print("algorithms, Insertion Sort, Bubble Sort, and Merge Sort.")


def skip():
    y = input("Would you like to skip the intro? \033[31m(Yes/No)\033[0m\n").lower()
    if y == "yes":
        text()
    elif y == "no":
        intro()

skip()
