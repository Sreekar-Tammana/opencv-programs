import cv2
import numpy as np

img = cv2.imread("./photos/robert.jpg")

kernel = np.ones((5,5), np.uint8)

imgErosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow("Original image", img)
cv2.imshow("Erode image", imgErosion)

cv2.waitKey(0)