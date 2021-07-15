import cv2
import numpy as np
 
img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)

imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)