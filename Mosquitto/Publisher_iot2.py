import paho.mqtt.client as mqtt
from gpiozero import LED, LightSensor
#import time
from threading import Thread

led = LED(21)
sensor = LightSensor(18)
client1 = mqtt.Client()
client2 = mqtt.Client()


def getLed(client, led):
	client.connect("localhost")
	while True:
		led.toggle()
		client.publish("iot", "LED = {}".format(led.value)
		#sleep(1)

def getSensor(client, sensor):
	client.connect("localhost")
	while True:
		client.publish("iot", "Light = {}".format(sensor.value))
		#sleep(1)
try:
	t1 = Thread(target = getLed, args = (client1, led))
	t1.start()
	t2 = Thread(target = getSensor, args = (client2, sensor))
	t2.start()
except Exception as err:
	print('Error : %s' % err)
