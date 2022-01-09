import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("Resources/contrasrt1.PNG", 0)
# 讀取圖片
hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
# 計算原圖的直方圖數值
# cv2.calcHist(影像, 通道, 遮罩, 區間數量, 數值範圍)
# 影像：影像的來源，其型別可以是 uint8 或 float32，變數必須放在中括號當中，例如：[img]。
# 通道：指定影像的通道（channel），同樣必須放在中括號當中。若為灰階影像，則通道就要指定為 [0]，若為彩色影像則可用 [0]、[1] 或 [2] 指定 藍色、綠色或紅色的通道。
# 遮罩：以遮罩指定要納入計算的圖形區域，若指定為 None 則會計算整張圖形的所有像素。
# 區間數量：指定直方圖分隔區間的數量（bins），也就是圖形畫出來要有幾條長方形。
# 數值範圍：指定要計算的像素值範圍，通常都是設為 [0,256]（計算所有的像素值）。
Imax = np.max(img)
# 原始圖像灰度最大值
Imin = np.min(img)
# 原始圖像灰度最小值
MAX = 255
# 要拉伸到的灰度空間的灰度最大值
MIN = 0
# 要拉伸到的灰度空間的灰度最小值
img_cs = (img - Imin) / (Imax - Imin) * (MAX - MIN) + MIN
# 帶入對比度拉伸公式
hist_cs = cv2.calcHist([img_cs.astype("uint8")], [0], None, [256], [0, 256])
# 計算對比度拉伸後的圖的直方圖數值
cv2.imshow("Origin", img)
cv2.imshow("farina_cs", img_cs.astype("uint8"))
plt.plot(hist_full)
plt.plot(hist_cs)
plt.show()
cv2.waitKey()
