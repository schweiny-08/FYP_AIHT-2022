import RPi.GPIO as GPIO
from time import sleep

default_speed = 100

class Movement_Controls:

    def __init__(self):

        self.motor1_in1 = 26
        self.motor1_in2 = 16
        self.motor1_en = 13
        self.temp1 = 1

        self.motor2_in1 = 4
        self.motor2_in2 = 17
        self.motor2_en = 18
        self.temp2 = 1
        
        self.speed = default_speed

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.motor1_in1, GPIO.OUT)
        GPIO.setup(self.motor1_in2, GPIO.OUT)
        GPIO.setup(self.motor1_en, GPIO.OUT)
        GPIO.setup(self.motor2_in1, GPIO.OUT)
        GPIO.setup(self.motor2_in2, GPIO.OUT)
        GPIO.setup(self.motor2_en, GPIO.OUT)


        GPIO.output(self.motor1_in1, GPIO.LOW)
        GPIO.output(self.motor1_in2, GPIO.LOW)
        self.p1 = GPIO.PWM(self.motor1_en, 1000)
       
        GPIO.output(self.motor2_in1, GPIO.LOW)
        GPIO.output(self.motor2_in2, GPIO.LOW)
        self.p2 = GPIO.PWM(self.motor2_en, 1000)

    def run(self):
        self.p1.start(self.speed)
        self.p2.start(self.speed)

    def left(self):
        print("left")
        GPIO.output(self.motor1_in1, GPIO.HIGH)
        GPIO.output(self.motor2_in1, GPIO.HIGH)
        GPIO.output(self.motor1_in2, GPIO.LOW)
        GPIO.output(self.motor2_in2, GPIO.LOW)
        self.p1.ChangeDutyCycle(default_speed)
        self.p2.ChangeDutyCycle(default_speed)

    def right(self):
        print("right")
        GPIO.output(self.motor1_in1, GPIO.LOW)
        GPIO.output(self.motor2_in1, GPIO.LOW)
        GPIO.output(self.motor1_in2, GPIO.HIGH)
        GPIO.output(self.motor2_in2, GPIO.HIGH)
        self.p1.ChangeDutyCycle(default_speed)
        self.p2.ChangeDutyCycle(default_speed)

    def forward(self):
        print("forward")
        GPIO.output(self.motor1_in1, GPIO.HIGH)
        GPIO.output(self.motor2_in1, GPIO.LOW)
        GPIO.output(self.motor1_in2, GPIO.LOW)
        GPIO.output(self.motor2_in2, GPIO.HIGH)
        self.p1.ChangeDutyCycle(default_speed)
        self.p2.ChangeDutyCycle(default_speed)

    def backward(self):
        print("backward")
        GPIO.output(self.motor1_in1, GPIO.LOW)
        GPIO.output(self.motor2_in1, GPIO.HIGH)
        GPIO.output(self.motor1_in2, GPIO.HIGH)
        GPIO.output(self.motor2_in2, GPIO.LOW)
        self.p1.ChangeDutyCycle(default_speed)
        self.p2.ChangeDutyCycle(default_speed)
    
    def get_speed(self):
        return self.speed

    def change_speed(self, speed):
        self.speed = speed
        self.p1.ChangeDutyCycle(speed)
        self.p2.ChangeDutyCycle(speed)
