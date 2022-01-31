import cv2 as cv
import numpy as np

def mousePoints(event,x,y,flags,params):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x,y)

img = cv.imread("Pics/Hogwarts.jpg")
cv.imshow("Original image",img)
cv.setMouseCallback("Original image",mousePoints)

cv.waitKey(0)