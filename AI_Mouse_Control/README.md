# AI Mouse Control with Hand Tracking

## Overview

This project implements a basic AI-based mouse control system using real-time hand tracking. The system detects hand landmarks via a webcam and maps finger movements to control the computer cursor. Additionally, a simple gesture (distance between thumb and index finger) is used to simulate mouse clicks.

The main objective of this project is to explore the integration of computer vision techniques with human-computer interaction.

---

## Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy
* PyAutoGUI

---

## How It Works

The system follows these steps:

1. **Video Capture**
   The webcam captures live video frames.

2. **Hand Detection**
   MediaPipe detects hand landmarks in real-time.

3. **Finger Tracking**
   The position of the index finger (landmark 8) is used to control the cursor.

4. **Coordinate Mapping**
   The camera coordinates are mapped to screen coordinates using interpolation.

5. **Cursor Movement**
   The cursor is moved smoothly using a basic interpolation formula to reduce jitter.

6. **Click Detection**
   The distance between the thumb (landmark 4) and index finger is calculated.
   If the distance is below a threshold, a mouse click is triggered.

---

## Features

* Real-time hand tracking
* Smooth cursor movement
* Gesture-based click mechanism
* FPS display for performance monitoring

---

## Installation

Install the required libraries:

pip install opencv-python mediapipe pyautogui numpy

---

## Usage

Run the script:

python main.py

Controls:

* Move your index finger → Moves the cursor
* Bring thumb and index finger closer → Click
* Press Q → Exit the application

---

## Notes

* Good lighting conditions improve detection accuracy.
* The system may behave differently depending on camera quality.
* Click sensitivity can be adjusted by modifying the distance threshold in the code.

---

## Limitations

* Only supports one hand
* Gesture detection is basic and may produce unintended clicks
* Performance depends on hardware and camera FPS

---

## Possible Improvements

* Multi-gesture support (right-click, drag, scroll)
* Adaptive click threshold based on hand size
* GUI interface for calibration
* Integration with machine learning models for gesture classification

---

## Conclusion

This project demonstrates a simple but effective approach to controlling a computer using hand gestures. While it is a prototype, it provides a solid foundation for more advanced human-computer interaction systems.
