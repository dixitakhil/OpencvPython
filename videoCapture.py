import cv2 as cv
import numpy as np

videoCapture=cv.VideoCapture('D:/movies/Now You See Me.mp4')


while(True):
    ret,videoFrame=videoCapture.read()
    # frame=cv.cvtColor(videoFrame,cv.COLOR_BGR2GRAY)
    cv.imshow('frame',videoFrame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


videoCapture.release()


# import numpy as np
# import cv2
#
# cap = cv2.VideoCapture(0)
#
# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Display the resulting frame
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()