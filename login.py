import cv2
import face_recognition

capture = cv2.VideoCapture(0)

class Recognition:
    def __init__(self):

        while True:
            # Captura cada fotograma
            ret, frame = capture.read()

            known_image = face_recognition.load_image_file("biden.jpg")
            unknown_image = face_recognition.load_image_file("unknown.jpg")

            biden_encoding = face_recognition.face_encodings(known_image)[0]
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

            results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

            # Muestra el frame resultante
            cv2.imshow("Reconociendo...", frame)
            if cv2.waitKey(20) & 0xFF == ord("q"):
                break

        # Closes screen
        cap.release()
        cv2.destroyAllWindows()