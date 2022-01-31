import cv2 as cv
#Reading pics
# img= cv.imread('Pics/Hogwarts.jpg')
# cv.imshow('Harry',img)
#Reading videos now

capture = cv.VideoCapture(0)#Add the vid locations 


while True:
    isTrue,frame = capture.read()#reads vid frame by frame
    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'): #if d is press destroy
        break

capture.release()
cv.waitKey(0)
