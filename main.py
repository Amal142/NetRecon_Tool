from network_discovery import arp_scan, is_alive
from scanner import scan_ports

def main():
    print("===================================")
    print("      🔍 NetRecon Tool")
    print("  Mini Network Scanner (Scapy)")
    print("===================================")

    target_range = input("\nEnter IP range (e.g. 192.168.1.1/24): ")

    # Step 1: Discover devices
    clients = arp_scan(target_range)

    if not clients:
        print("No devices found.")
        return

    print("\nAvailable devices:")
    print("IP\t\t\tMAC")
    print("-------------------------------------------")
    for client in clients:
        print(f"{client['ip']}\t{client['mac']}")

    # Common ports
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443]

    # Step 2 & 3: Alive check + Port scan
    for client in clients:
        ip = client['ip']

        print(f"\n[+] Checking if {ip} is alive...")
        if is_alive(ip):
            print(f"   {ip} is ACTIVE")
            scan_ports(ip, common_ports)
        else:
            print(f"   {ip} is not responding")


if __name__ == "__main__":
    main()
