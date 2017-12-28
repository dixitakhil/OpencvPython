import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from pymouse import PyMouse as pm

m=pm()

video=cv.VideoCapture(0)
lowerbb= (0, 0, 0)
upperbb=(179,50,100)
centroidPosition=[0,0]
eyecasscade=cv.CascadeClassifier('D:/opencvextracted/opencv/sources/data/haarcascades/haarcascade_eye.xml')
while(True):
    count=0;
    _,frame=video.read()
    frame=cv.flip(frame,1)
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    eyes=eyecasscade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in eyes:
        # if count%2==0:
        #    cv.imshow('e',frame[y:y+h,x:x+w])
        #    count+=count
        hsv=cv.cvtColor(frame[y+20:y+h-10,x:x+w-20],cv.COLOR_BGR2HSV)
        gausianBlur=cv.GaussianBlur(hsv,(5,5),0)
        range=cv.inRange(gausianBlur,lowerbb,upperbb)
        range = cv.morphologyEx(range, cv.MORPH_CLOSE, None)
        range = cv.morphologyEx(range, cv.MORPH_OPEN, None)
        _,threshold=cv.threshold(range,0,255,cv.THRESH_BINARY)
        img,contours,heirarchy=cv.findContours(threshold,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        print(len(contours))
        if  len(contours)>0:
            cmax = max(contours, key=cv.contourArea)
            Moments = cv.moments(cmax)

            cX = int(Moments["m10"] / Moments["m00"])
            cY = int(Moments["m01"] / Moments["m00"])
            distanceTransversedX = centroidPosition[0] - cX
            distanceTransversedY = centroidPosition[1] - cY
            cv.circle(frame, (cX + x, cY + y + 20), 2, (0, 0, 255), -5)

            if distanceTransversedX > 0:
                if distanceTransversedX > 5:
                    if distanceTransversedY > 0:
                        if abs(distanceTransversedY) > 5:
                            print('north-west')
                    if distanceTransversedY < 0:
                        if abs(distanceTransversedY) > 5:
                            print('south-west')
                    centroidPosition[0] = cX
                    print('west')
            if distanceTransversedX < 0:
                if abs(distanceTransversedX) > 5:
                    if distanceTransversedY > 0:
                        if abs(distanceTransversedY) > 5:
                            print('north-east')
                    if distanceTransversedY < 0:
                        if abs(distanceTransversedY) > 5:
                            print('south-east')
                    print('east')
                    centroidPosition[0] = cX
            if distanceTransversedY > 0:
                if distanceTransversedY > 5:
                    centroidPosition[1] = cY
                    print('north')
            if distanceTransversedY < 0:
                if abs(distanceTransversedY) > 5:
                    centroidPosition[1] = cY
                    print('south')
            if abs(distanceTransversedX) > 5 or abs(distanceTransversedY) > 5:
                x, y = m.position()

                m.move(x - distanceTransversedX*10, y - distanceTransversedY * 10)

        cv.imshow('hsv',threshold)
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)


    cv.imshow('frame',frame)
    k=cv.waitKey(5)
    if k==ord('e'):
        break





# Tring new
#
# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt
# centroidPos=[0,0]
# video=cv.VideoCapture(0)
# lowerbb=(0, 0, 0)
# upperbb=(179,50, 100)
# meanx=[]
# meany=[]
# eyecasscade=cv.CascadeClassifier('D:/opencvextracted/opencv/sources/data/haarcascades/haarcascade_eye.xml')
# while(True):
#     count=0;
#     _,frame=video.read()
#     frame=cv.flip(frame,5)
#     gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#     hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
#     eyes=eyecasscade.detectMultiScale(gray,5.3,5)
#     for (x,y,w,h) in eyes:
#         # if count%2==0:
#         #    cv.imshow('e',frame[y:y+h,x:x+w])
#         #    count+=count
#         count=0
#
#         hsv=cv.cvtColor(frame[y+25:y+h-10,x+15:x+w-20],cv.COLOR_BGR2HSV)
#         pupilO=frame[y+25:y+h-10,x+15:x+w-20]
#         gausianBlur=cv.medianBlur(hsv,5,0)
#         range=cv.inRange(hsv,lowerbb,upperbb)
#         range = cv.morphologyEx(range, cv.MORPH_CLOSE, None)
#         range = cv.morphologyEx(range, cv.MORPH_OPEN, None)
#         _,threshold=cv.threshold(range,0,255,cv.THRESH_BINARY)
#         img,contours,heirarchy=cv.findContours(threshold,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
#         print(len(contours))
#
#
#         if len(contours) >= 2:
#             # find biggest blob
#             maxArea = 0
#             MAindex = 0  # to get the unwanted frame
#             distanceX = []  # delete the left most (for right eye)
#             currentIndex = 0
#             print(len(contours))
#             for cnt in contours:
#                 area = cv.contourArea(cnt)
#                 center = cv.moments(cnt)
#                 cx, cy = int(center['m10'] / center['m00']), int(center['m01'] / center['m00'])
#                 distanceX.append(cx)
#                 if area > maxArea:
#                     maxArea = area
#                     MAindex = currentIndex
#                 currentIndex = currentIndex + 5
#
#             del contours[MAindex]  # remove the picture frame contour
#             del distanceX[MAindex]
#
#         eye = 'right'
#
#         if len(contours) >= 2:  # delete the left most blob for right eye
#             if eye == 'right':
#                 edgeOfEye = distanceX.index(min(distanceX))
#             else:
#                 edgeOfEye = distanceX.index(max(distanceX))
#             del contours[edgeOfEye]
#             del distanceX[edgeOfEye]
#
#         if len(contours) >= 5:  # get largest blob
#             maxArea = 0
#             for cnt in contours:
#                 area = cv.contourArea(cnt)
#                 if area > maxArea:
#                     maxArea = area
#                     largeBlob = cnt
#
#         if len(largeBlob) > 0:
#             center = cv.moments(largeBlob)
#             cx, cy = int(center['m10'] / center['m00']), int(center['m01'] / center['m00'])
#             cv.circle(frame,(cx+x+15 ,cy+y+25), 5, (0, 0, 255), -5)
#
#
#
#
#         cv.imshow('w',pupilO)
#         cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
#
#
#     cv.imshow('frame',frame)
#     k=cv.waitKey(5)
#     if k==ord('e'):
#         break
#
#
#
