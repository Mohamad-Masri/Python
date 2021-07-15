import cv2
import numpy as np
 
img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)
 

imgCanny = cv2.Canny(img,150,200)


cv2.imshow("Canny Image",imgCanny)

cv2.waitKey(0)