import numpy as np
import cv2
import sys
face_cascade = cv2.CascadeClassifier('Webcam-Face-Detect-master\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create();
rec.read("Train Data/trainingdataf.yml")
id=0
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255, 255, 255)
t=0
f=0
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if id==2:
            id="Valid"
            t=t+1
        elif id==1:
            id="Valid"
            t=t+1
        elif id==3:
            id="Valid"
            t=t+1
        elif id==4:
            id="Valid"
            t=t+1
        elif id==5:
            id="Valid"
            t=t+1
        else:
            id="Invalid, press q"
            f=f+1
        cv2.putText(img,str(id),(x,y+h),fontface,fontscale,fontcolor)
        fa=f*100/(f+t)
        ta=t*100/(f+t)
        print("False Percentage:"+str(fa))
        print("Truth Percentage:"+str(ta))
        print("")
        if ta >= 80.00000000:
            print ("Car Unlocked")
            sys.exit()
            break
            
    cv2.imshow('img',img)
    if cv2.waitKey(1) == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        inp=input('Enter PIN:')
        f=open('Pin.txt',"r")
        contents=f.read();
        if contents==inp:
            print ("Car Unlocked")
            break
        else:
            print("Invalid PIN")
            print ("Burglar Alert")
            break
cap.release()
cv2.destroyAllWindows()