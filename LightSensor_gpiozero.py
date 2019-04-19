from gpiozero import LightSensor
from time import sleep

sensor = LightSensor(20)

while True:
    #sensor.wait_for_light()
    #print("It's light! :)")
    #sensor.wait_for_dark()
    #print("It's dark :(")
    print(sensor.value)
    sleep(1)
