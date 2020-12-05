import numpy as np
import cv2

#**********************
#\\\\\ Generate image (background)
#**********************
# 512x512 pixels and 3(BGR) channels
# all values equal to 0 => black image 
background = np.zeros((512,512,3))

#**********************
#\\\\\ Draw radial lines 
#**********************
# radius 
r = 200

for theta in range(0,360,10):
    rad = theta * np.pi/180
    # polar coordinate system (complex numbers z = r(cos(theta)+ i sin(theta))
    x = r * np.cos(rad)
    y = r * np.sin(rad)
                       # start p't    |    end p't     |    color | thickness
    cv2.line(background, (250,250),(int(x+250),int(y+250)),(250,0,0),1)

cv2.imshow("image",background)
cv2.waitKey(0)
cv2.destroyAllWindows

cv2.imwrite("00_test.png",background)


