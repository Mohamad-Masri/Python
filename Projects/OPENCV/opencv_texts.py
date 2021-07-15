import cv2
import numpy as np
 
img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[:]= 255,0,0

cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)
 
cv2.imshow("Image",img)
cv2.waitKey(0)