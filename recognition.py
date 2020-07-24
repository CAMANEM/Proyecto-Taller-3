import cv2
import face_recognition
import time
import threading
import tkinter
from encoder import Encode

class Login:
    def __init__(self):
        
        self.saved = False
        self.faceOnScreen = False
        self.logueado = False
        self.user = ""
        self.recognized = False
        self.hiloIniciado = False
        self.breaked = False
        self.faceEncodings = Encode("Loader")
        self.hiloReconocimiento = threading.Thread(target=self.Recognition())
        self.hiloReconocimiento.daemon = True
        self.hiloReconocimiento.start()

        if self.hiloIniciado: self.Pantalla()
    
    def Recognition(self):

        cap = cv2.VideoCapture(0)

        while self.logueado:
            #start=time.time()
            ret, self.img = cap.read()
            self.hiloIniciado = True
            gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

            try:
                unknown_encoding = face_recognition.face_encodings(self.img)[0]
                for face_encoding in self.faceEncodings:
                    if face_recognition.compare_faces([face_encoding[0]], unknown_encoding)[0]:
                        self.user = face_encoding[1]
                        print ("Bienvenido: ", self.user)
                        
                        self.recognized = True
            except:
                pass
            return

    def Capture(self):
        cv2.imwrite("./files/faceRecognitionFiles/dont try this at home/"+user+".jpg", self.img)

    def ReturnImg(self):
        return self.img

    def MostrarCara(self,tiempo):
        if tiempo >= 15 or self.recognized:
            return
        self.canvas.create_image(0,0, image=self.img)
        time.sleep(0.1)
        self.MostrarCara(tiempo+0.1)

    def Pantalla(self):
        tkinter.Tk().wm_withdraw()
        vent = tkinter.Toplevel()
        vent.geometry("640x550+350+200")
        vent.rezisable(False,False)
        self.canvas = tkinter.Canvas(vent, width=640, height=550, bg="white")
        threading.Thread(target=self.MostrarCara, args=[0])

        self.canvas.update()
        vent.mainloop()

Login()