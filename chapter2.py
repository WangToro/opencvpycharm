import cv2
import numpy as np



img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)

Ori_img = img
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# turn into gray picture
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# make picture into Blur EX:(3,3)or(7,7)or(9,9).....more Blur
imgCanny = cv2.Canny(img,150,200)
# detect edge
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
# make line more thicker
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
# make line more thinner
img_arr = img[np.where((img == [0, 0, 0]).all(axis=2))]
img_arr1 = img_arr
img_arr = [0, 0, 255]
img_arr2 = img_arr




#cv2.imshow("Gray Image",imgGray)
#cv2.imshow("Blur Image",imgBlur)
#cv2.imshow("Canny Image",imgCanny)
#cv2.imshow("Dialation Image",imgDialation)
#cv2.imshow("Eroded Image",imgEroded)
cv2.imshow("origin", Ori_img)
cv2.imshow("arr1", img_arr1)
cv2.imshow("arr2", img_arr2)

cv2.waitKey(0)