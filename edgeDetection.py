import cv2 as cv

video=cv.VideoCapture(0)
while(1):
    temp,frame=video.read()
    edge=cv.Canny(frame,400,500)
    cv.imshow('original',frame)
    cv.imshow('edge',edge)
    k=cv.waitKey(1)
    if k==ord('e'):
        break

cv.destroyAllWindows()