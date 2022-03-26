import RPi.GPIO as GPIO
from multiprocessing import Process

from utils.robot.Movement_Controls import Movement_Controls
from utils.robot.camera_record import Camera_Record

movement_controls = Movement_Controls()
camera_record = Camera_Record()

speed = 40

camera_process = Process(target=camera_record.start_camera_thread)
camera_process.start()


while 1:

    x = input()
    speed = movement_controls.get_speed()

    if x == 'w':
        movement_controls.forward()
    elif x == 's':
        movement_controls.backward()
    elif x == 'a':
        movement_controls.left()
    elif x == 'd':
        movement_controls.right()
    elif x == 'e':
        if speed < 80:
            speed += 5
            movement_controls.change_speed(speed)
        
    elif x == 'q':
        if speed > 10:
            speed -= 5
            movement_controls.change_speed(speed)
            print("Speed is " + speed.__str__())
        else:
            print("cannot go slower")
    elif x == 'z':
        print("exit")
        GPIO.cleanup()
        print("GPIO Clean Up")
        camera_process.kill()
        camera_record.stop_camera()
        print("Stopped camera")
        break
    elif x == 'r':
        print("run")
        movement_controls.run()
    else:
        print("BAD INPUT")
