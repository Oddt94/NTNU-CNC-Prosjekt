# Standard imports
import cv2

import numpy as np;


# Read image
im = cv2.imread("William_sitt_lekerom/shapes.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow('Input', im)
cv2.waitKey(0)
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()

# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
blank = np.zeros((1,1))
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255),
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
blobs = cv2.drawKeypoints(im, keypoints, blank, (0,255,255), cv2.DRAW_MATCHES_FLAGS_DEFAULT)
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.imshow("Keypoints2", blobs)
cv2.waitKey(0)