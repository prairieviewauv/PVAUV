import cv2
import rospy
import time
import visualizer



#initializes farame capture from CAM_0
cap0 = visualizer()


while(True):
    # Capture frame-by-frame
	ret, frame = cap0.read()
	cap0.detectGate()
	# print "Found {0} gates!".format(len(gates))

	# # Draw a rectangle around the gate
	# for (x, y, w, h) in faces:
	#     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)


  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




