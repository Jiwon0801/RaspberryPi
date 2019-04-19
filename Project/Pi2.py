from gpiozero import DistanceSensor, LED, Button
from time import sleep
from datetime import datetime
from signal import pause
from picamera import PiCamera

dist_sensor = DistanceSensor(23,24, max_distance=1, threshold_distance=0.2)
capture_button = Button(12)
camera = PiCamera()
led = LED(25)


def capture():
	for i in range(10000):
		print(i)   
def recording_on():
	for i in range(2000000000000000):
		print(i)


#def recording_off():
	

capture_button.when_pressed = capture
dist_sensor.when_in_range = recording_on
#dist_sensor.when_out_of_range = recording_off

pause()
