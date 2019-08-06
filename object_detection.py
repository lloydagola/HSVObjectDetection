import cv2.cv2
import numpy as np

def nothing(x):
    pass

cv2.cv2.namedWindow("Tracking")
cv2.cv2.createTrackbar("LowerHueValue", "Tracking", 0, 255, nothing)
cv2.cv2.createTrackbar("LowerSaturationValue", "Tracking", 0, 255, nothing)
cv2.cv2.createTrackbar("LowerValue", "Tracking", 0, 255, nothing)
cv2.cv2.createTrackbar("UpperHueValue", "Tracking", 255, 255, nothing)
cv2.cv2.createTrackbar("UpperSaturationValue", "Tracking", 255, 255, nothing)
cv2.cv2.createTrackbar("UpperValue", "Tracking", 255, 255, nothing)

while True:
    picture = cv2.cv2.imread('colored_balls.jpg')

    hsv_picture = cv2.cv2.cvtColor(picture, cv2.cv2.COLOR_BGR2HSV)

    lower_hue = cv2.cv2.getTrackbarPos("LowerHueValue", "Tracking")
    lower_saturation = cv2.cv2.getTrackbarPos("LowerSaturationValue", "Tracking")
    lower_value = cv2.cv2.getTrackbarPos("LowerValue", "Tracking")

    upper_hue = cv2.cv2.getTrackbarPos("UpperHueValue", "Tracking")
    upper_saturation = cv2.cv2.getTrackbarPos("UpperSaturationValue", "Tracking")
    upper_value = cv2.cv2.getTrackbarPos("UpperValue", "Tracking")

    lower_blue_limit = np.array([lower_hue, lower_saturation, lower_value])
    upper_blue_limit = np.array([upper_hue, upper_saturation, upper_value])

    mask = cv2.cv2.inRange(hsv_picture, lower_blue_limit, upper_blue_limit)

    result = cv2.cv2.bitwise_and(picture, picture, mask=mask)

    cv2.cv2.imshow("picture", picture)
    cv2.cv2.imshow("mask", mask)
    cv2.cv2.imshow("result", result)

    key = cv2.cv2.waitKey(1)
    if key == 27:
        break

cv2.cv2.destroyAllWindows()