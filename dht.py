import RPi.GPIO as GPIO
import Adafruit_DHT

GPIO.setmode(GPIO.BCM)
pin = 20 
GPIO.setup(pin, GPIO.IN)

try:
    while True:
        humi, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)

        if humi is not None and temp is not None:
            print('Temp={0:0.1f}* Humi={1:0.1f}%'.format(temp, humi))
        else:
            print('Failed to get reading. Try again!')
finally:
    GPIO.cleanup()
