import face_recognition
import pickle
import cv2
import numpy as np

class Encode:

    def __init__(self, accion, parametros=None):
        if accion == "Encoder":
            self.Encoder(parametros[0], parametros[1])
        elif accion == "Loader":
            self.Loader()
        elif accion == "Saver":
            self.Saver(parametros[0])

    def Saver(self, faceEncodings):
        with open('files/faces_data.dat', 'wb') as f:
            pickle.dump(faceEncodings, f)
        print("guardado")

    def Loader(self):
        with open('files/faces_data.dat', 'rb') as f:
	        encodings = pickle.load(f)
        print("cargado")
            
        faceEncodings = np.array(encodings)
        return faceEncodings

    def Encoder(self, imgCaras = [], nombres = []):
        faceEncodings = self.Loader()
        
        if len(imgCaras) == len(nombres):
            for i in range(len(nombres)):

                faceEncodings += [[face_recognition.face_encodings(imgCaras[i])[0], nombres[i]]]

        else:
            print("inconsistencias en datos enviados a Encoder()")
            return

        print("codificado")

        self.Saver(faceEncodings)

        return faceEncodings
    
Encode("Encoder", [[cv2.imread("./files/faceRecognitionFiles/luis.jpg"), cv2.imread("./files/faceRecognitionFiles/david.jpg")], ["Luis", "David"]])