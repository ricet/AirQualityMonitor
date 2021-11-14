#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time, signal, sys

BEEP = "P9_42"
GPIO.setup(BEEP, GPIO.OUT)
GPIO.output(BEEP, 0)

GAS_HEAT_EN = "P9_23"
GPIO.setup(GAS_HEAT_EN, GPIO.OUT)
GPIO.output(GAS_HEAT_EN, 1)

CO_HEAT_EN = "P9_41"
GPIO.setup(CO_HEAT_EN, GPIO.OUT)
GPIO.output(CO_HEAT_EN, 1)

CO_HEAT_CTL = "P9_26"
GPIO.setup(CO_HEAT_CTL, GPIO.OUT)
GPIO.output(CO_HEAT_CTL, 1)

ADC.setup()

def signal_handler(sig, frame):
    GPIO.output(GAS_HEAT_EN, 0)
    GPIO.output(CO_HEAT_EN, 0)
    GPIO.output(CO_HEAT_CTL, 0)
    GPIO.output(BEEP, 0)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


while (1):
    GPIO.output(CO_HEAT_CTL, 0)
    time.sleep(30)
    gas_value = ADC.read_raw("P9_37")
    co_value = ADC.read_raw("P9_39")
    print("gas: " + str(gas_value))
    print("co: " + str(co_value))
    time.sleep(1)
    GPIO.output(CO_HEAT_CTL, 1)
    time.sleep(60)

