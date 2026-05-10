import cv2
import matplotlib.pyplot as plt
import os
from os.path import join , isfile
import pandas as pd
import seaborn as sns
import numpy as np
import time

list = ["frame_number","identify_number","left","top","width","height","score","class","visibility"]

ptime = 0
ctime = 0
data = pd.read_csv("gt.txt",names=list)


car = data[data["class"] == 3]

pathOut = "Videoxxx.mp4"

cap = cv2.VideoCapture(pathOut)

id = 29
number_of_image = np.max(data["frame_number"])

for i in range(number_of_image):
    ret , frame = cap.read()

    if ret:
        filter_id = np.logical_and(car["frame_number"] == i+1 , car["identify_number"] == id)

        x = int(car[filter_id]["left"].iloc[0])
        y = int(car[filter_id]["top"].iloc[0])
        w = int(car[filter_id]["width"].iloc[0])
        h = int(car[filter_id]["height"].iloc[0])

        cv2.rectangle(frame , (x,y) , (x+w,y+h) , (255,0,255) , 2)

        ptime = time.time()
        fps = 1 / (ptime-ctime)
        ctime = ptime

        cv2.putText(frame , f"FPS : {np.round(fps)}" , (20,50) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 1.2 , (0,255,0) , 2)


        cv2.imshow("frame" , frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()



















