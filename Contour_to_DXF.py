import cv2
import numpy as np
from Stacking_func import stackImages

frameWidth = 640
frameHeight = 480
paused = False

cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Error opening video")

cap.set(3, frameWidth)
cap.set(4, frameHeight)


def empty(a):
    pass


cv2.namedWindow("Output", flags=cv2.WINDOW_AUTOSIZE)


# Using 'value' pointer is unsafe and deprecated. Use NULL as value pointer. To fetch trackbar value setup callback
# This is a bug from OpenCV, pay no attention to it.

print("Press P for Pause\nPress Q for quit\nPress S for Save and Quit")
while True:
    # If not paused - get next
    if not paused:
        ret, frame = cap.read()

    Contrast = 6.10
    Brightness = 500
    Threshold_1 = 128

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

    cv2.drawContours(image=blank_image, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                    lineType=cv2.LINE_AA)

    imgStack = stackImages(0.65, ([frame, blank_image],
                                [thresh, image_copy]))
    cv2.imshow("Output", imgStack)

    key_press = cv2.waitKey(1)
    if key_press & 0xFF == ord('s'):
        # Make the coordinate arrays
        cx_data = []
        cy_data = []
        x = []
        y = []

        # this for loop iterates through all the contour elements found by openCV
        for cnt in contours:
            M = cv2.moments(cnt)
            # Finds the centers of all contour objects
            if M['m00'] is None or M['m00'] == 0:
                cx = 1
                cy = 1
            else:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
            cx_data.append(cx)
            cy_data.append(cy)
            # Separates out all the x and y coordinates of the contour edges
            for i in range(len(cnt)):
                x.append(cnt[i][0][0])
                y.append(cnt[i][0][1])
        print("Saving image...")
        cv2.imwrite("Saved_img/test_img.png", imgStack)
        file_cont = open("./test.txt", "a")
        print("Saving Contours...")
        for i in range(len(x)):
            line = str(x[i]) + "," + str(y[i]) + "\n"
            file_cont.writelines(line)
        file_cont.close()
        print("Quitting...")
        break
    elif key_press & 0xFF == ord('q') or key_press == 27:
        print("Quitting...")
        break
    elif key_press & 0xFF == ord("p"):
        paused = not paused
cap.release()
cv2.destroyAllWindows()