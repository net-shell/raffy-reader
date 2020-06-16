# Raffy Reader

RFID Reader messaging and processing for Raffy.

## Requirements

1. Raspbian 10 (buster)

2. Python 3

`sudo apt-get install -y python python3 python-pip python3-pip`

3. Dependencies

`sudo pip3 install spidev mfrc522`

## Setup

### Clone

Clone the repository:

`git clone git@github.com:net-shell/raffy-reader.git /home/pi/raffy-reader`

### Startup

Run `crontab -e`. Add the following line at the end, write changes and exit the editor.

`@reboot sudo bash /home/pi/raffy-reader/log-tags.sh > /home/pi/logs/cronlog 2>&1`

### Network up

1. Create a service

`sudo systemctl edit --force --full raffy-start.service`

2. Enter the following contents:
```
[Unit]
Description=Raffy Start
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/raffy-reader
ExecStart=/home/pi/raffy-reader/start-reader.sh

[Install]
WantedBy=multi-user.target
```

3. Enable and start the service:
```
sudo systemctl enable raffy-start.service
sudo systemctl start raffy-start.service
```

4. Reboot

`sudo systemctl reboot`
