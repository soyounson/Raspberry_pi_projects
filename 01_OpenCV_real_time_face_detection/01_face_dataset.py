import cv2
import os

# create VideoCapture Object
cam = cv2.VideoCapture(0)
# set width
cam.set(3,640)
# set height
cam.set(4,480)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

# For several ppl detection, consider different face ids
face_id = input('\n enter user id end press <return> ==>   ')
print("\n [INFO] Initializing face capture. Look at the camera lense and wait plz... ")

# initialize individual sampling face count 
count = 0
while(True):
    # ret : captured frame result (boolean), img : captured frame
    ret, img = cam.read()
    img = cv2.flip(img, -1)
    # convert image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)
        count += 1
        # save image in dataset folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image',img)
    # if 64-bit operating system, otherwise just 'k = cv2.waitKey(30)'    
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    # take 30 face sample and stop video
    elif count >= 30:
        break
# clean up?
print("\n [INFO] Exiting program and cleanup stuff")
cam.release()
# close window 
cv2.destroyAllWindows()
