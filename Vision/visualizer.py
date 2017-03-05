import cv2
import imutils
import numpy as np
import sys
import time


class visualizer:
    def __init__(self, frameRate=24, whRes=640, hRes = 480, camera=0):

        #start video capture stream; return assertion if stream not started
        self.vidStream = cv2.VideoCapture(camera)
        #if (!vidStream.isOpened()):
         #   CV_Assert("I can't see out this eye!")

        #intialize camera capture resolution and frame rate
        vidStream.set(CV_CAP_PROP_FRAME_WIDTH, wRes)
        vidStream.set(CV_CAP_PROP_FRAME_HEIGHT, hRes)
        vidStream.set(CV_CAP_PROP_FPS, frameRate)

        
    #deletes visualizer object and cleans up allocated resources   
    def __del__(self):
        self.vidStream.release()
        cv2.destroyAllWindows()

    #returns frameRate of visualizer object
    def getFrameRate(self):
        return frameRate

    #returns tuple containing resolution of visualizer
    def getResolution(self):
        return (wRes, hRes)

    #captures current frame and writes it to the screen
    def capFrame(self):
        ret, frame = self.videoStream.read()
        cv2.imshow("Capture", frame)

    #returns current frame to process
    def getFrame(self):
        ret, frame = self.videoStream.read()
        return frame

    #converts BGR image to HSV image in order to threshold color in stream
    #detect circle with color
    #return true if circle of color found
    def detectBuoy(self, color):
        ret, frame = self.videoStream.read()
        hsv_img = cv2.cvtColor(frame, cvt.COLOR_BGR2HSV)

        if color == "red":
            lower = np.array([0,160,160], dtype="uint8")
            upper = np.array([10,180,180], dtype="uint8")
        elif color == "green":
            lower = np.array([45,100,50], dtype="uint8")
            upper = np.array([75,255,255], dtype="uint8")
        else:
            print "Please enter a valid buoy color"
        
        #thresholding to check if color in image
        mask = cv2.inRange(hsv_img, lower, upper)
        output = cv2.bitwise_and(hsv_image, hsv_image, mask=mask)

        
        #cv2.imshow("{0} detected".format(color), output)
        return True


    #detects 
    def detectGateLeft(self):
        ret, frame = self.vidStream.read()
       
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
            return "true"

        else:
            return "false"


    def detectGateRight(self):
        ret, frame = self.vidStream.read()
       
        frame = cv2.imread(args["image"])
        height, width, chan = frame.shape
        right = frame[0:height, (width/2)+1:width]
        hsv_img = cv2.cvtColor(right, cv2.COLOR_BGR2HSV)

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
            return "true"

        else:
            return "false"


    def detectColor(self, color):
        
        return
    
    def detectLine(self,color):
        return

    def detectChannel(self):
        return
