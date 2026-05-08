# Real-Time Face Detection and Tracking with MediaPipe and MeanShift

This project is a real-time face detection and tracking application developed using Python, OpenCV, and MediaPipe.

The main purpose of this project is to better understand the difference between **object detection** and **object tracking** in computer vision systems.

In this application, the face is first detected using MediaPipe Face Detection. After the detection step, the detected face region is tracked using the MeanShift tracking algorithm based on HSV histogram backprojection.

This project was developed as a practice project while learning computer vision and real-time image processing concepts.

---

# Features

- Real-time webcam processing
- Face detection using MediaPipe
- Face tracking using MeanShift
- HSV histogram-based tracking
- FPS calculation and display
- OpenCV visualization tools
- Simple and lightweight pipeline

---

# Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy

---

# How the Project Works

The webcam is opened and the first frame is captured.

MediaPipe Face Detection is used to detect the face in the frame. After detecting the face, the bounding box coordinates are calculated using relative bounding box values.

The detected face area becomes the ROI (Region of Interest).

The ROI is converted from BGR color space to HSV color space. Then, a histogram is created using the Hue channel and normalized.

During the main loop:

- Each frame is converted to HSV
- Histogram backprojection is applied
- MeanShift updates the tracking window
- A rectangle is drawn around the tracked face
- FPS value is displayed on the screen



# Project Pipeline

```text
Webcam Input
     |
     v
Face Detection (MediaPipe)
     |
     v
Bounding Box Extraction
     |
     v
ROI Selection
     |
     v
HSV Conversion
     |
     v
Histogram Calculation
     |
     v
Back Projection
     |
     v
MeanShift Tracking
     |
     v
Visualization + FPS
```



# Installation

Install the required libraries:

```bash
pip install opencv-python mediapipe numpy
```

---

# Usage

Run the project:

```bash
python main.py
```

Press `q` to close the application.

---

# Project Structure

```text
project-folder/
│
├── main.py
├── README.md
└── requirements.txt
```

---

# requirements.txt

```text
opencv-python
mediapipe
numpy
```



# What I Learned

While developing this project, I practiced and learned:

- Real-time video processing with OpenCV
- Face detection using MediaPipe
- Difference between detection and tracking
- HSV color space usage
- Histogram creation and normalization
- Histogram backprojection
- MeanShift tracking algorithm
- FPS calculation in real-time systems



# Notes

This project uses MediaPipe only for the initial face detection step.

After the face is detected, the MeanShift algorithm handles the tracking process. This reduces the need for continuous face detection in every frame and makes the system more lightweight.

Compared to traditional Haar Cascade methods, MediaPipe generally provides:

- Better detection stability
- Better angle handling
- More robust detection under different lighting conditions

However, MeanShift tracking can still fail in situations such as:

- Very fast movement
- Sudden lighting changes
- Similar colored objects entering the frame



# Possible Improvements

Some future improvements for this project:

- Switching from MeanShift to CamShift
- Automatic face re-detection if tracking is lost
- Adding tracking smoothing
- Using YOLO-based face detection
- Multi-face tracking support
- Better low-light performance



# Conclusion

This project helped me better understand how modern face detection systems can work together with classical tracking algorithms in computer vision applications.

It was also a good practice project for learning real-time image processing, tracking logic, and OpenCV fundamentals.
