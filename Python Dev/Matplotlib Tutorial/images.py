import numpy as np
from matplotlib import pyplot as plt
from scipy.misc import imread, imresize

img = imread('unnamed.jpg')
img_tinted = img*[1, 0.9, 0.7]

plt.subplot(2, 1, 1)
plt.title('Original Image')
plt.imshow(img)

plt.subplot(2, 1, 2)
plt.title('Tinted Image')

img_tinted_correct = np.uint8(img_tinted)

plt.imshow(img_tinted_correct)
plt.show()