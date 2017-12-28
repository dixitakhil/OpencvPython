import cv2 as cv
import numpy as np

video=cv.VideoCapture(0)

while(1):

    temp,frame=video.read()

    hsv=cv.cvtColor(frame , cv.COLOR_BGR2HSV)

    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    print(lower_blue)

    mask=cv.inRange(hsv,lower_blue,upper_blue)

    result=cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow('original',frame)
    cv.imshow('result',result)
    k = cv.waitKey(5) & 0xFF
    if k == ord('e'):
     break
cv.destroyAllWindows()
#
# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture(0)
#
# while(1):
#
#     # Take each frame
#     _, frame = cap.read()
#
#     # Convert BGR to HSV
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     # define range of blue color in HSV
#     lower_blue = np.array([110,50,50])
#     upper_blue = np.array([130,255,255])
#
#     # Threshold the HSV image to get only blue colors
#     mask = cv2.inRange(hsv, lower_blue, upper_blue)
#
#     # Bitwise-AND mask and original image
#     res = cv2.bitwise_and(frame,frame, mask= mask)
#
#     cv2.imshow('frame',frame)
#     cv2.imshow('mask',mask)
#     cv2.imshow('res',res)
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         break
#
# cv2.destroyAllWindows()