#!/usr/bin/env python3

import Adafruit_BBIO.ADC as ADC
import time

ADC.setup()

while (1):
    value = ADC.read_raw("P9_37")
    print(str(value))
    time.sleep(0.1)