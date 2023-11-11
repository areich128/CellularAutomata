# This is a sample Python script.

# BUILDING BLOCKS TO LENIA
# https://www.youtube.com/watch?v=mSy4z8nDLno

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


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

image_path = 'C://Users//zhasi//Downloads//convolutiontest.png'
img_arr = Image.open(image_path)
gray_img = img_arr.convert('L')
garray_2d = np.array(gray_img)
array_2d = garray_2d / 255.0

# array_2d = np.random.random((100,100))

kernel1 = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])


def convolve(array_2d, kernel):
    result = np.zeros_like(array_2d)
    for i in range(1, array_2d.shape[0] - 1):
        for j in range(1, array_2d.shape[1] - 1):
            # working on wrap-around function here
            result[i][j] = np.sum(array_2d[i-1:i+2, j-1:j+2] * kernel)
    return result


plt.subplot(1, 3, 1)
plt.imshow(kernel1, cmap='Greys')
plt.colorbar()

plt.subplot(1, 3, 2)
plt.imshow(array_2d, cmap='Greys')
plt.colorbar()

plt.subplot(1, 3, 3)
plt.imshow(convolve(array_2d, kernel1), cmap='Greys')
plt.colorbar()
plt.show()

if __name__ == '__main__':
    print('hello')



