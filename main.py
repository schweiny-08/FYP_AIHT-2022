import RPi.GPIO as GPIO
from multiprocessing import Process
import threading
import keyboard
import time
import sys
from select import select

from utils.robot.Movement_Controls import Movement_Controls
from utils.robot.Camera_Controls import Camera_Controls
from utils.robot.Ultrasound_Controls import Ultrasound_Controls

movement_controls = Movement_Controls()
camera_controls = Camera_Controls()
ultrasound_controls = Ultrasound_Controls()

speed = 40
input_timeout = 0.1
#is_running = False

#camera_process = Process(target=camera_controls.start_camera)
#camera_process.start()

movement_controls.run()
movement_controls.forward()

while 1:
	try:
#		print("RUNNING1")
#		x = input()
#		speed = movement_controls.get_speed()
#		camera_controls.start_camera()

#		if x == 'w':
#			movement_controls.forward()
#		elif x == 's':
#			movement_controls.backward()
#		elif x == 'a':
#			movement_controls.left()
#		elif x == 'd':
#			movement_controls.right()
#		if keyboard.is_pressed('e'):
#			if speed < 80:
#				speed += 5
#				movement_controls.change_speed(speed)

#		if keyboard.is_pressed('q'):
#			if speed > 10:
#				speed -= 5
#				movement_controls.change_speed(speed)
#				print("Speed is " + speed.__str__())
#			else:
#				print("cannot go slower")

#		if keyboard.is_pressed('z'):
#			print("exit")
#			GPIO.cleanup()
#			print("GPIO Clean Up")
#			camera_process.kill()
#			print("Camera process killed")
#			camera_controls.stop_camera()
#			print("Stopped camera")
#			break

#		if keyboard.is_pressed('r'):
#		print("run")
#		movement_controls.run()
#		movement_controls.forward()
#		is_running = True

#		else:
#			print("BAD INPUT")

#		if is_running:
		camera_controls.start_camera()
		c = camera_controls.get_line()
#		print("C VALUE")
#		print(c)
		forward_edge = c[1]
#		print(forward_edge)
		y = (min(c))
#		print("Y VALUE")
#		print(y)

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

#		user_input = select([sys.stdin],[], [],  input_timeout)
#		print("USER INPUT")
#		print(user_input)
#		if user_input == 'q' or user_input == 'Q':
#			GPIO.cleanup()
#			print("GPIO Clean Up")
#			camera_controls.stop_camera()
#			print("Stopped camera")
#			break


	except Exception as e:
		print("SOMETHING WENT WRONG\nERROR MESSAGE:")
		print(e)
