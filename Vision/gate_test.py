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
left = frame[0:height, 0:width/2]
hsv_img = cv2.cvtColor(left, cv2.COLOR_BGR2HSV)

#orange color range
lower = np.array([5,50,50], dtype="uint8")
upper = np.array([15,255,255], dtype="uint8")

#thresholding to check if color in image
mask = cv2.inRange(hsv_img, lower, upper)
output = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)


thresh = cv2.threshold(mask, 5, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.dilate(thresh,None, iterations=2)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
if len(cnts) > 2:
    for c in cnts:
        cv2.drawContours(left, [c], -1, (0,255,0), 2)
    print "true"

else:
    print "false"
"""
cv2.imshow('left',left)
cv2.imshow('hsv',hsv_img)
cv2.imshow('mask',mask)
cv2.imshow('output',output)
cv2.imshow('left',left)

cv2.waitKey(0)

"""

