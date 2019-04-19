import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print("Connected with result code", rc)
	if rc == 0:
		client.subscribe("iot/#")
	else:
		print('Connection Fail : ', rc)

def on_message(client, userdata, msg):
	print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

try:
	client.connect("localhost", 1883, 60)
	client.loop_forever()
except Exception as err:
	print('Error : %s' % err)
