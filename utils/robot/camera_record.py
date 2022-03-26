import cv2

class Camera_Record:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def start_camera(self):
        while True:
            ret, frame = self.cap.read()
            cv2.imshow('frame', frame)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break

    def stop_camera(self):
        self.cap.release()
        cv2.destroyAllWindows()