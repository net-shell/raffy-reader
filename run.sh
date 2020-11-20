#!/bin/sh
cd /home/pi/raffy-reader;
date;
sudo killall python3;
python3 StartReader.py;
sudo python3 LogTags.py;
