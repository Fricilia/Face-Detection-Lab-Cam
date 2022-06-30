#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

videoCam = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while True :
    cond, frame = videoCam.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    muka = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in muka:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 5)
        
        roi_warna = frame[y:y+h, x:x+w]
        roi_gray = gray[y:y+h, x:x+w]
        mata = eye_cascade.detectMultiScale(roi_gray)
        for (mx, my, mw, mh) in mata:
            cv2.rectangle(roi_warna,(mx,my),(mx+mw,my+mh),(255,255,0), 2)
            
    cv2.imshow('Face and Eye detection', frame)
    
    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        break
        
videoCam.release()
cv2.destroyAllWindows()

