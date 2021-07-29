import cv2
import numpy as np
from Stacking_func import stackImages

frameWidth = 640
frameHeight = 480
image = True
image_source = "Bordtest.png"
camera_source = 0


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

    # cv2.findContours( canny_output, contours, hierarchy, Imgproc.RETR_EXTERNAL, CV_CHAIN_APPROX_SIMPLE, Point(0, 0) );
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

    image_copy = effect.copy()
    blank_image = np.zeros((frameHeight, frameWidth, 3), np.uint8)

    cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                     lineType=cv2.LINE_AA)

    cv2.drawContours(image=blank_image, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                     lineType=cv2.LINE_AA)
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)

        # draws boundary of contours.
        cv2.drawContours(frame, [approx], 0, (0, 0, 255), 5)

        # Used to flatted the array containing
        # the co-ordinates of the vertices.
        n = approx.ravel()
        i = 0

    contours_cordinates_counter = True
    if contours_cordinates_counter:
        for j in n:
            if i % 2 == 0:
                x = n[i]
                y = n[i + 1]

                # String containing the co-ordinates.
                string = str(x) + " " + str(y)

                if i == 0:
                    # text on topmost co-ordinate.
                    cv2.putText(cap, "Arrow tip", (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
                else:
                    # text on remaining co-ordinates.
                    cv2.putText(cap, string, (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
            i = i + 1
        contours_cordinates_counter = False
        else
        print("poop")

    imgStack = stackImages(0.65, ([frame, blank_image],
                                  [thresh, image_copy]))
    cv2.imshow("Output", imgStack)
    end_button = cv2.waitKey(1)
    if end_button == ord('q') or end_button == 27:
        print("Quitting...")
        break
    elif end_button == ord('s'):
        print("Saving image...")
        cv2.imwrite("Saved_img/main_v2.png", imgStack)
        file = open("William_sitt_lekerom/main_v2_contours.txt", "w")
        print("Saving Contours...")
        file.write(repr(contours))
        print("Quitting...")
        break
cap.release()
cv2.destroyAllWindows()