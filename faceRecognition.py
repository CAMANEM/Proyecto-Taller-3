import cv2

capture = cv2.VideoCapture(0)

while True:
    # Captura cada fotograma
    ret, frame = capture.read()

    # Muestra el frame resultante
    cv2.imshow("Reconociendo...", frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

# Closes screen
cap.release()
cv2.destroyAllWindows()