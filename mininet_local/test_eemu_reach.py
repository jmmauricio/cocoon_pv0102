'''
This file can be run within inside mininet: 

    mininet> POI python3 test_eemu_reach.py

Example:

    mininet> POI python3 ./mininet_local/test_eemu_reach.py
    V_POI = 0.999

This file can be run in linux guest:

    python3 ./mininet_local/test_eemu_reach.py
    
Example:

    $ python3 test_eemu_reach.py
    V_POI = 0.999
'''
from colinker.modbus.modbus_client import Modbus_client

# POI python3 test_mininet_local.py
ip = "10.20.0.2"
port = 5000
mb = Modbus_client(ip,port=port)
mb.start()
reg_number = 500
value = mb.read(reg_number, 'int16',format = 'AB')
print(f'V_POI = {value/1000:0.3f}')
mb.close()
