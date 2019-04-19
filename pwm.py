import RPi.GPIO as GPIO
from time import sleep

led = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

pwm_led = GPIO.PWM(led, 500)
pwm_led.start(100)

def fade():
    for duty in range(101):
        pwm_led.ChangeDutyCycle(duty)
        sleep(0.1)
    
    for duty in range(100, -1, -1):
        pwm_led.ChangeDutyCycle(duty)
        sleep(0.1)
        print(duty)
try:
    while True:
        #duty_s = input("Enter Brightness ( 0 to 100 ):")
        fade()
        
finally:
    print("Cleaning up")
    GPIO.cleanup()