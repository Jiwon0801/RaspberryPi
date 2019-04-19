from gpiozero import Button, LED
from time import sleep
import random

led = LED(24)

player_1 = Button(16)
player_2 = Button(20)

time = random.uniform(5, 10)
sleep(time)
led.on()

while True:
	if player_1.is_pressed:
		print("Player 1 wins!")
		break
	if player_2.is_pressed:
		print("Player 2 wins!")
		break

led.off()
