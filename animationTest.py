import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


kernel = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

# array = np.zeros((100, 100))
# center = (50, 50)
# radius = 10
# x, y = np.indices((100, 100))
# distance = np.sqrt((x - center[0]) ** 2 + (y - center[1]) ** 2)
# array[distance <= radius] = 1
array = np.random.randint(2, size=(100, 100)) < 0.005
array = array.astype(int)
# array = np.zeros((100,100))
# array[:][49:55] = 1
age = np.zeros_like(array)

# Function to update the plot in each animation frame
def update(frame):
    global array, age
    new_array = array.copy()
    conv_sum = 0
    for i in range(1, 99):
        for j in range(1, 99):
            kernel_sum = np.sum(array[max(0, i-1):min(100, i+2), max(0, j-1):min(100, j+2)])
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
    # push test change
    im.set_array(normalized_age)
    print(age[50][50])

    return [im]


# Create a figure and axis
fig, ax = plt.subplots()

# Display the initial array as an image
im = ax.imshow(array, cmap='hot', animated=True)

# Set up the animation
ani = FuncAnimation(fig, update, frames=range(10000), interval=100, blit=True)

plt.colorbar(im)
plt.show()
