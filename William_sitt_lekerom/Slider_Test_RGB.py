import cv2
import numpy as np


def make_slid(a_min: int, a_max: int, curr: int, slider_id: str, root_win_name: str, on_change_callback=lambda x: x):
    cv2.createTrackbar(slider_id, root_win_name, a_min, a_max, on_change_callback)
    cv2.setTrackbarPos(slider_id, root_win_name, curr)
    return slider_id


def getslid(*ids, window: str):
    try:
        results = [cv2.getTrackbarPos(idd, window) for idd in ids]
        return results[0] if len(results) == 1 else results
    except Exception as e:
        print(f'Error in getting slider value - {str(e)}')
        return None


def setslid(id_: str, value: int, window: str):
    cv2.setTrackbarPos(id_, window, value)


# Name your window
window = 'main'
cv2.namedWindow(window)

sliders = [
    make_slid(0, 255, 20, 'r', window),
    make_slid(0, 255, 50, 'g', window),
    make_slid(0, 255, 120, 'b', window)
]

# Create a black image
img = np.ones((512, 512, 3), np.uint8)
while True:

    img[:, :] = getslid('r', 'g', 'b', window=window)
    cv2.imshow(window, img)

    code = cv2.waitKey(1)

    if code == ord('q'):
        break

    if code == ord('w'):
        r, g, b = getslid('r', 'g', 'b', window=window)
        print(r, g, b)

    if code == ord('e'):
        setslid('r', 10, window=window)
        setslid('g', 10, window=window)
        setslid('b', 10, window=window)

cv2.destroyAllWindows()
