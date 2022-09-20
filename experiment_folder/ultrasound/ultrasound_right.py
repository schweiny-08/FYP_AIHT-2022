import RPi.GPIO as GPIO
import time

try:
#	while True:
	GPIO.setmode(GPIO.BCM)

	pin_trigger_r = 6
	pin_echo_r = 5

	GPIO.setup(pin_trigger_r, GPIO.OUT)
	GPIO.setup(pin_echo_r, GPIO.IN)

	GPIO.output(pin_trigger_r, GPIO.LOW)

	print("Waiting for sensors")
	time.sleep(1)

	print("Getting distance")

	GPIO.output(pin_trigger_r, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(pin_trigger_r, GPIO.LOW)

	while GPIO.input(pin_echo_r)==0:
		pulse_start_time_r = time.time()
	while GPIO.input(pin_echo_r)==1:
		pulse_end_time_r = time.time()

	pulse_duration_r = pulse_end_time_r - pulse_start_time_r
	distance_r = round((pulse_duration_r*34300)/2, 2)
	print("Distance Right: ", distance_r, "cm")


except Exception as e:
	print(e)
finally:
	GPIO.cleanup()
