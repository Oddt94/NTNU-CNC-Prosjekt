import cv2

cap = cv2.VideoCapture(1)
cap.set(3, 640)  # width
cap.set(4, 480)  # height
#cap.set(10, 100)  # Brightness

def Brightnesscontrast(brightness=0):
    brightness = cv2.getTrackbarPos("Brightness", "Image")
    contrast = cv2.getTrackbarPos("Contrast", "Image")
    effect = controller(output_c, brightness, contrast)

    cv2.imshow("Effect", effect)


def controller(img, brightness=255, contrast=127):
    brightness = int(brightness * (255*2) / (255*2) + (-255))
    print(brightness)
    contrast = int(contrast * (127*2) / (127*2) + (-127))

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

while True:
    ret, captured_frame = cap.read()
    output = captured_frame.copy()

    output_c = output.copy()
    cv2.imshow("frame", output)
    #cv2.imshow("framecopy", output_c)

    cv2.createTrackbar("Brightness", "output_c", 255, 2 * 255, Brightnesscontrast)

    cv2.createTrackbar("Contrast", "output_c", 127, 2 * 127, Brightnesscontrast)

    Brightnesscontrast(0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
