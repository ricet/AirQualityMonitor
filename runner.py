#!/usr/bin/env python3
import sqlite3
from random import randrange
from datetime import datetime
import time
import board
import adafruit_scd30


con = sqlite3.connect('example.db')

cur = con.cursor()

i2c = board.I2C()
scd = adafruit_scd30.SCD30(i2c)

data_CO2 = 0

def getCO2():
    if scd.data_available:
        global data_CO2
        data_CO2 = scd.CO2

try:
# Create table
    cur.execute('''CREATE TABLE stocks
               (date text, rndVal real, trans text, symbol text, qty real, price real)''')

# Insert a row of data
except:
    for tem in range(100):
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")
        getCO2()
#    cur.execute("INSERT INTO stocks VALUES ('2006-01-05T12:" + str(randrange(50)) + ":00Z','" + str(randrange(100000)) + "','BUY','RHAT'," + str(randrange(1000) + 100) +  "," + str(35.14 + randrange(20)) + ")")
#    cur.execute("INSERT INTO stocks VALUES ('2021-11-14T12:" + str(randrange(50)) + ":00Z','" + str(randrange(100000)) + "','BUY','RHAT'," + str(randrange(1000) + 100) +  "," + str(35.14 + randrange(20)) + ")")
        cur.execute("INSERT INTO stocks VALUES ('" + date_time + "','" + str(data_CO2) + "','BUY','RHAT'," + str(randrange(1000) + 100) +  "," + str(35.14 + randrange(20)) + ")")

# Save (commit) the changes
        con.commit()
        time.sleep(5)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
    con.close()

    con = sqlite3.connect('example.db')
    cur = con.cursor()


    for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)
