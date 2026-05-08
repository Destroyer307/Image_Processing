import cv2
import mediapipe as mp
import time
import numpy as np


cap = cv2.VideoCapture(0)

ptime = 0
ctime = 0

ret , frame = cap.read()

if not ret:
    print("Hata")

frame = cv2.flip(frame , 1)

mpface = mp.solutions.face_detection

face = mpface.FaceDetection()

imRGB = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

result = face.process(imRGB)

detection = result.detections[0]

bbox = detection.location_data.relative_bounding_box

h , w , c = frame.shape

x = int(bbox.xmin*w)
y = int(bbox.ymin*h)
w = int(bbox.width*w)
h = int(bbox.height*h)

track_window = (x,y,w,h)

roi = frame[y:y+h,x:x+w]

roi_hsv = cv2.cvtColor(roi , cv2.COLOR_BGR2HSV)

roi_hist = cv2.calcHist([roi_hsv] , [0] , None , [180] , [0,180])

cv2.normalize(roi_hist , roi_hist , 0 , 255 , cv2.NORM_MINMAX)

while True:
    ret , frame = cap.read()
    if ret:
        frame = cv2.flip(frame , 1)
        hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv] , [0] , roi_hist , [0,180] , 1)
        criteries = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT , 5 , 1)

        ret , track_window = cv2.meanShift(dst , track_window , criteries)
        x,y,w,h = track_window

        cv2.rectangle(frame , (x,y) , (x+w,y+h) , (255,0,255) , 5)

        ptime = time.time()
        fps = 1 / (ptime-ctime)
        ctime = ptime
        cv2.putText(frame , f"FPS : {np.round(fps)}" , (20,50) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.8 , (0,255,0) , 2)
        cv2.imshow("a" , frame)


        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()