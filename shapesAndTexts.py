import cv2
import numpy as np

img = cv2.imread('./photos/robert.jpg')

#### Creating 512x512 pixels block using numpy
block = np.zeros((512,512,3), np.uint8)

#### Filling block with color
block[:] = 255,255,0 #(Blue, Green, Red)
cv2.imshow("block image", block)
cv2.waitKey(0)

#### Creating Line
#### cv2.line(image_variable, (starting origin), (ending_origin), (color_code), thickness)
cv2.line(block, (0,0), (300,300), (0,255,0), 3)
cv2.imshow("Line on block", block)
cv2.waitKey(0)

#### Creating Rectangle
cv2.rectangle(block, (0,0), (250, 250), (0,0,255), 4)
cv2.imshow("Rectangle", block)
cv2.waitKey(0)

#### Filling rectangle with color
cv2.rectangle(block, (0,0), (300,300), (255,0,0),cv2.FILLED)
cv2.imshow("Filled color", block)
cv2.waitKey(0)

#### Creating Circle
#### cv2.circle(image_variable, (center_point), radius, (color_code), thickness)
cv2.circle(block, (400, 50), 50, (255,255,0), 8)
cv2.imshow("Circle", block)
cv2.waitKey(0)

#### Put Text on image
#### cv2.putText(image_variable, "Text to be written", (width, height), text_font, scale, (color_code), thickness)
cv2.putText(img, "Mr. Robert D", (10, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (150,0,0), 2)
cv2.imshow("Text on image", img)
cv2.waitKey(0)