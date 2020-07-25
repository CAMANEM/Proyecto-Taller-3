import cv2
import face_recognition
import time
import threading
import tkinter
from PIL import Image, ImageTk
from encoder import encode

class Camara:
    def __init__(self):
        
        self.saved = False
        self.user = ""
        self.recognized = False
        self.hiloIniciado = False
        self.breaked = False
        self.faceEncodings = encode.Loader()
        
    def InicioSesion(self):

        cap = cv2.VideoCapture(0)

        #threading.Thread(target=self.Pantalla()).start()
        
        tiempoEjecutando = 0
        print("iniciado el reconocimiento")

        while tiempoEjecutando < 15:
            start=time.time()
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            cv2.imshow('Reconociendo...', img)
            
            try:
                noIdentificado = face_recognition.face_encodings(img)[0]
                for faceEncoding in self.faceEncodings:
                    if self.recognized:  break
                    if face_recognition.compare_faces([faceEncoding[0]], noIdentificado)[0]:
                        self.user = faceEncoding[1]
                        print ("Bienvenido: ", self.user)

                        tiempoEjecutando = 10.0
                        
                        self.recognized = True
            except:
                pass
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            tiempoEjecutando += round(time.time()-start, 2)

        if not self.recognized:
            print("usuario no reconocido, intente de nuevo")

        return [self.recognized, self.user]
            
        cap.release()
        cv2.destroyAllWindows()
            
    def Capture(self):
        cv2.imwrite("./files/faceRecognitionFiles/dont try this at home/"+user+".jpg", self.img)

    def ReturnImg(self):
        return self.img

    def MostrarCara(self,tiempo):
        if tiempo >= 15 or self.recognized:
            return
        #elif not self.hiloIniciado:
        #    return self.MostrarCara(tiempo)
        try:
            self.canvas.create_image(0,0, image=self.tkinterImage, anchor=NW)
        except:
            print("esta picha no sirve, bote esto")
        time.sleep(0.1)
        self.canvas.update()
        print("hijueputa puta")
        return self.MostrarCara(tiempo+0.1)

    def RegistrarCara(self, user):
        self.user = user
        cap = cv2.VideoCapture(0)
        tiempo = 0

        cascade = cv2.CascadeClassifier('./files/haarcascade_frontalface_default.xml')


        while tiempo < 60:
            start=time.time()
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            faces = cascade.detectMultiScale(gray, 1.3, 5)

            lenFaces = len(faces)

            if cv2.waitKey(1) == 13 and lenFaces and not self.saved:
                #threading.Thread(target=encode.Encoder([img],[self.user]))
                self.saved = True
                tiempo = 58

            if lenFaces == 0:
                cv2.putText(img, "No se detectan caras", (100,30), cv2.FONT_ITALIC, 1, (0, 80, 200, 255), 2) 
            
            else:
                cv2.putText(img, "Cara detectada, enter para registrar", (10,30), cv2.FONT_ITALIC, 1, (0, 80, 200, 255), 2) 

            if self.saved:
                cv2.putText(img, "Registro satisfactorio", (120,450), cv2.FONT_ITALIC, 1, (0, 80, 200, 255), 2) 

            print("hay ", lenFaces, " caras en pantalla")
            cv2.imshow('Buscando rostro para registrar', img)

            tiempo += time.time() - start

            if cv2.waitKey(1) == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
        
camara = Camara()