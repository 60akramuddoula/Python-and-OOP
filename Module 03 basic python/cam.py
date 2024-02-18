
import cv2
cam = cv2.VideoCapture(0)
while True:
    _ ,frame= cam.read()
    cv2.imshow('my camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    