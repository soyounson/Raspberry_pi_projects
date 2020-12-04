import numpy as np
import cv2

# call video
cap = cv2.VideoCapture(0)
# set width
cap.set(3,640)
# set Height
cap.set(4,480)
while(True):
    # read camera
    ret, frame = cap.read()
    # flip camera vertically
    frame = cv2.flip(frame, -1)
    # change color 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # show image what you read
    cv2.imshow('frame',frame)
#     cv2.imshow('gray',gray)
    
    # wait for 30 sec
    k = cv2.waitKey(30) & 0xff
    # press 'ESC' to quit
    if k ==27:
        break
    
# disconnect    
cap.release()
cv2.destroyAllWindows()
