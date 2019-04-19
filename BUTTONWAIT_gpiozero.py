from gpiozero import Button

button = Button(25)

button.wait_for_press()
print("Button was pressed")