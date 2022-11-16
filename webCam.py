import cv2

cam = cv2.VideoCapture(0)

cam.set(3, 500)
cam.set(4, 500)

while True:
    success, img = cam.read()
    # Helps to convert color to gray scale live feed
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Live feed", imgGray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break