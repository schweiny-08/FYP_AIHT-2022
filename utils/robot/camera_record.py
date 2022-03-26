import cv2
import skimage

class Camera_Record:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def start_camera_thread(self):
        while True:
            ret, raw_img = self.cap.read()
            grayscale_img = skimage.color.rgb2gray(raw_img)
            cv2.imshow('gray', gray)
            # denoised_img = skimage.restoration.denoise_tv_chambolle(grayscale_img, weight=60)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
    def stop_camera(self):
        self.cap.release()
        cv2.destroyAllWindows()
