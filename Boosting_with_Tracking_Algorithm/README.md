# KCF Object Tracking with OpenCV

This project demonstrates real-time object tracking in a video using the KCF (Kernelized Correlation Filter) tracking algorithm from OpenCV.

The user manually selects an object in the first frame, and the tracker follows that object throughout the video while also displaying the FPS value in real time.

## Features

- Real-time object tracking
- Manual ROI (Region of Interest) selection
- FPS calculation and visualization
- Bounding box drawing
- Tracking failure detection
- Video processing with OpenCV

## Technologies Used

- Python
- OpenCV
- NumPy

## Installation

Install the required libraries:

```bash
pip install opencv-contrib-python numpy
```

## How It Works

1. The video is loaded using OpenCV.
2. The first frame is displayed.
3. The user selects an object manually using `selectROI()`.
4. The KCF tracker is initialized with the selected bounding box.
5. The tracker predicts the object's new position frame-by-frame.
6. Bounding boxes and FPS information are displayed on the video.

## Example Concepts Used

- `cv2.VideoCapture()`
- `cv2.selectROI()`
- `TrackerKCF_create()`
- `tracker.update()`
- `cv2.rectangle()`
- `cv2.putText()`
- FPS calculation using `time`

## Notes

- Press `q` to quit the application.
- If no object is selected, the program exits safely.
- KCF tracking is fast and lightweight, but it may fail if the object disappears for a long time.

## Project Goal

The purpose of this project is to better understand:

- Object tracking logic
- Bounding box systems (`x, y, w, h`)
- Real-time video processing
- OpenCV tracking workflows
- FPS calculation in computer vision systems

## Future Improvements

- YOLO object detection integration
- Automatic re-detection
- Multi-object tracking
- Webcam support
- Video output saving

## Author

Yiğit İbat Balta
