import cv2

img = cv2.imread('./photos/ironman.jpg')
cv2.imshow("Ironman", img)
cv2.waitKey(0)