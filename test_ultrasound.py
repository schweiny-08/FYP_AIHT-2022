from utils.robot.Ultrasound_Controls import Ultrasound_Controls
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

u_c = Ultrasound_Controls()

left_dist = u_c.get_distance_left_1()
right_dist = u_c.get_distance_right_2()

print("LEFT: ", left_dist)
print("RIGHT", right_dist)
