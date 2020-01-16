import cv2
import os
import time
from datetime import datetime	

def faces(imagePath,time) :
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
	faces = faceCascade.detectMultiScale(
	    gray,
	    scaleFactor=1.3,
	    minNeighbors=3,
	    minSize=(30, 30)
	)

	print("[INFO] Found {0} Faces.".format(len(faces)))
	i = 0
	for (x, y, w, h) in faces:
	    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
	    roi_color = image[y:y + h, x:x + w]
	    print("[INFO] Object found. Saving locally.")
	    cv2.imwrite("faces1/" + str(i)  + " "+ str(time) + '.jpg', roi_color)
	    i += 1

video_capture = cv2.VideoCapture(0)
i = 0
def listToString(s):  
    str1 = ""    
    for ele in s:  
        str1 += str(ele)
        str1 += " "
    return str1  
while True:
    _, frame = video_capture.read()
    dtt = datetime.now()
    dtl = [dtt.year, dtt.month, dtt.day, dtt.hour, dtt.minute, dtt.second]
    ans = listToString(dtl)
    path = "Images/" + ans + ".jpg"
    cv2.imwrite(path,frame)
    # cv2.imshow('Video', canvas)
    faces(path,ans)
    i += 1
    time.sleep(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
# cv2.destroyAllWindows()

# status = cv2.imwrite('faces_detected.jpg', image)
# print("[INFO] Image faces_detected.jpg written to filesystem: ", status)