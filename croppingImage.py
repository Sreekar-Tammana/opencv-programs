import cv2

img  = cv2.imread('./photos/robert.jpg')

print(img.shape)
imgCropped = img[0:200, 200:360]

cv2.imshow("Original image", img)
cv2.imshow("Cropped image", imgCropped)
cv2.waitKey(0)