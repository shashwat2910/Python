import cv2 as cv
import numpy as np

img = cv.imread('OpenCv/Photos/pic1.jpg')
res = cv.resize(img, dsize=(500, 750), interpolation=cv.INTER_CUBIC)

# Translation

def translate(res, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (res.shape[1], res.shape[0])
    return cv.warpAffine(res, transMat, dimensions)

# -x --> Left
# -y --> Up
# x  --> Right
# y  --> Down

translated = translate(res, 100, 100)
cv.imshow('Translated', translated)
# Rotation
def rotate(res, angle, rotPoint=None):
    (height,width) = res.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height //2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(res, rotMat, dimensions)

rotated = rotate(res, 45)
cv.imshow('Rotated', rotated)

# Flipping
flip = cv.flip(res, -1)
cv.imshow('Flipped',flip)

cv.waitKey(0)