import cv2 
import numpy as np

criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
ojbp = np.zeros((11*8,3),np.float32)
ojbp[:,:2] = np.mgrid[0:8,0:11].T.reshape(-1,2)
objpoints = [] 
imgpoints = []

for i in range(1,16):
    
    img = cv2.imread("./Q2_image/"+str(i)+".bmp")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(img, (8,11), None)
    
    objpoints.append(ojbp)
    imgpoints.append(corners)
    sh = cv2.drawChessboardCorners(img,(8,11),corners,ret)
    

ret , mtx,dist,rvecs,tvecs = cv2.calibrateCamera(objpoints, imgpoints, img.shape[::-1],None,None)


for i in range(1,16):
    
    img2 = cv2.imread("./Q2_image/"+str(i)+".bmp")
    img3 = cv2.imread("./Q2_image/"+str(i)+".bmp")
    
    newcameramtx ,roi=cv2.getOptimalNewCameraMatrix(mtx, dist,(2048,2048), 0,(2048,2048))
    dst = cv2.undistort(img2,mtx,dist,None,newcameramtx)

    dst = cv2.resize(dst, (512,512))
    img3 = cv2.resize(img3, (512,512))
    f = np.hstack([img3,dst])
    cv2.imshow('img',f)
    cv2.waitKey(500)

cv2.waitKey(0)
cv2.destroyAllWindows()