import numpy as np
import cv2

# cap = cv2.VideoCapture("earth.mp4")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error opening video")


def empty(a):
    pass


cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Contrast", "Parameters", 43, 1000, empty)
cv2.createTrackbar("Brightness", "Parameters", 1376, 10000, empty)

while True:
    ret, frame = cap.read()
    effect = frame.copy()

    Contrast = float(cv2.getTrackbarPos("Contrast", "Parameters") / 100)
    Brightness = float(cv2.getTrackbarPos("Brightness", "Parameters") / 100)

    effect = cv2.cvtColor(effect, cv2.COLOR_BGR2HSV)
    effect[:, :, 2] = np.clip(Contrast * effect[:, :, 2] + Brightness, 0, 255)
    effect = cv2.cvtColor(effect, cv2.COLOR_HSV2BGR)

    imghorz = np.hstack((frame, effect))
    cv2.imshow("Results", imghorz)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
