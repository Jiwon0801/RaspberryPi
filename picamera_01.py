from picamera import PiCamera
from time import sleep


with PiCamera() as camera:
    res = int(input('Resolution(1:320x240, 2:640x480, 3:1024x768)?'))
    
    if res == 3:
        camera.resolution = (1024, 768)
    elif res == 2:
        camera.resolution = (640, 480)
    else:
        camera.resolution = (320, 240)
    
    filename = input('File Name?')
    camera.start_preview()
    
    for i in range(5):
        sleep(3)
        camera.capture("{0}{1}.jpg".format(filename, i))
        
    camera.stop_preview()
    
    
    