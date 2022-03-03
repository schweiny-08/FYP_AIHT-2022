import RPi.GPIO as GPIO
from time import sleep


class Movement_Controls:

    def __init__(self):

        self.motor1_in1 = 23
        self.motor1_in2 = 24
        self.motor1_en = 25
        self.temp1 = 1

        self.motor2_in1 = 4
        self.motor2_in2 = 17
        self.motor2_en = 18
        self.temp2 = 1

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.motor1_in1, GPIO.OUT)
        GPIO.setup(self.motor1_in2, GPIO.OUT)
        GPIO.setup(self.motor1_en, GPIO.OUT)
        GPIO.output(self.motor1_in1, GPIO.LOW)
        GPIO.output(self.motor1_in2, GPIO.LOW)
        self.p1 = GPIO.PWM(self.motor1_en, 1000)

        GPIO.setup(self.motor2_in1, GPIO.OUT)
        GPIO.setup(self.motor2_in2, GPIO.OUT)
        GPIO.setup(self.motor2_en, GPIO.OUT)
        GPIO.output(self.motor2_in1, GPIO.LOW)
        GPIO.output(self.motor2_in2, GPIO.LOW)
        self.p2 = GPIO.PWM(self.motor2_en, 1000)

    def run(self):
        self.p1.start(40)
        self.p2.start(40)

    def forward(self):
        print("forward")
        GPIO.output(self.motor1_in1, GPIO.HIGH)
        GPIO.output(self.motor2_in1, GPIO.HIGH)
        GPIO.output(self.motor1_in2, GPIO.LOW)
        GPIO.output(self.motor2_in2, GPIO.LOW)

    def backward(self): 
        print("backward")
        GPIO.output(self.motor1_in1, GPIO.LOW)
        GPIO.output(self.motor2_in1, GPIO.LOW)
        GPIO.output(self.motor1_in2, GPIO.HIGH)
        GPIO.output(self.motor2_in2, GPIO.HIGH)

    def left(self):
        print("left")
        GPIO.output(self.motor1_in1, GPIO.HIGH)
        GPIO.output(self.motor2_in1, GPIO.LOW)
        GPIO.output(self.motor1_in2, GPIO.LOW)
        GPIO.output(self.motor2_in2, GPIO.HIGH)
    
    def right(self):
        print("right")
        GPIO.output(self.motor1_in1, GPIO.LOW)
        GPIO.output(self.motor2_in1, GPIO.HIGH)
        GPIO.output(self.motor1_in2, GPIO.HIGH)
        GPIO.output(self.motor2_in2, GPIO.LOW)

    def change_speed(self, speed):
        self.p1.ChangeDutyCycle(speed)
        self.p2.ChangeDutyCycle(speed)