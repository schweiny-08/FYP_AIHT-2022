import RPi.GPIO as GPIO
from multiprocessing import Process
import threading
import keyboard
import time
import sys
from select import select

sys.path.append('../..')

from utils.robot.Movement_Controls import Movement_Controls
from utils.robot.Camera_Controls import Camera_Controls
from utils.robot.Ultrasound_Controls import Ultrasound_Controls

movement_controls = Movement_Controls()
camera_controls = Camera_Controls()
ultrasound_controls = Ultrasound_Controls()

speed = 40
input_timeout = 0.1

movement_controls.run()
movement_controls.forward()

while 1:
	try:
		camera_controls.start_camera()
		c = camera_controls.get_line()
		forward_edge = c[1]
		y = (min(c))

		left_distance = ultrasound_controls.get_distance_left_1()
		right_distance = ultrasound_controls.get_distance_right_2()

		print("Left: ", left_distance)
		print("Right: ", right_distance)

		if left_distance < 50 and right_distance < 50:
			movement_controls.backward()
			print("Moving back")
		else:
			if left_distance < 50 or right_distance < 50 or forward_edge[0] > 230:
				if right_distance < 50 or y[1] < 310:
					movement_controls.left()
					print("Moving left")
				elif left_distance < 50 or y[i] > 310:
					movement_controls.right()
					print("Moving right")
			else:
				movement_controls.forward()
				print("Moving forward")

	except Exception as e:
		print("SOMETHING WENT WRONG\nERROR MESSAGE:")
		print(e)
