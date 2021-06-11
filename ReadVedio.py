'''
Read the video feeding through camera.
'''

# opencv library required
import numpy
import cv2

# command to capture the vedio through webcam
capture=cv2.VideoCapture(0)

# a loop for the process if camera detected or exit the code for false
while True:
    ret, frame = capture.read()
    
    # when camera not detected
    if ret==False:
        continue

    # the name of the window in which frame will be showing
    cv2.imshow("Detector", frame)

    exit = cv2.waitKey(1) & 0xFF

    if exit == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()