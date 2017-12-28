# import numpy as np
# import cv2
#
# face_cascade = cv2.CascadeClassifier('D:/opencvextracted/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('D:/opencvextracted/opencv/sources/data/haarcascades/haarcascade_eye.xml')
#
# img = cv2.imread('D:/my_pics/2017-05-30/IMG_5462.JPG')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#     roi_gray = gray[y:y+h, x:x+w]
#     roi_color = img[y:y+h, x:x+w]
#     eyes = eye_cascade.detectMultiScale(roi_gray)
#     for (ex,ey,ew,eh) in eyes:
#         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('D:/opencvextracted/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('D:/opencvextracted/opencv/sources/data/haarcascades/haarcascade_eye.xml')

img = cv2.VideoCapture(0)

while(1):
 temp,frame=img.read()
 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 for (x,y,w,h) in faces:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
 cv2.imshow('img',frame)
 cv2.waitKey(1)


cv2.destroyAllWindows()