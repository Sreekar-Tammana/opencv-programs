import cv2

video = cv2.VideoCapture('./videos/car.mp4')

while True:
        success, img = video.read()
        cv2.imshow("Car", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break