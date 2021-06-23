import numpy as np
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)
frameWidth = 720
frameHeight = 480
cap.set(3, frameWidth)
cap.set(4, frameHeight)
#  WTV

while True:
    ret, captured_frame = cap.read()
    output = captured_frame.copy()
    captured_frame_bgr = cv2.cvtColor(captured_frame, cv2.COLOR_BGRA2BGR)  # BGR T BGR
    captured_frame_bgr = cv2.medianBlur(captured_frame_bgr, 3)  # for guds skyld hold den på 3
    captured_frame_blue = cv2.inRange(captured_frame_bgr, np.array([110, 50, 0]),
                                      np.array([237, 204, 80]))  # Farge!!! keep da colour
    captured_frame_blue = cv2.GaussianBlur(captured_frame_blue, (5, 5), 2, 2)
    circles = cv2.HoughCircles(captured_frame_blue, cv2.HOUGH_GRADIENT, 1, captured_frame_blue.shape[0] / 8,
                               param1=100, param2=18, minRadius=5, maxRadius=200)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            pos = (str(('x:', x, "y:", y)))
            clean_pos = pos.replace("'", "").replace(",", "")
            cv2.rectangle(output, (x - r, y + r), (x + r, y - r), (0, 255, 0), 1)
            cv2.putText(output, clean_pos, (x - r, y + r), font, (r / 100), (0, 255, 255), 1, cv2.LINE_AA)
    # cv2.imshow('Org', captured_frame)
    cv2.imshow('Blue_Filter', captured_frame_blue)
    cv2.imshow('frame', output)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 1ms
        break

cap.release()
cv2.destroyAllWindows()
