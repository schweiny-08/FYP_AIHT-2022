from utils.robot.Movement_Controls import Movement_Controls
import RPi.GPIO as GPIO

movement_controls = Movement_Controls()

speed = 40

while 1:
    x = input()
    speed = 0

    if x == 'w':
        movement_controls.forward()
    elif x == 's':
        movement_controls.backward()
    elif x == 'a':
        movement_controls.left()
    elif x == 'd':
        movement_controls.right()
    elif x == 'e':
        speed += 5
        movement_controls.change_speed(speed)
        
    elif x == 'q':
        if speed > 0:
            speed -= 5
        print("Speed is" + speed.__str__())
    elif x == 'z':
        print("exit")
        GPIO.cleanup()
        print("GPIO Clean Up")
        break
    elif x == 'r':
        print("run")
        movement_controls.run()
    else:
        print("BAD INPUT")