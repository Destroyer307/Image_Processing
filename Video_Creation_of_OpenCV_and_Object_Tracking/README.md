# MOT Video Creation and Object Tracking with OpenCV

This project demonstrates a basic computer vision workflow using Python and OpenCV.  
The project has two main parts:

1. Creating a video from image frames
2. Reading ground-truth annotation data and drawing a bounding box on a selected object ID

The project is based on a MOT-style dataset structure, where image frames are stored in a folder and object annotations are stored in a text file.

---

## Project Overview

In the first part, image frames inside the `img1` folder are combined into a video file named `Videoxxx.mp4`.

In the second part, the generated video is opened with OpenCV. The annotation file `gt.txt` is read using Pandas, and a specific object is selected by its class and identity number. Then, a bounding box is drawn around the selected object frame by frame.

This project helped me understand how image sequences, video writing, annotation files, filtering operations, and basic object tracking visualization work together in computer vision.

---

## Technologies Used

- Python
- OpenCV
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Dataset Structure

The project expects the following structure:

```text
project-folder/
│
├── img1/
│   ├── 000001.jpg
│   ├── 000002.jpg
│   ├── 000003.jpg
│   └── ...
│
├── gt.txt
├── create_video.py
├── object_tracking.py
└── README.md
