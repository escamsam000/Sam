import matplotlib.pyplot as plt
import time as t


def v_chart(xx, yy):
    # Number of bars
    num_bars = len(xx)
    # This list is the point on the y-axis where each
    # Bar is centered. Here it will be [1, 2, 3...]
    positions = range(1, num_bars+1)
    plt.bar(positions, yy, align='center')
    # Set the label of each bar
    plt.xticks(positions, xx)
    plt.xlabel(name)
    plt.ylabel(units)
    plt.title(title)
    # Turns on the grid which may assist in visual estimation
    plt.grid()
    plt.show()


def h_chart(yy, xx):
    # Number of bars
    num_bars = len(yy)
    # This list is the point on the y-axis where each
    # Bar is centered. Here it will be [1, 2, 3...]
    positions = range(1, num_bars+1)
    plt.barh(positions, xx, align='center')
    # Set the label of each bar
    plt.yticks(positions, xx)
    plt.xlabel(units)
    plt.ylabel(name)
    plt.title(title)
    # Turns on the grid which may assist in visual estimation
    plt.grid()
    plt.show()


# to do - add options

if __name__ == '__main__':
    print("Welcome to the bar graph program.")
    t.sleep(2)
    print("Set up your graph with the options below.\n")
    # Temperatures for this week
    t.sleep(2)
    print("Choose your bar alignment.")
    print("A. Vertical")
    a = input("B. Horizontal\n")
    title = input("Input the title of your bar graph:\n")
    t.sleep(2)

    # Corresponding days
    x = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    v_chart(x, y)
