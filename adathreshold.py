import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Resources/word.jpg", 0)
plt.figure(figsize=(10, 8), dpi=100)
TF, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# 大於門檻的變成255 ,其他為0
TF, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# 大於門檻的變成0 ,其他為255
TF, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# 大於門檻的變成門檻值,其他不變
TF, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# 小於門檻值得為0,其他不變
TF, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
# 大於門檻值得為0,其他不變

adt1_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 4)

adt2_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 4)

adt3_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 8)

adt4_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 4)

adt5_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 4)

adt6_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 10)

titles = ['Origin', 'Global', 'Adaptive G1', 'Adaptive G2', 'Adaptive G3', 'Adaptive M1', 'Adaptive M2', 'Adaptive M3']
images = [img, thresh1, adt1_img, adt2_img, adt3_img, adt4_img, adt5_img, adt6_img]

for i in range(8):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i], 'gray')
    # plt.subplot(總行,總列,位置[1,2,3],[4,5,6])
    # plt.imshow(圖片變數,類型)
    plt.title(titles[i])
    # plt.imshow(圖片標題)
    plt.xticks([]), plt.yticks([])
    # plt.xticks([]) 圖片位置x軸
    # plt.yticks([]) 圖片位置y軸

plt.show()
