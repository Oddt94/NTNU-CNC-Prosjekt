import numpy as np
import cv2

# cap = cv2.VideoCapture("earth.mp4")
cap = cv2.VideoCapture(0)


contrast = 2.2
brightness = 50

while True:
    ret, frame = cap.read()
    cv2.imshow("Original", frame)
    effect = frame.copy()

    effect = cv2.cvtColor(effect, cv2.COLOR_BGR2HSV)
    effect[:,:,2] = np.clip(contrast * effect[:,:,2] + brightness, 0, 255)
    effect = cv2.cvtColor(effect, cv2.COLOR_HSV2BGR)

    cv2.putText(effect, 'B:{},C:{}'.format(brightness,
                                        contrast),
                (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 255), 1)

    cv2.imshow("effect",effect)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()