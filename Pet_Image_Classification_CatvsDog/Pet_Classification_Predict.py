from keras.models import load_model
from PIL import Image
import numpy as np


model = load_model("Pet_Classification_CATvsDOG.keras")

img_path = "cat.jpg"

img = Image.open(img_path).convert("RGB")

img = img.resize((64,64))

img = np.array(img)

img = img / 255

img = np.expand_dims(img , axis = 0)

predict = model.predict(img)[0][0]

if predict > 0.5:
    print("Dog " , "oran :" , model.predict(img)[0][0])

else:
    print("Cat" , "Oran : " , model.predict(img)[0][0])

