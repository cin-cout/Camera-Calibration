import cv2 
for i in range(1,16):
    
    img = cv2.imread("./Q2_image/"+str(i)+".bmp")
    ret, corners = cv2.findChessboardCorners(img, (8,11), flags=3)
    
    img = cv2.drawChessboardCorners(img,(8,11),corners,ret)
    img = cv2.resize(img, (512,512))
    cv2.imshow('img',img)
    cv2.waitKey(500)

cv2.waitKey(0)
cv2.destroyAllWindows()