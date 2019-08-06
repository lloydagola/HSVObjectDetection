import cv2
import numpy as np

def nothing(x):
    pass

while True:
    picture = cv2.cv2.imread("colored_balls.jpg")

    hsv_picture = cv2.cv2.cvtColor(picture, cv2.cv2.COLOR_BGR2HSV)

    lower_blue_limit = np.array([110, 50, 50])
    upper_blue_limit = np.array([130, 255, 255])

    mask = cv2.cv2.inRange(hsv_picture, lower_blue_limit, upper_blue_limit)

    result = cv2.cv2.bitwise_and(picture, picture, mask=mask)

    cv2.cv2.imshow("Object Detection", picture)
    cv2.cv2.imshow("Mask", mask)
    cv2.cv2.imshow("Result", result)

    if cv2.cv2.waitKey(0) & 0xFF == 27:
        break

cv2.cv2.destroyAllWindows()


