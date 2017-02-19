import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

img1 = cv2.imread('test1.png',0)          # queryImage

# Initiate ORB detector
orb = cv2.ORB_create()

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

kp1, des1 = orb.detectAndCompute(img1,None)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    kp2, des2 = orb.detectAndCompute(frame,None)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,frame,kp2,matches[:10], None, flags=2)

    # Apply ratio test
    #good = []
    #for m,n in matches:
    #    if m.distance < 0.75*n.distance:
    #        good.append([m])

    # cv2.drawMatchesKnn expects list of lists as matches.
    #img3 = cv2.drawMatchesKnn(img1,kp1,frame,kp2,good, None, flags=2)

    # Display the resulting frame
    cv2.imshow('frame',img3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
