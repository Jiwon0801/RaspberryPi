from picamera import PiCamera, Color
from time import sleep

with PiCamera() as camera:
    camera.start_preview()
    camera.annotate_text_size = 50
    camera.annotate_background = Color('green')
    camera.annotate_foreground = Color('white')
    camera.annotate_text = " Hello World "
    sleep(5)
    camera.capture("picamera_02.jpg")
    camera.stop_preview()
