#!/usr/bin/python

from scapy.all import *
import sys

conf.verb = 0

ports = [443, 8080]

pIP = IP(dst=sys.argv[1])
pTCP = TCP(dport=ports, flags="S")
pacote = pIP/pTCP
response, noresponse = sr(pacote)
for resp in response:
	porta = resp[1][TCP].sport
	flag = resp[1][TCP].flags
	if (flag == "SA"):
		print ("PORTA %d ABERTA" %(porta))
	elif (flag == "RA"):
		print ("PORTA %d FECHADA" %(porta))
