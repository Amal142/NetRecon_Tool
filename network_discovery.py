from scapy.all import ARP, Ether, srp, IP, ICMP, sr1

# ARP Scan — Discover devices
def arp_scan(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=2, verbose=0)[0]

    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    return clients


# ICMP Check — Is host alive?
def is_alive(ip):
    packet = IP(dst=ip)/ICMP()
    response = sr1(packet, timeout=1, verbose=0)

    return response is not None
