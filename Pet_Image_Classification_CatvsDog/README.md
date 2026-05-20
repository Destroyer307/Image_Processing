# Cat vs Dog Image Classification with CNN

This project is a basic Convolutional Neural Network (CNN) model that classifies images as either **Cat** or **Dog**.

The model was built with Keras and trained on images stored in two separate folders: `Cat` and `Dog`.

---

# Project Purpose

The main purpose of this project is to practice image classification using deep learning.

The project includes:

- Loading image data from folders
- Resizing images
- Converting images into NumPy arrays
- Normalizing pixel values
- Splitting data into training and test sets
- Applying basic data augmentation
- Building and training a CNN model
- Saving the trained model

---

# Dataset Structure

The dataset folder should be named:

```text
PetImages/
│
├── Cat/
│   ├── image1.jpg
│   ├── image2.jpg
│
└── Dog/
    ├── image1.jpg
    ├── image2.jpg
```

---

# Technologies Used

- Python
- NumPy
- Keras
- TensorFlow
- PIL
- Scikit-learn

---

# Model Architecture

The CNN model contains:

- Convolutional layers
- MaxPooling layers
- Flatten layer
- Dense layer
- Dropout layer
- Sigmoid output layer

Since this is a binary classification problem, the final layer uses `sigmoid` activation and the model is compiled with `binary_crossentropy`.

---

# Data Augmentation

Basic data augmentation was used to improve model generalization.

```python
ImageDataGenerator(
    rotation_range=20,
    horizontal_flip=True
)
```

This allows the model to see slightly modified versions of the training images during training.

---

# Training Result

The model reached approximately:

```text
Training Accuracy : 84%
Validation Accuracy : 81%
Validation Loss : 0.4290
```

These results show that the model learned the general difference between cats and dogs, although there is still room for improvement.

---

# Early Stopping

Early stopping was used to prevent unnecessary training when validation loss stopped improving.

```python
EarlyStopping(
    monitor="val_loss",
    patience=2,
    restore_best_weights=True
)
```

---

# Saved Model

After training, the model is saved as:

```text
Pet_Classification_CATvsDOG.keras
```

---

# How to Run

Install the required libraries:

```bash
pip install numpy pillow scikit-learn tensorflow
```

Run the Python file:

```bash
python main.py
```

---

# Notes

This project is a beginner-level CNN image classification project created for learning the basic deep learning workflow with image data.

Possible future improvements:

- Using larger image sizes
- Adding more data augmentation
- Using transfer learning
- Testing architectures such as MobileNetV2 or ResNet50
- Improving the CNN architecture
