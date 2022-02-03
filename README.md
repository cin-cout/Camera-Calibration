# Camera-Calibration

Implement the Camera-Calibration using OpenCV,and build the UI interface using PyQT5.

## Build the project 
* You need to install Python 3.7 first.
* Install opencv-contrib-python, and pyqt5.
```
pip install opencv-contrib-python
pip install PyQt5
```

## Usage

* Execute controller
```
python controller.py
```
* You will see the UI interface

![](https://i.imgur.com/3Zv6DHE.png)

* Corner Detection

Find and draw the corners on the chessboard for each image.

Show each picture like below every 0.5 seconds(there are total 15 pictures).

![](https://i.imgur.com/MtOyDow.png)

* Find the Intrinsic Matrix

You will get the Intrinsic Matrix on the terminal
 ```
Camera-Intrinsics:
 [[2.22547908e+03 0.00000000e+00 1.02514624e+03]
 [0.00000000e+00 2.22512237e+03 1.03925201e+03]
 [0.00000000e+00 0.00000000e+00 1.00000000e+00]]
 ```
 
 * Find the Extrinsic Matrix
 Choose a picture 1~15 and will get the Extrinsic Matrix on the terminal
 ```
 3
[[-2.23139076e-01 -5.23755794e-01  8.22124577e-01  4.25210425e+00]
 [ 9.64251080e-01  5.06558397e-03  2.64941871e-01 -2.04383464e+00]
 [-1.42929381e-01  8.51853396e-01  5.03901760e-01  1.39827928e+01]]
 ```
 * Find the Distortion Matrix
 
 You will get the Distortion Matrix on the terminal
 ```
 Camera-Distortion Matrix :
 [[-1.28863499e-01  9.39670823e-02 -9.26653406e-04 -2.03033843e-05
  -5.61426780e-03]]
 ```
 
 * Show the undistorted  result 
 Undistort the chessboard images and show a distorted and undistorted image every 0.5 seconds(there are total 15 pictures).
 ![](https://i.imgur.com/WMz8Xrc.png)
