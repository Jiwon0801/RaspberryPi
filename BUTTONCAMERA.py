from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause

button = Button(25)
camera = PiCamera()

def capture():
    datetime1 = datetime.now().isoformat()
    camera.capture('/home/pi/%s.jpg' % datetime1)
    
button.when_pressed = capture

pause()