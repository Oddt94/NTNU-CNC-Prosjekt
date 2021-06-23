import cv2

img = cv2.imread("Resources/shapes.png", 1)

while True:
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 1ms
        break

cv2.destroyAllWindows()
