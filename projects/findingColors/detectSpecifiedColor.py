import cv2 as cv
import numpy as np
color=[1,2,3]
kernel = np.ones((5,5),np.uint8)
video=cv.VideoCapture(0)
backSub=cv.createBackgroundSubtractorMOG2(10,10)
def mouseEvents(event,x,y,flags,params):
    global color
    if event==cv.EVENT_LBUTTONDBLCLK:
        print('hello')
        cv.circle(frame, (x, y), 15, (255, 0, 0, 0), 2)
        color=frame[x,y]
        print(color)

cv.namedWindow('result')
cv.setMouseCallback('result',mouseEvents)

while(True):

    _,frame=video.read(0)
    blue=cv.getTrackbarPos('blue','result')
    green = cv.getTrackbarPos('green', 'result')
    red = cv.getTrackbarPos('red', 'result')



    b=color[0]
    g=color[1]
    r=color[2]

    lowerBound=np.array([b,g,r],np.uint8)
    upperBound=np.array([b+12,g+12,r+12],np.uint8)
    mask=cv.inRange(frame,lowerBound,upperBound)
    fgmask=backSub.apply(mask)


#    print('The contou is ',conotors.length())

    res=cv.bitwise_and(frame,frame,mask=fgmask)
    resGray=cv.cvtColor(res,cv.COLOR_BGR2GRAY)
    _, conotors, heirarcy = cv.findContours(resGray, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
   # res=cv.dilate(res,kernel,iterations=1)
    res=cv.morphologyEx(res,cv.MORPH_OPEN,kernel)
    res=cv.morphologyEx(res,cv.MORPH_CLOSE,kernel)
    cv.drawContours(frame,conotors,-1,(0,0,255),2)
    # for i in conotors:
    #     x,y,w,h=cv.boundingRect(i)
    #     cv.rectangle(res,(x,y),(x+w,y+h),(255,0,0),1)



    cv.imshow('result',frame)
    cv.imshow('track',res)
    k=cv.waitKey(1)
    if k==ord('e'):
        break


