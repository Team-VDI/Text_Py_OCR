import cv2
import numpy as np

#edge detect test
img = cv2.imread('res/cat2.jpg')
cv2.imshow('Original', img)

new_img = cv2.Canny(img, 0, 200)
cv2.imshow('new image', new_img)

cv2.waitKey(0)