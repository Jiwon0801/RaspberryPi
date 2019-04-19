from picamera import PiCamera
from time import sleep

with PiCamera() as camera:
    camera.start_preview()
    for balance in camera.AWB_MODES:
        camera.awb_mode = balance
        camera.annotate_text = "Balance: %s" % balance
        sleep(5)
    camera.stop_preview()