from gpiozero import Button, LED
from signal import pause

led = LED(24)
button = Button(25)

#button.when_pressed = led.on
#button.when_released = led.off

led.source = button.values

pause()