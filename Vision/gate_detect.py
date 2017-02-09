import cv2
import sys
import time



#sets path to gate image cascade
cascPath = sys.argv[1]

#initializes farame capture from CAM_0
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Create the haar cascade
	gateCascade = cv2.CascadeClassifier(cascPath)

    # Detect faces in the image
	gates = faceCascade.detectMultiScale(
	    gray,
	    scaleFactor=1.1,
	    minNeighbors=5,
	    minSize=(30, 30),
	    flags = cv2.CASCADE_SCALE_IMAGE
	      )
	# 
	print "Found {0} gates!".format(len(gates))

	# Draw a rectangle around the gate
	for (x, y, w, h) in faces:
	    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)


    # Display the resulting frame
    cv2.imshow('Frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



