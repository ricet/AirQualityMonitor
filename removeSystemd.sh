#!/bin/sh

sudo systemctl stop airQuality.service
sudo systemctl disable airQuality.service
sudo rm /etc/systemd/system/airQuality.service
sudo systemctl daemon-reload

echo "Done"
