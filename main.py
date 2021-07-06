import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("William_sitt_lekerom/shapes.png", 1)

# convert the image to grayscale format
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply binary thresholding
ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

# visualize the binary image
cv2.imshow('Binary image', thresh)
cv2.waitKey(0)
cv2.imwrite('image_thres1.jpg', thresh)

# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

# draw contours on the original image
image_copy = image.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                 lineType=cv2.LINE_AA)

# see the results
cv2.imshow('None approximation', image_copy)
cv2.waitKey(0)
cv2.imwrite('contours_none_image1.jpg', image_copy)

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
    # Separates out all he x and y coordinates of the contour edges
    for i in range(len(cnt)):
        x.append(cnt[i][0][0])
        y.append(cnt[i][0][1])
cv2.destroyAllWindows()

# Starts plots to visualize the lists
plt.figure()

# Sets the coordinates such that all contours found are displayed
plt.axis([0, np.max(x), 0, np.max(y)])

# Flips the y-axis to match the openCV data format
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])

# Plots the centers of found objects in green and edges in red
plt.plot(cx_data, cy_data, 'go')
plt.plot(x, y, 'rx')
plt.show()

