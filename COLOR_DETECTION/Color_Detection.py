import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
ptime = 0
ctime = 0


blueklower = (85,50,30)
bluekupper = (145,255,255)

while True:
    ret , frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame , 1)

    blurred = cv2.GaussianBlur(frame , ksize=(9,9) , sigmaX=0)
    hsv = cv2.cvtColor(blurred , cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv , lowerb=blueklower , upperb=bluekupper)
    mask = cv2.erode(mask , None , iterations=2)
    mask = cv2.dilate(mask , None , iterations=2)

    contour , hierarchy = cv2.findContours(mask , cv2.RETR_CCOMP , cv2.CHAIN_APPROX_SIMPLE)

    if len(contour) > 0:
        c = max(contour , key=cv2.contourArea)

        if cv2.contourArea(c) > 400:
            rect = cv2.minAreaRect(c)
            ((x,y) , (width,height) , iteration) = rect
            box = cv2.boxPoints(rect)
            box = np.int64(box)

            cv2.drawContours(frame , [box] , 0 , (255,0,0) , 4)
            cv2.putText(frame ,f"x : {int(x)} , y: {int(y)}" , (20,50) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.8 , (0,0,255) , 2)
            cv2.putText(frame , f"width : {int(width)} , height: {int(height)}" , (20,80) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.8 , (0,0,255) , 2)
            cv2.putText(frame , f"iteration : {int(iteration)}" , (20,100) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.8 , (0,0,255) , 2)
    ptime = time.time()
    fps = 1 / (ptime - ctime)
    ctime = ptime
    cv2.putText(frame , "FPS :"+str(int(fps)) , (20,120) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.9 , (0,0,255))
    cv2.imshow("a",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
        

