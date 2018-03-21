import cv2
import numpy as np
import sqlite3

faceDetect= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam= cv2.VideoCapture(0)

def insertorupdate(Id,name,age,gender):
    conn=sqlite3.connect('FaceBase.db')
    cmd="SELECT * FROM Person WHERE ID = "+str(Id)
    cursor=conn.execute(cmd)
    isrecordexist=0
    for row in cursor:
        isrecordexist=1
    if(isrecordexist==1):
        cmd="UPDATE Person SET Name="+str(name)+", Age="+str(age)+", Gender="+str(gender)+" WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO Person(ID, Name, Age, Gender) VALUES("+str(Id)+","+str(name)+","+str(age)+","+str(gender)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()
    
id= raw_input('Enter user id')
name= raw_input('Enter your name')
age=raw_input('Enter age')
gender=raw_input('Enter gender(M/F)')

insertorupdate(id,name,age,gender)
sampleNum=0

while(True):
    ret, img= cam.read()
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        sampleNum= sampleNum+1
        cv2.imwrite('dataset/user.'+str(id)+'.'+str(sampleNum)+'.jpg', gray[y:y+h, x:x+h])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(500)
    cv2.imshow('face',img)
    cv2.waitKey(1)
    if(sampleNum>20):
        break
cam.release()
cv2.destroyAllWindows()
    
