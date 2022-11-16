import cv2

img = cv2.imread("./photos/shapes.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7,7), 2) #Optional
imgCanny =  cv2.Canny(imgGray, 50, 50) # it is mandatory to convert img to canny

contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

for cn in contours:
    area = cv2.contourArea(cn)
    cv2.drawContours(img, cn, -1, (0,255,100), 4)

cv2.imshow("C",img)
cv2.imshow("Canny", imgCanny)
cv2.waitKey(0)