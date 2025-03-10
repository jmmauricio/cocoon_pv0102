from scapy.all import sniff, IP, TCP, UDP, DNS, ARP, Raw  # Added Raw import
from datetime import datetime
import sys

def analyze_packet(packet):
    """Analyze and decode network packet information"""
    timestamp = datetime.now()
    print(f"\n[{timestamp}] New Packet:")

    # ARP Analysis
    if packet.haslayer(ARP):
        print(f"ARP:")
        print(f"  Source MAC: {packet[ARP].hwsrc}")
        print(f"  Dest MAC: {packet[ARP].hwdst}")
        print(f"  Source IP: {packet[ARP].psrc}")
        print(f"  Dest IP: {packet[ARP].pdst}")
        return

    # IP Layer Analysis
    if packet.haslayer(IP):
        print(f"IP:")
        print(f"  Source: {packet[IP].src}")
        print(f"  Destination: {packet[IP].dst}")
        print(f"  Protocol: {packet[IP].proto}")
        
        # TCP Analysis
        if packet.haslayer(TCP):
            print(f"TCP:")
            print(f"  Source Port: {packet[TCP].sport}")
            print(f"  Dest Port: {packet[TCP].dport}")
            print(f"  Flags: {packet[TCP].flags}")
            
            # HTTP Detection
            if packet[TCP].dport == 80 or packet[TCP].sport == 80:
                print("  Service: HTTP")
            # HTTPS Detection    
            elif packet[TCP].dport == 443 or packet[TCP].sport == 443:
                print("  Service: HTTPS")
            # FTP Detection
            elif packet[TCP].dport == 21 or packet[TCP].sport == 21:
                print("  Service: FTP")
            # HTTPS Detection    
            elif packet[TCP].dport == 5002 or packet[TCP].sport == 5002:
                print("  Service: MODBUS")

        # UDP Analysis
        elif packet.haslayer(UDP):
            print(f"UDP:")
            print(f"  Source Port: {packet[UDP].sport}")
            print(f"  Dest Port: {packet[UDP].dport}")
            
            # DNS Analysis
            if packet.haslayer(DNS):
                print(f"DNS:")
                if packet[DNS].qr == 0:  # Query
                    print(f"  Query: {packet[DNS].qd.qname.decode()}")
                else:  # Response
                    print("  Response: ", end="")
                    if packet[DNS].an:
                        print(packet[DNS].an.rdata)
            
        # Payload Analysis
        if packet.haslayer(Raw):
            print(f"Payload (hex):")
            print(f"  {packet[Raw].load.hex()}")

def start_sniffer(interface="eth0"):
    """Start capturing all network traffic on specified interface"""
    print(f"Starting network traffic monitor on {interface}")
    print("Press CTRL+C to stop...")
    
    try:
        # Sniff packets without storing them (store=0)
        sniff(iface=interface,
              prn=analyze_packet,
              store=0)
    except KeyboardInterrupt:
        print("\nStopping packet capture...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Use command line argument for interface if provided
    interface = sys.argv[1] if len(sys.argv) > 1 else "CPN-eth0"
    start_sniffer(interface)