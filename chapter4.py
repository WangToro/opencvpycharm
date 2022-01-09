import cv2
import numpy as np


img = np.zeros((512,512,3),np.uint8)

'''

# change a defined range's color

print(img)
img[100:300,100:200] = 255,0,0
# img[long begin:long end,weight begin :weight end] = color
# img[:] => this means whole img
# change a defined range's color

'''



'''

# draw line ,circle,text.....

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# cv2.line(img,(starting point),(ending point),(color),thickness)
# cv2.line(img,(0,0),(300,300),(0,255,0),3)
# cv2.line(img,(0,0),(img.shpae[1],img.shape[0]),(0,255,0),3) from 0 to end

cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
# cv2.rectangle(img,(starting point),(ending point),(color),thickness)

cv2.circle(img,(400,50),30,(255,255,0),5)
# cv2.circle(img,(center point),radius,(color),thickness)

cv2.putText(img," OPENCV ",(300,100),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,150,0),2)
# cv2.putText(img,"Text",FONT,scale,color,thickness) which scale can be down to 0 point

'''



cv2.imshow("Image",img)


cv2.waitKey(0)