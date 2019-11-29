import cv2
import numpy as np

boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
]

cap = cv2.VideoCapture(0)

while True:
    if cap.grab():
        ret, frame = cap.retrieve()
        if not ret:
            continue
        else:
            
            #gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #laplacian = cv2.Laplacian(frame,cv2.CV_64F) #need gray
            #edges = cv2.Canny(frame,100,200)
            
            img_hsv=cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)


            cv2.imshow('video', img_hsv)
    if cv2.waitKey(10) == 27:
        break
