from gpiozero import PWMLED
from time import sleep
from signal import pause

led = PWMLED(25)

#while True:
#    led.value = 0
#    sleep(1)
#    led.value = 0.5
#    sleep(1)
#   led.value = 1
#    sleep(1)

led.pulse()
pause()