import cv2
import numpy as np

img = cv2.imread('Resources/lena.png')

# 添加躁點
for i in range(2000):
    temp_x = np.random.randint(0,img.shape[0])
    temp_y = np.random.randint(0, img.shape[1])
    img[temp_x][temp_y] = 255

img_bilateral =cv2.bilateralFilter(img, 9, 50, 50)
cv2.imshow('Origin', img)
cv2.imshow('Bilateral',img_bilateral)
cv2.waitKey()