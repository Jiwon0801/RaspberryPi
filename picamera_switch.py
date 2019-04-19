import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

GPIO.setmode(GPIO.BCM)

switch_pin = 16
GPIO.setup(switch_pin, GPIO.IN)

with PiCamera() as camera:
    camera.start_preview()
    
    try:
        count = 0
        while True:
            if GPIO.input(switch_pin) == True:
                camera.capture("image{0}.jpg".format(count))
                count += 1
                sleep(0.2)
    finally:
        GPIO.cleanup()
    
    camera.stop_preview()
