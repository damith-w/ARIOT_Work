import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

img1 = cv2.imread('test1.png',0)          # queryImage

sift = cv2.xfeatures2d.SIFT_create()
bf = cv2.BFMatcher()

kp1, des1 = sift.detectAndCompute(img1,None)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    kp2, des2 = sift.detectAndCompute(frame,None)
    matches = bf.knnMatch(des1,des2, k=2)

    # Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])

    # cv2.drawMatchesKnn expects list of lists as matches.
    img3 = cv2.drawMatchesKnn(img1,kp1,frame,kp2,good, None, flags=2)

    # Display the resulting frame
    cv2.imshow('frame',img3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
