import cv2

img = cv2.imread('./photos/robert.jpg')

imgBlur = cv2.GaussianBlur(img, (7,7), 0)

cv2.imshow("Original image", img)
cv2.imshow("Blur image", imgBlur)

cv2.waitKey(0)