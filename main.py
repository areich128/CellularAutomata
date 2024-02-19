# This is a sample Python script.

#BUILDING BLOCKS TO LENIA

import numpy as np
import matplotlib.pyplot as plt


# array_2d = np.array([
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# ])

array_2d = np.random.random((100,100))

kernel = np.array([
    [0.8, 0.8, 0.8],
    [0.8, 0, 0.8],
    [0.8, 0.8, 0.8]
])

result = np.zeros_like(array_2d)

for i in range(1, array_2d.shape[0] - 1):
    for j in range(1, array_2d.shape[1] - 1):
        if (i - 1 >= 1) and (i+2 <= array_2d.shape[0]):
            if (j - 1 >= 1) and (j + 2 <= array_2d.shape[1]):
                result[i][j] = np.sum(array_2d[i-1:i+2, j-1:j+2] * kernel)
            

plt.subplot(1, 3, 1)
plt.imshow(kernel, cmap='Grays')
plt.colorbar()

plt.subplot(1, 3, 2)
plt.imshow(array_2d, cmap='Grays')
plt.colorbar()

plt.subplot(1, 3, 3)
plt.imshow(result, cmap='Grays')
plt.colorbar()
plt.show()

if __name__ == '__main__':
    print('hello')



