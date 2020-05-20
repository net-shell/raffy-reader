#!/usr/bin/env python

import requests
import base64
import time
from uuid import getnode as get_mac

url = 'http://raffy-admin/iot/start-reader'

reader = str(get_mac())
reader_bytes = reader.encode('ascii')
reader_base64 = base64.b64encode(reader_bytes)

postdata = {'reader': reader_base64}
x = requests.post(url, data = postdata, verify = False)
print(x.text)
