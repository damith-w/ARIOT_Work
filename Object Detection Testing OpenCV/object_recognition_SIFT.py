# import statements
import numpy as np
import cv2

# Minimum number of matching points needed for a match
MIN_MATCH_COUNT = 10

# Getting the Video Stream from default webcam (cam0)
cap = cv2.VideoCapture(0)

# Initializing SIFT object
sift = cv2.xfeatures2d.SIFT_create()

# Initial Parameters 
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

# Reference Image read and finding SIFT distence
img1 = cv2.imread('test1.png',0)
kp1, des1 = sift.detectAndCompute(img1,None)
k = 0 
while(True):
    print k
    k = k+1
    ret, img2 = cap.read()
    print "Calculating................."
    #img2 = cv2.imread('test2.jpg',0) # trainImage
    kp2, des2 = sift.detectAndCompute(img2,None)
    try:
        matches = flann.knnMatch(des1,des2,k=2)
    except cv2.error as e:
        continue
    
    # store all the good matches as per Lowe's ratio test.
    good = []
    good1 = []
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)

    if len(good)>MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        if mask is not None:
            matchesMask = mask.ravel().tolist()
        else:
            matchesMask = [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1]
            print "Handling exception 'M' is None ......................"

        h,w = img1.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        
        if M == None:
            print "M ============ None"
            M = np.zeros(shape=(3,3))
            #M = np.array([[ -1.26476052e+00,-5.37809282e-01,4.70907776e+02],[  4.68551145e-01,-9.66603143e-01,2.27542443e+02],[ -5.17111716e-04,1.55056727e-04,1.00000000e+00]])

        print M
        dst = cv2.perspectiveTransform(pts,M)

        img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)

    else:
        print "Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT)
        matchesMask = None

    draw_params = dict(matchColor = None, #(0,255,0), # draw matches in green color
                       singlePointColor = None,
                       matchesMask = [],#matchesMask, # draw only inliers
                       flags = 2)

    try:
        img3 = cv2.drawMatches(img1,kp1,img2,kp2,good1,None,**draw_params)
    except cv2.error as e:
        print "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD"
        continue

    cv2.imshow('frame',img3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #gc.collect()

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
