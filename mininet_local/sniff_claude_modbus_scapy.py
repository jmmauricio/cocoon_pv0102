from scapy.all import sniff, TCP
from pymodbus.constants import Defaults
from pymodbus.utilities import computeCRC, checkCRC
import struct
import datetime

def decode_modbus_packet(packet):
    """Decode a Modbus TCP packet and extract key information"""
    if not packet.haslayer(TCP) or not packet.load:
        return
        
    # Check if this is a Modbus TCP packet (port 5002)
    if packet[TCP].sport != 5002 and packet[TCP].dport != 5002:
        return
        
    raw_data = bytes(packet.load)
    
    # Parse Modbus TCP header
    try:
        transaction_id = struct.unpack('>H', raw_data[0:2])[0]
        protocol_id = struct.unpack('>H', raw_data[2:4])[0]
        length = struct.unpack('>H', raw_data[4:6])[0]
        unit_id = raw_data[6]
        function_code = raw_data[7]
        
        # Log packet details
        timestamp = datetime.datetime.now()
        print(f"\n[{timestamp}] Modbus Packet:")
        print(f"Transaction ID: {transaction_id}")
        print(f"Function Code: {function_code}")
        print(f"Unit ID: {unit_id}")
        
        # Decode common function codes
        if function_code == 1:
            print("Read Coils")
        elif function_code == 2:
            print("Read Discrete Inputs") 
        elif function_code == 3:
            print("Read Holding Registers")
        elif function_code == 4:
            print("Read Input Registers")
        elif function_code == 5:
            print("Write Single Coil")
        elif function_code == 6:
            print("Write Single Register")
            
        # Print data payload in hex
        data = raw_data[8:]
        print(f"Data Payload: {data.hex()}")
        
    except Exception as e:
        print(f"Error parsing packet: {e}")

def start_modbus_sniffer(interface="eth0"):
    """Start sniffing for Modbus TCP packets on specified interface"""
    print(f"Starting Modbus TCP traffic monitor on {interface}")
    print("Listening for packets...\n")
    
    # Filter for TCP port 5002 (standard Modbus TCP)
    sniff(iface=interface,
          filter="port 5002",
          prn=decode_modbus_packet,
          store=0)

if __name__ == "__main__":
    # Specify your network interface
    INTERFACE = "CPN-eth0"  
    start_modbus_sniffer(INTERFACE)