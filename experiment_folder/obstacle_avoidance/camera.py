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

movement_controls = Movement_Controls()
camera_controls = Camera_Controls()

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

		if forward_edge[0] > 230:
			if y[1] < 310:
				movement_controls.left()
				print("Moving left")
			elif y[i] > 310:
				movement_controls.right()
				print("Moving right")
		else:
			movement_controls.forward()
			print("Moving forward")

	except Exception as e:
		print("SOMETHING WENT WRONG\nERROR MESSAGE:")
		print(e)
