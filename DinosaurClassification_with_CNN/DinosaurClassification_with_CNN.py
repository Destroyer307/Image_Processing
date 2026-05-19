import os
import numpy as np
from keras.layers import Conv2D , MaxPooling2D , Flatten , Dense , Dropout
from keras.models import Sequential
from PIL import Image
from sklearn.model_selection import train_test_split


dataset_path = "Dinosaur_CNN/dataset"

width = 128
height = 128

X = []
y = []

classes = ["indominus" , "t_rex"]

for label , class_name in enumerate(classes):
    class_path = os.path.join(dataset_path , class_name)
    
    for imgs in os.listdir(class_path):
        img_path = os.path.join(class_path , imgs)

        try:
            img = Image.open(img_path).convert("RGB")

            img = img.resize((width,height))

            img_arrray = np.array(img)

            X.append(img_arrray)
            y.append(label)


        except:
            print("Hata" , imgs)

X = np.array(X)
y = np.array(y)

X = X / 255


X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.5,random_state=42)


model = Sequential()

model.add(Conv2D(64 , kernel_size=(3,3) , activation="relu" , input_shape = (128,128,3)))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(128 , activation="relu"))
model.add(Dropout(0.8))

model.add(Dense(1 , activation="sigmoid"))

model.compile(optimizer="adam" , loss="binary_crossentropy" , metrics=["accuracy"])

model.fit(X_train , y_train , epochs = 10 , batch_size = 5,validation_data = (X_test , y_test))

