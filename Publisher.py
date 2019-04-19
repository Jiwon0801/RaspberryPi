import paho.mqtt.client as mqtt

client = mqtt.Client()

try:
	client.connect("localhost")

	client.publish("$SYS", "Hello World")
	client.loop(2)
except Exception as err:
	print('Error : %s' % err)
