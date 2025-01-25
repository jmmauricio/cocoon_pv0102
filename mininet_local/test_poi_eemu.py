'''
This file have to be run within inside mininet: 

    mininet> POI python3 test_poi_eemu.py

Example:

    mininet> POI python3 test_poi_eemu.py
    V_POI = 0.999

'''
from colinker.modbus.modbus_client import Modbus_client

# POI python3 test_mininet_local.py
ip = "10.10.0.5"
port = 5002
mb = Modbus_client(ip,port=port)
mb.start()
reg_number = 372
value = mb.read(reg_number, 'int16',format = 'AB')
print(f'V_POI = {value/1000:0.3f}')
mb.close()
