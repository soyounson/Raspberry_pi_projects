import numpy as np
import matplotlib.pyplot as plt
import cv2

#**********************
#\\\\\ Data 
#**********************
x = np.random.randint(25,50,(50,2))
y = np.random.randint(60,85,(50,2))
# Stack arrays in sequence vertically 
z = np.vstack((x,y))
z = np.float32(z)

#**********************
#\\\\\ Build a model 
#**********************
# define criteria
# a. cv2.TERM_CRITERIA_EPS : stop the algorithm iteration if accuracy(epsilon) is reached.
# b. cv2.TERM_CRITERIA_MAX_ITER : stop the algorithm after the specified number of iterations, max_iter (aka. maximum interations)
# c. cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER : stop the iteration when any of the above condition is met (either accuracy <= epsilon or iter == max iter)
# my initial setup : max_iter : 10, epsilon : 1.
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)

# Flags : to specify how initial centers are taken (aka. intial setup)
#        (cv2.KMEANS_PP_CENTERS and cv2.KMEANS_RANDOM_CENTERS.)
flags = cv2.KMEANS_RANDOM_CENTERS 


# A model (k = 2 )
# 1. z : input 
# 2. 2 = # of clusters
# 3. None : Input/output integer array that stores the cluster indices for every sample
# 4. criteria : already defined 
# 5. 10 : Flag to specify the number of times the algorithm is executed using different initial labellings
# 6. criteria : Flag that can take values of cv::KmeansFlags
ret,label,center=cv2.kmeans(z,2,None,criteria,10,flags)


# divide data into 2 groups (lables have values (0 or 1))
A = z[label.ravel()==0]
B = z[label.ravel()==1]

#**********************
#\\\\\ Visualization 
#**********************
plt.figure(figsize = (6,6))
plt.rc('font',family='Times New Roman')
plt.scatter(A[:,0],A[:,1], c = 'b')
plt.scatter(B[:,0],B[:,1], c = 'r')
plt.scatter (center[:,0], center[:,1], s= 80, c = 'y')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show(block=False)
plt.savefig("01_kmeans",bbox_inches='tight')