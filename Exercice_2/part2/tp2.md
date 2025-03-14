# 🌞 Ajouter des ACL sur le routeur
```bash
ip access-list extended BLOCK_ADMIN
deny ip any 10.2.30.0 0.0.0.255
permit ip any any

interface FastEthernet0/0
ip access-group BLOCK_ADMIN in
```  

# 🌞 Activer le DAI sur les switches  
Création de la table ARP  
```bash
arp 10.2.10.1 00:50:79:66:68:05 ARPA
arp 10.2.10.2 00:50:79:66:68:07 ARPA
arp 10.2.10.254 ca01.0c18.0000 ARPA

arp 10.2.20.1 00:50:79:66:68:06 ARPA
arp 10.2.20.2 00:50:79:66:68:08 ARPA
arp 10.2.20.254 ca01.0c18.0000 ARPA

arp 10.2.30.1 00:50:79:66:68:09 ARPA
arp 10.2.30.254 ca01.0c18.0000 ARPA
```

access1  
```bash
interface Ethernet0/0
ip arp inspection trust
```  

access2  
```bash
interface Ethernet0/0
ip arp inspection trust
```  

core1  
```bash
interface Ethernet0/0
ip arp inspection trust
interface Ethernet0/1
ip arp inspection trust
interface Ethernet0/2
ip arp inspection trust
```  
```bash
arp access-list DAI  
permit ip host 10.2.10.1 mac host 00:50:79:66:68:05
permit ip host 10.2.10.2 mac host 00:50:79:66:68:07
permit ip host 10.2.10.254 mac host ca01.0c18.0000
permit ip host 10.2.20.1 mac host 00:50:79:66:68:06
permit ip host 10.2.20.2 mac host 00:50:79:66:68:08
permit ip host 10.2.20.254 mac host ca01.0c18.0000
permit ip host 10.2.30.1 mac host 00:50:79:66:68:09
permit ip host 10.2.30.254 mac host ca01.0c18.0000
deny ip any mac any

ip arp inspection filter DAI vlan 10
ip arp inspection filter DAI vlan 20
ip arp inspection filter DAI vlan 30

ip arp inspection vlan 10
ip arp inspection vlan 20
ip arp inspection vlan 30
```  

# 🌞 Activer BPDUGuard sur vos switches par port sauf ceux qui sont connectés vers les autres switches

Sur access1, access2 et core1  
```bash
spanning-tree portfast edge bpduguard default
```  

access1  
```bash
interface Ethernet0/0
spanning-tree bpduguard disable
```

access2  
```bash
interface Ethernet0/0
spanning-tree bpduguard disable
```  

core1  
```bash
interface Ethernet0/0
spanning-tree bpduguard disable
exit
interface Ethernet0/1
spanning-tree bpduguard disable
exit
interface Ethernet0/2
spanning-tree bpduguard disable
```  

Exemple pour vérifier que c'est bien activé  
```bash
core1#show spanning-tree summary               
Switch is in pvst mode
Root bridge for: VLAN0001, VLAN0010, VLAN0020, VLAN0030
Extended system ID                      is enabled
Portfast Default                        is disabled
Portfast Edge BPDU Guard Default        is enabled
Portfast Edge BPDU Filter Default       is disabled
Loopguard Default                       is disabled
PVST Simulation Default                 is enabled but inactive in pvst mode
Bridge Assurance                        is enabled but inactive in pvst mode
EtherChannel misconfig guard            is enabled
Configured Pathcost method used is short
UplinkFast                              is disabled
BackboneFast                            is disabled

Name                   Blocking Listening Learning Forwarding STP Active
---------------------- -------- --------- -------- ---------- ----------
VLAN0001                     0         0        0          1          1
VLAN0010                     0         0        0          3          3
VLAN0020                     0         0        0          3          3
VLAN0030                     0         0        0          3          3
---------------------- -------- --------- -------- ---------- ----------
4 vlans                      0         0        0         10         10
```  

# 🌞 La running-config des 4 équipements réseau

Running-config [R1](./part2/r1_running-config.md)
Running-config [core1](./part2/core1_running-config.md)
Running-config [access1](./part2/access1_running-config.md)
Running-config [access2](./part2/access2_running-config.md)


🌞 Ajouter la VM à la topologie
🌞 Essayer de mener une attaque ARP poisoning
🌞 Tirer un câble entre les deux switches d'accès
🌞 Déterminer quels ports ont été fermés
🌞 Déterminer qui est le root bridge
🌞 Couper l'un des autres liens

🦈 Capture STP -->