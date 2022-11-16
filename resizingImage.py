import cv2

img = cv2.imread('./photos/robert.jpg')

# cv2.resize(image_variable, (Width, Height))
imgResized = cv2.resize(img, (200, 200))

cv2.imshow("Original image", img)
cv2.imshow("Resized image", imgResized)

cv2.waitKey(0)