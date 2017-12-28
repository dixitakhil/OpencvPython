import cv2 as cv
import numpy as np

video=cv.VideoCapture(0)
eye_cascade = cv.CascadeClassifier('D:/opencvextracted/opencv/sources/data/haarcascades/haarcascade_eye.xml')
windowClose = np.ones((5, 5), np.uint8)
windowOpen = np.ones((2, 2), np.uint8)
windowErode = np.ones((2, 2), np.uint8)
while(True):
    _,frame=video.read()
    gray=cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
    eyes=eye_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in eyes:
        roiEye=gray[y:y+h,x:x+h]
        thresh=cv.equalizeHist(gray[y:y+h,x:x+h])
        ret,thresh=cv.threshold(roiEye,50,255,cv.THRESH_BINARY)
        #gray=cv.cvtColor(thresh,cv.COLOR_BGR2GRAY)
        thresh = cv.morphologyEx(thresh, cv.MORPH_CLOSE, windowClose)
        thresh = cv.morphologyEx(thresh, cv.MORPH_ERODE, windowErode)
        thresh = cv.morphologyEx(thresh, cv.MORPH_OPEN, windowOpen)

        threshold=cv.inRange(thresh,250,255)
        _, contours, hierarchy = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
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
                    cv.circle(roiEye, (cx, cy), 5, 255, -1)
        cv.imshow('result', roiEye)



    cv.waitKey(1)