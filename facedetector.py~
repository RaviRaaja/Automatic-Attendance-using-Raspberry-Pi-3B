import cv2
import numpy as np

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
rec = cv2.createLBPHFaceRecognizer();
rec.load('recog/trainningdata.yml')
id = 0
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,4,1,0,2)

while True:
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5);
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
	id,conf = rec.predict(gray[y:y+h,x:x+w])
	if(id==1):
		id = "Ravi"
	elif(id==2):
		id = "Kamalkant"
        elif(id==3):
		id = "Jaipoorna"
	elif(id==4):
		id = "Jenny Rajan"
	elif(id==5):
		id = "Parth"
	elif(id==6):
		id = "peanut"
	elif(id==7):
		id = "vivek"
		
	cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255)
	
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cam.release()
cv2.destroyAllWindows()
