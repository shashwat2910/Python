import cv2 as cv



img = cv.imread('OpenCv/Photos/pic2.jpg')
resoriginal = cv.resize(img, dsize=(500, 750), interpolation=cv.INTER_CUBIC)
cv.imshow('Image', resoriginal)

# GrayScale Image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
res = cv.resize(gray, dsize=(500, 750), interpolation=cv.INTER_CUBIC)
cv.imshow('Gray', res)

# Edge Cascade

canny = cv.Canny(resoriginal, 125, 175)
cv.imshow('Canny', canny)

# Dilating The Image

dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

# Eroding

eroded = cv.erode()
cv.waitKey(0)