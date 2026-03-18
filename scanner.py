import threading
from scapy.all import IP, TCP, sr1

# Scan a single port
def scan_port(ip, port):
    packet = IP(dst=ip)/TCP(dport=port, flags="S")
    response = sr1(packet, timeout=1, verbose=0)

    if response and response.haslayer(TCP):
        if response[TCP].flags == 18:  # SYN-ACK → OPEN
            print(f"   [OPEN] Port {port}")


# Scan multiple ports using threads
def scan_ports(ip, ports):
    print(f"\n[+] Scanning ports for {ip}...")

    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
