import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
 
while(True): 
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("frame", frame) 
    cv2.imshow("gray", gray) 
    # cv2.waitKey(20)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
