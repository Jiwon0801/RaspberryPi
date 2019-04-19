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
    print("capture")
    camera.capture('/home/pi/python_Pi/Project/image/%s.jpg' % datetime.now().isoformat())

def recording_on():
	print("recording_on")
	led.on()
	camera.start_recording(output = '/home/pi/python_Pi/Project/record/%s.h264' % datetime.now().isoformat())

def recording_off():
	print("recording_off")
	led.off()
	camera.stop_recording()

capture_button.when_pressed = capture
dist_sensor.when_in_range = recording_on
dist_sensor.when_out_of_range = recording_off

pause()
