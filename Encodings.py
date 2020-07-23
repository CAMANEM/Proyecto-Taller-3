import face_recognition
import pickle
import numpy as np

class Encoders:
    def __init__(self):
        self.path = 'faces_data.dat'

    def Saver(faces_encodings):
        with open('faces_data.dat', 'wb') as f:
            pickle.dump(faces_encodings, f)

    def Loader():
        with open('faces_data.dat', 'rb') as f:
	        all_face_encodings = pickle.load(f)
            

        # Grab the list of names and the list of encodings
        #face_names = list(all_face_encodings.keys())
        faces_encodings = np.array(all_face_encodings)
        return faces_encodings

    def Encoder():
        luis = face_recognition.load_image_file("./files/faceRecognitionFiles/luis.jpg")
        david = face_recognition.load_image_file("./files/faceRecognitionFiles/david.jpg")

        luis_encoding = [face_recognition.face_encodings(luis)[0], "Luis"]
        david_encoding = [face_recognition.face_encodings(david)[0], "David"]

        faces_encodings = [luis_encoding, david_encoding]
        return faces_encodings