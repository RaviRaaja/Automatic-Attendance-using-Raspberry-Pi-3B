import cv2
import numpy as np
import pickle
import sqlite3
from PIL import Image
import os

rec = cv2.createLBPHFaceRecognizer();
rec.load('recog/trainningdata.yml')
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cascadePath = 'recog/trainningdata.yml'
path = 'dataset'

def getProfile(id):
	conn = sqlite3.connect("database1")
	cmd = "SELECT * FROM People WHERE ID="+str(id)
	cursor = conn.execute(cmd)
	profile = None
	for row in cursor:
		profile = row
	conn.close()
	return profile

cam = cv2.VideoCapture(1)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
 
while True:
    ret,im=cam.read()
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5);
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
	id,conf = rec.predict(gray[y:y+h,x:x+w])
	profile = getProfile(id)
	if(profile!=None):	
		cv2.cv.PutText(cv2.cv.fromarray(img),profile[1],(x,y+h+30),font,255)
		cv2.cv.PutText(cv2.cv.fromarray(img),profile[2],(x,y+h+70),font,255)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cam.release()
cv2.destroyAllWindows()
