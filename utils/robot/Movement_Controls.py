import RPi.GPIO as GPIO
from time import sleep


class Movement_Controls:

    def __init__(self):

        motor1_in1 = 23
        motor1_in2 = 24
        motor1_en = 25
        temp1 = 1

        motor2_in1 = 4
        motor2_in2 = 17
        motor2_en = 18
        temp2 = 1

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(motor1_in1, GPIO.OUT)
        GPIO.setup(motor1_in2, GPIO.OUT)
        GPIO.setup(motor1_en, GPIO.OUT)
        GPIO.output(motor1_in1, GPIO.LOW)
        GPIO.output(motor1_in2, GPIO.LOW)
        p1 = GPIO.PWM(motor1_en, 1000)

        GPIO.setup(motor2_in1, GPIO.OUT)
        GPIO.setup(motor2_in2, GPIO.OUT)
        GPIO.setup(motor2_en, GPIO.OUT)
        GPIO.output(motor2_in1, GPIO.LOW)
        GPIO.output(motor2_in2, GPIO.LOW)
        p2 = GPIO.PWM(motor2_en, 1000)

    def forward(self):
        print("forward")
        GPIO.output(motor1_in1, GPIO.HIGH)
        GPIO.output(motor2_in1, GPIO.HIGH)
        GPIO.output(motor1_in2, GPIO.LOW)
        GPIO.output(motor2_in2, GPIO.LOW)

    def backward(self): 
        print("backward")
        GPIO.output(motor1_in1, GPIO.LOW)
        GPIO.output(motor2_in1, GPIO.LOW)
        GPIO.output(motor1_in2, GPIO.HIGH)
        GPIO.output(motor2_in2, GPIO.HIGH)

    def left(self):
        print("left")
        GPIO.output(motor1_in1, GPIO.HIGH)
        GPIO.output(motor2_in1, GPIO.LOW)
        GPIO.output(motor1_in2, GPIO.LOW)
        GPIO.output(motor2_in2, GPIO.HIGH)
    
    def right(self):
        print("right")
        GPIO.output(motor1_in1, GPIO.LOW)
        GPIO.output(motor2_in1, GPIO.HIGH)
        GPIO.output(motor1_in2, GPIO.HIGH)
        GPIO.output(motor2_in2, GPIO.LOW)

    def change_speed(self, speed):
        p1.ChangeDutyCycle(speed)
        p2.ChangeDutyCycle(speed)