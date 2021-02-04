import cv2 as cv
import numpy as np

res = cv.imread('OpenCv/Photos/pic2.jpg')
img = cv.resize(res, dsize=(500,750), interpolation=cv.INTER_CUBIC)
cv.imshow('Image', img)

# Averaging

average = cv.blur(img, (9,9))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (9,9), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img , 3)
cv.imshow('Median', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 15) 
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)