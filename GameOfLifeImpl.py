import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# array = np.zeros((100, 100))
# center = (50, 50)
# radius = 10
# x, y = np.indices((100, 100))
# distance = np.sqrt((x - center[0]) ** 2 + (y - center[1]) ** 2)
# array[distance <= radius] = 1

array = np.random.randint(2, size=(150, 150)) < 0.001
array = array.astype(int)

# array = np.zeros((100, 100))
# array[1][40:60] = 1
# array[99][40:60] = 1
age = np.zeros_like(array)
age[1][1] = 1


# Function to update the plot in each animation frame, with GoL rules
def update(frame):
    global array, age
    new_array = array.copy()
    kernel = np.ones((3, 3))
    conv_sum = 0
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            conv_sum = 0
            # kernel_sum = np.sum(array[max(0, i - 1):min(100, i + 2), max(0, j - 1):min(100, j + 2)])
            # conv_sum = kernel_sum - array[i][j]
            kernel_sum = 0
            for m in range(kernel.shape[0]):
                for n in range(kernel.shape[1]):
                    row_idx = ((i + m) % array.shape[0]) - 1
                    col_idx = ((j + n) % array.shape[1]) - 1
                    kernel_sum += array[row_idx, col_idx]
                    conv_sum = kernel_sum - array[i][j]
            if array[i][j] == 0 and conv_sum == 3:
                age[i][j] += 1
                new_array[i][j] = 1
            elif array[i][j] == 1 and (conv_sum < 2 or conv_sum > 3):
                new_array[i][j] = 0
                age[i][j] = 0
            elif array[i][j] == 1:
                age[i][j] += 1

    array = new_array
    normalized_age = age / np.max(age)
    age_status = 0
    if age_status == 0:
        im.set_array(array)
    elif age_status == 1:
        im.set_array(normalized_age)

    return [im]


# Create a figure and axis
fig, ax = plt.subplots()

# Display the initial array as an image
im = ax.imshow(array, cmap='hot', animated=True)

# Set up the animation
ani = FuncAnimation(fig, update, frames=range(10000), interval=100, blit=True)

plt.colorbar(im)
plt.show()
