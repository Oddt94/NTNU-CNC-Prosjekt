import cv2
import numpy as np

frameWidth = 340
frameHeight = 300

img = cv2.imread("lena.png")
img_sized = cv2.resize(img, (frameWidth, frameHeight))

imghorz = np.hstack((img_sized, img_sized))
imgvert = np.vstack((img_sized, img_sized))


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


# The stack needs to be at: n x n
# If the stack is for example: 2x3. It won't work!

img_sized_grey = cv2.cvtColor(img_sized, cv2.COLOR_BGR2GRAY)

imgStack = stackImages(0.5, ([img_sized_grey , img_sized, img_sized], [img_sized, img_sized_grey , img_sized]))

cv2.imshow("Horz", imghorz)
cv2.imshow("Vert", imgvert)
cv2.imshow("Stacks", imgStack)

cv2.waitKey(0)
