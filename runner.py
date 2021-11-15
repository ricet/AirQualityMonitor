#!/usr/bin/env python3
import sqlite3
from random import randrange
from datetime import datetime
import time
import board
import adafruit_scd30
import adafruit_bme680
from adafruit_pm25.i2c import PM25_I2C
import busio
from adafruit_pm25.i2c import PM25_I2C


con = sqlite3.connect("example.db")

cur = con.cursor()

i2c = board.I2C()
scd = adafruit_scd30.SCD30(i2c)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)
bme680.sea_level_pressure = 1013.25
temperature_offset = -5
i2c2 = busio.I2C(board.SCL, board.SDA, frequency=100000)
reset_pin = None
pm25 = PM25_I2C(i2c2, reset_pin)


def getCO2():
    global data_CO2
    if scd.data_available:
        data_CO2 = scd.CO2


def getBME():
    global data_temp_bme
    global data_gas_bme
    global data_hum_bme
    global data_pres_bme
    global data_alt_bme
    data_temp_bme = bme680.temperature + temperature_offset
    data_gas_bme = bme680.gas
    data_hum_bme = bme680.relative_humidity
    data_pres_bme = bme680.pressure
    data_alt_bme = bme680.altitude


def getParticles():
    try:
        aqdata = pm25.read()
        global env_pm10
        global env_pm25
        global env_pm100
        global particles_03um
        global particles_05um
        global particles_10um
        global particles_25um
        global particles_50um
        global particles_100um
        env_pm10 = aqdata["pm10 env"]
        env_pm25 = aqdata["pm25 env"]
        env_pm100 = aqdata["pm100 env"]
        particles_03um = aqdata["particles 03um"]
        particles_05um = aqdata["particles 05um"]
        particles_10um = aqdata["particles 10um"]
        particles_25um = aqdata["particles 25um"]
        particles_50um = aqdata["particles 50um"]
        particles_100um = aqdata["particles 100um"]
    except RuntimeError:
        print("Unable ro read from sensor, retrying...")


try:
    # Create table
    cur.execute(
        """CREATE TABLE stocks
               (date text, data_CO2 real, data_temp_bme real, data_gas_bme real, data_hum_bme real, data_pres_bme real, data_alt_bme real, env_pm10 real, env_pm25 real, env_pm100 real, particles_03um real, particles_05um real, particles_10um real, particles_25um real, particles_50um real, particles_100um real)"""
    )

# Insert a row of data
except:
    global data_CO2
    global data_temp_bme
    global data_gas_bme
    global data_hum_bme
    global data_pres_bme
    global data_alt_bme
    global env_pm10
    global env_pm25
    global env_pm100
    global particles_03um
    global particles_05um
    global particles_10um
    global particles_25um
    global particles_50um
    global particles_100um
    for tem in range(100):
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")
        getCO2()
        cur.execute(
            "INSERT INTO stocks VALUES ('"
            + date_time
            + "',"
            + str(data_CO2)
            + ","
            + str(data_temp_bme)
            + ","
            + str(data_gas_bme)
            + ","
            + str(data_hum_bme)
            + ","
            + str(data_pres_bme)
            + ","
            + str(data_alt_bme)
            + ","
            + str(env_pm10)
            + ","
            + str(env_pm25)
            + ","
            + str(env_pm100)
            + ","
            + str(particles_03um)
            + ","
            + str(particles_05um)
            + ","
            + str(particles_10um)
            + ","
            + str(particles_25um)
            + ","
            + str(particles_50um)
            + ","
            + str(particles_100um)
            + ","
            + ")"
        )

        # Save (commit) the changes
        con.commit()
        time.sleep(5)

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    con.close()

    con = sqlite3.connect("example.db")
    cur = con.cursor()

    for row in cur.execute("SELECT * FROM stocks ORDER BY price"):
        print(row)
