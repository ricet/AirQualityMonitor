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

BTN_C = "P9_15"
GPIO.setup(BTN_C, GPIO.IN)

USR3 = "USR3"
GPIO.setup(USR3, GPIO.OUT)
GPIO.output(USR3, 0)

while True:
    if GPIO.input(BTN_C):
        GPIO.output(BEEP, 0)
    else:
        GPIO.output(BEEP, 1)
