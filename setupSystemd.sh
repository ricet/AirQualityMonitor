#!/bin/sh

sudo cp airQuality.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start airQuality.service
sudo systemctl enable airQuality.service

echo "Done"
