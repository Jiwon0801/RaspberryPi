import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

trig = 24
echo = 23

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)

try:
    while True:
        gpio.output(trig, False)
        time.sleep(0.5)

        gpio.output(trig, True)
        time.sleep(0.00001)
        gpio.output(trig, False)

        while gpio.input(echo) == 0:
            pulse_start = time.time()

        while gpio.input(echo) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17000
        distance = round(distance, 2)

        print("Distance: ", distance, "cm")
except:
    gpio.cleanup()
