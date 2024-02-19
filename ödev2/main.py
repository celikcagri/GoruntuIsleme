import cv2
import numpy as np

path=cv2.imread("images.jpg",0)
cv2.imshow("duz",path)
cv2.waitKey()
enbuyuk = np.max(path)
[h,w]=np.shape(path)
for i in range (0,h):
    for j in range (0,w):
        path[i,j] = enbuyuk-path[i,j]

cv2.imshow("ters",path)
cv2.waitKey()