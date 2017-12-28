import cv2 as cv

video=cv.VideoCapture(0)
def motion(tminus,t,tplus):
    d1=cv.absdiff(tplus,t)
    d2=cv.absdiff(t,tminus)
    return cv.bitwise_and(d1,d2)

tminus=cv.cvtColor(video.read()[1],cv.COLOR_BGR2GRAY)
t=cv.cvtColor(video.read()[1],cv.COLOR_BGR2GRAY)
tplus=cv.cvtColor(video.read()[1],cv.COLOR_BGR2GRAY)

while (True):
    cv.imshow('here',motion(tminus,t,tplus))
    tminus=t
    t=tplus
    tplus=cv.cvtColor(video.read()[1],cv.COLOR_BGR2GRAY)

    k=cv.waitKey(1)
    if k==ord('e'):
        break
cv.destroyAllWindows()