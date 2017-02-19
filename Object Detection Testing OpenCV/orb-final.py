import numpy as np
import cv2
from matplotlib import pyplot as plt

# Minimum number of matching points needed for a match
MIN_MATCH_COUNT = 10

# Initial Parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)

cap = cv2.VideoCapture(0)

img1 = cv2.imread('test1.png',0)          # queryImage

# Initiate ORB detector
orb = cv2.ORB_create()

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

kp1, des1 = orb.detectAndCompute(img1,None)


while(True):
    # Capture frame-by-frame
    ret, img2 = cap.read()
    kp2, des2 = orb.detectAndCompute(img2,None)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    good = matches#[:10]
    print len(good)
    if len(good) > MIN_MATCH_COUNT:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        if mask is not None:
            matchesMask = mask.ravel().tolist()
            print "Handling exception 'M' is None ......................"
        else:
            matchesMask = [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1]

        h, w = img1.shape
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)

        if M == None:
            print "M ============ None"
            # M = np.zeros(shape=(3,3))
            M = np.array(
                [[-1.26476052e+00, -5.37809282e-01, 4.70907776e+02], [4.68551145e-01, -9.66603143e-01, 2.27542443e+02],
                 [-5.17111716e-04, 1.55056727e-04, 1.00000000e+00]])

        print M
        dst = cv2.perspectiveTransform(pts, M)

        img2 = cv2.polylines(img2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)

    else:
        print "Not enough matches are found - %d/%d" % (len(good), MIN_MATCH_COUNT)
        matchesMask = None

    draw_params = dict(matchColor=None,  # (0,255,0), # draw matches in green color
                       singlePointColor=None,
                       matchesMask=None,  # matchesMask, # draw only inliers
                       flags=2)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, **draw_params)#flags=2)

    print "x";
    print img3;

    # Display the resulting frame
    cv2.imshow('frame',img3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
