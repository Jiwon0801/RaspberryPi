import smbus
import time

i2c = smbus.SMBus(1)

i2c.write_byte(0x27, 0x8)
time.sleep(1)
i2c.write_byte(0x27, 0x0)

