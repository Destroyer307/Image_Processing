# Face Detection with OpenCV and MediaPipe

This project performs real-time face detection using the computer's webcam.  
When a face is detected, a red rectangle is drawn around it, and the video is also saved as an `.mp4` file.

The main goal of this project was to understand how camera processing works with OpenCV and how face detection works with MediaPipe.

---

## Libraries Used

### OpenCV (`cv2`)

Used for:

- Opening the webcam
- Displaying the video on screen
- Drawing rectangles around detected faces
- Saving the video output

---

### MediaPipe (`mediapipe`)

Used for:

- Real-time face detection

---

## Installation

First, install the required libraries:

```bash
pip install opencv-python mediapipe
