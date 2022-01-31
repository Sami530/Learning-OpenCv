import cv2 as cv

framewidth = 600
frameheight = 360

cap = cv.VideoCapture("Vid\Vid1.mp4")

while True:
    success,img = cap.read()
    cv.imshow("Videp",img)