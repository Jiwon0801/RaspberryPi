import RPi.GPIO as gpio
import time
from threading import Thread, Lock

gpio.setmode(gpio.BCM)

trig = 20
echo = 16
buzzer = 12

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)
gpio.setup(buzzer, gpio.OUT)

def getDist():
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
               
        return distance
    
lock = Lock()
def buzzerSet(distance):
        gpio.output(buzzer, True)
        time.sleep(distance)
        gpio.output(buzzer, False)
        time.sleep(distance)

try:
    while True:
        #lock.acquire()
        distance = getDist()
        #lock.release()
        print(distance)
        if distance < 12:
            t = Thread(target = buzzerSet, args = (distance,))
            t.start()
            #buzzerSet(0.03)
        #else:
            #gpio.output(buzzer, False)
            #buzzerSet(2)
except:
    gpio.cleanup()
