# Brain Tumor Classification with CNN

## Project Overview

This project uses a Convolutional Neural Network (CNN) built with Keras and TensorFlow to classify brain MRI images into four categories:

* Glioma Tumor
* Meningioma Tumor
* Pituitary Tumor
* No Tumor

The model is trained on MRI scans and can automatically predict the tumor type from a given image.

---

## Dataset

Dataset Structure:

```text
Training/
├── glioma/
├── meningioma/
├── notumor/
└── pituitary/

Testing/
├── glioma/
├── meningioma/
├── notumor/
└── pituitary/
```

Each image is:

* Converted to RGB format
* Resized to 64x64 pixels
* Normalized to the range [0,1]

---

## Model Architecture

```text
Input Layer (64x64x3)

Conv2D (128 filters, 3x3, ReLU)
MaxPooling2D (2x2)

Conv2D (64 filters, 3x3, ReLU)
MaxPooling2D (2x2)

Flatten

Dense (128, ReLU)
Dropout (0.2)

Dense (4, Softmax)
```

Loss Function:

```python
sparse_categorical_crossentropy
```

Optimizer:

```python
Adam
```

Metric:

```python
Accuracy
```

---

## Training

The model uses:

```python
EarlyStopping(
    monitor="val_loss",
    patience=3,
    restore_best_weights=True
)
```

Training Parameters:

```python
Epochs: 15
Batch Size: 40
Validation Split: 25%
```

---

## Test Results

```text
Correct Predictions : 1364
Total Predictions   : 1600
Accuracy            : 85.25%
```

Final Test Accuracy:

```text
85.25%
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Brain-Tumor-Classification-CNN.git
cd Brain-Tumor-Classification-CNN
```

Install required libraries:

```bash
pip install tensorflow keras numpy pillow scikit-learn
```

---

## Usage

### Train Model

```bash
python train.py
```

This will generate:

```text
Tumor_Predict_MY_MODEL.keras
```

---

### Evaluate Model

```bash
python test.py
```

Example Output:

```text
Doğru Tahmin : 1364
Toplam Tahmin : 1600
Accuracy : 0.8525
```

---

## Classes

| Label | Class      |
| ----- | ---------- |
| 0     | Glioma     |
| 1     | Meningioma |
| 2     | No Tumor   |
| 3     | Pituitary  |

---

## Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Pillow
* Scikit-Learn

---

## Future Improvements

* Data Augmentation
* Transfer Learning (MobileNetV2, EfficientNet)
* Larger Input Resolution
* Real-Time MRI Prediction Interface
* Gradio Web Application Deployment

---

## Author

Yiğit İbat Balta

Artificial Intelligence & Machine Learning Student

GitHub: Destroyer307
