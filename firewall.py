import os

def add_firewall_rule(ip):
    rule_name = f"Block_{ip.replace('.', '_')}"
    command = f'netsh advfirewall firewall add rule name="{rule_name}" dir=in interface=any action=block remoteip={ip}'
    os.system(command)
    print(f"[+] Firewall rule added to block {ip}")
