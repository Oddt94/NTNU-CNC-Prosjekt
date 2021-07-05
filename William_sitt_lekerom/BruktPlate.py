import numpy as np
import cv2

cap = cv2.imread("Bordtest2.jpg", 1)

contrast = 1
brightness = 0

while True:
    frame = cap.copy()
    cv2.imshow("Original", frame)
    effect = frame.copy()

    effect = cv2.cvtColor(effect, cv2.COLOR_BGR2HSV)
    effect[:, :, 2] = np.clip(contrast * effect[:, :, 2] + brightness, 0, 255)
    effect = cv2.cvtColor(effect, cv2.COLOR_HSV2BGR)

    frame_gray = cv2.cvtColor(effect, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(frame_gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(effect, contours, -1, (0, 255, 0), 3)

    cv2.putText(effect, 'B:{},C:{}'.format(brightness,
                                           contrast),
                (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 255), 1)

    cv2.imshow("effect", effect)
    # cv2.imshow("frame gray", frame_gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#cap.release()
cv2.destroyAllWindows()
