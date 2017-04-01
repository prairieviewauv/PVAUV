import cv2
import imutils
import numpy as np
import sys
import time


class visualizer:
    def __init__(self, frameRate=24, whRes=640, hRes = 480, camera=0):

        #start video capture stream; return assertion if stream not started
        self.vidStream = cv2.VideoCapture(camera)

        '''
        #intialize camera capture resolution and frame rate
        vidStream.set(CV_CAP_PROP_FRAME_WIDTH, wRes)
        vidStream.set(CV_CAP_PROP_FRAME_HEIGHT, hRes)
        vidStream.set(CV_CAP_PROP_FPS, frameRate)
        '''
        
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

  


    #detects the left side of the validation gate/channel by checking for orange on the left side of the captured frame
    def detectGateLeft(self, color):
        ret, frame = self.vidStream.read()
        height, width, chan = frame.shape
        left = frame[0:height, 0:width/2]
        hsv_img = cv2.cvtColor(left, cv2.COLOR_BGR2HSV)

        if color == "orange":
            lower = np.array([0, 160, 160], dtype="uint8")
            upper = np.array([10, 180, 180], dtype="uint8")
        elif color == "yellow":
            lower = np.array([45, 100, 50], dtype="uint8")
            upper = np.array([75, 255, 255], dtype="uint8")

        #thresholding to ease contourig process
        mask = cv2.inRange(hsv_img, lower, upper)
        output = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)
        thresh = cv2.threshold(mask, 5, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh,None, iterations=2)
                        
        #finds contours (shape) of orange in image; if no contours found, gate not found
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        if len(cnts) > 2:
            for c in cnts:
                cv2.drawContours(left, [c], -1, (0, 255, 0), 2)
            return True

        else:
            return False

    #detects the right side of the validation gate/channel by checking for color on the left side of the captured frame
    def detectGateRight(self, color):
        ret, frame = self.vidStream.read()
        height, width, chan = frame.shape
        right = frame[0:height, (width/2)+1:width]
        hsv_img = cv2.cvtColor(right, cv2.COLOR_BGR2HSV)

        #orange color range
        lower = np.array([5, 50, 50], dtype="uint8")
        upper = np.array([15, 255, 255], dtype="uint8")

        #thresholding to ease contouring process
        mask = cv2.inRange(hsv_img, lower, upper)
        output = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)
        thresh = cv2.threshold(mask, 5, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh,None, iterations=2)
        
        #finds contours (shape) of orange in image; if no contours found, gate not found
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        if len(cnts) > 2:
            for c in cnts:
                cv2.drawContours(right, [c], -1, (0,255,0), 2)
            return True

        else:
            return False

    #detects the bottom of the channel by checking for color on the left side of the captured frame
    def detectGateBottom(self, color):
        ret, frame = self.vidStream.read()
        height, width, chan = frame.shape
        bottom = frame[(height/2)+1:height, 0:width]
        hsv_img = cv2.cvtColor(bottom, cv2.COLOR_BGR2HSV)

        #yellow color range
        lower = np.array([20,100,100], dtype="uint8")
        upper = np.array([30,255,255], dtype="uint8")

        #thresholding to ease contouring process
        mask = cv2.inRange(hsv_img, lower, upper)
        output = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)
        thresh = cv2.threshold(mask, 5, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh,None, iterations=2)
        
        #finds contours (shape) of orange in image; if no contours found, gate not found
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        
        #check if anything detected
        if len(cnts) < 2:
            return -1

        #center (x,y) for target
        cX=0
        cY=0
        for c in cnts:
          M = cv2.moments(c)
          if (M['m00']==0):
              M['m01']=1
              cX = int(M['m10']/M['m01'])
              cY = int(M['m01']/M['m00'])

        #checks if center of bottom gate is in center of frame
        #return 0,1 (move forward or ascend)
        if cY > height/2:
            return 1
        else:
            return 0


    def detectLine(self, color):
        ret, frame = self.vidStream.read()
       
        height, width, chan = frame.shape
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #orange color range
        lower = np.array([5,50,50], dtype="uint8")
        upper = np.array([15,255,255], dtype="uint8")

        #thresholding to ease contouring process
        mask = cv2.inRange(hsv_img, lower, upper)
        output = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)
        thresh = cv2.threshold(mask, 5, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh,None, iterations=2)
        
        #finds contours (shape) of orange in image; if no contours found, gate not found
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        
        if len(cnts) < 2:
            return -1

        #center (x,y) for target
        cX=0
        cY=0
        for c in cnts:
          M = cv2.moments(c)
          if (M['m00']==0):
              M['m01']=1
              cX = int(M['m10']/M['m01'])
              cY = int(M['m01']/M['m00'])

        #checks if center of line is in center of frame
        # if not return 0,1,2 (move forward, curve right, curve left)
        if cX > width/2:
            return 1
        elif cX < width/2:
            return 2
        else:
            return 0
        



'''
    #returns center (x,y) for color target; can be used to set heading for contact with target
    def lockOn(self, color):
        frame = self.getFrame()
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
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]

        #center (x,y) for target
        cX=0
        cY=0
        for c in cnts:
          M = cv2.moments(c)
          if (M['m00']==0):
              M['m01']=1)
              cX = int(M['m10']/M['m01'])
              cY = int(M['m01']/M['m00'])

        return cX, cY


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
        thresh = cv2.threshold(mask, 5, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh,None, iterations=2)
                        
        #finds contours (shape) of orange in image; if no contours found, gate not found
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        if len(cnts) > 2:
            for c in cnts:
                cv2.drawContours(left, [c], -1, (0,255,0), 2)
            return True

        else:
            return False
       ''' 