from os import path
from turtle import width
import cv2 as cv
from cv2 import waitKey

path ="Pics/HarryPotter1.jpg"
img = cv.imread(path)
# print(img.shape)
width,height = 200,200
# imgresize = cv.resize(img,(width,height))
# print(imgresize.shape)

# cv.imshow("Harry Potter",imgresize)

#Cropping the image
imgcropped = img[100: 175,0:100]
cv.imshow("Cropped",imgcropped)

cv,waitKey(0)