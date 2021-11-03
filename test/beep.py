#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time

BEEP = "P9_42"
GPIO.setup(BEEP, GPIO.OUT)
GPIO.output(BEEP, 0)

GAS_HEAT_EN = "P9_23"
GPIO.setup(GAS_HEAT_EN, GPIO.OUT)
GPIO.output(GAS_HEAT_EN, 0)

CO_HEAT_EN = "P9_41"
GPIO.setup(CO_HEAT_EN, GPIO.OUT)
GPIO.output(CO_HEAT_EN, 0)

CO_HEAT_CTL = "P9_26"
GPIO.setup(CO_HEAT_CTL, GPIO.OUT)
GPIO.output(CO_HEAT_CTL, 0)


while True:
    GPIO.output(BEEP, 1)
    time.sleep(0.05)
    GPIO.output(BEEP, 0)
    time.sleep(0.9)
