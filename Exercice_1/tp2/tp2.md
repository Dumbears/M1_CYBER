🌞 Installer un service DHCP sur la machine dhcp.tp1.my  
```bash
dnf -y install dhcp-server
nano /etc/dhcp/dhcpd.conf

# Adresse IP du serveur DNS
option domain-name-servers	1.1.1.1;

# Duree du bail par defaut
default-lease-time 86400;

# Duree du bail maximum
max-lease-time 172800;

# this DHCP server to be declared valid
authoritative;

# Adresse reseau et masque sous-reseau
subnet 10.1.1.0 netmask 255.255.255.0 {
	# Range IP dynamique
	range dynamic-bootp 10.1.1.100 10.1.1.200;
	# Adresse de broadcast
	option broadcast-address 10.0.0.255;

systemctl enable --now dhcpd
firewall-cmd --add-service=dhcp
firewall-cmd --runtime-to-permanent
```
# 🌞 Demander une adresse IP depuis node1.tp1.my  
```bash  
sudo dhclient -v eth0
```

# Capture DHCP  
```bash
sudo tcpdump -w dhcp_1.pcap
```  
SFTP de la VM à mon PC, puis extraction des 4 lignes

🦈 Capture DHCP --> [dhcp_1.pcap](dhcp_1.pcap)


# 🌞 Afficher le bail DHCP serveur  
```bash
sudo grep -A10 "node1" /var/lib/dhcpd/dhcpd.leases
  client-hostname "node1";
}
lease 10.1.1.101 {
  starts 2 2025/02/11 14:47:46;
  ends 3 2025/02/12 14:47:46;
  cltt 2 2025/02/11 14:47:46;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 00:15:5d:01:01:05;
}
```  

