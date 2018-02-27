import matplotlib.pyplot as plt


def create_bar_chart(xx, yy):
    # Number of bars
    num_bars = len(xx)
    # This list is the point on the y-axis where each
    # Bar is centered. Here it will be [1, 2, 3...]
    positions = range(1, num_bars+1)
    plt.bar(positions, yy, align='center')
    # Set the label of each bar
    plt.xticks(positions, xx)
    plt.xlabel('Day')
    plt.ylabel('Temperature (F°)')
    plt.title('Weather for the Week')
    # Turns on the grid which may assist in visual estimation
    plt.grid()
    plt.show()


if __name__ == '__main__':
    # Temperatures for this week
    y = [79, 83, 71, 70, 69, 76,  76]
    # Corresponding days
    v = "79, 71, 83, 60, 71, 52, 70, 52, 69, 61, 76, 65, 76, 56, 71, 52"
    x = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    create_bar_chart(x, y)
