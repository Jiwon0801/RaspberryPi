import RPi.GPIO as GPIO
from time import sleep

led = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

try:
    while True:
        GPIO.output(led, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(led, GPIO.LOW)
        sleep(0.5)
finally:
    GPIO.cleanup()