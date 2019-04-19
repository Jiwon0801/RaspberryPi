from picamera import PiCamera
from time import sleep

with PiCamera() as camera:
    res = int(input('Resolution( 1: 320,240 / 2: 640,480 / 3: 1024,768)?'))
    
    if res == 3:
        camera.resolution = (1024,768)
    elif res == 2:
        camera.resolution = (640,480)
    else:
        camera.resolution = (320,240)
        
    filename = input('Filename ?')
    
    camera.framerate = 15
    camera.start_preview()
    
    camera.start_recording(output = filename + '.h264')
    
    camera.wait_recording(5)
    
    camera.stop_recording()
    
    camera.stop_preview()