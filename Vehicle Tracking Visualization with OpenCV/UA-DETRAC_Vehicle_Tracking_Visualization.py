import cv2
import os
import numpy as np
import time
import xml.etree.ElementTree as ET

img_folder = "DETRAC-Images/DETRAC-Images/MVI_20011"
xml_path = "DETRAC-Train-Annotations-XML/DETRAC-Train-Annotations-XML/MVI_20011.xml"

ptime = 0
ctime = 0

tree = ET.parse(xml_path)
root = tree.getroot()

for frame in root.findall("frame"):
    frame_num = frame.attrib["num"]
    img_name = f"img{int(frame_num):05d}.jpg"
    img_path = os.path.join(img_folder,img_name)

    img = cv2.imread(img_path)

    if img is None:
        print("Hata!")
        continue

    target_list = frame.find("target_list")

    for target in target_list.findall("target"):
        target_id = target.attrib["id"]

        box = target.find("box")

        x = int(float(box.attrib["left"]))
        y = int(float(box.attrib["top"]))
        w = int(float(box.attrib["width"]))
        h = int(float(box.attrib["height"]))

        cv2.rectangle(img , (x,y) , (x+w,y+h) , (255,0,0) , 2)
        cv2.putText(img , f"ID : {target_id}" , (x,y-10) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.9 , (0,0,255) , 2)
    
    ptime = time.time()
    fps = 1 / (ptime-ctime)
    ctime = ptime
    cv2.putText(img , f"FPS : {np.round(fps)}" , (20,50) , cv2.FONT_HERSHEY_DUPLEX , 0.9 , (0,255,0) , 2)

    cv2.imshow("video" , img)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()