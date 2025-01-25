'''
This file have to be run within inside mininet: 

    mininet> PPC python3 ./mininet_local/test_ppc_pvs.py

Example:

    mininet> PPC python3 ./mininet_local/test_ppc_pvs.py
    V_POI = 1.020
    LV0101: P = 900.00 kW
    LV0102: P = 900.00 kW
    LV0101: Q = 500.00 kvar
    LV0102: Q = 500.00 kvar

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

reg_number = 370
value = mb.read(reg_number, 'int32',format = 'CDAB')
print(f'P_POI = {value:0.3f}')
reg_number = 374
value = mb.read(reg_number, 'int32',format = 'CDAB')
print(f'Q_POI = {value:0.3f}')

mb.close()


ip_prefix = "10.10"
port = "5002"
M=1
N=2
   
# active power references 
p_ppc = int(0.9e6)
for m in range(M):
    for n in range(N):
        name =  f'LV{str(m+1).zfill(2)}{str(n+1).zfill(2)}'
        ip = f'{ip_prefix}.{str(m+1)}.{str(n+1)}'
        mb = Modbus_client(ip,port=port)
        mb.start()
        reg_number = 40424
        mb.write(p_ppc, reg_number, 'uint32',format = 'CDAB')
        mb.close()

# active power measurements 
for m in range(M):
    for n in range(N):
        name =  f'LV{str(m+1).zfill(2)}{str(n+1).zfill(2)}'
        ip = f'{ip_prefix}.{str(m+1)}.{str(n+1)}'
        mb = Modbus_client(ip,port=port)
        mb.start()
        reg_number = 40525
        p = mb.read(reg_number, 'int32',format = 'CDAB')
        mb.close()
        print(f'{name}: P = {p/1000:5.2f} kW')

        
# reactive power references 
q_ppc = int(0.5e6)
for m in range(M):
    for n in range(N):
        name =  f'LV{str(m+1).zfill(2)}{str(n+1).zfill(2)}'
        ip = f'{ip_prefix}.{str(m+1)}.{str(n+1)}'
        mb = Modbus_client(ip,port=port)
        mb.start()
        reg_number = 40426
        mb.write(q_ppc, reg_number, 'int32',format = 'CDAB')
        mb.close()

# reactive power measurements 
for m in range(M):
    for n in range(N):
        name =  f'LV{str(m+1).zfill(2)}{str(n+1).zfill(2)}'
        ip = f'{ip_prefix}.{str(m+1)}.{str(n+1)}'
        mb = Modbus_client(ip,port=port)
        mb.start()
        reg_number = 40544
        q = mb.read(reg_number, 'int32',format = 'CDAB')
        mb.close()
        print(f'{name}: Q = {q/1000:5.2f} kvar')

