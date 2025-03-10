import pyshark

# Define the interface you want to sniff on
interface = 'CPN-eth0'  # Replace with your network interface

# Create a live capture object
capture = pyshark.LiveCapture(interface=interface)

# Start capturing packets
print("Starting packet capture on interface:", interface)
for packet in capture.sniff_continuously():
    try:
        # Check if the packet has an IP layer
        if 'IP' in packet:
            src_ip = packet.ip.src
            dst_ip = packet.ip.dst
            print(f"Source IP: {src_ip:15s} -> Destination IP: {dst_ip:15s}")
    except AttributeError:
        # Handle packets that do not have an IP layer
        continue