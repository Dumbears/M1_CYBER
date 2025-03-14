# 🌞 Effectuer un scan ARP depuis la machine attaquante node1.tp1.my

sudo tcpdump -i eth0 arp -w nmap_1.pcap
sudo nmap -sn -PR 10.1.1.0/24

🦈 Capture ARP Scan --> [nmap_1.pcap](nmap_1.pcap)



# 🌞 Effectuer un scan de service et d'OS depuis la machine attaquante node1.tp1.my
```bash
sudo nmap -sS -sV -O -p 22,67 10.1.1.10
sudo tcpdump -i eth0 host 10.1.1.10 and src host node1.tp1.my -w nmap_2.pcap
```

```bash
[administrateur@node1 ~]$ sudo nmap -sS -sV -O -p 22,67 10.1.1.10
Starting Nmap 7.92 ( https://nmap.org ) at 2025-02-11 10:23 EST
Nmap scan report for 10.1.1.10
Host is up (0.0012s latency).

PORT   STATE    SERVICE VERSION
22/tcp open     ssh     OpenSSH 8.7 (protocol 2.0)
67/tcp filtered dhcps
MAC Address: 00:15:5D:01:01:03 (Microsoft)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 2.6.32 (93%), Linux 3.10 - 4.11 (93%), Linux 3.2 - 4.9 (93%), Linux 3.4 - 3.10 (93%), Linux 4.15 - 5.6 (93%), Linux 5.0 - 5.4 (93%), Linux 2.6.32 - 3.10 (93%), Linux 2.6.32 - 3.13 (93%), Linux 3.10 (92%), Linux 5.0 - 5.3 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.20 seconds
```  
🦈 Capture Service Scan --> [nmap_2.pcap](nmap_2.pcap)