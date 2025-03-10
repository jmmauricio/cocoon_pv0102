from scapy.all import sniff, IP, TCP

def process_packet(packet):
    # Check if the packet has a TCP layer
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        tcp_sport = packet[TCP].sport
        tcp_dport = packet[TCP].dport

        print(f"[+] TCP Packet: {ip_src}:{tcp_sport} -> {ip_dst}:{tcp_dport}")

# Capture TCP packets on the specified interface (default: 'eth0')
interface = "CPN-eth0"  # Change to your network interface, e.g., 'wlan0', 'lo'
interface = "Ethernet 11"

print("Starting TCP packet capture...")
try:
    sniff(iface=interface, filter="tcp", prn=process_packet, store=False)
except PermissionError:
    print("[!] Permission denied: Please run the script as root.")
except Exception as e:
    print(f"[!] An error occurred: {e}")
