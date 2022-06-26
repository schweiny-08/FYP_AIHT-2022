import cv2
import skimage
from skimage.restoration import denoise_tv_chambolle

class Camera_Record:

    def __init__(self):
        self.cap = cv2.VideoCapture(-1)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def start_camera_thread(self):
        while True:
            ret, raw_img = self.cap.read()
            grayscale_img = skimage.color.rgb2gray(raw_img)
            cv2.imshow('gray', grayscale_img)
            #denoised_img = denoise_tv_chambolle(skimage.img_as_float(grayscale_img), weight=0.1)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
    def stop_camera(self):
        self.cap.release()
        cv2.destroyAllWindows()
