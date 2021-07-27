import numpy as np
import cv2

# cap = cv2.VideoCapture("earth.mp4")
cap = cv2.VideoCapture(0)


def empty(a):
    pass



cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Threshold1","Parameters",220,1000,empty)
cv2.createTrackbar("Threshold2","Parameters",5000,10000,empty)


while True:
    ret, frame = cap.read()
    effect = frame.copy()

    contrast = 1.25
    brightness = 50

    threshold1 = float (cv2.getTrackbarPos("Threshold1", "Parameters") / 100)
    threshold2 = float (cv2.getTrackbarPos("Threshold2", "Parameters") / 100)

    effect = cv2.cvtColor(effect, cv2.COLOR_BGR2HSV)
    effect[:,:,2] = np.clip(threshold1 * effect[:,:,2] + threshold2, 0, 255)
    effect = cv2.cvtColor(effect, cv2.COLOR_HSV2BGR)


    imghorz = np.hstack((frame, effect))
    cv2.imshow("Results",imghorz)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()