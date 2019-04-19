import spidev, time
import RPi.GPIO as GPIO

sw_pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw_pin, GPIO.IN)

spi = spidev.SpiDev()
spi.open(0,0)
spi.mode = 3
spi.max_speed_hz = 1000000

def analog_read(channel):
    r = spi.xfer2([1, (channel + 0x08)<<4, 0])
    adc_out = ((r[1]&0x03)<<8) + r[2]
    return adc_out


while True:
    x = analog_read(2)
    y = analog_read(3)
    if GPIO.input(sw_pin) == True:
        sw = 'OFF'
    else:
        sw = 'ON'
        
    voltage_x = x*3.3/1023
    voltage_y = y*3.3/1023
    
    print("X = %s(%d) Voltage_X = %.3fV" % (hex(x), x, voltage_x))
    print("Y = %s(%d) Voltage_Y = %.3fV" % (hex(y), y, voltage_y))
    print("SW = %s" % sw)
    time.sleep(0.5)
