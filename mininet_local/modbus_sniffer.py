from scapy.all import *
from scapy.contrib.modbus import *

# Define a callback function to process captured packets
def modbus_sniffer(packet):
    if ModbusADURequest in packet or ModbusADUResponse in packet:
        print(packet.show())

def debug_sniffer(packet):
    print(packet.summary())


# Sniff for Modbus traffic (default port 502)
#sniff(filter="tcp port 50003", prn=modbus_sniffer, iface="PPC-eth0", store=False)
sniff(filter="tcp port 5002", prn=debug_sniffer, iface="PPC-eth0", store=False)
