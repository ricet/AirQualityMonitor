#!/usr/bin/python3

import time
import board
import adafruit_pct2075
import graphyte

i2c = board.I2C()  # uses board.SCL and board.SDA
pct = adafruit_pct2075.PCT2075(i2c)

pct.high_temperature_threshold = 35.5
pct.temperature_hysteresis = 30.0
pct.high_temp_active_high = False
print("High temp alert active high? %s" % pct.high_temp_active_high)

# Attach an LED with the Cathode to the INT pin and Anode to 3.3V with a current limiting resistor

graphyte.init('localhost', prefix='system.sync')

while True:
    temp = pct.temperature
    print("Temperature: %.2f C" % temp)
    graphyte.send('monitor.temp', temp)
    time.sleep(2)
