import cv2 as cv
import numpy as np

#This is a normal pic(bgr)
img = cv.imread('Pics/Hogwarts.jpg')
# cv.imshow("Harry",img)

#Converting img to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

#Blurring the image
blur = cv.GaussianBlur(img, (7,7),cv.BORDER_DEFAULT)
# cv.imshow('Blurred Img',blur)
#Edge Cascade
canny= cv.Canny(img,125,175) 
cv.imshow('Canny Edges',canny)

#Dilating the image
dilated = cv.dilate(canny,(5,5), iterations=5)
cv.imshow('dilated',dilated)

#Eroding
erodd = cv.erode(dilated,(3,3),iterations=1)
cv.imshow('erod',erodd)
cv.waitKey(0)