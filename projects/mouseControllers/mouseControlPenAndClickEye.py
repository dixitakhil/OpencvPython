import numpy as np
import cv2 as cv
import ctypes
from threading import Timer
import time
from pymouse import PyMouse as pm
video=cv.VideoCapture(0)

eyeCount=0
def discard():
    global eyeCount
    eyeCount=0

lowerbb= (0, 0, 0)
upperbb=(179,50,100)

firstTime=0
eyecasscade=cv.CascadeClassifier('D:/opencvextracted/opencv/sources/data/haarcascades/haarcascade_eye.xml')

#lowerb=(29, 86, 6)
#upperb=(64, 255, 255)
upperb=(130,255,255)
lowerb=(110,50,50)
lowerRed=(0, 100, 100)
upperRed=(10, 255, 255)
m=pm()
centroidPosition=[0,0]
backGroundSubtractor=cv.createBackgroundSubtractorMOG2()
while(True):
    _,frame=video.read()
    frame=cv.flip(frame,1)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    eyes = eyecasscade.detectMultiScale(gray, 1.3, 5)
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    rangedblue = cv.GaussianBlur(hsv, (5, 5), 0)
    rangedblue=cv.inRange(rangedblue,lowerb,upperb)
    rangedblue=cv.morphologyEx(rangedblue,cv.MORPH_CLOSE,None)
    rangedblue = cv.morphologyEx(rangedblue, cv.MORPH_OPEN, None)
    _,threshold=cv.threshold(rangedblue,10,255,cv.THRESH_BINARY)

    #for red
    rangedred = cv.inRange(hsv, lowerRed, upperRed)
    rangedred = cv.morphologyEx(rangedred, cv.MORPH_CLOSE, None)
    rangedred = cv.morphologyEx(rangedred, cv.MORPH_OPEN, None)
    _c, thresholdred = cv.threshold(rangedred, 10, 255, cv.THRESH_BINARY)

    imgr,contoursr,heirarchyr=cv.findContours(thresholdred,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    if len(contoursr)>0:
        cr=max(contoursr,key=cv.contourArea)
        (xr,yr,wr,hr)=cv.boundingRect(cr)
        cv.rectangle(frame,(xr,yr),(xr+wr,yr+hr),(0,255,0),2)
        Momentsr=cv.moments(cr)
        cXr = int(Momentsr["m10"] / Momentsr["m00"])
        cYr = int(Momentsr["m01"] / Momentsr["m00"])
        cv.circle(frame, (cXr, cYr), 2, (0, 0, 255), -1)
    #red end

    img,contours,heirarchy=cv.findContours(threshold,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    #cv.drawContours(frame,contours,-1,(0,0,255),3)
    if len(contours)>0:
        c=max(contours,key=cv.contourArea)
        (x,y,w,h)=cv.boundingRect(c)
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        Moments=cv.moments(c)
        cX = int(Moments["m10"] / Moments["m00"])
        cY = int(Moments["m01"] / Moments["m00"])

        cv.line(frame,(centroidPosition[0],centroidPosition[1]),(cX,cY),(12,120,144),3)
        cv.circle(frame,(cX,cY),2,(0,255,0),-1)
        distanceTransversedX=centroidPosition[0]-cX
        distanceTransversedY = centroidPosition[1] - cY
        if distanceTransversedX>0:
            if distanceTransversedX>2:
                if distanceTransversedY>0:
                    if abs(distanceTransversedY)>2:
                        print('north-west')
                if distanceTransversedY<0:
                    if abs(distanceTransversedY)>2:
                        print('south-west')
                centroidPosition[0] = cX
                print('west')
        if distanceTransversedX<0:
            if abs(distanceTransversedX)>2:
                if distanceTransversedY>0:
                    if abs(distanceTransversedY)>2:
                        print('north-east')
                if distanceTransversedY<0:
                    if abs(distanceTransversedY)>2:
                        print('south-east')
                #print('east')
                centroidPosition[0] = cX
        if distanceTransversedY>0:
            if distanceTransversedY>2:
                centroidPosition[1] = cY
                #print('north')
        if distanceTransversedY<0:
            if abs(distanceTransversedY)>2:
                centroidPosition[1] = cY
               # print('south')
        if abs(distanceTransversedX)>2 or abs(distanceTransversedY)>2:
            x,y=m.position()
            m.move(x-distanceTransversedX*9,y-distanceTransversedY*9)
        if eyeCount>2:
                 ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left down
                 ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
                 discard()

        print('The eye count is ***********************',eyeCount)
        if len(eyes)==0:
             eyeCount=eyeCount+1
             timer = Timer(2, discard)
             timer.start()
    cv.imshow('movingCursor',frame)
    k=cv.waitKey(1)
    if k==ord('e'):
        break
