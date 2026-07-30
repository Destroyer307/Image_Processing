# Garbage Classification with PyTorch

This project is an image classification application developed to classify garbage images into 12 different categories.

The model was built and trained using PyTorch with a custom Convolutional Neural Network architecture. The project follows a modular structure where data preparation, model creation, training, evaluation, model saving, and prediction processes are separated into different Python files.

## Project Objective

The main objective of this project is to develop a deep learning model that can automatically classify garbage images into different waste categories.

The project was also created to practice:

- Image classification with PyTorch
- Convolutional Neural Networks
- Custom training and testing loops
- Modular deep learning project structure
- Model saving and loading
- Prediction on new images

## Project Structure

```text
Garbage_Classification/
│
├── data/
│   └── garbage_classification_split/
│       ├── train/
│       └── val/
│
├── models/
│   └── Gargabe_Classification_12.pth
│
├── main.py
├── model_create.py
├── setup_data.py
├── Training_Testing_Engine.py
├── utils.py
├── load_model_make_prediction.py
├── requirements.txt
└── README.md
```

## File Descriptions

### `main.py`

This is the main execution file of the project.

It performs the following operations:

- Defines image transformations
- Creates the training and validation DataLoaders
- Initializes the CNN model
- Defines the loss function
- Creates the optimizer
- Trains and evaluates the model
- Saves the trained model weights

### `model_create.py`

This file contains the custom CNN architecture used for garbage classification.

The model mainly uses the following layers:

- `Conv2d`
- `ReLU`
- `MaxPool2d`
- `Flatten`
- `Linear`

The convolutional layers extract visual features from the input images, while the classifier converts these features into class scores.

### `setup_data.py`

This file is responsible for preparing the dataset.

It performs the following operations:

- Reads the training and validation directories
- Applies image transformations
- Creates datasets using `ImageFolder`
- Creates PyTorch DataLoaders
- Returns the class names

### `Training_Testing_Engine.py`

This file contains the training and evaluation functions.

During each epoch, the following metrics are calculated:

- Training loss
- Training accuracy
- Validation loss
- Validation accuracy

The model parameters are updated using backpropagation during the training stage.

### `utils.py`

This file contains utility functions used throughout the project.

It is mainly responsible for saving the trained model weights inside the `models` directory.

### `load_model_make_prediction.py`

This file loads the saved model and makes a prediction on a new image.

The prediction workflow is:

1. Create the model architecture
2. Load the saved model weights
3. Read the input image
4. Apply the required transformations
5. Add a batch dimension
6. Pass the image through the model
7. Select the predicted class using `argmax`
8. Display the predicted class

## Technologies Used

- Python
- PyTorch
- Torchvision
- NumPy
- Matplotlib
- Pillow

## Installation

Clone the repository:

```bash
git clone https://github.com/Destroyer307/Computer_Vision.git
```

Navigate to the project directory:

```bash
cd Computer_Vision/Garbage_Classification
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Training the Model

Run the following command to train the model:

```bash
python main.py
```

After the training process is completed, the model weights are saved inside the `models` directory.

## Making a Prediction

To make a prediction using the saved model, run:

```bash
python load_model_make_prediction.py
```

The path of the image that will be classified should be specified inside the prediction file.

## Training Configuration

```text
Loss Function: CrossEntropyLoss
Optimizer: Adam
Learning Rate: 0.0005
Batch Size: 32
Number of Classes: 12
Number of Epochs: 20
```

## Model Performance

The final training results were approximately:

```text
Training Accuracy: 84.7%
Validation Accuracy: 80.4%
```

The exact results may vary depending on the dataset split, random seed, image transformations, and training environment.

## Model Workflow

```text
Input Images
      ↓
Image Transformations
      ↓
PyTorch DataLoader
      ↓
Convolutional Neural Network
      ↓
Class Logits
      ↓
CrossEntropyLoss
      ↓
Backpropagation
      ↓
Optimizer Step
      ↓
Updated Model Parameters
      ↓
Saved PyTorch Model
```

## Prediction Logic

The model outputs raw logits for each class.

`CrossEntropyLoss` is used directly with these logits, so applying Softmax before calculating the loss is not required.

For prediction, the class with the highest logit value is selected using:

```python
predicted_class = torch.argmax(logits, dim=1)
```

## Possible Improvements

The project can be improved by adding:

- Data augmentation
- Transfer learning
- Learning rate scheduling
- Early stopping
- Confusion matrix visualization
- Precision, recall, and F1-score metrics
- Class imbalance analysis
- Web interface for image prediction
- Real-time camera classification
- ONNX model export
- Docker support

## Notes

This project was developed to practice PyTorch image classification, modular project organization, custom CNN architectures, training loops, model evaluation, model saving, and prediction on new images.

## Author

Developed by [Destroyer307](https://github.com/Destroyer307)
