#!/usr/bin/env python
import time
import sys
import requests
import base64
import json
import RPi.GPIO as GPIO
from uuid import getnode as get_mac
from rfidhid.core import RfidHid

url = 'http://raffy-admin/iot/log-tag'

try:
    #rfid = RfidHid(0x16c0, 0x27db)
    rfid = RfidHid()
    print("Listening...")
except Exception as e:
    print("ERROR", e)
    exit()

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
print("Control pins are set.")

def listen():
    try:
        while True:
                tag = rfid.read_tag()
                id = tag.get_tag_uid()
                print("CARD", id)

                encoded = str(id)
                encoded_bytes = encoded.encode('ascii')
                base64_bytes = base64.b64encode(encoded_bytes)

                reader = str(get_mac())
                print("READER", reader)
                reader_bytes = reader.encode('ascii')
                reader_base64 = base64.b64encode(reader_bytes)

                postdata = {'id': base64_bytes, 'reader': reader_base64}
                x = requests.post(url, data = postdata, verify = False)
                print(x.text)

                result = json.loads(x.text)
                wait = 2
                pin = 17
                print("STATUS", result['status'])
                rfid.beep()

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
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print("ERROR!", str(e))
        #listen()
    finally:
        print("Cleaning up...")
        GPIO.cleanup()

listen()
