import cv2

imgFile = cv.imread('1.jpg')

cv.imshow('dst_rt', imgFile)
cv.waitKey(0)
cv.destroyAllWindows()
