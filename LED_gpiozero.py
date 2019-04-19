from gpiozero import LED
from time import sleep
from signal import pause

red = LED(24)

red.blink()

pause()