# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 22:45:31 2020

@author: nhunh
"""

import cv2
import numpy as np
import datetime 
from keras.models import load_model
from pygame import mixer

# load pretrained model
model = load_model("C:/Users/nhunh/.spyder-py3/Drowsiness.h5")

mixer.init()
sound = mixer.Sound("C:/Users/nhunh/.spyder-py3/alarm.wav")

# sound.play()
#print(img)
"""
cv2.imshow("image", img)
cv2.waitKey(1000)
cv2.destroyAllWindows() 

cv2.imwrite("lena_copy.png", img)
"""

""

close_time = 0

# OpenCV's pretrained haar-cascade
face_cascade = cv2.CascadeClassifier("C:/Users/nhunh/.spyder-py3/cascades/haarcascade_frontalface_alt2.xml")
left_eye_cascade = cv2.CascadeClassifier("C:/Users/nhunh/.spyder-py3/cascades/haarcascade_lefteye_2splits.xml")
right_eye_cascade = cv2.CascadeClassifier("C:/Users/nhunh/.spyder-py3/cascades/haarcascade_righteye_2splits.xml")

cap = cv2.VideoCapture(0) # use input from default camera


fourcc = cv2.VideoWriter_fourcc(* "XVID")
out = cv2.VideoWriter(r"C:\Users\nhunh\.spyder-py3\output.mp4", fourcc, 20.0, (640, 480))


while True:
    ret, frame = cap.read()
    
    OpenR = 1
    OpenL = 1
    
    # convert to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # play around with this
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    
    for (x,y,w,h) in faces:
        # print(x, y, w, h)
        # region of interest
        roi_gray = gray[y:y+h, x:x+w]
        roi_frame = frame[y:y+h, x:x+w]
        #cv2.imwrite(r"C:\Users\nhunh\.spyder-py3\Face_img.png", roi_gray)
        
        color = [0, 255, 0]
        cv2.rectangle(frame, (x,y), (x+w,y+h), color, thickness = 2)
        
        
    left_eye = left_eye_cascade.detectMultiScale(gray) # eyes are only in the face
    right_eye = right_eye_cascade.detectMultiScale(gray) # eyes are only in the face
    ecolor = [0, 0, 255]
        
    for (lex, ley, lew, leh) in left_eye:
        cv2.rectangle(frame, (lex, ley), (lex+lew, ley+leh), ecolor, thickness=2)
        
        left_eye = frame[ley:ley+leh, lex:lex+lew]
        left_eye = cv2.cvtColor(left_eye, cv2.COLOR_BGR2GRAY)
        left_eye = cv2.resize(left_eye, (24,24))
        left_eye = left_eye / 255
        left_eye = left_eye.reshape(24, 24, -1)
        left_eye = np.expand_dims(left_eye, axis=0)
        
        left_prediction = model.predict_classes(left_eye)
        
        OpenL = left_prediction[0]
        
        
    for (rex, rey, rew, reh) in right_eye:
        cv2.rectangle(frame, (rex, rey), (rex+rew, rey+reh), ecolor, thickness=2)
        
        right_eye = frame[rey:rey+reh, rex:rex+rew]
        right_eye = cv2.cvtColor(right_eye, cv2.COLOR_BGR2GRAY)
        right_eye = cv2.resize(right_eye, (24,24))
        right_eye = right_eye / 255
        right_eye = right_eye.reshape(24, 24, -1)
        right_eye = np.expand_dims(right_eye, axis=0)
        
        right_prediction = model.predict_classes(right_eye)
        
        OpenR = right_prediction[0]
        
    
    print(OpenL, OpenR)
        
    if OpenR == False and OpenL == False:
        close_time += 1
    else:
        close_time = max(0, close_time-1)
        
    if close_time >= 80:
        frame = cv2.putText(frame, "Dangerous!!!", (100,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), thickness = 5)
        sound.play()
    
    cv2.imshow("frame", frame)
    
    out.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()

###############################################################################################

