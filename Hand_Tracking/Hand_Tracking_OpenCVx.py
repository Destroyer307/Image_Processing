import cv2
import mediapipe as mp
import random
import math
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands = 1)

mpDraw = mp.solutions.drawing_utils

finger_x = 0
finger_y = 0
ptime = 0
ctime = 0
score = 0
fruit_speed = 10
target_x = random.randint(100,500)
target_y = random.randint(100,500)
target_radius = 50

while True:
    ret , frame = cap.read()

    frame = cv2.flip(frame , 1)

    imRGB = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

    results = hands.process(imRGB)
    h , w , c = frame.shape

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame , handlms , mpHands.HAND_CONNECTIONS)

            
            
            lm = handlms.landmark[8]
            finger_x , finger_y = int(lm.x*w) , int(lm.y*h)

            cv2.circle(frame , (finger_x , finger_y) , 12 , (255,0,0) , cv2.FILLED)
    target_y = target_y - fruit_speed
    if target_y < -target_radius:
        target_x = random.randint(target_radius, w - target_radius)
        target_y = h
        
    cv2.circle(frame , (target_x , target_y) , target_radius , (0,0,255) , cv2.FILLED)

    if finger_x is not None and finger_y is not None:
        distance = math.sqrt((finger_x - target_x)**2 + (finger_y - target_y)**2)
        if distance < target_radius:
            score = score + 1
            target_x = random.randint(100 , 500)
            target_y = random.randint(100 , 500)

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(frame ,f"FPS : {int(fps)}", (20,40) , cv2.FONT_HERSHEY_DUPLEX , 2 , (255,0,0) , 2)
    cv2.putText(frame , f"Score : {int(score)}" , (20,100) , cv2.FONT_HERSHEY_DUPLEX , 2 , (255,0,0) , 2)

    cv2.imshow("Recording",frame)

    if cv2.waitKey(1) & 0xFF == ord("a"):
        break

cap.release()
cv2.destroyAllWindows()


