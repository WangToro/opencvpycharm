import cv2
import numpy as np

img = cv2.imread('Resources/lena.png')

# 添加躁點
for i in range(2000):
    temp_x = np.random.randint(0,img.shape[0])
    temp_y = np.random.randint(0, img.shape[1])
    img[temp_x][temp_y] = 255

img_gaussian = cv2.GaussianBlur(img, (5, 5), 0)
img_gaussian_ksize = cv2.GaussianBlur(img, (11, 11), 0)
img_gaussian_sigma = cv2.GaussianBlur(img, (5, 5), 3)
img_gaussian_ksize_sigma = cv2.GaussianBlur(img, (11, 11), 3)
cv2.imshow('Origin', img)
cv2.imshow('Gaussian', img_gaussian)
cv2.imshow('Gaussian_k', img_gaussian_ksize)
cv2.imshow('Gaussian_s', img_gaussian_sigma)
cv2.imshow('Gaussian_ks', img_gaussian_ksize_sigma)

cv2.waitKey()

