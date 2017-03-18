import cv2
import sys
import time
import imutils
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required = True, help="path to input image")
args = vars(ap.parse_args())

frame = cv2.imread(args["image"])
height, width, chan = frame.shape
hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#color range
lower = np.array([5,50,50], dtype="uint8")
upper = np.array([15,255,255], dtype="uint8")

#thresholding to ease contouring process
mask = cv2.inRange(hsv_img, lower, upper)
output = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)
thresh = cv2.threshold(mask, 5, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.dilate(thresh,None, iterations=2)
        
#finds contours (shape) of orange in image; if no contours found, gate not found
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

#center (x,y) for target
cX=0
cY=0
for c in cnts:
	M = cv2.moments(c)
        if (M["m00"]==0):
		M["m01"]=1
              	cX = int(M["m10"]/M["m00"])
              	cY = int(M["m01"]/M["m00"])
        cv2.drawContours(frame, [c], -1, (0,255,0), 2)      
	cv2.circle(frame, (cX,cY), 7, (255,255,255), -1)
cv2.imshow('frame', frame)
cv2.waitKey(0)
