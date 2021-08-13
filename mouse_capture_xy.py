import cv2

frameWidth = 640
frameHeight = 480
camera_source = 1
paused = False

cap = cv2.VideoCapture(camera_source)
if not cap.isOpened():
    print("Error opening video")
cap.set(3, frameWidth)
cap.set(4, frameHeight)
ret, frame = cap.read()


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('x:', x, ' ', "y:", y)


while True:
    if not paused:
        ret, frame = cap.read()
        flipped = cv2.flip(frame, 1)
        (h, w) = frame.shape[:2]
        (cX, cY) = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D((cX, cY), -90, 0.7)
        rotated = cv2.warpAffine(flipped, M, (w, h))
    cv2.imshow('output', rotated)
    cv2.setMouseCallback('output', click_event)
    key_press = cv2.waitKey(1)

    if key_press == ord('q') or key_press == 27:
        print("Quitting...")
        break
    elif key_press & 0xFF == ord("p"):
        paused = not paused
cv2.destroyAllWindows()
