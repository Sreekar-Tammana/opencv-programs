import cv2
import numpy as np

img = cv2.imread("./photos/cards.jpg")

width, height = 500, 800

pts1 = np.float32([[69, 28], [169, 12], [91, 158], [193, 138]])
pts2 = np.float32([[0,0], [width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOut = cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow("Result", imgOut)
cv2.waitKey(0)