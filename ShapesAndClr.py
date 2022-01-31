#Drawing and writing text in img
import cv2 as cv
import numpy as np

# img = cv.imread('Pics/HarryPotter1.jpg')
# #Stanalone pic

# blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank',blank) 

# #Paint the img by some color
# blank[200:300, 300:400] = 0,255,0 ##rgb color
# cv.imshow('Green',blank)

# #Draw a rectangle
# cv.rectangle(blank,(0,0),(250,250),(0,255,0), thickness=cv.FILLED )
# cv.imshow('Rectangle',blank)

# cv.waitKey(0)  

img = np.zeros((512,512,3),np.uint8)#3 here means 3 diff channels for color without that we can only see the img in black and white
print(img)
# img[:] = 255,0,0 

cv.line(img,(0,0),(512,512),(0,255,0),3)
# cv.line(img,(512,0),(0,512),(255,0,0),3)
# cv.line(img,(256,0),(0,256),(255,255,255),3)
cv.rectangle(img,(350,100),(450,200),(255,255,255),cv.FILLED)
cv.circle(img,(150,400),50,(255,0,0),cv.FILLED)
cv.putText(img,"Draw Shapes",(75,50),cv.FONT_HERSHEY_SCRIPT_COMPLEX,1,(255,255,25),2)
cv.imshow('Blank',img)
cv.waitKey(0)