import face_recognition
import pickle
import cv2
import numpy as np
import os

class Encode:

    def __init__(self):
        pass

    def Saver(self, faceEncodings):
        """Guarda los datos de los usuarios en un archivo .dat"""

        try:
            os.remove('files/datos de caras.dat') # borra el archivo en caso de contener algún error
        except FileNotFoundError: # en caso de que no exista el archivo, saltar a la siguiente instrucción
            pass
        with open('files/datos de caras.dat', 'wb') as f: # almacena los datos en disco
            pickle.dump(faceEncodings, f) # guarda usando pickle

    def Loader(self):
        """Carga los datos de los usuarios desde el almacenamiento"""

        try:
            with open('files/datos de caras.dat', 'rb') as f: # los lee
	            faceEncodings = pickle.load(f) # lee usando pickle
            
        except FileNotFoundError: # si el archivo no existe
            faceEncodings = [] # no hay datos, por tanto, se retorna una lista vacía
            
        return faceEncodings

    def Encoder(self, imgCaras = [], nombres = []):
        """Codifica las caras como datos útiles para el reconocimiento, a parit de imágenes. Además, almacena los nombres relacionados con esa cara"""

        faceEncodings = self.Loader() # carga los datos usando Loader()
        
        if len(imgCaras) == len(nombres): # si los datos son precisos, es decir, existe la misma cantidad de imágenes que de nombres

            for i in range(len(nombres)): 

                for nombre in nombres:
                    try:
                        if nombre == faceEncodings[i][1]: # si ya existe un usuario con el mismo nombre
                            return "existe un usuario con el mismo nombre" # indica que ya existe
                    except:
                        pass

                faceEncodings += [[np.array(face_recognition.face_encodings(imgCaras[i])), nombres[i]]] # almacena los nuevos datos

        self.Saver(faceEncodings) # almacena los datos codificados

        return "registro completo"
        

encode = Encode()