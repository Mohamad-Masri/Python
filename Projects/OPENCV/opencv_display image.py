import cv2
# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("Resources/image.png")
# DISPLAY
cv2.imshow("Lena Soderberg",img)
cv2.waitKey(0)