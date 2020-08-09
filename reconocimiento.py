import cv2
import face_recognition
import time
from encoder import encode

class Camara:
    def __init__(self):
        pass

    def InicioSesion(self):
        """Reconoce la cara e inicia sesión con el nombre asociado a la cara en caso de reconocerla"""

        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # comienza a capturar video

        faceEncodings = encode.Loader() # carga los datos de las caras registradas

        # INICIALIZA DATOS NECESARIOS
        tiempoEjecutando = 0 
        usuario = "" 
        reconocido = False

        # BUCLE DE RECONOCIMIENTO
        while tiempoEjecutando < 15: # se detiene a los 15 segundos con el fin de ahorrar recursos

            start=time.time() # toma la hora a la que empezó, para medir el tiempo de ejecución
            ret, img = cap.read() # toma una imagen aislada del momento actual, para analizarla

            if reconocido:
                cv2.putText(img, "Bienvenido, "+usuario, (100,30), cv2.FONT_ITALIC, 1, (60, 200, 0, 255), 2) # muestra un mensaje de bienvenida al reconocer el rostro
            
            cv2.imshow('Reconociendo...', img) # muestra la imagen en pantalla
            

            # PROCESO DE RECONOCIMIENTO
            try:
                if not reconocido: # si la cara ya fue reconocida, omitir este paso
                    noIdentificado = face_recognition.face_encodings(img)[0] # codifica la imagen actual en pantalla para compararla con las almacendas

                for faceEncoding in faceEncodings:
                    if reconocido:  break # si la cara ya fue reconocida, omitir este paso
                    if face_recognition.compare_faces([faceEncoding[0][0]], noIdentificado)[0]: # Compara la imagen de cámara con las caras almacenadas
                        usuario = faceEncoding[1] # asigna el nombre

                        tiempoEjecutando = 12.0 # da 3 segudnos después de reconocer
                        
                        reconocido = True # indica que se detectó la cara
            except:
                pass
            print("duante el bucle, reconocido es ", reconocido)

            if cv2.waitKey(1) == 27: # cierra la ventana forzosamente cuando se presione la tecla 'Esc'
                break

            tiempoEjecutando += round(time.time()-start, 2) # compara la hora de inicio y la actual, con el fin de definir el tiempo de ejecución

        cap.release() # libera la cámara web para otros usos
        cv2.destroyAllWindows() # elimina todas las ventanas

        return [reconocido, usuario] # devuelve los datos de si fue reconocido y el nombre del usuario

    def RegistrarCara(self, usuario):
        """Almacena los datos de los nuevos usuarios que se deseen añadir a la plataforma"""
        
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # captura el video de cámara

        # INICIALIZA VALORES REQUERIDOS
        tiempo = 0
        guardado = False
        datosGuardados = ""

        cascade = cv2.CascadeClassifier('./files/haarcascade_frontalface_default.xml') # cascade para detectar caras en pantalla

        while tiempo < 60:
            start=time.time() # toma el tiempo de inicio
            ret, img = cap.read() # almacena la imagen para leerla
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            faces = cascade.detectMultiScale(gray, 1.3, 5) # toma datos de las caras

            lenFaces = len(faces) # asigna el valor de la cantidad de caras que hay en pantalla

            if cv2.waitKey(1) == 13 and lenFaces > 0  and not guardado: # solo cuando haya caras es posible almacenar datos
                datosGuardados = encode.Encoder([img],[usuario])
                guardado = True
                tiempo = 58

            if datosGuardados == "existe un usuario con el mismo nombre":
                guardado = False
                cv2.putText(img, "El nombre ya está registrado", (100,50), cv2.FONT_ITALIC, 1, (0, 60, 200, 255), 2) # cuando ya existe alguien con este nombre

            cv2.putText(img, "Mantenga escape para salir", (10,400), cv2.FONT_ITALIC, 1, (0, 0, 200, 255), 2) # instrucción por si desea salir

            if lenFaces == 0:
                cv2.putText(img, "No se detectan caras", (100,30), cv2.FONT_ITALIC, 1, (0, 60, 200, 255), 2) # si no hay caras en pantalla
            
            else:
                cv2.putText(img, "Cara detectada, enter para registrar", (10,30), cv2.FONT_ITALIC, 1, (60, 200, 0, 255), 2) # cuando hay caras

            if guardado:
                cv2.putText(img, "Registro satisfactorio", (120,450), cv2.FONT_ITALIC, 1, (0, 80, 200, 255), 2) # al registrarse 

            cv2.imshow('Buscando rostro para registrar', img) # muestra la cara en una ventana

            tiempo += time.time() - start # toma la hora de inicio y la hora actual, para medir el tiempo en ejecución

            if cv2.waitKey(1) == 27: # presionar 'Esc' para salir
                break

        cap.release() # libera la cámara para otros usos
        cv2.destroyAllWindows() # destruye todas las ventanas
        return [guardado, usuario, datosGuardados] # devuelve los datos requeridos en la clase Main
        
camara = Camara() # crea una instancia desde la que se accede con más facilidad desde Main