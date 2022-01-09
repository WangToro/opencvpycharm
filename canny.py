import cv2
import numpy as np

img = cv2.imread("Resources/coin.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (17, 17), 0)

canny = cv2.Canny(blurred, 30, 150)

result = np.hstack([gray, blurred, canny])

cv2.imshow("Result:", result)
cv2.waitKey(0)
