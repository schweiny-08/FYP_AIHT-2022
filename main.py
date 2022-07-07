import RPi.GPIO as GPIO
from multiprocessing import Process
import threading

from utils.robot.Movement_Controls import Movement_Controls
from utils.robot.Camera_Controls import Camera_Controls

movement_controls = Movement_Controls()
camera_controls = Camera_Controls()

speed = 40
is_running = False

#camera_process = Process(target=camera_controls.start_camera)
#camera_process.start()

while 1:
	print("RUNNING2")
	try:
		print("RUNNING1")
		x = input()
		speed = movement_controls.get_speed()
#		camera_controls.start_camera()

		if x == 'w':
			movement_controls.forward()
		elif x == 's':
			movement_controls.backward()
		elif x == 'a':
			movement_controls.left()
		elif x == 'd':
			movement_controls.right()
		elif x == 'e':
			if speed < 80:
				speed += 5
				movement_controls.change_speed(speed)
		elif x == 'q':
			if speed > 10:
				speed -= 5
				movement_controls.change_speed(speed)
				print("Speed is " + speed.__str__())
			else:
				print("cannot go slower")
		elif x == 'z':
			print("exit")
			GPIO.cleanup()
			print("GPIO Clean Up")
#			camera_process.kill()
#			print("Camera process killed")
			camera_controls.stop_camera()
			print("Stopped camera")
			break
		elif x == 'r':
			print("run")
			movement_controls.run()
			is_running = True
		else:
			print("BAD INPUT")

		if is_running:
			camera_controls.start_camera()
#			c = camera_controls.get_line()
			c = camera_controls.c
			print("C VALUE")
			print(c)
			forward_edge = c[0][1]
		print(forward_edge)
	except Exception as e:
		print("SOMETHING WENT WRONG\nERROR MESSAGE:")
		print(e)
