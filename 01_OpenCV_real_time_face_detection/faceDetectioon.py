import numpy as np
import cv2

# use haarcascade-frontalface_default.xml as a classifier
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
# set width
cap.set(3,640)
# set height
cap.set(4,480)

while True:
    reg, img = cap.read()
    # scene inversion
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (20,20)
        )
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w]
    # print out 'video'    
    cv2.imshow('video',img)
    # if 64-bit operating system, otherwise just 'k = cv2.waitKey(30)'
    k = cv2.waitKey(30) & 0xff
    # to quit, press 'ESC'
    if k == 27:
        break
cap.release()
# close window
cv2.destroyAllWindows()