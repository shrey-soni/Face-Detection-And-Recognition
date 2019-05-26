import os
import numpy as np
import cv2
from PIL import Image 
recog = cv2.face.LBPHFaceRecognizer_create();
path="Faces Data";
def getImage(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)];
    faces = [];
    ids = [];
    for image_path in image_paths:
        face_img = Image.open(image_path).convert('L');
        face_np = np.array(face_img, 'uint8');
        id= int(os.path.split(image_path)[-1].split(".")[1]);
        faces.append(face_np);
        ids.append(id);
        cv2.imshow("Adding faces for traning",face_np);
        cv2.waitKey(10);
    return np.array(ids), faces;
ids,faces  = getImage(path);
recog.train(faces,ids);
recog.save("Train Data/trainingdataf.yml");
cv2.destroyAllWindows();