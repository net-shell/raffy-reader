# Raffy Reader

RFID Reader messaging and processing for Raffy.

## Requirements

1. Raspbian 10 (buster)

2. Python 3

`sudo apt-get install -y python python3`

## Setup

### Clone

Clone the repository:

`git clone git@github.com:net-shell/raffy-reader.git /home/pi/raffy-reader`

### Startup

Run `crontab -e`. Add the following line at the end, write changes and exit the editor.

`@reboot sudo bash /home/pi/raffy-reader/log-tags.sh > /home/pi/logs/cronlog 2>&1`

### Network up

TODO
