import cv2
import numpy as np
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import math
import time

factory = PiGPIOFactory()
H = 13
servo = Servo(H, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
angle = 0
servo.value = math.sin(math.radians(angle))

previous_error = 0
I_error = 0
KP = 0.05
KI = 0.01
KD = 0.002

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

x_medium = int(480/2)
center = int(480/2)

while True:
    _, frame = cap.read()
    frame = cv2.rotate(frame, cv2.ROTATE_180)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_red = np.array([169, 50, 50])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        x_medium = int((x+(x+w))/2)
        break
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.line(frame, (x_medium, 0), (x_medium, 320), (0, 255, 0), 2)
    cv2.imshow("Frame", frame)
    if abs(center - x_medium) > 50:
        error = center - x_medium
        I_error += error
        D_error = error - previous_error
        previour_error = error
        angle = (KP*error + KI*I_error + KD*D_error) 
        if angle > 90:
            angle = 90
        if angle < -90:
            angle = -90
        servo.value = math.sin(math.radians(angle))
    key = cv2.waitKey(1)
    if key == 27:
        break

angle = 0
servo.value = math.sin(math.radians(angle))
cap.release()
cv2.destroyAllWindows()