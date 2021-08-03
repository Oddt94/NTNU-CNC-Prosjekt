import cv2
import numpy as np
from functions.Stacking_func import stackImages

frameWidth = 640
frameHeight = 480
image = False
image_source = "1Triangle.png"
camera_source = 1
font = cv2.FONT_HERSHEY_COMPLEX
paused = False


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

print("Press P for Pause\nPress Q for quit\nPress S for Save and Quit")
while True:
    if not paused:
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

    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

    image_copy = effect.copy()
    blank_image = np.zeros((frameHeight, frameWidth, 3), np.uint8)

    cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                     lineType=cv2.LINE_AA)

    cv2.drawContours(image=blank_image, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                     lineType=cv2.LINE_AA)

    pointers_open = 0
    cx_data = []
    cy_data = []
    x = []
    y = []

    for cnt in contours:
        M = cv2.moments(cnt)
        if M["m00"] is None or M["m00"] == 0:
            cx = 1
            cy = 1
        else:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
        cx_data.append(cx)
        cy_data.append(cy)
        for i in range(len(cnt)):
            x.append(cnt[i][0][0])
            y.append(cnt[i][0][1])
    cxy_data = np.column_stack([cx_data, cy_data])
    imgStack = stackImages(0.65, ([frame, blank_image],
                                  [thresh, image_copy]))

    cv2.imshow("Output", imgStack)
    key_press = cv2.waitKey(1)
    if key_press == ord('s'):
        print("Saving image...")
        cv2.imwrite("./main_v2.png", imgStack)
        # file_cont = open("./main_copytst3_contours.txt", "w+")
        print("Saving Contours...")
        np.savetxt("./main_copytst3_contours.txt", cxy_data, fmt=['%d', '%d'])
        # file_cont.write(cx_data + "\n" + cy_data)
        # file_cont.close()
        print("Quitting...")
        break
    elif key_press == ord('q') or key_press == 27:
        print("Quitting...")
        break
    elif key_press & 0xFF == ord("p"):
        paused = not paused
cv2.destroyAllWindows()
if not image:
    cap.release()

