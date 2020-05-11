#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests

reader = SimpleMFRC522()

print('Ready. Listening...');

try:
        id, text = reader.read()
        print("ID = ", id)
        print("TEXT = ", text)

        url = 'https://raffy-admin/rfid-endpoint'
        postdata = {'id': id, 'text': text}
        x = requests.post(url, data = postdata, verify = False)
        print(x.text)
finally:
        GPIO.cleanup()
