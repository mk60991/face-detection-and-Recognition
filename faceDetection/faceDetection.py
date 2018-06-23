
import os
import numpy as np
import cv2
def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('C:\\Users\\hp\\Downloads\\Compressed\\OpenCV-Face-Recognition-master\\FaceDetection\\Cascades\\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
assure_path_exists("C:\\Users\\hp\\Downloads\\Compressed\\OpenCV-Face-Recognition-master\\FaceDetection\\Cascades\\dataset/")
while True:
    ret, img = cap.read()
    #to reverse the image
    #img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        

    cv2.imshow('video',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
