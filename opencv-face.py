import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 960)
cap.set(4, 540)
cap.set(cv2.CAP_PROP_FPS, 30)
df = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    _, frame = cap.read()
    iPB = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    
    faces = df.detectMultiScale(iPB, scaleFactor = 1.05, \
        minNeighbors = 7, minSize = (24,24), flags = cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    cv2.imshow(str(len(faces))+" face(s) encontrada(s).", frame)
    key = cv2.waitKey(1)
    
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
