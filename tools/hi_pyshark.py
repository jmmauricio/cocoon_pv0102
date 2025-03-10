# import pyshark

# def packet_callback(packet):
#     # Print basic packet information
#     print(f"Packet: {packet}")

#     # Check if the packet has an IP layer
#     if 'IP' in packet:
#         print(f"Source IP: {packet.ip.src} -> Destination IP: {packet.ip.dst}")

#     # Check if the packet has a TCP layer
#     if 'TCP' in packet:
#         print(f"TCP Source Port: {packet.tcp.srcport} -> TCP Destination Port: {packet.tcp.dstport}")

#     # Check if the packet has a UDP layer
#     if 'UDP' in packet:
#         print(f"UDP Source Port: {packet.udp.srcport} -> UDP Destination Port: {packet.udp.dstport}")

#     print("-" * 50)

# # Start capturing packets
# capture = pyshark.LiveCapture(interface='Ethernet 11')  # Replace 'eth0' with your network interface
# capture.apply_on_packets(packet_callback, packet_count=10)  # Capture 10 packets

# import pyshark

# def monitor_traffic(interface="eth0"):
#     capture = pyshark.LiveCapture(interface=interface)
#     print(f"Listening on {interface}... Press Ctrl+C to stop.")
#     for packet in capture.sniff_continuously():
#         try:
#             print(f"Packet: {packet}")
#             if hasattr(packet, 'ip'):
#                 print(f"Source: {packet.ip.src} -> Destination: {packet.ip.dst}")
#         except AttributeError:
#             pass  # Handle packets without IP layer

# # Specify your interface (e.g., wlan0, eth0)
# monitor_traffic(interface="Ethernet 11")



import pyshark

def modbus_packet_callback(packet):
    # Check if the packet has a Modbus layer
    if 'MODBUS' in packet:
        print(f"Modbus Packet: {packet.modbus}")

        # Extract Modbus TCP-specific fields
        if 'TCP' in packet:
            print(f"Source IP: {packet.ip.src} -> Destination IP: {packet.ip.dst}")
            print(f"Source Port: {packet.tcp.srcport} -> Destination Port: {packet.tcp.dstport}")

        # Extract Modbus function code
        if hasattr(packet.modbus, 'func_code'):
            func_code = int(packet.modbus.func_code)
            print(f"Modbus Function Code: {func_code}")

            # Common Modbus function codes
            if func_code == 3:
                print("Function: Read Holding Registers")
            elif func_code == 6:
                print("Function: Write Single Register")
            elif func_code == 16:
                print("Function: Write Multiple Registers")
            else:
                print(f"Unknown Function Code: {func_code}")

        # Extract additional Modbus fields (e.g., transaction ID, unit ID)
        if hasattr(packet.modbus, 'trans_id'):
            print(f"Transaction ID: {packet.modbus.trans_id}")
        if hasattr(packet.modbus, 'unit_id'):
            print(f"Unit ID: {packet.modbus.unit_id}")

        print("-" * 50)

# Start capturing Modbus TCP traffic on port 502
capture = pyshark.LiveCapture(interface='Ethernet 11', display_filter='tcp.port == 5002')  # Replace 'eth0' with your interface
capture.apply_on_packets(modbus_packet_callback, packet_count=10)  # Capture 10 Modbus packets