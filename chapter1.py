import cv2
print("Package Imported")

### Images ###
# img = cv2.imread('./photos/ironman.jpg')
# cv2.imshow("Ironman", img)
# cv2.waitKey(0)
### Images ###

### Read WebCam ###
cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 500)

while True:
    success, img = cap.read()
    cv2.imshow("Live Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
### Read WebCam ###