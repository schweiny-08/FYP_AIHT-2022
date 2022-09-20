import RPi.GPIO as GPIO
import time

try:
#	while True:
	GPIO.setmode(GPIO.BCM)

	pin_trigger_l = 27
	pin_echo_l = 22

	GPIO.setup(pin_trigger_l, GPIO.OUT)
	GPIO.setup(pin_echo_l, GPIO.IN)

	GPIO.output(pin_trigger_l, GPIO.LOW)

	print("Waiting for sensor")
	time.sleep(1)

	print("Getting distance")
	GPIO.output(pin_trigger_l, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(pin_trigger_l, GPIO.LOW)

	while GPIO.input(pin_echo_l)==0:
		pulse_start_time_l = time.time()
	while GPIO.input(pin_echo_l)==1:
		pulse_end_time_l = time.time()

	pulse_duration_l = pulse_end_time_l - pulse_start_time_l

	distance_l = round((pulse_duration_l*34300)/2, 2)

	print("Distance Left: ", distance_l, "cm")
except Exception as e:
	print(e)
finally:
	GPIO.cleanup()
