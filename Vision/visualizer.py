import cv2
import imutils
import numpy as np
import sys
import time


class visualizer:
    def __init__(self, name, frameRate=24, whRes=640, hRes = 480, camera=0):
        self.name=name

        #start video capture stream; return assertion if stream not started
        self.vidStream= cv2.VideoCapture(camera)
        if (!vidStream.isOpened()):
            CV_Assert("I can't see out this eye!")

        #intialize camera capture resolution and frame rate
        vidStream.set(CV_CAP_PROP_FRAME_WIDTH, wRes)
        vidStream.set(CV_CAP_PROP_FRAME_HEIGHT, hRes)
        vidStream.set(CV_CAP_PROP_FPS, frameRate)

        
    #deletes visualizer object and cleans up allocated resources   
    def __del__(self):
        self.vidStream.release()
        cv2.destroyAllWindows()

    #returns frameRate of visualizer object
    def getFrameRate():
        return frameRate

    #returns tuple containing resolution of visualizer
    def getRsolution():
        return (wRes, hRes)

    #captures current frame and writes it to the screen
    def capFrame():
        ret, frame = self.videoStream.read()
        cv2.imshow("Capture", frame)

    #returns current frame to process
    def getFrame():
        ret, frame = self.videoStream.read()
        return frame

    #converts BGR image to HSV image in order to threshold color in stream
    #detect circle with color
    #return true if circle of color found
    def detectBuoy(color):
        ret, frame = self.videoStream.read()
        hsv_img = cv2.cvtColor(frame, cvt.COLOR_BGR2HSV)

        if color == "red":
            lower = np.array([0,160,160],dtype="uint8")
            upper = np.array([10,180,180],dtype="uint8")
        elif color == "green":
            lower = np.array([45,100,50],dtype="uint8")
            upper = np.array([75,255,255],dtype="uint8")
        else:
            print("Please enter a valid buoy color")

        mask = cv2.inRange(hsv_img,lower,upper)
        output = cv2.bitwise_and(hsv_image, hsv_image, mask=mask)
        
        #cv2.imshow("{0} detected".format(color), output)
        return True


    #detects
    def detectGate():
        
        return

    def detectColor(color):
        
        return
    
    def detectLine(color):
        return

    def detectChannel():
        return
