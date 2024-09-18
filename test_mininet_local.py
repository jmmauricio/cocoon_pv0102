from colinker.modbus.modbus_client import Modbus_client

# PPC python3 test_mininet_local.py
ip = "10.10.0.5"
port = 5002
mb = Modbus_client(ip,port=port)
mb.start()
reg_number = 372
value = mb.read(reg_number, 'int16',format = 'AB')
print(f'V_POI = {value/1000:0.3f}')
mb.close()


ip_prefix = "10.10"
port = "5002"
M=1
N=2

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
        print(f'{name}: P = {p/1000:5.2f} kvar')
        
# active power references 
p_ppc = int(0.9e6)
for m in range(M):
    for n in range(N):
        name =  f'LV{str(m+1).zfill(2)}{str(n+1).zfill(2)}'
        ip = f'{ip_prefix}.{str(m+1)}.{str(n+1)}'
        mb = Modbus_client(ip,port=port)
        mb.start()
        reg_number = 40424
        mb.write(p_ppc, reg_number, 'int32',format = 'CDAB')
        mb.close()




# reactive power references 
q_ppc = int(0.1e6)
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




# '''
# 2024-09-18 06:27:53,347 device: p_s_ppc_LV0102@127.0.1.2:50102/40424 = 0 -> linker: p_s_ppc_LV0102@127.100.0.1:5000/2000
# 2024-09-18 06:27:53,349 device: q_s_ppc_LV0102@127.0.1.2:50102/40426 = 100000 -> linker: q_s_ppc_LV0102@127.100.0.1:5000/2004
# 2024-09-18 06:27:53,350 linker: p_s_LV0102@127.100.0.1:5000/2008 = 0 (int32) -> device: p_s_LV0102@127.0.1.2:50102/40525
# 2024-09-18 06:27:53,352 linker: q_s_LV0102@127.100.0.1:5000/2012 = 99999 (int32) -> device: q_s_LV0102@127.0.1.2:50102/40544
# 2024-09-18 06:27:53,404 device: p_s_ppc_LV0102@127.0.1.2:50102/40424 = 0 -> linker: p_s_ppc_LV0102@127.100.0.1:5000/2000
# 2024-09-18 06:27:53,405 device: q_s_ppc_LV0102@127.0.1.2:50102/40426 = 100000 -> linker: q_s_ppc_LV0102@127.100.0.1:5000/2004
# 2024-09-18 06:27:53,406 linker: p_s_LV0102@127.100.0.1:5000/2008 = 0 (int32) -> device: p_s_LV0102@127.0.1.2:50102/40525
# 2024-09-18 06:27:53,407 linker: q_s_LV0102@127.100.0.1:5000/2012 = 99999 (int32) -> device: q_s_LV0102@127.0.1.2:50102/40544
# '''