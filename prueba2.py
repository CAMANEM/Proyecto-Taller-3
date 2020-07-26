from encoder import encode
import cv2

#encode.Encoder()
#print(encode.Loader())
encode.Encoder([cv2.imread("./files/faceRecognitionFiles/luis.jpg"), cv2.imread("./files/faceRecognitionFiles/david.jpg")], ["Luis", "David"])