import cv2
import numpy as np
 
img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)
 
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image",imgGray)
cv2.waitKey(0)