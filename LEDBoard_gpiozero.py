from gpiozero import LEDBoard
from time import sleep
from signal import pause

leds = LEDBoard(24, 25, pwm=True)

#leds.on()
#sleep(1)
#leds.off()
#sleep(1)

#leds.value = (1,0)
#sleep(1)
#leds.blink()

leds.value = (0.2, 1.0)

pause()
