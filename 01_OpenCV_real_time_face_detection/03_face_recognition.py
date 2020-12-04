import cv2
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

# indicate id counter
id = 0
# naems related to ids
#        id0.id1,id2 
names = ['A','B','C']

# initialize and start real time video capture
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

# define minimum window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret, img = cam.read()
    img = cv2.flip(img,-1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
        )
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        # check if confidence is less them 100 ==>"0", perfect!
        if (confidence < 100):
            id = names[id]
            confidence = " {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = " {0}%".format(round(100 - confidence))
            
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255),2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0),1)

    # show image 
    cv2.imshow('camera',img)
    # if 64-bit operating system, otherwise just 'k = cv2.waitKey(30)'
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break
    
print("\n [INFO] Exiting program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
        
        
