import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


kernel = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

array = np.random.randint(2, size=(100, 100)) < 0.001
array = array.astype(int)


# Function to update the plot in each animation frame
def update(frame):
    global array
    new_array = array.copy()
    conv_sum = 0
    for i in range(100):
        for j in range(100):
            kernel_sum = np.sum(array[max(0, i-1):min(100, i+2), max(0, j-1):min(100, j+2)])
            conv_sum = kernel_sum - array[i][j]
            if array[i][j] == 0 and conv_sum == 3:
                new_array[i][j] = 1
            elif array[i][j] == 1 and conv_sum < 2 or conv_sum > 3:
                new_array[i][j] = 0

    array = new_array
    # push test change
    im.set_array(array)
    return [im]


# Create a figure and axis
fig, ax = plt.subplots()

# Display the initial array as an image
im = ax.imshow(array, cmap='viridis', animated=True)

# Set up the animation
ani = FuncAnimation(fig, update, frames=range(1000), interval=100, blit=True)

plt.colorbar(im)
plt.show()
