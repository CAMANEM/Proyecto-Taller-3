import cv2
import face_recognition
import time
from Encodings import Encoders

recognized = False
processFrame = True

faces_encodings = Encoders.Encoder()


class Registro:
    def __init__(self):
        self.Recognition()
        self.saved = False
        self.faceOnScreen = False
        self.user = ""
    
    def Recognition(self):
        global recognized, processFrame
        face_cascade = cv2.CascadeClassifier('files/haarcascade_frontalface_default.xml')

        cap = cv2.VideoCapture(0)

        while not recognized:
            #start=time.time()
            ret, self.img = cap.read()
            gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            try:
                unknown_encoding = face_recognition.face_encodings(self.img)[0]
                for face_encoding in faces_encodings:
                    if face_recognition.compare_faces([face_encoding[0]], unknown_encoding)[0]:
                        self.user = face_encoding[1]
                        print ("face recognized for user: ", self.user)
                        
                        #recognized = True
            except:
                pass
            
            #print("face on screen ",self.faceOnScreen)

            for (x,y,w,h) in faces:
                cv2.rectangle(self.img,(x,y),(x+w,y+h),(0,255,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = self.img[y:y+h, x:x+w]

            cv2.imshow('Reconociendo...', self.img)


            #print("loop time", time.time() - start)
            if cv2.waitKey(20) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()

        return [recognized, self.user]

    def Capture(self):
        cv2.imwrite("./files/faceRecognitionFiles/dont try this at home/"+user+".jpg", self.img)
    def ReturnImg(self):
        return self.img
