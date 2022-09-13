import cv2 as cv
import sys
try:
    img = cv.imread(cv.samples.findFile("starry_night.jpg"),cv.IMREAD_COLOR  )
except:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)