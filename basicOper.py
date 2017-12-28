import cv2 as cv

image=cv.imread('C:/Users/Akhil Dixit/Desktop/attenImages/urban-slums_0.jpg')
crop=image[100:300,50:200]
image[:,:,0]=2
image[:,:,1]=2
image[:,:,2]=2
cv.imshow('hello',image)

cv.waitKey(0)