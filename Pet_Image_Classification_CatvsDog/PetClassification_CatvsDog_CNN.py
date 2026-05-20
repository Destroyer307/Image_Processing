import os
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D , Flatten , Dropout , Dense
from PIL import Image
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping
from keras.src.legacy.preprocessing.image import ImageDataGenerator


datasets = "PetImages"

classes = ["Cat" , "Dog"]

X = []
y = []

for label , class_name in enumerate(classes):
    class_path = os.path.join(datasets , class_name)
    for images in os.listdir(class_path):
        imgs_path = os.path.join(class_path , images)

        try:
            img = Image.open(imgs_path).convert("RGB")
            img = img.resize((64,64))
            img_array = np.array(img)

            X.append(img_array)
            y.append(label)

        except:
            print("Hata :" , images)

X = np.array(X)
y = np.array(y)

X = X / 255

X_train , X_test , y_train , y_test = train_test_split(X , y , test_size = 0.25 , random_state = 42)


datagen = ImageDataGenerator(rotation_range = 20 , horizontal_flip = True)

early_stop = EarlyStopping(monitor = "val_loss" , patience = 2 , restore_best_weights = True)

model = Sequential()

model.add(Conv2D(128 , kernel_size=(3,3) , activation = "relu" , input_shape = (64,64,3)))
model.add(Conv2D(64 , kernel_size=(3,3) , activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32 , kernel_size = (3,3) , activation = "relu"))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Flatten())

model.add(Dense(128 , activation="relu"))
model.add(Dropout(0.3))

model.add(Dense(1 , activation="sigmoid"))

model.compile(optimizer = "adam" , loss = "binary_crossentropy" , metrics = ["accuracy"])

model.fit(datagen.flow(X_train , y_train , batch_size = 40) , epochs = 15 , callbacks = [early_stop] , validation_data = (X_test , y_test))

model.save("Pet_Classification_CATvsDOG.keras")
# Epoch 12/15
# 469/469 ━━━━━━━━━━━━━━━━━━━━ 102s 218ms/step - accuracy: 0.8405 - loss: 0.3606 - val_accuracy: 0.8149 - val_loss: 0.4290