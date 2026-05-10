# UA-DETRAC Vehicle Tracking Visualization

This project visualizes vehicle tracking annotations from the UA-DETRAC dataset using OpenCV and XML parsing.

The system reads annotation data frame-by-frame, extracts vehicle IDs and bounding box coordinates, and visualizes tracked vehicles directly on the video frames.

## Features

- XML annotation parsing
- Multi-object vehicle tracking visualization
- Bounding box drawing with OpenCV
- Vehicle ID display
- Frame-by-frame playback
- FPS display support
- UA-DETRAC dataset integration

## Technologies Used

- Python
- OpenCV
- XML ElementTree

## Dataset

Dataset used in this project:

- UA-DETRAC Dataset

## Project Structure

```bash
DETRAC-Images/
DETRAC-Train-Annotations-XML/
tracking.py
README.md
pip install opencv-python
