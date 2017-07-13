import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE)


plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
