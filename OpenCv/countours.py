import cv2 as cv
import numpy as np

img = cv.imread('OpenCv/Photos/pic2.jpg')
res = cv.resize(img, dsize=(500,750), interpolation=cv.INTER_CUBIC)

gray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# canny = cv.Canny(res, 125, 125)
# cv.imshow('Canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

coutours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(coutours)} contours found')
cv.waitKey(0)