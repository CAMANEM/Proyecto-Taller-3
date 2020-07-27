from encoder import encode
import cv2

#encode.Encoder()
datos = encode.Loader()
#print(datos)
"""print(len(datos[0]))
for i in range(len(datos)):
    print(datos[i][0])
    print(datos[i][1])"""
#encode.Encoder([cv2.imread("./files/faceRecognitionFiles/luis.jpg"), cv2.imread("./files/faceRecognitionFiles/david.jpg")], ["Luis", "David"])
