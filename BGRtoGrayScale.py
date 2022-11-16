import cv2

img = cv2.imread('./photos/robert.jpg')

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("BGR image", img)
cv2.imshow("GrayScale image", imgGray)

cv2.waitKey(0)