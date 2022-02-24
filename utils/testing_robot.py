import RPi.GPIO as GPIO
from time import sleep

motor1in1 = 23
motor1in2 = 24
motor1en = 25
temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1in1, GPIO.OUT)
GPIO.setup(motor1in2, GPIO.OUT)
GPIO.setup(motor1en, GPIO.OUT)
GPIO.output(motor1in1, GPIO.LOW)
GPIO.output(motor1in2, GPIO.LOW)
p = GPIO.PWM(motor1en, 1000)

p.start(25)

print("\n")
print("Default speed is LOW and direction is Forward")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

while(1):
    x = raw_input()

    if x == 'r':
        print("run")
        if temp1 == 1:
            GPIO.output(motor1in1, GPIO.HIGH)
            GPIO.output(motor1in2, GPIO.LOW)
            print("forward")
            x = 'z'
        else:
            GPIO.output(motor1in1, GPIO.LOW)
            GPIO.output(motor1in2, GPIO.HIGH)
            print("backward")
            x = 'z'

    elif x == 's':
        print("stop")
        GPIO.output(motor1in1, GPIO.LOW)
        GPIO.output(motor1in2, GPIO.LOW)
        x = 'z'
    
    elif x == 'f':
        print("forward")
        GPIO.output(motor1in1, GPIO.HIGH)
        GPIO.output(motor1in2, GPIO.LOW)
        temp1 = 1
        x = 'z'
    
    elif x == 'b':
        print("backward")
        GPIO.output(motor1in1, GPIO.LOW)
        GPIO.output(motor1in2, GPIO.LOW)
        temp1 = 0
        x = 'z'

    elif x == 'l':
        print("low")
        p.ChangeDutyCycle(25)
        x = 'z'

    elif x == 'm':
        print("medium")
        p.ChangeDutyCycle(50)
        x = 'z'

    elif x == 'h':
        print("high")
        p.ChangeDutyCycle(75)
        x = 'z'

    elif x == 'e':
        print("exit")
        GPIO.cleanup()
        print("GPIO Clean Up")
        break

    else:
        print("<<< WRONG INPUT >>>")