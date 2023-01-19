from flask import Flask, render_template, Response
from datetime import datetime
import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

RF = 12 #Right - Forward  - Blue
RB = 32 #Right - Backward - Green 
LF = 33 #Left  - Forward  - Orange
LB = 35 #Left  - Backward - Yellow
GPIO.setup(RF, GPIO.OUT) 
GPIO.setup(RB, GPIO.OUT)
GPIO.setup(LF, GPIO.OUT)
GPIO.setup(LB, GPIO.OUT)
GPIO.output(RF, False)
GPIO.output(RB, False)
GPIO.output(LF, False)
GPIO.output(LB, False)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def gen(cap):
    global photo
    while True:
        _, frame = cap.read()
        frame = cv2.rotate(frame, cv2.ROTATE_180)
        _, jpeg = cv2.imencode('.jpg', frame)
        if photo:
            name = datetime.today().strftime("%Y-%m-%d_%Hh%Mm%Ss.png")
            cv2.imwrite(name, frame)
            photo = False
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n\r\n")

@app.route("/video_feed")
def video_feed():
    global photo
    photo = False
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 10)
    return Response(gen(cap), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/p")
def photo():
    global photo
    photo = True
    return "Success"

@app.route("/f")
def forward():
    GPIO.output(RF, True)
    GPIO.output(LF, True)
    time.sleep(0.5)
    GPIO.output(RF, False)
    GPIO.output(LF, False)
    return "Success"

@app.route("/b")
def backward():
    GPIO.output(RB, True)
    GPIO.output(LB, True)
    time.sleep(0.5)
    GPIO.output(RB, False)
    GPIO.output(LB, False)
    return "Success"

@app.route("/l")
def left():
    GPIO.output(RF, True)
    GPIO.output(LB, True)
    time.sleep(0.15)
    GPIO.output(RF, False)
    GPIO.output(LB, False)
    return "Success"

@app.route("/r")
def right():
    GPIO.output(RB, True)
    GPIO.output(LF, True)
    time.sleep(0.15)
    GPIO.output(RB, False)
    GPIO.output(LF, False)
    return "Success"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, threaded=True)
