# Autonomous Robot with Computer Vision

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

1. Clone this repository:
   ```bash
   git clone https://github.com/sofiasawczenko/robot_using_computervision.git
  ```

- Configurações para a montagem da carcaça:
![image](https://user-images.githubusercontent.com/102625995/213512193-e9fb21fe-8b2e-4cc8-a5c1-bce0abad373d.png)
