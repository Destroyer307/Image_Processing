import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpface = mp.solutions.face_detection
face = mpface.FaceDetection(0.2)
# ne kadar küçük seçersen o kadar iyi tespit eder
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

mpDraw = mp.solutions.drawing_utils
writer = cv2.VideoWriter("face_detection.mp4" , cv2.VideoWriter_fourcc(*"mp4v") , 20 , (width , height))

while True:
    ret , frame = cap.read()
    if ret is None:
        break
    frame = cv2.flip(frame , 1)
    imRGB = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    result = face.process(imRGB)
    if result.detections:
        for id , detection in enumerate(result.detections):
            bboxc = detection.location_data.relative_bounding_box

            h , w , _ = frame.shape
            bbox = int(bboxc.xmin*w) , int(bboxc.ymin*h) , int(bboxc.width*w) , int(bboxc.height*h)
            # x , y , width , height
            cv2.rectangle(frame , bbox , (0,0,255) , 3)



    cv2.imshow("video" , frame)
    cv2.waitKey(8)