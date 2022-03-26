from utils.robot.Movement_Controls import Movement_Controls
import utils.robot.camera_record as cam_script

import RPi.GPIO as GPIO
import concurrent.futures


record_time = 20

# from multiprocessing import Process

movement_controls = Movement_Controls()

speed = 40


with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:

    executor.map(cam_script)

    while 1:

        cam_record.start()

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
            executor.shutdown()
            print("Subprocess Shutdown")
            break
        elif x == 'r':
            print("run")
            movement_controls.run()
        else:
            print("BAD INPUT")
