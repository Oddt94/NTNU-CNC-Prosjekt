import cv2
import numpy as np


img = cv2.imread("shapes.png")
kernel =  np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (9, 9), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1) # Iteraltions = thickness
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

# cv2.imshow("Gray Img", imgGray)
# cv2.imshow("Blury Im", imgBlur)
cv2.imshow("Blury Img", imgCanny)
cv2.imshow("Dialation Img", imgDialation)
cv2.imshow("Eroded Img", imgEroded)

cv2.waitKey(0)
