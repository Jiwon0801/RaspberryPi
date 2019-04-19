import time
import I2C_LCD_driver

mylcd = I2C_LCD_driver.lcd()


try:
	while True:
		mylcd.lcd_display_string("Time: %s" % time.strftime("%H:%M:%S"), 1)
		mylcd.lcd_display_string("Date: %s" % time.strftime("%m/%d/%Y"), 2)
finally:
	mylcd.lcd_
