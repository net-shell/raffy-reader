#!/usr/bin/env python

import requests
import base64
import time
import platform
import psutil
from uuid import getnode as get_mac
from gpiozero import CPUTemperature

url = 'http://raffy-admin/iot/start-reader'

reader = str(get_mac())
reader_bytes = reader.encode('ascii')
reader_base64 = base64.b64encode(reader_bytes)

hdd = psutil.disk_usage('/')

cput = CPUTemperature()

postdata = {
  'reader': reader_base64,
  'platform': platform.platform(),
  'cpu': psutil.cpu_percent(),
  'cpu_temp': cput.temperature,
  'ram': psutil.virtual_memory().percent,
  'hdd_used': hdd.used // (2**30),
  'hdd_total': hdd.total // (2**30)
}
x = requests.post(url, data = postdata, verify = False)
print(x.text)
