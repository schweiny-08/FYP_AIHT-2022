from utils.robot.Movement_Controls import Movement_Controls
import RPi.GPIO as GPIO

from utils.robot.camera_record import record_video

record_time = 20

from multiprocessing import Process

cam_record = Process(target=record_video, args=(record_time))
cam_record.start()
cam_record.join()
cam_record.close()

# movement_controls = Movement_Controls()

# speed = 40

# while 1:
#     x = input()
#     speed = movement_controls.get_speed()

#     if x == 'w':
#         movement_controls.forward()
#     elif x == 's':
#         movement_controls.backward()
#     elif x == 'a':
#         movement_controls.left()
#     elif x == 'd':
#         movement_controls.right()
#     elif x == 'e':
#         if speed < 80:
#             speed += 5
#             movement_controls.change_speed(speed)
        
#     elif x == 'q':
#         if speed > 10:
#             speed -= 5
#             movement_controls.change_speed(speed)
#             print("Speed is " + speed.__str__())
#         else:
#             print("cannot go slower")
#     elif x == 'z':
#         print("exit")
#         GPIO.cleanup()
#         print("GPIO Clean Up")
#         break
#     elif x == 'r':
#         print("run")
#         movement_controls.run()
#     else:
#         print("BAD INPUT")