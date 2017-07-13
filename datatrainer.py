import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.createLBPHFaceRecognizer();
path = 'dataset'

def getImageswithID(path):
    imagePaths =[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagepath in imagePaths:
        faceimg = Image.open(imagepath).convert('L'); 
        faceNp = np.array(faceimg,'uint8')
        ID = int(os.path.split(imagepath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow("Training",faceNp)
        cv2.waitKey(10)
    return IDs, faces

Ids,faces = getImageswithID(path)
recognizer.train(faces,np.array(Ids))
recognizer.save('recog/trainningdata.yml')
cv2.destroyAllWindows()
