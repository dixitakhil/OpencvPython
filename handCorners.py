import cv2 as cv
import numpy as np

image=cv.imread('C:/Users/Akhil Dixit/Desktop/attenImages/hands.jpg')
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
#gray=np.float32(gray)
gray=cv.Canny(gray,100,200)

corners=cv.cornerHarris(gray,3,5,0.04)
print(corners)
corners=cv.dilate(corners,None)


image[corners>0.09*corners.max() ]=[0,0,255]
cv.imshow('corners',image)


cv.waitKey(0)
# video=cv.VideoCapture(0)
#
# while (True):
#     _,frame=video.read()
#     gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#     gray=np.float32(gray)
#     corners=cv.cornerHarris(gray,2,3,0.04)
#     corners=cv.dilate(corners,None)
#     frame[corners>0.1*corners.max()]=[0,0,255]
#     cv.imshow('corners',frame)
#     k=cv.waitKey(1)
#     if k==ord('e'):
#         break
# cv.destroyAllWindows()