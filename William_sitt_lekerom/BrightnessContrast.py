import cv2


# Opplærings vvvv
# https://www.geeksforgeeks.org/changing-the-contrast-and-brightness-of-an-image-using-python-opencv/


def Brightnesscontrast(brightness=0):
    brightness = cv2.getTrackbarPos("Brightness", "Image")
    contrast = cv2.getTrackbarPos("Contrast", "Image")
    effect = controller(img, brightness, contrast)

    cv2.imshow("Effect", effect)


def controller(img, brightness=255, contrast=127):
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))

    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))

    if brightness != 0:

        if brightness > 0:

            shadow = brightness

            max = 255

        else:

            shadow = 0
            max = 255 + brightness

        al_pha = (max - shadow) / 255
        ga_mma = shadow

        # The function addWeighted
        # calculates the weighted sum
        # of two arrays
        cal = cv2.addWeighted(img, al_pha,
                              img, 0, ga_mma)

    else:
        cal = img

    if contrast != 0:
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        Gamma = 127 * (1 - Alpha)

        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv2.addWeighted(cal, Alpha,
                              cal, 0, Gamma)

    # putText renders the specified
    # text string in the image.
    cv2.putText(cal, 'B:{},C:{}'.format(brightness,
                                        contrast),
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)

    return cal


if __name__ == '__main__':  # Guarded Script
    original = cv2.imread("lena.png")
    img = original.copy()

    cv2.namedWindow("Image")
    cv2.imshow("Image", original)

    # Trackbar(trackbars, window_name, value, count, onchange)"
    # Brightness range -255 to 255
    cv2.createTrackbar("Brightness", "Image", 255, 2 * 255, Brightnesscontrast)

    # Contrast range -127 to 127
    cv2.createTrackbar("Contrast", "Image", 127, 2 * 127, Brightnesscontrast)

    Brightnesscontrast(0)

    cv2.waitKey(0)
