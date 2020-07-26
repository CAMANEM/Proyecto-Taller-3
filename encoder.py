import face_recognition
import pickle
import json
import cv2
import numpy as np
import os

class Encode:

    def __init__(self, accion=None, parametros=None):
        pass

    def Saver(self, faceEncodings):
        try:
            os.remove('files/datos de caras.dat')
        except FileNotFoundError:
            pass
        with open('files/datos de caras.dat', 'wb') as f:
            pickle.dump(faceEncodings, f)
        print("guardado")

    def Loader(self):
        try:
            with open('files/datos de caras.dat', 'rb') as f:
	            faceEncodings = pickle.load(f)
            #faceEncodings = np.array(encodings)
        except FileNotFoundError:
            faceEncodings = [[],[]]
        print("cargado")
            

        return faceEncodings

    def Encoder(self, imgCaras = [], nombres = []):
        try:
            faceEncodings = self.Loader()
        except FileNotFoundError:
            print("cargando lista vacía")
            faceEncodings = [[],[]]

        listaCaras = faceEncodings[0]
        listaNombres = faceEncodings[1]
        
        if len(imgCaras) == len(nombres):
            for i in range(len(nombres)):

                for nombre in listaNombres:
                    if nombre == nombres[i]:
                        return "existe un usuario con estos mismos datos"
                print("antes de añadir datos")
                faceEncodings[0] += [np.array(face_recognition.face_encodings(imgCaras[i])[0])]
                faceEncodings[1] += [nombres[i]]

        else:
            print("inconsistencias en datos enviados a Encoder()")
            return

        print("codificado")

        self.Saver(faceEncodings)

        return "registro completo"
        

encode = Encode()