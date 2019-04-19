import spidev, time

spi = spidev.SpiDev()
spi.open(0,0)
spi.mode = 3
spi.max_speed_hz = 1000000

def analog_read(channel):
    r = spi.xfer2([1, (channel + 0x08)<<4, 0])
    adc_out = ((r[1]&0x03)<<8) + r[2]
    
    return adc_out

while True:
    adc = analog_read(0)
    voltage = adc*3.3/1023
    
    print("ADC = %s(%d) Voltage = %.3fV" % (hex(adc), adc, voltage))
    time.sleep(0.5)