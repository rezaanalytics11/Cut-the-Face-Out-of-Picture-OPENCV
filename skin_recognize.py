import cv2
import numpy as np

img=cv2.imread(r'C:\Users\Ariya Rayaneh\Desktop\human4.jpg')
img=cv2.resize(img,(0,0),fx=4,fy=4)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(hsv)

lower = np.array([7, 70, 170])
upper = np.array([60, 220, 250])


mask = cv2.inRange(hsv, lower, upper)

res = cv2.bitwise_or(img,img, mask= mask)

# cv2.imshow('frame',img)
# cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.imwrite(r'C:\Users\Ariya Rayaneh\Desktop\human_face_only.jpg',res)
cv2.waitKey()

