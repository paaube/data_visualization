import matplotlib.pyplot as plt

from random_walk import RandomWalk

# keep making new walks, as long as the program is active
while True:

    # make a random walk
    rw = RandomWalk(5000)
    rw.fill_walk()

    # plot the points in the walk
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_val, rw.y_val, linewidth = 2)

    # emphasize the first and last point
    ax.scatter(0, 0, c='blue', edgecolor='none', s=100)
    ax.scatter(rw.x_val[-1], rw.y_val[-1], c='red', edgecolors='none', s=100)

    # remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break