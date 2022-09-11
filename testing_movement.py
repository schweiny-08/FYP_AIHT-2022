from utils.robot.Movement_Controls import Movement_Controls
import RPi.GPIO as GPIO

m_v = Movement_Controls()

while True:
	x = input()

	if x == 'r':
		m_v.run()
	if x == 'w':
		m_v.forward()
	if x == 's':
		m_v.backward()
	if x == 'a':
		m_v.left()
	if x == 'd':
		m_v.right()
	if x == 'e':
		GPIO.cleanup()
		break
