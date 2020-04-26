# face detection using OpenCV
import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("C:\Users\Admin\Downloads\Akka_wedding\venkat2k19.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face = face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)
print(type(face))
print(face)
for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    
cv2.destroyAllWindows()