import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue, frames = capture.read()
    cv.imshow('Frames', frames)

    if(cv.waitKey(20) and 0xFF==ord('d')):
        break
capture.release()
cv.destroyAllWindows()