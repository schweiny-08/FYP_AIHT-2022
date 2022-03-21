import cv2
from utils.robot.video_capture import VideoCaptureAsync
import time

vid_w = 1080
vid_h = 720

capture = VideoCaptureAsync(0, vid_w, vid_h)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

def record_video():
    capture.start()
    time_end = time.time() + duration

    frames = 0
    images = []

    # This loop only captures time for above duration
    while True:
        ret, new_frame = capture.read()
        images.append(new_frame)
        
        # Creates the display
        cv2.namedWindow('image', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        
        # Shows every 5th frame to the display
        if frames == 0 or frame%5 == 0:
            frame = cv2.flip(new_frame, 180)
            cv2.imshow('frame', frame)
        
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
    
def stop_video():
    capture.stop()
    cv2.destroyAllWindows()

    fps = frames/duration

    print(frames)
    print(fps)
    print(len(images))

    