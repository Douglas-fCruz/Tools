
from scapy.all import *
import sys

conf.verb = 0

target = sys.argv[1]
ports = [int(port) for port in sys.argv[2:]]

pIP = IP(dst=target)
pTCP = TCP(dport=ports, flags="S")

response, noresponse = sr(pIP/pTCP)

for resp in response:
    porta = resp[1][TCP].sport
    flag = resp[1][TCP].flags

    if flag == "SA":
        print(f"[+] PORTA {porta} ABERTA")
    elif flag == "RA":
        print(f"[-] PORTA {porta} FECHADA")