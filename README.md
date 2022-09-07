# Raffy Reader

RFID Reader messaging and processing for Raffy.

## Requirements

1. Raspbian 10 (buster)

2. Git

`sudo apt-get install -y git`

3. Python 3

`sudo apt-get install -y python3 python3-pip python3-gpiozero`

4. Dependencies

`sudo pip3 install spidev mfrc522`

## Setup

### RPi Wiring

![Wiring](https://raw.githubusercontent.com/net-shell/raffy-reader/master/rc522_wiring.jpg)

### Clone

Clone the repository:

`git clone https://github.com/net-shell/raffy-reader.git /home/pi/raffy-reader`

### Hosts File Entry

The Python scripts that read the RFID tags are using a non-existent domain `raffy-admin` to target the server that will process the activity.
In order to resolve this domain properly, add the IP address of the server either in local network or the internet.

```
# /etc/hosts
raffy-admin  192.168.0.100 # The IP where raffy-admin is running
```

### Schedule

Run `sudo crontab -e`. Add the following line at the end, write changes and exit the editor.

`*/5 * * * * /home/pi/raffy-reader/run.sh >> /home/pi/logs/run.log`

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
