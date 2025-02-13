capture DHCP
sudo tcpdump -w dhcp_1.pcap
SFTP de la VM à mon PC, puis extraction des 4 lignes

Afficher le bail DHCP serveur

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