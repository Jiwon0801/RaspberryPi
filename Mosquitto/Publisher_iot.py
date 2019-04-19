import paho.mqtt.client as mqtt
from gpiozero import LED, LightSensor
from time import sleep
from threading import Thread

led = LED(21)
sensor = LightSensor(18)
client = mqtt.Client()

try:
	client.connect("localhost")	
	while True:
		led.toggle()
		client.publish("iot", "LED = {} / Light = {}".format(led.value, sensor.value))
		sleep(1)
#	client.loop(2)
except Exception as err:
	print('Error : %s' % err)
