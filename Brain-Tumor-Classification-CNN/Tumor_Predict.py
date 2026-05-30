from keras.models import load_model
import numpy as np
import os
from PIL import Image


model = load_model("Tumor_Predict_MY_MODEL.keras")

path = "Testing"

classes = ["glioma", "meningioma", "notumor", "pituitary"]

img_parh = "Testing/pituitary/Te-pi_1.jpg"

img = Image.open(img_parh).convert("RGB")

img = img.resize((64,64))
img_array = np.array(img)

img = img_array / 255

img = np.expand_dims(img , axis = 0)


prediction = model.predict(img)[0]

class_id = np.argmax(prediction)

print("Predict :" , classes[class_id])
print("Oran :" , prediction[class_id])
