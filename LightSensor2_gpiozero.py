from gpiozero import LightSensor, LED
from signal import pause

sensor = LightSensor(20)
led = LED(24)

sensor.when_dark = led.on
sensor.when_light = led.off

pause()

