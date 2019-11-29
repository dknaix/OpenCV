import cv2

cap = cv2.VideoCapture("out.mp4")

while True:
    if cap.grab():
        flag, frame = cap.retrieve()
        if not flag:
            continue
        else:
            cv2.imshow('video', frame)
    if cv2.waitKey(10) == 27:
        break
