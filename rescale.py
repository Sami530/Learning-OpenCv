from turtle import width
import cv2 as cv

# img = cv.imread('Pics/Hogwarts.jpg')
# cv.imshow('Hogwarts', img)

def rescaleframe(frame,scale=0.25 ):
    #for images vid and live vid
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #only for live vid
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('vid/Vid1.mp4')

while True:
    isTrue,frame = capture.read()#reads vid frame by frame
    frame_resized = rescaleframe(frame)
    cv.imshow('Video',frame)
    cv.imshow('Resized Vid',frame)
    
    
    if cv.waitKey(20) & 0xFF==ord('d'): #if d is press destroy
        break

capture.release()
cv.waitKey(0)

cv.waitKey(0)