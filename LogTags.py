#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests
import base64
import time
import json
from uuid import getnode as get_mac

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

rc522_reader = SimpleMFRC522()
url = 'http://raffy-admin/iot/log-tag'

print('Ready. Listening...');

try:
        while True:
                id, text = rc522_reader.read()
                print("CARD", id, text)

                encoded = str(id)
                encoded_bytes = encoded.encode('ascii')
                base64_bytes = base64.b64encode(encoded_bytes)

                reader = str(get_mac())
                print("READER", reader)
                reader_bytes = reader.encode('ascii')
                reader_base64 = base64.b64encode(reader_bytes)

                postdata = {'id': base64_bytes, 'text': text, 'reader': reader_base64}
                x = requests.post(url, data = postdata, verify = False)
                result = json.loads(x.text)
                wait = 2
                pin = 17

                print("STATUS", result['status'])

                if result['status'] == 'success':
                        wait = int(result['action']['time'])
                        if result['action']['is_exit'] > 0:
                                pin = 27

                        print("OPENING PIN", pin)
                        GPIO.output(pin, GPIO.HIGH)
                        time.sleep(wait)
                        GPIO.output(pin, GPIO.LOW)
                        print("CLOSED PIN", pin)
                else:
                        time.sleep(2)
except:
	print("ERROR!")
finally:
        GPIO.cleanup()
