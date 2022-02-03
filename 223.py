import cv2 
import numpy as np

criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
ojbp = np.zeros((11*8,3),np.float32)
ojbp[:,:2] = np.mgrid[0:8,0:11].T.reshape(-1,2)
objpoints = [] # 存儲世界坐標系中的3D點(實際上Zw在標定板上的值為0)
imgpoints = []

for i in range(1,16):
    
    img = cv2.imread("./Q2_image/"+str(i)+".bmp")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(img, (8,11), None)
    
    objpoints.append(ojbp)
    imgpoints.append(corners)
    sh = cv2.drawChessboardCorners(img,(8,11),corners,ret)
    

ret , mtx,dist,rvecs,tvecs = cv2.calibrateCamera(objpoints, imgpoints, img.shape[::-1],None,None)

b = input("input:　")
a = int(b)
ma = cv2.Rodrigues(rvecs[a-1])[0]
f = np.hstack((ma,tvecs[a-1]))
print(f)


