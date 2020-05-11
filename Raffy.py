#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests
import base64
import time
from uuid import getnode as get_mac

rc522_reader = SimpleMFRC522()
url = 'https://raffy-admin/rfid-endpoint'

print('Ready. Listening...');

try:
        while True:
                id, text = rc522_reader.read()
                print("ID = ", id)
                print("TEXT = ", text)

                encoded = str(id)
                encoded_bytes = encoded.encode('ascii')
                base64_bytes = base64.b64encode(encoded_bytes)

                reader = str(get_mac())
                print("READER = ", reader)
                reader_bytes = reader.encode('ascii')
                reader_base64 = base64.b64encode(reader_bytes)

                postdata = {'id': base64_bytes, 'text': text, 'reader': reader_base64}
                x = requests.post(url, data = postdata, verify = False)
                print(x.text)
                time.sleep(2)
finally:
        GPIO.cleanup()
