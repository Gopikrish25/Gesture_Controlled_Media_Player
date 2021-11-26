import cv2
import math

face_cascade = cv2.CascadeClassifier('face_cascade.xml')
def detect_face(frame, block=False, colour=(0, 0, 0)):
    fill = [1, -1][block]
    

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    area = 0
    X = Y = W = H = 0
    for (x, y, w, h) in faces:
        if w * h > area:
            area = w * h
            X, Y, W, H = x, y, w, h
    cv2.rectangle(frame, (X, Y), (X + W, Y + H), colour, fill)
