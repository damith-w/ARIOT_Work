import numpy as np
import cv2
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 30

cap = cv2.VideoCapture(0)

img1 = cv2.imread('test1.png',0)          # queryImage

sift = cv2.xfeatures2d.SIFT_create()
bf = cv2.BFMatcher()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
#FLANN_INDEX_KDTREE = 0
#index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
#search_params = dict(checks = 50)
#flann = cv2.FlannBasedMatcher(index_params, search_params)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

kp1, des1 = sift.detectAndCompute(img1,None)



while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    kp2, des2 = sift.detectAndCompute(frame,None)
    matches = bf.knnMatch(des1,des2, k=2)
    

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
    #matches = flann.knnMatch(des1,des2, k=2)
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Apply ratio test
    good = []

    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #if len(good)>MIN_MATCH_COUNT:
    #    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    #    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

    #    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    #    matchesMask = mask.ravel().tolist()

    #    h,w = img1.shape
    #    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    #    dst = cv2.perspectiveTransform(pts,M)

    #    frame = cv2.polylines(frame,[np.int32(dst)],True,255,3, cv2.LINE_AA)

    #else:
    #    print "Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT)
    #    matchesMask = None
   
    

    #draw_params = dict(matchColor = (0,255,0), # draw matches in green color
    #               singlePointColor = None,
    #               matchesMask = matchesMask, # draw only inliers
    #               flags = 2)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


    # cv2.drawMatchesKnn expects list of lists as matches.
    img3 = cv2.drawMatchesKnn(img1,kp1,frame,kp2,good, None, flags=2)

    # Display the resulting frame
    cv2.imshow('frame',img3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
