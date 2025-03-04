# 🌞 Ajouter des ACL sur le routeur

ip access-list extended BLOCK_ADMIN
deny ip any 10.2.30.0 0.0.0.255
permit ip any any

interface FastEthernet0/0
ip access-group BLOCK_ADMIN in

# 🌞 Activer le DAI sur les switches

arp 10.2.10.1 00:50:79:66:68:05 ARPA
arp 10.2.10.2 00:50:79:66:68:07 ARPA
arp 10.2.10.254 ca01.0c18.0000 ARPA

arp 10.2.20.1 00:50:79:66:68:06 ARPA
arp 10.2.20.2 00:50:79:66:68:08 ARPA
arp 10.2.20.254 ca01.0c18.0000 ARPA

arp 10.2.30.1 00:50:79:66:68:09 ARPA
arp 10.2.30.254 ca01.0c18.0000 ARPA


ip arp inspection vlan 10
ip arp inspection vlan 20
ip arp inspection vlan 30


ip arp inspection trust


access1
interface Ethernet0/0
ip arp inspection trust
interface Ethernet0/1
ip arp inspection untrust
interface Ethernet0/2
ip arp inspection untrust

access2
interface Ethernet0/0
ip arp inspection trust
interface Ethernet0/1
ip arp inspection untrust
interface Ethernet0/2
ip arp inspection untrust
interface Ethernet0/3
ip arp inspection untrust

core1
interface Ethernet0/0
ip arp inspection trust
interface Ethernet0/1
ip arp inspection trust
interface Ethernet0/2
ip arp inspection trust