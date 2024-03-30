#netcapy
import socket
from datetime import datetime

def GetInput():
    while True:
        try:
            host = input("Enter host to scan: ")
            host = socket.gethostbyname(host)
            break
        except socket.gaierror:
            try:
                host = socket.gethostname()
            except socket.gaierror:
                pass
    return host

def GetChoiceInput():
    choice = 0
    while choice != 1 or choice != 2:
        try:
            choice = int(input("Enter a scan option: \n1.From port range to port range \n2.Scan default ports: "))
        except:
            pass
    return choice



def FindDefaultPort():
    current_date = datetime.now()
    print(f"{current_date.strftime('%H:%M:%S')} Starting scanning at {host}...\n")
    open_ports = []
    default_ports = [21,22,23,80,81,443,445,3089,8080]

    for port in default_ports:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.5)
            if client.connect_ex((host, port)):
                pass
            else:
                open_ports.append(port)
        except Exception:
            pass
    client.close()
    return open_ports

def FindPort(host, from_range, to_range):
    current_date = datetime.now()
    if from_range > to_range:
        return None
    print(f"{current_date.strftime('%H:%M:%S')} Starting scanning at {host}...\n")
    open_ports = []

    for port in range(from_range, to_range + 1):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.5)
            if client.connect_ex((host, port)):
                pass
            else:
                open_ports.append(port)
        except Exception:
            pass
    client.close()
    return open_ports


def ShowPorts(open_ports):
    current_date = datetime.now()
    if len(open_ports) > 0:
        print("****************************************")
        for open_port in open_ports:
            print(f"Open port: {open_port} on {host}")
        print("****************************************")
    else:
        print("No open ports found!")
    if len(open_ports) > 1:
        print(f"{current_date.strftime('%H:%M:%S')} Scan finished found {len(open_ports)} open ports on the server")
    elif len(open_ports) <= 1:
        print(f"{current_date.strftime('%H:%M:%S')} Scan finished found {len(open_ports)} open port on the server")

host = GetInput()
choice = GetChoiceInput()

if choice == 1:
    from_port_range = int(input("Enter a from port range: "))
    to_port_range = int(input("Enter a to port range: "))
    open_ports = FindPort(host, from_port_range, to_port_range)
    ShowPorts(open_ports)
elif choice == 2:
    open_ports = FindDefaultPort()
    ShowPorts(open_ports)
