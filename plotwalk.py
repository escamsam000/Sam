import matplotlib.pyplot as plt
from b import RandomWalk
# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(6, 4))
    # Plot the points, and show the plot.
    point_numbers = list(range(rw.num_points))
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.cool, edgecolor='none', s=1)

    plt.show()

    keep_running = input("Make another walk? (y/n): ").lower()
    if keep_running == 'n':
        break
