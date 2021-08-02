import cv2
import numpy as np
from Stacking_func import stackImages

frameWidth = 640
frameHeight = 480
image = True
image_source = "1Triangle.png"
camera_source = 0
font = cv2.FONT_HERSHEY_COMPLEX


def empty(a):
    pass


if image:
    cap = cv2.imread(image_source, 1)
    frame = cap.copy()
else:
    cap = cv2.VideoCapture(camera_source)
    if not cap.isOpened():
        print("Error opening video")
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    ret, frame = cap.read()

cv2.namedWindow("Output", flags=cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Contrast", "Output", 100, 1000, empty)
cv2.createTrackbar("Brightness", "Output", 1400, 10000, empty)
cv2.createTrackbar("Threshold1", "Output", 155, 255, empty)

# Using 'value' pointer is unsafe and deprecated. Use NULL as value pointer. To fetch trackbar value setup callback
# This is a bug from OpenCV, pay no attention to it.

print("Press Q for quit\nPress S for Save and Quit")
while True:
    Contrast = float(cv2.getTrackbarPos("Contrast", "Output") / 100)
    Brightness = float(cv2.getTrackbarPos("Brightness", "Output") / 100)
    Threshold_1 = cv2.getTrackbarPos("Threshold1", "Output")

    effect = frame.copy()
    effect = cv2.cvtColor(effect, cv2.COLOR_BGR2HSV)
    effect[:, :, 2] = np.clip(Contrast * effect[:, :, 2] + Brightness, 0, 255)
    effect = cv2.cvtColor(effect, cv2.COLOR_HSV2BGR)

    img_gray = cv2.cvtColor(effect, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(img_gray, Threshold_1, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

    image_copy = effect.copy()
    blank_image = np.zeros((frameHeight, frameWidth, 3), np.uint8)

    cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                     lineType=cv2.LINE_AA)

    cv2.drawContours(image=blank_image, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                     lineType=cv2.LINE_AA)

    pointers_open = 0

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
        cv2.drawContours(image_copy, [approx], 0, (0, 0, 255), 5)
        n = approx.ravel()

    for j in n:
        if pointers_open % 2 == 0:
            x = n[pointers_open]
            y = n[pointers_open + 1]

            # String containing the co-ordinates.
            stringpos = str(x) + " " + str(y)

            if pointers_open == 0:
                # text on topmost co-ordinate.
                cv2.putText(image_copy, stringpos, (x, y),
                            font, 1, (0, 255, 0))
            else:
                # text on remaining co-ordinates.
                cv2.putText(image_copy, stringpos, (x, y),
                            font, 1, (0, 255, 0))
        pointers_open = pointers_open + 1

    imgStack = stackImages(0.65, ([frame, blank_image],
                                  [thresh, image_copy]))

    cv2.imshow("Output", imgStack)
    end_button = cv2.waitKey(1)
    if end_button == ord('s'):
        print("Saving image...")
        cv2.imwrite("./main_v2.png", imgStack)
        file_cont = open("./main_copytst3_contours.txt", "w+")
        print("Saving Contours...")
        file_cont.write(repr(approx))
        file_cont.close()
        print("Quitting...")
        break
    elif end_button == ord('q') or end_button == 27:
        print("Quitting...")
        break
cv2.destroyAllWindows()
if not image:
    cap.release()

# Contours output aren't xy, it's centroids.
# https://docs.opencv.org/4.5.2/dd/d49/tutorial_py_contour_features.html
