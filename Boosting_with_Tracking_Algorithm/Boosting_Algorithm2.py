import cv2
import time
import numpy as np

cap = cv2.VideoCapture("video_name")

ret , frame = cap.read()

if not ret:
    print("hata")
    exit()

ptime = 0
ctime = 0

tracker = cv2.legacy.TrackerKCF_create()

bbox = cv2.selectROI("Nesne Sec" , frame , False)

cv2.destroyWindow("Nesne Sec")

if bbox == (0,0,0,0):
    print("Nesne secilmedi")
    exit()

tracker.init(frame , bbox)

while True:
    ret , frame = cap.read()

    if not ret:
        break

    success , bbox = tracker.update(frame)

    if success:
        x , y , w , h = map(int , bbox)

        
        cv2.rectangle(frame , (x,y) , (x+w,y+h) , (255,0,0) , 2)

        cv2.putText(frame , "KCF TRACKING" , (x,y-10) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.7 ,(255,0,255) , 1)
        
    else:
        cv2.putText(frame , "TRACKING FAILED" , (20,80) , cv2.FONT_HERSHEY_COMPLEX , 0.7 , (0,0,255) , 2)
    ptime = time.time()
    fps = 1 / (ptime - ctime)

    ctime = ptime
    cv2.putText(frame , f"FPS : {np.round(fps)}" , (20,50) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.9 , (0,255,0) , 2)

    cv2.imshow("KCF Tracking" , frame)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

