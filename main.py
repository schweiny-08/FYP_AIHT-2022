import Movement_Controls

movement_controls = Movement_Controls()

speed = 0

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
    elif x == 'q':
        speed += 5
        movement_controls.change_speed(speed)
        
    elif x == 'e':
        if speed > 0:
            speed -= 5
        print("Speed is" + speed)
    elif x == 'z':
        print("exit")
        GPIO.cleanup()
        print("GPIO Clean Up")
        break
    else:
        print("BAD INPUT")