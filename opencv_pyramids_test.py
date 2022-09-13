import cv2 as cv
import numpy as np
img = cv.imread('messi5.jpg')
lower_reso = cv.pyrDown(img)
lower_reso = cv.pyrDown(lower_reso)
lower_reso = cv.pyrDown(lower_reso)
hi_reso = cv.pyrUp(img)
hi_reso = cv.pyrUp(hi_reso)
cv.imshow('window',hi_reso)
k=cv.waitKey(0)