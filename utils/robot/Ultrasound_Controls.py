import RPi.GPIO as GPIO
import time

class Ultrasound_Controls:

	def __init__(self):
		self.pin_trig_1 = 27
		self.pin_echo_1 = 22
		self.pin_trig_2 = 6
		self.pin_echo_2 = 5

		GPIO.setup(self.pin_trig_1, GPIO.OUT)
		GPIO.setup(self.pin_trig_2, GPIO.OUT)
		GPIO.setup(self.pin_echo_1, GPIO.IN)
		GPIO.setup(self.pin_echo_2, GPIO.IN)

		GPIO.output(self.pin_trig_1, GPIO.LOW)
		GPIO.output(self.pin_trig_2, GPIO.LOW)

	def get_distance_left_1(self):
		start_time = 0
		end_time = 0
		GPIO.output(self.pin_trig_1, GPIO.HIGH)
		time.sleep(0.00001)
		GPIO.output(self.pin_trig_1, GPIO.LOW)

		while GPIO.input(self.pin_echo_1)==0:
			start_time = time.time()
		while GPIO.input(self.pin_echo_1)==1:
			end_time = time.time()

		duration = end_time - start_time
		distance = round((duration*34300)/2, 2)
		return distance

	def get_distance_right_2(self):
		start_time = 0
		end_time = 0
		GPIO.output(self.pin_trig_2, GPIO.HIGH)
		time.sleep(0.00001)
		GPIO.output(self.pin_trig_2, GPIO.LOW)

		while GPIO.input(self.pin_echo_2)==0:
			start_time = time.time()
		while GPIO.input(self.pin_echo_2)==1:
			end_time = time.time()

		duration = end_time - start_time
		distance = round((duration*34300)/2, 2)
		return distance
