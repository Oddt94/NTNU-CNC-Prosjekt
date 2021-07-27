import cv2
import matplotlib.pyplot as plt
import numpy as np
from Stacking_func import stackImages

contrast = 1.25
brightness = 50

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

effect = frame.copy()
effect = cv2.cvtColor(effect, cv2.COLOR_BGR2HSV)
effect[:, :, 2] = np.clip(contrast * effect[:, :, 2] + brightness, 0, 255)
effect = cv2.cvtColor(effect, cv2.COLOR_HSV2BGR)

img_gray = cv2.cvtColor(effect, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

image_copy = effect.copy()

cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                 lineType=cv2.LINE_AA)

imgStack = stackImages(0.8, ([frame, effect],
                             [thresh, image_copy]))
cv2.imshow("Result", imgStack)

cv2.waitKey(0)

cx_data = []
cy_data = []
x = []
y = []

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
    for i in range(len(cnt)):
        x.append(cnt[i][0][0])
        y.append(cnt[i][0][1])
cv2.destroyAllWindows()

plt.figure()

plt.axis([0, np.max(x), 0, np.max(y)])

ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])

plt.plot(cx_data, cy_data, 'go')
plt.plot(x, y, 'rx')
plt.show()

# Vil ikkje lage en blank_images
blank_image = np.zeros((np.max(y), np.max(x), 3), np.uint8)
cv2.drawContours(image=blank_image, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                 lineType=cv2.LINE_AA)
cv2.imshow('only edge', blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
