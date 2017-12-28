import cv2 as cv
import numpy  as np

video=cv.VideoCapture(0)
frame=cv.createBackgroundSubtractorMOG2()

while(1):
    temp,img=video.read()
    mask=frame.apply(img)
    cv.imshow('here',mask)
    cv.waitKey(1)


cv.destroyAllWindows()
#
# import numpy as np
# import cv2
#
# cap = cv2.VideoCapture(0)
#
# fgbg = cv2.createBackgroundSubtractorMOG2()
#
# while(1):
#     ret, frame = cap.read()
#
#     fgmask = fgbg.apply(frame)
#
#     cv2.imshow('frame',fgmask)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()