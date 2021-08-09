import cv2

frameWidth = 640
frameHeight = 480
camera_source = 0
paused = False

cap = cv2.VideoCapture(camera_source)
if not cap.isOpened():
    print("Error opening video")
cap.set(3, frameWidth)
cap.set(4, frameHeight)
ret, frame = cap.read()


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)
    if event == cv2.EVENT_RBUTTONDOWN:
        print(x, ' ', y)
        cv2.imshow('image', cap)


while True:
    if not paused:
        ret, frame = cap.read()

    cv2.imshow('output', frame)
    cv2.setMouseCallback('output', click_event)
    key_press = cv2.waitKey(1)

    if key_press == ord('q') or key_press == 27:
        print("Quitting...")
        break
    elif key_press & 0xFF == ord("p"):
        paused = not paused
cv2.destroyAllWindows()
