from gpiozero import Servo
from time import sleep

servo = Servo(21)

while True:
    servo.mid()
    print("mid")
    sleep(2)
    servo.min()
    print("min")
    sleep(2)
    servo.mid()
    print("mid")
    sleep(2)
    servo.max()
    print("max")
    sleep(2)