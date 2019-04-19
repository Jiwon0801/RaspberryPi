from picamera import PiCamera
from time import sleep

with PiCamera() as camera:
    camera.start_preview()
    for exposure in camera.EXPOSURE_MODES:
        camera.exposure_mode = exposure
        camera.annotate_text = "Exposure: %s" % exposure
        sleep(5)
    camera.stop_preview()