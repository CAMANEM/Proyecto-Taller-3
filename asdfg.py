import cv2
import face_recognition
import time
guardado = False

user = "luis"

known_image = face_recognition.load_image_file("./files/faceRecognitionFiles/"+user+".jpg")

class Registro:
    def __init__(self):
        self.Recognition()
        self.saved = False
    
    def Recognition(self):
        global guardado
        face_cascade = cv2.CascadeClassifier('files/haarcascade_frontalface_default.xml')

        cap = cv2.VideoCapture(0)

        while not guardado:
            start=time.time()
            ret, self.img = cap.read()
            gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            try:
                known_ecoding = face_recognition.face_encodings(known_image)[0]
                unknown_encoding = face_recognition.face_encodings(self.img)[0]
            except:
                pass

            try:
                results = face_recognition.compare_faces([known_ecoding], unknown_encoding)
            except IndexError:
                pass
            print(results)

            for (x,y,w,h) in faces:
                cv2.rectangle(self.img,(x,y),(x+w,y+h),(0,255,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = self.img[y:y+h, x:x+w]

            cv2.imshow('Reconociendo...', self.img)


            print("loop time", time.time() - start)
            if cv2.waitKey(20) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()

    def Capture(self):
        self.guardado = True
        cv2.imwrite("./files/faceRecognitionFiles/dont try this at home/"+user+".jpg", self.img)
    def ReturnImg(self):
        return self.img

Registro()