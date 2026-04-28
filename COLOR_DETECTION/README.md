# Blue Object Detection with OpenCV

This project detects blue objects in real-time using a webcam. It uses OpenCV to process camera frames, create a blue color mask, detect contours, and draw a rotated bounding box around the detected object.

## Features

* Real-time webcam detection
* Blue color detection using HSV
* Gaussian Blur for noise reduction
* Erosion and dilation for mask cleaning
* Contour detection
* Rotated bounding box drawing
* Object position and size display
* Rotation angle display
* FPS counter

## Technologies Used

* Python
* OpenCV
* NumPy
* Time module

## Installation

Install required libraries:

```bash
pip install opencv-python numpy
```

## Run the Project

```bash
python main.py
```

Press `q` to close the program.

## How It Works

### 1. Capture Webcam Frames

The webcam continuously reads video frames.

```python
cap = cv2.VideoCapture(0)
```

### 2. Flip the Frame

The frame is flipped horizontally to create a mirror effect.

```python
frame = cv2.flip(frame, 1)
```

### 3. Blur the Image

Gaussian Blur reduces noise and improves color detection.

```python
blurred = cv2.GaussianBlur(frame, (9,9), 0)
```

### 4. Convert BGR to HSV

HSV color space makes color detection easier than BGR.

```python
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
```

### 5. Define Blue Color Range

The program detects blue colors inside this HSV range.

```python
blueklower = (85,50,30)
bluekupper = (145,255,255)
```

### 6. Create the Mask

Only blue areas remain white, everything else becomes black.

```python
mask = cv2.inRange(hsv, blueklower, bluekupper)
```

### 7. Remove Noise

Erosion removes small unwanted pixels, dilation restores the main object.

```python
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)
```

### 8. Find Contours

Contours represent the borders of detected objects.

```python
contour, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
```

### 9. Select the Largest Object

The largest contour is assumed to be the target object.

```python
c = max(contour, key=cv2.contourArea)
```

### 10. Draw Rotated Bounding Box

A rotated rectangle is created around the object.

```python
rect = cv2.minAreaRect(c)
box = cv2.boxPoints(rect)
box = np.int64(box)
```

### 11. Show Object Information

The program displays:

* X and Y center position
* Width and height
* Rotation angle
* FPS

## Controls

| Key | Action       |
| --- | ------------ |
| q   | Quit program |

## Notes

If blue detection is weak, adjust the HSV values:

```python
blueklower = (85,50,30)
bluekupper = (145,255,255)
```

Lighting conditions affect detection quality, so better lighting improves results.

## Example Use Cases

* Learning OpenCV basics
* Color-based object tracking
* Contour detection practice
* Real-time computer vision projects
