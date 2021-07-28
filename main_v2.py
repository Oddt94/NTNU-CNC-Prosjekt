import cv2
import numpy as np
from Stacking_func import stackImages

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error opening video")

cap.set(3, frameWidth)
cap.set(4, frameHeight)


def empty(a):
    pass

cv2.namedWindow("Output", flags=cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Contrast", "Output", 100, 1000, empty)
cv2.createTrackbar("Brightness", "Output", 1400, 10000, empty)
cv2.createTrackbar("Threshold1", "Output", 155, 255, empty)


# Using 'value' pointer is unsafe and deprecated. Use NULL as value pointer. To fetch trackbar value setup callback
# This is a bug from OpenCV, pay no attention to it.

while True:
    ret, frame = cap.read()
    Contrast = float(cv2.getTrackbarPos("Contrast", "Output") / 100)
    Brightness = float(cv2.getTrackbarPos("Brightness", "Output") / 100)
    Threshold_1 = cv2.getTrackbarPos("Threshold1", "Output")

    effect = frame.copy()
    effect = cv2.cvtColor(effect, cv2.COLOR_BGR2HSV)
    effect[:, :, 2] = np.clip(Contrast * effect[:, :, 2] + Brightness, 0, 255)
    effect = cv2.cvtColor(effect, cv2.COLOR_HSV2BGR)

    img_gray = cv2.cvtColor(effect, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(img_gray, Threshold_1, 255, cv2.THRESH_BINARY)

    # cv2.findContours( canny_output, contours, hierarchy, Imgproc.RETR_EXTERNAL, CV_CHAIN_APPROX_SIMPLE, Point(0, 0) );
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

    image_copy = effect.copy()
    blank_image = np.zeros((frameHeight, frameWidth, 3), np.uint8)

    cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                     lineType=cv2.LINE_AA)

    # blank_image = np.zeros(frame.shape)
    cv2.drawContours(image=blank_image, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                     lineType=cv2.LINE_AA)

    imgStack = stackImages(0.65, ([frame, blank_image],
                                 [thresh, image_copy]))
    cv2.imshow("Output", imgStack)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Saved_img/main_v2.png", imgStack)
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
