import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('OpenCv/Photos/pic2.jpg')
res = cv.resize(img, dsize=(500,750), interpolation=cv.INTER_CUBIC)

# cv.imshow('Image', res)

# BGR TO RGB

rgb = cv.cvtColor(res, cv.COLOR_BGR2RGB)

# Graph Image

plt.imshow(rgb)
plt.show()


# # BGR TO GRAYSCALE IMAGE

# gray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # BGR TO HSV

# hsv = cv.cvtColor(res, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# # BGR TO LAB

# lab = cv.cvtColor(res, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# cv.waitKey(0)