import cv2 as cv
import numpy as np
video=cv.VideoCapture(0)
def motion(tminus,t,tplus):
    d1=cv.absdiff(tplus,t)
    d2=cv.absdiff(t,tminus)
    return cv.bitwise_and(d1,d2)
kernel = np.ones((5,5),np.uint8)
tminus=cv.cvtColor(video.read()[1],cv.COLOR_BGR2GRAY)
t=cv.cvtColor(video.read()[1],cv.COLOR_BGR2GRAY)
tplus=cv.cvtColor(video.read()[1],cv.COLOR_BGR2GRAY)
height, width= tminus.shape
min_x, min_y = width, height
max_x = max_y = 0

while (True):
    frame=motion(tminus,t,tplus)
    ret,imageFrame=video.read()
    frame= cv.GaussianBlur(frame,(5,5),0)

    frame=cv.morphologyEx(frame,cv.MORPH_OPEN,kernel=kernel)
    frame=cv.morphologyEx(frame, cv.MORPH_CLOSE,kernel=kernel)
    ret,frame=cv.threshold(frame, 10, 255, cv.THRESH_BINARY)
    # frame=cv.equalizeHist(frame)

    #_,frame=cv.threshold(frame,200,255,cv.THRESH_BINARY)
    #frame=cv.inRange(frame,200,255)
    img,contours,heirarycy=cv.findContours(frame,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)


    cv.drawContours(imageFrame,contours,-1,(255,0,0),0)
    for cont in contours:
        font = cv.FONT_HERSHEY_SIMPLEX
        (x,y,w,h)=cv.boundingRect(cont)
        #cv.rectangle(imageFrame,(x,y),(x+w,y+h),(0,0,255),1)
        min_x, max_x = min(x, min_x), max(x + w, max_x)
        min_y, max_y = min(y, min_y), max(y + h, max_y)
    #     if w > 80 and h > 80:
    #      # cv.rectangle(imageFrame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #
    #
    #     if max_x - min_x > 0 and max_y - min_y > 0:
    # #cv.rectangle(imageFrame, (min_x, min_y), (max_x, max_y), (0, 255, 0), 2)
    #



    if len(contours)>1:
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(imageFrame, 'movement detected', (50, 50), font, 1, (255, 255, 255), 2, cv.LINE_AA)

    print(len(contours))

    cv.imshow('imageFrame',imageFrame)
    cv.imshow('frame',frame)

    tminus=t
    t=tplus
    tplus=cv.cvtColor(video.read()[1],cv.COLOR_BGR2GRAY)

    k=cv.waitKey(1)
    if k==ord('e'):
        break
cv.destroyAllWindows()