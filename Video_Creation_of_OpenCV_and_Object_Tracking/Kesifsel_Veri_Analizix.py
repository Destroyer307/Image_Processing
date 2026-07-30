import cv2
import matplotlib.pyplot as plt
import os 
from os.path import join , isfile

pathIn = "img1"
pathOut = "Videoxxx.mp4"

files = [f for f in os.listdir("img1") if isfile(join(pathIn , f))]

fps = 25
size = (1920,1080)

out = cv2.VideoWriter(pathOut , cv2.VideoWriter_fourcc(*"MP4V") , fps , size)

for i in files:
    file_name = join(pathIn,i)
    print(file_name)

    img = cv2.imread(file_name)

    out.write(img)

out.release()

