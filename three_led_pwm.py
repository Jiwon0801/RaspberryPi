import RPi.GPIO as GPIO
from time import sleep

led_pins = [18, 20, 21]
pwm_leds = []
GPIO.setmode(GPIO.BCM)

for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 500)
    pwm.start(0)
    pwm_leds.append(pwm)

def fade(ix):
    for duty in range(101):
        pwm_leds[ix].ChangeDutyCycle(duty)
        sleep(0.01)
    
    for duty in range(100, -1, -1):
        pwm_leds[ix].ChangeDutyCycle(duty)
        sleep(0.01)
try:
    current = 0
    while True:
        #duty_s = input("Enter Brightness ( 0 to 100 ):")
        fade(current)
        current = (current + 1)%len(pwm_leds)
        
finally:
    print("Cleaning up")
    GPIO.cleanup()