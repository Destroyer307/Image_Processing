# Dinosaur CNN Classification Project

This project is my first convolutional neural network (CNN) experiment using Keras and TensorFlow.  
The aim of the project is to classify two dinosaur categories:

- Indominus Rex
- T-Rex

The model was trained with custom image datasets and basic deep learning techniques.

---

## Technologies Used

- Python
- Keras
- TensorFlow
- NumPy
- PIL (Pillow)
- Scikit-learn

---

## Dataset Structure

```bash
Dinosaur_CNN/
│
├── dataset/
│   ├── indominus/
│   └── t_rex/
```

Each folder contains images belonging to its own class.

---

## Project Workflow

1. Read images from dataset folders  
2. Resize images to `128x128`  
3. Convert images into NumPy arrays  
4. Normalize pixel values  
5. Split dataset into training and test sets  
6. Build CNN model  
7. Train the model  
8. Evaluate accuracy with validation data  

---

## CNN Architecture

- Conv2D Layer
- MaxPooling2D Layer
- Flatten Layer
- Dense Layer
- Dropout Layer
- Sigmoid Output Layer

The model uses:

- `ReLU` activation for hidden layers
- `Sigmoid` activation for binary classification
- `Binary Crossentropy` loss function
- `Adam` optimizer


## Notes

This project was created while learning CNN fundamentals and image classification.  
The main purpose is to understand:

- Image preprocessing
- CNN logic
- Training process
- Binary classification
- Deep learning workflow

Future improvements may include:

- More dataset images
- Data augmentation
- Additional convolution layers
- Better accuracy optimization

---

## Author

Yiğit İbat Balta  
2nd Year Artificial Intelligence and Machine Learning Student
