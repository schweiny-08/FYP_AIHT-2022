import cv2
cam = cv2.VideoCapture(0)

while True:
    ret, image = cam.read()
    