# Hand Tracking Fruit Ninja Mini Demo

This project is a simple mini game built with Python using OpenCV and MediaPipe.

The main idea is:
your index finger controls the game like a blade.

A moving fruit (circle) appears on the screen and moves upward.
When your finger touches the fruit, it gets “cut” and your score increases.

I made this project to better understand:

* MediaPipe hand tracking
* Landmark logic
* Collision detection
* Coordinate systems in OpenCV
* Real-time camera processing
* Basic game mechanics with computer vision

Instead of only detecting hands, I wanted to turn it into something more visual and interactive.

---

## Technologies Used

* Python
* OpenCV
* MediaPipe
* Math
* Random
* Time

---

## How It Works

### 1. Webcam Detection

The webcam opens and captures live video using OpenCV.

---

### 2. Hand Tracking

MediaPipe detects the hand and tracks 21 hand landmarks.

In this project, I use:

```python
landmark[8]
```

which represents the tip of the index finger.

This point acts like the “blade”.

---

### 3. Fruit Movement

A circle is created as the fruit.

It continuously moves upward using:

```python
target_y -= fruit_speed
```

When it leaves the screen, it respawns from the bottom.

---

### 4. Collision Detection

The distance between:

* finger tip
* fruit center

is calculated using Euclidean distance.

If the finger enters the fruit radius:

```python
if distance < target_radius:
```

the score increases.

---

### 5. Score + FPS

The project also displays:

* live FPS
* current score

on the screen.

This helps both performance tracking and game feedback.

---

## What I Learned

This project helped me understand that:

Hand tracking alone is not the final goal.

The real value comes from turning detection into interaction.

Even a simple circle collision can become the base of bigger projects like:

* Fruit Ninja style games
* Virtual mouse control
* Gesture-based systems
* Smart computer vision products

This project was a good step for that.

---


## Run Project

Install required libraries:

```bash
pip install opencv-python mediapipe
```

Then run:

```bash
python main.py
```



to close the game.

---

## Project Goal

The goal was not just writing code.

It was understanding how computer vision can become a real interactive product.

This is a small project, but it builds the mindset for much bigger systems later.
