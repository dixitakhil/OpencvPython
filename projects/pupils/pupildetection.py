import cv2 as cv
import numpy as np

video=cv.VideoCapture(0)
windowClose = np.ones((5, 5), np.uint8)
windowOpen = np.ones((2, 2), np.uint8)
windowErode = np.ones((2, 2), np.uint8)
face_cascade = cv.CascadeClassifier('D:/opencvextracted/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('D:/opencvextracted/opencv/sources/data/haarcascades/haarcascade_eye.xml')

while(True):
    _,frame=video.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        roiForEyes = gray[y:y+h,x:x+w]
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        eyes=eye_cascade.detectMultiScale(roiForEyes)

        for (ex,ey,ew,eh) in eyes:


            mainEyeRegion=gray[eyes[0][1]+y:eyes[0][1]+h+eyes[0][3],eyes[0][0]+x:eyes[0][0]+w+eyes[0][2]]
            # if len(eyes)>0:
            #  cv.imshow('gg',mainEyeRegion)
            ret,eyeFrame=cv.threshold(mainEyeRegion,55,255,cv.THRESH_BINARY)
            if eyeFrame is not None:
             eyeFrame = cv.morphologyEx(eyeFrame, cv.MORPH_CLOSE, windowClose)
             eyeFrame = cv.morphologyEx(eyeFrame, cv.MORPH_ERODE, windowErode)
             eyeFrame = cv.morphologyEx(eyeFrame, cv.MORPH_OPEN, windowOpen)

             im2, contours, hierarchy = cv.findContours(eyeFrame, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

             if len(contours) >= 2:
                 # find biggest blob
                 maxArea = 0
                 MAindex = 0  # to get the unwanted frame
                 distanceX = []  # delete the left most (for right eye)
                 currentIndex = 0
                 for cnt in contours:
                     area = cv.contourArea(cnt)
                     center = cv.moments(cnt)
                     cx, cy = int(center['m10'] ), int(center['m01'] )
                     distanceX.append(cx)
                     if area > maxArea:
                         maxArea = area
                         MAindex = currentIndex
                     currentIndex = currentIndex + 1

                 del contours[MAindex]  # remove the picture frame contour
                 del distanceX[MAindex]

             eye = 'right'

             if len(contours) >= 2:  # delete the left most blob for right eye
                 if eye == 'right':
                     edgeOfEye = distanceX.index(min(distanceX))
                 else:
                     edgeOfEye = distanceX.index(max(distanceX))
                 del contours[edgeOfEye]
                 del distanceX[edgeOfEye]

             if len(contours) >= 1:  # get largest blob
                 maxArea = 0
                 for cnt in contours:
                     area = cv.contourArea(cnt)
                     if area > maxArea:
                         maxArea = area
                         largeBlob = cnt

             if len(largeBlob) > 0:
                 center = cv.moments(largeBlob)
                 cx, cy = int(center['m10'] / center['m00']), int(center['m01'] / center['m00'])
                 cv.circle(eyeFrame, (cx, cy), 5, 255, -1)

             if contours is not None:

              print('circles',len(contours))
              cv.drawContours(frame,contours,-1,(0,0,255),3)
              cv.resizeWindow('eyecontours',400,400)
              cv.imshow('eyecontours',eyeFrame)
             cv.rectangle(frame[y:y+h,x:x+w],(ex,ey),(ex+ew,ey+eh),(255,0,0),2)



    cv.imshow('final',frame)
    cv.waitKey(1)







