import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt
import time
cap = cv2.VideoCapture(0)

mshand = mp.solutions.hands

hands = mshand.Hands(max_num_hands = 2)

mpDraw = mp.solutions.drawing_utils
ctime = 0
ptime = 0
while True:
    ret , frame = cap.read()
    imRGB = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    results = hands.process(imRGB)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame , handlms , mshand.HAND_CONNECTIONS)
            for id , lm in enumerate(handlms.landmark):
                h,w,c = frame.shape

                cx , cy = int(lm.x*w) , int(lm.y*h)
          

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(frame , "FPS :"+str(int(fps)), (10,60) , cv2.FONT_HERSHEY_DUPLEX , 3 , (0,255,0) , 4)
    cv2.imshow("img",frame)
    cv2.waitKey(1)  

