import numpy as np
import cv2
id =input('enter user id = '); 
inp=input('Y: To change PIN \n N: To keep the existing PIN\n:');

if inp == 'Y':
    f=open('Pin.txt',"w");
    inp=input('Enter PIN:');
    f.write(inp);
    f.close();
fce_cascade = cv2.CascadeClassifier('Webcam-Face-Detect-master\haarcascade_frontalface_default.xml');
cap = cv2.VideoCapture(0)

sam_no=0
while 1:
    ret, img = cap.read()
    #print (ret)
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = fce_cascade.detectMultiScale(grey, 1.3, 5)
    
    for (x,y,w,h) in faces:
        
        sam_no=sam_no+1
        cv2.imwrite('Faces Data/User'+str(id)+ '.' +str(sam_no)+ '.jpg', grey[y:y+h, x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(1)
    cv2.imshow('img',img)
    cv2.waitKey(10)
    if sam_no == 10:
        break
        
cap.release();
cv2.destroyAllWindows();