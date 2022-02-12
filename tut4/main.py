import cv2 
 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture("http://192.168.91.186:8080/video")
# cap = cv2.VideoCapture(0)


rect_color = (255, 0, 0)
rect_stroke = 2

while(True): 
    ret, frame = cap.read() 
    frame = cv2.resize(frame, (1280, 720), interpolation =cv2.INTER_AREA)  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        print(x, y, w, h) 
         
        roi_gray = frame[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        img_item = "my-image1.png"
        cv2.imwrite(img_item, roi_color)
        
        end_cord_x = x+w
        end_cord_y = y+h   
        
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), rect_color, rect_stroke)
        
    cv2.imshow("frame", frame)  
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
cap.release() 
cap.destroyAllWindows()
    
