import cv2 as cv
import numpy as np

img = cv.imread('OpenCv/Photos/pic2.jpg')
res = cv.resize(img, dsize=(500,750), interpolation=cv.INTER_CUBIC)
blank = np.zeros(res.shape[:2], dtype='uint8')
cv.imshow('Image', res)

b, g, r = cv.split(res)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])


cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)
print(res.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merge', merged)

cv.waitKey(0)