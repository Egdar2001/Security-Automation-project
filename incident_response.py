import psutil
import time

def monitor_ports():
    print("[*] Monitoring suspicious ports (e.g., 4444, 5555)...")
    suspicious_ports = [4444, 5555]
    for _ in range(5):  # Run for a few seconds
        connections = psutil.net_connections()
        for conn in connections:
            if conn.laddr.port in suspicious_ports:
                print(f"[!] Suspicious port {conn.laddr.port} open by PID {conn.pid}")
        time.sleep(2)
