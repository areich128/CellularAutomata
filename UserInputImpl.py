# using matplotlib to allow the user to draw the initial conditions for the GoL simulation

import numpy as np
import matplotlib.pyplot as plt


def disp_matrix(matrix):
    plt.imshow(matrix, cmap='binary')
    plt.show()


# This function needs to
# 1. prompt user input to click
# 2. record coords of each click
# 3. set coords of clicks to 1 and return that 

def initialize_world(shape):
    world = np.zeros(shape, dtype=int)
    fig, ax = plt.subplots()
    ax.imshow(world, cmap='binary', interpolation='none')
    while True:
        print("click on figure (press q to exit")
        click = plt.ginput(n=1, timeout=-1, show_clicks=False)
        if click:
            x, y = int(round(click[0][0])), int(round(click[0][1]))
            world[y, x] = 1
            ax.imshow(world, cmap='binary', interpolation='none')
            plt.draw()
        else:
            key = plt.waitforbuttonpress()
            if key and plt.get_current_fig_manager().toolbar.mode == '':
                break

    plt.close()

    return world


shape = (100, 100)
start_universe = initialize_world(shape)
# fig, ax = plt.subplots()
# ax.imshow(start_universe)
