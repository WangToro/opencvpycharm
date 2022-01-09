import cv2
import numpy as np

img = cv2.imread("Resources/lambo.png")
print(img.shape)
# (373, 463, 3)

imgResize = cv2.resize(img,(1000,500))
# imgResize = cv2.resize(img,(weight,hight))
# when picture size change to bigger one the quality won't be as clear as origin
print(imgResize.shape)

imgCropped = img[0:200,100:400]
# imgCropped = img[heigh,weight]

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)