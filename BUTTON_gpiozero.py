from gpiozero import Button, LED

button = Button(25)
led = LED(24)

while True:
    if button.is_pressed:
        led.on()
    else:

        led.off()