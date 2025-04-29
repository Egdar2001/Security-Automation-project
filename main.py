from scanner import scan_target
from firwall import add_firewall_rule
from incident_response import monitor_ports

def main():
    print("Security Automation Tool for Windows")

    ip = input("Enter the IP for scan: ")
    print("\n[+]Scanning for vulnerbilities...")
    scan_target(ip)

    print("\n[+] Monitoring ports for suspicious activity...")
    monitor_ports()

    block = input("\nDo you want to block an IP? (yes/no): ")
    if block.lower() == 'yes':
        ip_to_block = input("Enter the IP to block: ")
        add_firewall_rule(ip_to_block)

if __name__ == "__main__":
    main()        