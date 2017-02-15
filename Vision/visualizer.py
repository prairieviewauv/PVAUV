import cv2
import numpy as np
import sys
import time


class visualizer:
    def __init__(self, name, frameRate=24, whRes=640, hRes = 480, camera=0):
        self.name=name

        #start video capture stream; ret assertion if stream not started
        self.vidStream= cv2.VideoCapture(camera)
        if (!vidStream.isOpened()):
            CV_Assert("I can't see out this eye!")

        #intialize camera capture resolution and frame rate
        vidStream.set(CV_CAP_PROP_FRAME_WIDTH, wRes)
        vidStream.set(CV_CAP_PROP_FRAME_HEIGHT, hRes)
        vidStream.set(CV_CAP_PROP_FPS, frameRate)

        
        
    def __del__(self):
        vidStream.release()
        cv2.destroyAllWindows()

    def getFrameRate():
        return frameRate

    def getRsolution():
        return (wRes, hRes)

    def capFrame():
        ret, frame = videoStream.read()
        cv2.imshow("Capture", frame)

    def detectBuoy(color):
        return 

    def detectGate():
        return

    def detectColor():
        return
    
    def detectLine(color):
        return

    def detectChannel():
        return
