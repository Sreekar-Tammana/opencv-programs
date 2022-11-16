import cv2

img = cv2.imread('./photos/robert.jpg')

imgCanny = cv2.Canny(img, 100, 100)

cv2.imshow("Original image", img)
cv2.imshow("Edge detector", imgCanny)

cv2.waitKey(0)