# using matplotlib to allow the user to draw the initial conditions for the GoL simulation

import numpy as np
import matplotlib.pyplot as plt

universe = np.zeros((100, 100))


def disp_matrix(matrix):
    plt.imshow(matrix, cmap='binary')
    plt.show()


def point_intput(matrix):
    fig, ax = plt.subplots()
    ax.plot(np.zeros(matrix.size[0], matrix.size[1]))
    alive_cells = plt.ginput()

