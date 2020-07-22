import cv2
guardado = False

user = "lucho el del cartucho bb"

class Registro:
    def __init__(self):
        self.Recognition()
        self.saved = False
    
    def Recognition(self):
        global guardado
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        cap = cv2.VideoCapture(0)

        while not guardado:
            ret, self.img = cap.read()
            gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x,y,w,h) in faces:
                cv2.rectangle(self.img,(x,y),(x+w,y+h),(0,255,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = self.img[y:y+h, x:x+w]

            cv2.imshow('Reconociendo...', self.img)
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