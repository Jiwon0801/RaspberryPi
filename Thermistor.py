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
    adc0 = analog_read(0)
    adc1 = analog_read(1)
    voltage0 = adc0*3.3/1023
    voltage1 = adc1*3.3/1023
    
    print("Light      = %s(%d)  Voltage0 = %.3fV" % (hex(adc0), adc0, voltage0))
    print("Thermistor = %s(%d) Voltage1 = %.3fV" % (hex(adc1), adc1, voltage1))
    time.sleep(0.5)