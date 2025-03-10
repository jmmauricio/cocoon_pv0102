from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())
    

# Capture 10 packets on all interfaces
sniff(prn=packet_callback, count=1000)