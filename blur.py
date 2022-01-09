import cv2

img = cv2.imread('Resources/lena.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(img, (5, 5))
blur2 = cv2.blur(img, (30, 30))
cv2.imshow('Origin', img)
cv2.imshow('Blur', blur)
cv2.imshow('Blur2', blur2)
cv2.waitKey()
