import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    if cap.grab():
        ret, img = cap.retrieve()
        if not ret:
            continue
        else:
            imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(imgray, 127, 255, 0)
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            #print("Number of contours = " + str(len(contours)))
            #print(contours[0])

            cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
            #cv2.drawContours(imgray, contours, -1, (0, 255, 0), 3)
            cv2.drawContours(thresh, contours, -1, (0, 255, 0), 3)
            
            cv2.imshow('Image', img)
            #cv2.imshow('Image GRAY', imgray)
            cv2.imshow('Image GRAY', thresh)


            #cv2.imshow('video', img_hsv)
    if cv2.waitKey(10) == 27:
        break
