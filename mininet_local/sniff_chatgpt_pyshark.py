import pyshark

def process_packet(packet):
    # Ensure the packet has necessary layers
    if 'IP' in packet and 'TCP' in packet:
        ip_src = packet.ip.src
        ip_dst = packet.ip.dst
        tcp_sport = packet.tcp.srcport
        tcp_dport = packet.tcp.dstport

        print(f"[+] TCP Packet: {ip_src}:{tcp_sport} -> {ip_dst}:{tcp_dport}")

# Capture TCP packets on the specified interface (default: 'eth0')
interface = "Ethernet 11"  # Change to your network interface, e.g., 'wlan0', 'lo'
interface = "Wi Fi"  # Change to your network interface, e.g., 'wlan0', 'lo'

print("Starting TCP packet capture...")
try:
    capture = pyshark.LiveCapture(interface=interface, bpf_filter='tcp')
    for packet in capture:
        process_packet(packet)
except PermissionError:
    print("[!] Permission denied: Please run the script as root.")
except Exception as e:
    print(f"[!] An error occurred: {e}")