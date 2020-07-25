import face_recognition
import pickle
import cv2
import numpy as np
import os

class Encode:

    def __init__(self, accion=None, parametros=None):
        pass

    def Saver(self, faceEncodings):
        try:
            os.remove('files/faces_data.dat')
        except FileNotFoundError:
            pass
        with open('files/faces_data.dat', 'wb') as f:
            pickle.dump(faceEncodings, f)
        print("guardado")

    def Loader(self):
        try:
            with open('files/faces_data.dat', 'rb') as f:
	            encodings = pickle.load(f)
            faceEncodings = np.array(encodings)
        except FileNotFoundError:
            faceEncodings = [[],[]]
        print("cargado")
            
        
        return faceEncodings

    def Encoder(self, imgCaras = [], nombres = []):
        try:
            faceEncodings = self.Loader()
        except FileNotFoundError:
            faceEncodings = [[],[]]
        
        if len(imgCaras) == len(nombres):
            for i in range(len(nombres)):

                faceEncodings += [face_recognition.face_encodings(imgCaras[i])[0], [nombres[i]]]

                #faceEncodings[0] = faceEncodings[0] + [face_recognition.face_encodings(imgCaras[i])[0]]
                #faceEncodings[1] = faceEncodings[1] + [nombres[i]]

        else:
            print("inconsistencias en datos enviados a Encoder()")
            return

        print("codificado")

        self.Saver(faceEncodings)

        return faceEncodings
        

encode = Encode()

hijueputa = Encode()
#hijueputa.Encoder([cv2.imread("./files/faceRecognitionFiles/luis.jpg"), cv2.imread("./files/faceRecognitionFiles/david.jpg")], ["Luis", "David"])