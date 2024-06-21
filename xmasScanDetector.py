from scapy.all import *

def processPacket(packet):
	if packet['TCP'].flags ==  'FPU':
		print("Xmas Scan on Port ",packet['TCP'].dport)

sniff(iface="eth0", count = 1000, filter="tcp", store=0, prn = processPacket)
