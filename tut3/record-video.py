from black import out
import numpy as np
import cv2
import os 

filename = 'video.mp4' 
frames_per_sec = 25
v_res = '720p' # 1080p

def change_res(cap, width, height):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Standard Video Dimensions Sizes
STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

def get_dims(cap, res='720p'):
    width, height = STD_DIMENSIONS["480p"]
    
    if res in STD_DIMENSIONS:
       width, height = STD_DIMENSIONS[res] 
    change_res(cap, width, height)
    return width, height

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}



def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']



cap = cv2.VideoCapture("http://192.168.91.186:8080/video")
 
dims = get_dims(cap, res=v_res) 
video_type_cv2 = get_video_type(filename)

out = cv2.VideoWriter(filename, video_type_cv2, frames_per_sec, dims)

while(True): 
    ret, frame = cap.read()
    frame = cv2.resize(frame, dims, interpolation =cv2.INTER_AREA)  
    
    out.write(frame)
    
    cv2.imshow("frame", frame)  
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
cap.release()
out.release()
cap.destroyAllWindows()
    
