import cv2 as cv
import numpy as np
cap = cv.VideoCapture(1)
#cap = cv.VideoCapture('video_test.avi')
while(1):
    # Take each frame
    _, frame = cap.read()


    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([100,43,43])
    upper_blue = np.array([130,255,255])

    lower_red = np.array([0,43,43])
    upper_red = np.array([10,255,255])

    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)

    blur = cv.GaussianBlur(mask_blue,(5,5),0)


    ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

    mask_red = cv.inRange(hsv, lower_red, upper_red)
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= th3)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask_blue)
    cv.imshow('res',res)
    cv.imshow('test',th3)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
