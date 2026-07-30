from keras.models import Sequential
from keras.layers import Dropout , Flatten , Dense , Conv2D , MaxPooling2D
import os
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping
from keras.src.legacy.preprocessing.image import ImageDataGenerator


path = "Training"

classes = ["glioma" , "meningioma" , "notumor" , "pituitary"]

x = []
y = []

for label , class_name in enumerate(classes):
    class_path = os.path.join(path , class_name)
    for tumor_img in os.listdir(class_path):
        img = os.path.join(class_path , tumor_img)

        img = Image.open(img).convert("RGB")
        img = img.resize((64 , 64))
        img_array = np.array(img)
        
        x.append(img_array)
        y.append(label)



x = np.array(x)
y = np.array(y)

x = x / 255


x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.25 , random_state = 42)

early = EarlyStopping(monitor = "val_loss" , patience = 3 , restore_best_weights = True)


model = Sequential()

model.add(Conv2D(128 , kernel_size = (3,3) , activation = "relu" , input_shape = (64 , 64 , 3)))
model.add(MaxPooling2D(pool_size =(2,2)))

model.add(Conv2D(64 , kernel_size = (3,3) , activation = "relu"))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Flatten())

model.add(Dense(128 , activation = "relu"))
model.add(Dropout(0.2))

model.add(Dense(4 , activation = "softmax"))


model.compile(optimizer = "adam" , loss = "sparse_categorical_crossentropy" , metrics = ["accuracy"])

model.fit(x_train , y_train , batch_size = 40 , epochs = 15 , validation_data=(x_test,y_test) , callbacks=[early])

model.save("Tumor_Predict_MY_MODEL.keras")