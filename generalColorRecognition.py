import cv2
import matplotlib as plt
import numpy as np

try:
    img = cv2.imread('forest.jpeg')
except:
    print("this failed")

wind = cv2.namedWindow("cool")
cv2.imshow("cool", img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
px = img[100,100]
print(px)