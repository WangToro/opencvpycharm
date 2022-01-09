import cv2
import numpy as np
# 讀取圖片
img = cv2.imread('Resources/lena.png')
color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 添加躁點
for i in range(2000):
    temp_x = np.random.randint(0,img.shape[0])
    temp_y = np.random.randint(0, img.shape[1])
    img[temp_x][temp_y] = 255

# 方框濾波
img_blur = cv2.blur(img, (5, 5))
img_normal = cv2.boxFilter(color, -1, (5, 5), normalize=True)
img_nonormal = cv2.boxFilter(color, -1, (5, 5), normalize=False)

cv2.imshow('Origin', img)
cv2.imshow('Blur', img_blur)
cv2.imshow('Box Blur normal', img_normal)
cv2.imshow('Box Blur nonormal', img_nonormal)
cv2.waitKey()
