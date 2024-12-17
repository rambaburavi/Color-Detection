import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    read_ok, img = cap.read()
    if not read_ok:
        print("Failed to read from camera.")
        break

    img = cv2.resize(img, (640, 480))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    lower_green = np.array([40, 20, 50])
    upper_green = np.array([90, 255, 255])
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([179, 255, 50])
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([179, 20, 255])
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    lower_cyan = np.array([80, 100, 100])
    upper_cyan = np.array([100, 255, 255])
    lower_magenta = np.array([140, 50, 50])
    upper_magenta = np.array([170, 255, 255])
    lower_orange = np.array([10, 100, 100])
    upper_orange = np.array([20, 255, 255])
    lower_pink = np.array([160, 50, 50])
    upper_pink = np.array([170, 255, 255])
    lower_brown = np.array([10, 100, 20])
    upper_brown = np.array([20, 255, 200])
    lower_violet = np.array([130, 50, 50])
    upper_violet = np.array([160, 255, 255])
    lower_gray = np.array([0, 0, 40])
    upper_gray = np.array([179, 50, 200])
    lower_beige = np.array([15, 30, 150])
    upper_beige = np.array([25, 70, 255])
    lower_turquoise = np.array([85, 50, 50])
    upper_turquoise = np.array([95, 255, 255])
    lower_lime = np.array([30, 100, 100])
    upper_lime = np.array([60, 255, 255])
    lower_indigo = np.array([130, 50, 50])
    upper_indigo = np.array([160, 255, 255])
    lower_peach = np.array([10, 50, 150])
    upper_peach = np.array([20, 150, 255])
    lower_lavender = np.array([130, 50, 150])
    upper_lavender = np.array([150, 255, 255])
    lower_teal = np.array([80, 50, 50])
    upper_teal = np.array([90, 255, 255])

    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_black = cv2.inRange(hsv, lower_black, upper_black)
    mask_white = cv2.inRange(hsv, lower_white, upper_white)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask_cyan = cv2.inRange(hsv, lower_cyan, upper_cyan)
    mask_magenta = cv2.inRange(hsv, lower_magenta, upper_magenta)
    mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)
    mask_pink = cv2.inRange(hsv, lower_pink, upper_pink)
    mask_brown = cv2.inRange(hsv, lower_brown, upper_brown)
    mask_violet = cv2.inRange(hsv, lower_violet, upper_violet)
    mask_gray = cv2.inRange(hsv, lower_gray, upper_gray)
    mask_beige = cv2.inRange(hsv, lower_beige, upper_beige)
    mask_turquoise = cv2.inRange(hsv, lower_turquoise, upper_turquoise)
    mask_lime = cv2.inRange(hsv, lower_lime, upper_lime)
    mask_indigo = cv2.inRange(hsv, lower_indigo, upper_indigo)
    mask_peach = cv2.inRange(hsv, lower_peach, upper_peach)
    mask_lavender = cv2.inRange(hsv, lower_lavender, upper_lavender)
    mask_teal = cv2.inRange(hsv, lower_teal, upper_teal)

    for mask, color, text, rect_color in [
        (mask_red, (0, 0, 255), "Red", (0, 0, 255)),
        (mask_green, (0, 255, 0), "Green", (0, 255, 0)),
        (mask_blue, (255, 0, 0), "Blue", (255, 0, 0)),
        (mask_black, (255, 255, 255), "Black", (255, 255, 255)),
        (mask_white, (0, 0, 0), "White", (0, 0, 0)),
        (mask_yellow, (0, 255, 255), "Yellow", (0, 255, 255)),
        (mask_cyan, (255, 255, 0), "Cyan", (255, 255, 0)),
        (mask_magenta, (255, 0, 255), "Magenta", (255, 0, 255)),
        (mask_orange, (0, 165, 255), "Orange", (0, 165, 255)),
        (mask_pink, (255, 105, 180), "Pink", (255, 105, 180)),
        (mask_brown, (42, 42, 165), "Brown", (42, 42, 165)),
        (mask_violet, (238, 130, 238), "Violet", (238, 130, 238)),
        (mask_gray, (128, 128, 128), "Gray", (128, 128, 128)),
        (mask_beige, (245, 245, 220), "Beige", (245, 245, 220)),
        (mask_turquoise, (64, 224, 208), "Turquoise", (64, 224, 208)),
        (mask_lime, (0, 255, 0), "Lime", (0, 255, 0)),
        (mask_indigo, (75, 0, 130), "Indigo", (75, 0, 130)),
        (mask_peach, (255, 218, 185), "Peach", (255, 218, 185)),
        (mask_lavender, (230, 230, 250), "Lavender", (230, 230, 250)),
        (mask_teal, (0, 128, 128), "Teal", (0, 128, 128)),
    ]:
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            contour_area = cv2.contourArea(cnt)
            if contour_area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x, y), (x + w, y + h), rect_color, 2)
                cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow('Color Recognition Output', img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()
