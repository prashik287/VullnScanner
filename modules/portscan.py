import subprocess
import socket
from datetime import datetime
import threading
import ipaddress

class PortScanner:
    def __init__(self):
        subprocess.run('clear', shell=True)

    @staticmethod
    def banner_grab(ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                sock.connect((ip, port))
                sock.send(b"HEAD / HTTP/1.1\r\n\r\n")
                banner = sock.recv(1024).decode("utf-8", errors="ignore").strip()
                b1 = banner.split("\n")[0]

                if "-" in b1:
                    return b1.split('-')[2]
                else:
                    return b1
        except Exception as e:
            return ""

    def scan_port(self, ip, port, open_ports):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                banner = self.banner_grab(ip, port)
                open_ports.append((port, banner))

    def scan_ports(self, target, start_port=1, end_port=30):
        open_ports = []
        threads = []
        
        # Parse the target to get network address and subnet mask
        try:
            network = ipaddress.IPv4Network(target, strict=False)
        except ValueError as e:
            return f"Invalid target: {e}"

        # Iterate over all hosts in the network except network and broadcast addresses
        for ip in network.hosts():
            ip_str = str(ip)
            for port in range(start_port, end_port + 1):
                t = threading.Thread(target=self.scan_port, args=(ip_str, port, open_ports))
                threads.append(t)
                t.start()
        
        for t in threads:
            t.join()

        return open_ports

    def main(self, target):
        print("\n" + "-" * 50)
        print("Scanning Target : " + target)
        print("Scanning started at : " + str(datetime.now()))
        print('-' * 50)

        open_ports = self.scan_ports(target)

        if open_ports:
            result = "Open Ports:\n"
            for port, banner in open_ports:
                result += f"{port}    {banner}\n"
            return result
        else:
            return "No open Ports found"