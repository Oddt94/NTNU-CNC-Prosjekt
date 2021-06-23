import cv2

img = cv2.imread("Resources/shapes.png")
original_dim = img.shape
original_hight = original_dim[0]
original_width = original_dim[1]

print("Original image hight: ", original_hight)
print("Original image widht:", original_width)


cv2.imshow("Original", img)



cv2.waitKey(0)
cv2.destroyAllWindows()
