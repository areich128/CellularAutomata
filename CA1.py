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
    [-4, 0, 1],
    [-4, 0, 1],
    [-4, 0, 1]
])


def wrapped_convolve(array_2d, kernel):
    result = np.zeros_like(array_2d)
    for i in range(array_2d.shape[0]):
        for j in range(array_2d.shape[1]):
            conv_sum = 0
            for m in range(kernel.shape[0]):
                for n in range(kernel.shape[1]):
                    row_idx = (i - m) % array_2d.shape[0]
                    col_idx = (j - n) % array_2d.shape[1]
                    conv_sum += array_2d[row_idx, col_idx] * kernel[m, n]
            result[i][j] = conv_sum
    return result


plt.subplot(1, 3, 1)
plt.imshow(kernel1, cmap='Greys')
plt.colorbar()

plt.subplot(1, 3, 2)
plt.imshow(array_2d, cmap='Greys')
plt.colorbar()

plt.subplot(1, 3, 3)
plt.imshow(wrapped_convolve(array_2d, kernel1), cmap='Greys')
plt.colorbar()
plt.show()

if __name__ == '__main__':
    print('hello')



