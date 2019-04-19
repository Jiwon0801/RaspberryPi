import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

switch_pin = 16
led_pin = 21

GPIO.setup(switch_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        if GPIO.input(switch_pin) == True:
            print("Button Pressed")
            GPIO.output(led_pin, GPIO.HIGH)
            sleep(0.2)
        GPIO.output(led_pin, GPIO.LOW)
finally:
    GPIO.cleanup()