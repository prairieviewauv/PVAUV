import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", help = "path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])




BLAZE_ORANGE = np.array([0,121,255],dtype="uint8")
   

mask = cv2.inRange(image,lower,upper)
output = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("images", np.hstack([image,output]))
    cv2.waitKey(0)
