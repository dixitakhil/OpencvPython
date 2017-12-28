import cv2 as cv
import numpy as np

cr,cb,cc=0,0,0
color=(0,0,255)

def nothing(x):
    pass
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)


image=np.zeros((512,512,3),np.uint8)
cv.namedWindow('hello')

cv.createTrackbar('R','hello',0,255,nothing)
cv.createTrackbar('G','hello',0,255,nothing)
cv.createTrackbar('B','hello',0,255,nothing)

draw=False
mode=True
ix,iy=-1,-1
color=[255,0,0]
def drawing(event,x,y,flags,params):

      global ix,iy,draw,mode,color,cr,cb,cc
      if event==cv.EVENT_LBUTTONDOWN:
          draw=True
          ix,iy=x,y


      elif event==cv.EVENT_MOUSEMOVE:
          if draw==True:
              if mode==True:
                  cv.rectangle(image,(ix,iy),(x,y),(cr,cb,cc),-1)
              else:cv.circle(image,(x,y),5,color,-1)

      elif event==cv.EVENT_LBUTTONUP:
          draw = False
          if mode == True:
              cv.rectangle(image, (ix, iy), (x, y), (cr,cb,cc), -1)
          else:
              cv.circle(image, (x, y), 5, (cr,cb,cc), -1)


cv.setMouseCallback('hello',drawing)

while(True):
    cv.imshow('hello',image)
    k=cv.waitKey(1)
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')

    color=(b,g,r)
    cr,cb,cc=r,b,g
    if k==ord('m'):
        mode=not mode

    if k==ord('e'):
        break

cv.destroyAllWindows()


def nothing(x):
    pass
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)

