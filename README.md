# AirQualityMonitor
With ever-growing issues plagueing air-quality control in houses and industrial complexes alike, the people inhabiting these buildings shouldn't risk their health by trusting in shaky systems.

This project aims to provide a simple and portable solution to help users idenitfy high-risk environment, in terms of the air quality. This product  offers range of sensors that can identify various characteristics of the air around you, such as:
- CO2
- Methane
- Carbone Monoxide
- Particulates (PPM)
- Temperature
- Humidity

This information is stored locally on the device in an SQLite database. The system runs a Grafana webserver - a graphing utility that organizes the aquired data into a time-series graph (data over time). This can be accessed at the device's IP address.

## Required Hardware
This product is currently not in mass production, as we are merely undergrad students without strong ties with industrial manufacturers. Consequently, we have provided a folder with all the PCB files and the following table with the required components.
| Components                  | Link to Purchase                       |
| --------------------------- | -------------------------------------- |
| CO2 Sensor                  | https://www.adafruit.com/product/4867  |
| Carbon Monoxide Sensor      | https://www.sparkfun.com/products/9403 |
| Particulate Sensor          | https://www.adafruit.com/product/4505  |
| Methane Sensor              | https://www.sparkfun.com/products/9404 |
| OLED Display                | https://www.adafruit.com/product/4650  |
| Temperature/Humidity Sensor | https://www.adafruit.com/product/5046  |
| Rechargeable Battery        | https://www.adafruit.com/category/889  |

Please refer to `/PCB Files` for the PCB schematic and gerber files.


## How to Run
This assumes that you have the required hardware to run. If you do not, this will not work.

The following table outlines the scripts to run, in order to download and install the required libraries and processes.

| Scripts to Run      | Description of Script                                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| libinstall.sh       | Installs all the necessary python libraries for interfacing with the sensors                                           |
| grafanainstall.sh   | Installs grafana with the sqlite3 plugin and boot-on-startup enabled on Linux. Use this OR grafanainstallv2            |
| grafanainstallv2.sh | Installs grafana with the sqlite3 plugin and boot-on-startup enabled on ARM based machines. Use this OR grafanainstall |
| sqlite3install.sh   | Installs sqlite3                                                                                                       |
| setupSystemd.sh     | Enables the code to auto-start on bootup                                                                               |
| removeSystemd.sh    | Removes the code from auto-starting on bootup                                                                          |

To install correctly, run the following:
```
bone$: sudo ./libinstall.sh
bone$: sudo ./grafanainstall.sh
bone$: sudo ./sqlite3install.sh
bone$: sudo ./setupSystemd.sh
```
You may need to run the other provided grafana installer if the first one fails.
```
bone$: sudo ./grafanainstallv2.sh
```
