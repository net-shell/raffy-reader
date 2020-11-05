#!/usr/bin/env python
import time
import sys
import requests
import base64
import json
from uuid import getnode as get_mac

url = 'http://raffy-admin/iot/log-tag';

try:
        while True:
                print("LISTENING")
                sys.stdin = open('/dev/tty0', 'r')
                id = input()
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
except Exception as e:
        print("ERROR!")
        print(str(e))
        logging.error(e)
finally:
        print("Closing...")
