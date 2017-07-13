import cv2
import numpy as np
import sqlite3

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

def InsertOrUpdate(id,name):
	conn = sqlite3.connect("database1") 
	query = "SELECT * FROM People WHERE ID="+str(id)
	cursor=conn.execute(query)
	isRecordExist=0
	for row in cursor:
		isRecordExist=1
	if(isRecordExist==1):
		query="UPDATE People SET Name="+str(name)+" WHERE ID="+str(id)
	else:
		query="INSERT INTO People(ID,Name) VALUES("+str(id)+","+str(name)+")"
	conn.execute(query)
	conn.commit()
	conn.close()

id = raw_input("Enter the user id? ")
name = raw_input("Enter your Name: ")

InsertOrUpdate(id,name)

numberr = 0



while True:
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        numberr =numberr+1
        cv2.imwrite("dataset/User."+str(id)+"."+str(numberr)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(100)
    cv2.imshow('img',img)
    cv2.waitKey(1)
    if numberr>20:
        break
    
cam.release()
cv2.destroyAllWindows()




