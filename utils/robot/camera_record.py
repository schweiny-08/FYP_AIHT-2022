import cv2
from multiprocessing import Process


class Camera_Record:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    

    def start_camera(self):
        self.camera_thread = Process(target=self.start_camera_thread)
        self.camera_thread.start()

    def start_camera_thread(self):
        while True:
            ret, frame = self.cap.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
    def stop_camera(self):
        #self.camera_thread.kill()
        self.cap.release()
        cv2.destroyAllWindows()
