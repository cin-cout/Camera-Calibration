from ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2 
import numpy as np

class Controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda:self.callhw("221"))
        self.ui.pushButton_2.clicked.connect(lambda:self.callhw("222"))
        self.ui.pushButton_3.clicked.connect(self.callhw223)
        self.ui.pushButton_4.clicked.connect(lambda:self.callhw("224"))
        self.ui.pushButton_5.clicked.connect(lambda:self.callhw("225"))
    
    def callhw(self,s): 
        f = open(s +".py","r",encoding="utf-8")  #注意此行
        exec(f.read())
    
    def callhw223(self):
        if self.ui.lineEdit.text() != "":
            print(self.ui.lineEdit.text())
            num = int(self.ui.lineEdit.text())

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
        a = int(num)
        ma = cv2.Rodrigues(rvecs[a-1])[0]
        f = np.hstack((ma,tvecs[a-1]))
        print(f)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Controller()
    window.show()
    sys.exit(app.exec_())


