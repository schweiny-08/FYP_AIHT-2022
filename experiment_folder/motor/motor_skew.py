import sys
import os
import RPi.GPIO as GPIO
from time import sleep

sys.path.append('../..')

from utils.robot.Movement_Controls import Movement_Controls

movement_controls = Movement_Controls()
movement_controls.run()
movement_controls.forward()

sleep(10)
GPIO.cleanup()


