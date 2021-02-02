import cv2 as cv
import numpy as np

blank = np.zeros((500, 500 , 3), dtype='uint8')

cv.imshow('Blank', blank)
# Draw A Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,250,0), thickness=-1)
cv.imshow('Rectangle', blank)

# Draw a circle
cv.circle(blank, (250,250), 100, (0,0,250), thickness=-1)
cv.imshow('Circle', blank)

# Draw a Line
cv.line(blank, (10,10), (100,100), (0,250,0), thickness=-1)
cv.imshow('Line', blank)
cv.waitKey(0)