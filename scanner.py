import nmap

def scan__target(ip):
    scanner = nmap.PortScanner()
    scanner.scan(ip, arguments='-sV')
    for host in scanner.all_hosts():
        print(f"Host: {host}")
        for proto in scanner[host].all_hosts():
            lport = scanner[host][proto].keys()
            for port in sorted(lport):
                for port in sorted(lport):
                    print(f"post: {port} | State: {scanner[host][proto]['state']}  | Service:  {scanner[host][proto][port]['name']}")
