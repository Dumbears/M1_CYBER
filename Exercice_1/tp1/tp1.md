# 🌞 Ping !
ping 10.1.1.253  
ping 10.1.1.100  
ping 10.1.1.101  



# 🌞 Nommez les machines
sudo hostnamectl set-hostname dhcp.tp1.my  
sudo hostnamectl set-hostname node1.tp1.my  
sudo hostnamectl set-hostname node2.tp1.my  

# 🌞 Fermer tous les ports inutilement ouverts dans le firewall
sudo firewall-cmd --permanent --remove-service dhcpv6-client  
sudo firewall-cmd --permanent --remove-service cockpit  
sudo firewall-cmd --reload  

# 🌞 Remplir le fichier hosts
127.0.0.1   localhost  
::1         localhost  
10.1.1.253  dhcp.tp1.my  
10.1.1.100  node1.tp1.my  
10.1.1.101  node2.tp1.my  
10.1.1.101  node2  

# Un ping node2.tp1.my
[administrateur@node1 ~]$ ping node2.tp1.my  
PING node2.tp1.my (10.1.1.101) 56(84) bytes of data.  
64 bytes from node2.tp1.my (10.1.1.101): icmp_seq=1 ttl=64 time=0.861 ms  
64 bytes from node2.tp1.my (10.1.1.101): icmp_seq=2 ttl=64 time=0.707 ms  
64 bytes from node2.tp1.my (10.1.1.101): icmp_seq=3 ttl=64 time=0.324 ms  
64 bytes from node2.tp1.my (10.1.1.101): icmp_seq=4 ttl=64 time=0.570 ms  

[administrateur@node1 ~]$ ping node2  
PING node2 (10.1.1.101) 56(84) bytes of data.  
64 bytes from node2.tp1.my (10.1.1.101): icmp_seq=1 ttl=64 time=0.489 ms  
64 bytes from node2.tp1.my (10.1.1.101): icmp_seq=2 ttl=64 time=0.805 ms  
64 bytes from node2.tp1.my (10.1.1.101): icmp_seq=3 ttl=64 time=1.72 ms  

🌞 Table ARP
ip neigh show  
[administrateur@node1 ~]$ ip neigh show  
10.1.1.253 dev eth0 lladdr 00:15:5d:01:01:04 DELAY   
10.1.1.101 dev eth0 lladdr 00:15:5d:01:01:05 STALE   

🌞 Manipuler la table ARP
ip neigh show  
[administrateur@node1 ~]$ ip neigh show  
10.1.1.253 dev eth0 lladdr 00:15:5d:01:01:04 DELAY  
10.1.1.101 dev eth0 lladdr 00:15:5d:01:01:05 STALE  
[administrateur@node1 ~]$ sudo ip neigh flush all  
[administrateur@node1 ~]$ ping node2.tp1.my  
PING node2.tp1.my (10.1.1.101) 56(84) bytes of data.  
64 bytes from node2.tp1.my (10.1.1.101): icmp_seq=1 ttl=64 time=0.807 ms  
64 bytes from node2.tp1.my (10.1.1.101): icmp_seq=2 ttl=64 time=0.399 ms  
64 bytes from node2.tp1.my (10.1.1.101): icmp_seq=3 ttl=64 time=1.12 ms  
64 bytes from node2.tp1.my (10.1.1.101): icmp_seq=4 ttl=64 time=3.55 ms  
