# Autonomous Robot with Computer Vision

![image](https://github.com/user-attachments/assets/360726dc-57e5-4f55-a249-713dce8f9764)

This repository contains the source code and necessary resources for building an autonomous robot using Python, C, Raspberry Pi, and Arduino. The robot features a navigation system based on computer vision.

## Overview

The goal of this project is to develop an autonomous robot capable of navigating independently in an environment using computer vision techniques to detect obstacles and make navigation decisions. The robot integrates hardware and software, with the Raspberry Pi handling image processing and decision-making, while the Arduino controls the motors and sensors.

## Key Features

- **Computer Vision**: Equipped with a camera, the robot captures images of its surroundings. The computer vision algorithm processes these images to identify obstacles, free paths, and other navigation-critical information.
- **Motor Control**: The Arduino is responsible for motor control, allowing the robot to move forward, backward, turn, and perform other maneuvers to avoid obstacles and follow predefined paths.
- **Obstacle Detection**: Using advanced computer vision techniques, the robot identifies obstacles and adjusts its movement to avoid collisions.
- **Autonomous Navigation**: The navigation system on the Raspberry Pi uses input from computer vision and sensors to make real-time decisions, enabling the robot to move autonomously.

## Hardware Requirements

- **Raspberry Pi**: For image processing and navigation logic.
- **Arduino**: To control motors and read sensor data.
- **Camera**: For capturing real-time images for computer vision.
- **Motors and Wheels**: For movement.
- **Sensors**: Optional for additional obstacle detection.

## Software Technologies

- **Programming Languages**: Python, C
- **Libraries**: OpenCV, Flask, NumPy, GPIO libraries (e.g., RPi.GPIO, gpiozero)
- **Frameworks**: Flask for web-based robot control

## Getting Started

### 1. Clone this repository:

```bash
   git clone https://github.com/sofiasawczenko/robot_using_computervision.git
```
###  2. Set up your Raspberry Pi and Arduino:

- Flash the appropriate Arduino code for motor and sensor control.
- Install the required Python libraries on the Raspberry Pi using pip:

```bash
pip install opencv-python flask numpy
```
### 3. Assemble the robot hardware, connecting the Raspberry Pi and Arduino as specified in the configuration.

### 4. Run the Flask server on the Raspberry Pi to control the robot:

```bash
python app.py
```

### 5. Code Snippets
1. Motor Control with Raspberry Pi


```bash
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
RF = 12  # Right Forward
RB = 32  # Right Backward
LF = 33  # Left Forward
LB = 35  # Left Backward

GPIO.setup(RF, GPIO.OUT)
GPIO.setup(RB, GPIO.OUT)
GPIO.setup(LF, GPIO.OUT)
GPIO.setup(LB, GPIO.OUT)

# Example movement: forward for 2 seconds
GPIO.output(RF, True)
GPIO.output(LF, True)
time.sleep(2)
GPIO.output(RF, False)
GPIO.output(LF, False)
GPIO.cleanup()
```

2. Computer Vision for Obstacle Detection

```bash
import cv2

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect obstacles using a classifier
    obstacles = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    detected = obstacles.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in detected:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Obstacle Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
```

### How to Contribute
Contributions are welcome! Follow these steps to contribute:

- Fork this repository.
- Clone the forked repository:
```bash
git clone https://github.com/YOUR_USERNAME/robot_using_computervision.git
Create a new branch:
```bash
git checkout -b feature-name
```
- Make your changes and commit:
```bash
git add .
git commit -m "Description of changes"
```
- Push your changes and open a pull request:
```bash
git push origin feature-name
```

- Car configuration:
![image](https://user-images.githubusercontent.com/102625995/213512193-e9fb21fe-8b2e-4cc8-a5c1-bce0abad373d.png)

## Acknowledgments
This project was inspired by the potential of integrating computer vision with robotics to create efficient autonomous systems.
