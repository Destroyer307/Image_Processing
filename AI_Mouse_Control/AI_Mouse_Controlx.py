import cv2
import numpy as np
import pyautogui as pyt
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

ctime = 0

mphand = mp.solutions.hands
hands = mphand.Hands(max_num_hands = 1)
mpDraw = mp.solutions.drawing_utils

prev_x = 0
prev_y = 0

last_click_time = 0
screen_w , screen_h = pyt.size()

while True:
    ret , frame = cap.read()
    frame = cv2.flip(frame , 1)
    h,w,c = frame.shape
    if not ret:
        break
    imRGB = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    result = hands.process(imRGB)

    if result.multi_hand_landmarks:
        for handlm in result.multi_hand_landmarks:
            
            index_finger = handlm.landmark[8]
            thumb = handlm.landmark[4]

            index_x = int(index_finger.x*w)
            index_y = int(index_finger.y*h)

            thumb_x = int(thumb.x*w)
            thumb_y = int(thumb.y*h)

            screen_x = np.interp(index_x , [0,w] , [0,screen_w])
            screen_y = np.interp(index_y , [0,h] , [0,screen_h])

            curr_x = prev_x + (screen_x-prev_x)/3
            curr_y = prev_y + (screen_y-prev_y)/3

            pyt.moveTo(curr_x,curr_y)
            prev_x = curr_x
            prev_y = curr_y

            distance = np.hypot(index_x-thumb_x,index_y-thumb_y)

            cv2.circle(frame , (index_x,index_y) , 10 , (255,0,255) , 5)
            cv2.circle(frame , (thumb_x,thumb_y) , 10 , (0,0,255) , 5)
            cv2.line(frame , (index_x,index_y) , (thumb_x,thumb_y) , (255,255,255) , 5)

            current_time = time.time()
            
            if distance < 30 and current_time - last_click_time > 0.7:
                pyt.click()
                last_click_time = current_time
                cv2.putText(frame , "Click" , (50,100) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 2 , (0,0,0) , 3)
            mpDraw.draw_landmarks(frame , handlm , mphand.HAND_CONNECTIONS)
    
    ptime = time.time()
    fps = 1 / (ptime-ctime)
    ctime = ptime
    cv2.putText(frame , f"FPS : {np.round(fps)}" , (20,50) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 2 , (0,255,0) , 5)
    
    cv2.imshow("AI MOUSE CONTROL" , frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


            
