import os
import cv2
import numpy as np
from PIL import Image
faceDetect= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.createLBPHFaceRecognizer()
path = 'dataset'

def getImagesWithID(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples=[]
    IDs=[]
    for imagePath in imagePaths:
            faceImg= Image.open(imagePath).convert('L');
            faceNp= np.array(faceImg,'uint8')
            ID=int(os.path.split(imagePath)[-1].split('.')[1])
            faces=faceDetect.detectMultiScale(faceNp)
            for (x,y,w,h) in faces: 
               faceSamples.append(faceNp[y:y+h,x:x+w])
               print ID
               IDs.append(ID)
            cv2.imshow('training',faceNp)
            cv2.waitKey(100)
    return IDs,faceSamples
IDs, faceSamples= getImagesWithID(path)
recognizer.train(faceSamples,np.array(IDs))
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()
    

