import cv2 as cv
import numpy as np

def mouseCallBack(event,x,y,flags,params):

        if(event==cv.EVENT_LBUTTONDBLCLK):
           cv.circle(image,(x,y),15,(255,0,0,0),-1)


image=np.zeros((512,512,3),np.uint8)
cv.namedWindow('imagee')
cv.setMouseCallback('imagee',mouseCallBack)

while(1):
    cv.imshow('imagee',image)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()


