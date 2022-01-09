import cv2
import numpy as np
import imutils
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('Resources/skoda.PNG')
# 變更圖片大小
img = cv2.resize(img, (640, 480))
# 灰階轉換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#二值化處理
# TF, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
# 高斯模糊
# gaussian = cv2.GaussianBlur(gray, (5, 5,), 10)
bilatera = cv2.bilateralFilter(gray, 13, 15, 15)
# 邊緣檢測
canny = cv2.Canny(bilatera, 30, 200)

#二值化處理
TF, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
''' 
# rec = cv2.rectangle(thresh, (0, 200), (640, 300), (0, 255, 0), 3)

contour, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

copy_img = img.copy()
for cnt in contour:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(copy_img, (x, y), (x+w, y+h), (0, 255, 0), 40)

imgRoi = img[200:300, 200:450]
cv2.imshow("ROI", imgRoi)
cv2.imshow("copy", copy_img)

'''
contours = cv2.findContours(canny.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
screenCnt = None

for c in contours:

    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)

    if len(approx) == 4:
        screenCnt = approx
        break

if screenCnt is None:
    detected = 0
    print("No contour detected")
else:
    detected = 1

if detected == 1:
    cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
new_image = cv2.bitwise_and(img, img, mask=mask)

(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]

text = pytesseract.image_to_string(Cropped, config='--psm 11')
print("programming_fever's License Plate Recognition\n")
print("Detected license plate Number is:", text)
img = cv2.resize(img, (500, 300))
Cropped = cv2.resize(Cropped, (400, 200))
cv2.imshow('car', img)
cv2.imshow('Cropped', Cropped)


# cv2.imshow('result', rec)
cv2.waitKey()
