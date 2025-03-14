# 🌞 show-run sur tous les équipements Cisco
[DHCP](./dhcp_running-config.md)  
[R1](./r1_running-config.md)  
[R2](./r2_running-config.md)  
[sw1](./sw1_running-config.md)  
[sw2](./sw2_running-config.md)  
[sw3](./sw3_running-config.md)  
[sw4](./sw4_running-config.md)  
[sw5](./sw5_running-config.md)  
[sw6](./sw6_running-config.md)  
[sw7](./sw7_running-config.md)  



# 🌞 Serveur DHCP, si c'est un serveur dédié
N'ayant pas réussi ) intégré le serveur DHCP en suivant le tuto, J'ai ajouté un 3ème routeur avec seulement la fonction DHCP  
Il est branché au switch d'accès 7 (sw7)  

# 🌞 Depuis pc4.tp3.my  
```bash
VPCS> ip dhcp
DORA IP 10.3.10.1/24 GW 10.3.10.254

VPCS> ping 10.3.30.11

84 bytes from 10.3.30.11 icmp_seq=1 ttl=63 time=21.444 ms
84 bytes from 10.3.30.11 icmp_seq=2 ttl=63 time=21.009 ms
84 bytes from 10.3.30.11 icmp_seq=3 ttl=63 time=14.282 ms
84 bytes from 10.3.30.11 icmp_seq=4 ttl=63 time=16.966 ms
84 bytes from 10.3.30.11 icmp_seq=5 ttl=63 time=13.317 ms

VPCS> ping ynov.com
Cannot resolve ynov.com
```  

Pas réussi.  
J'ai fait un [tcpdump](./debug_ping_ynov.com.pcap) sur mon R1. Il voit bien les paquets passer mais "no response found". Comme si il ne savait pas où renvoyer.  
J'ai pourtant mis une ip route sur R1 et R2...  
```bash
ip route 0.0.0.0 0.0.0.0 10.99.99.1
```  

# 🌞 Depuis pc2.tp3.my  
```bash
VPCS> ip dhcp
DDORA IP 10.3.20.1/24 GW 10.3.20.254

VPCS> ping 10.3.30.11

84 bytes from 10.3.30.11 icmp_seq=1 ttl=63 time=30.273 ms
84 bytes from 10.3.30.11 icmp_seq=2 ttl=63 time=12.891 ms
84 bytes from 10.3.30.11 icmp_seq=3 ttl=63 time=14.885 ms
84 bytes from 10.3.30.11 icmp_seq=4 ttl=63 time=13.639 ms
84 bytes from 10.3.30.11 icmp_seq=5 ttl=63 time=13.879 ms

VPCS> ping ynov.com
Cannot resolve ynov.com
```  
Même problème que pour pc4.tp3.my  

# 🌞 Vérifier, à l'aide de commandes dédiées

Etat de l'agrégation LACP entre sw1 et sw2  
```bash
sw1#show etherchannel 1 detail        
Group state = L2 
Ports: 2   Maxports = 4
Port-channels: 1 Max Port-channels = 1
Protocol:    -
Minimum Links: 0


                Ports in the group:
                -------------------
Port: Et0/1
------------

Port state    = Up Mstr In-Bndl 
Channel group = 1           Mode = On              Gcchange = -
Port-channel  = Po1         GC   =   -             Pseudo port-channel = Po1
Port index    = 0           Load = 0x00            Protocol =    -

Age of the port in the current state: 0d:02h:12m:08s

Port: Et0/2
------------

Port state    = Up Mstr In-Bndl 


sw2#show etherchannel 1 detail
Group state = L2 
Ports: 2   Maxports = 4
Port-channels: 1 Max Port-channels = 1
Protocol:    -
Minimum Links: 0


                Ports in the group:
                -------------------
Port: Et0/1
------------

Port state    = Up Mstr In-Bndl 
Channel group = 1           Mode = On              Gcchange = -
Port-channel  = Po1         GC   =   -             Pseudo port-channel = Po1
Port index    = 0           Load = 0x00            Protocol =    -

Age of the port in the current state: 0d:02h:13m:14s

Port: Et0/2
------------

Port state    = Up Mstr In-Bndl 


Etat de la liaison HSRP entre r1 et r2

r1#show standby
FastEthernet0/0.10 - Group 10
  State is Active
    2 state changes, last state change 02:13:08
  Virtual IP address is 10.3.10.254
  Active virtual MAC address is 0000.0c07.ac0a (MAC In Use)
    Local virtual MAC address is 0000.0c07.ac0a (v1 default)
  Hello time 3 sec, hold time 10 sec
    Next hello sent in 0.416 secs
  Preemption enabled
  Active router is local
  Standby router is unknown
  Priority 150 (configured 150)
  Group name is "hsrp-Fa0/0.10-10" (default)
FastEthernet0/0.20 - Group 20
  State is Active
    2 state changes, last state change 02:13:10
  Virtual IP address is 10.3.20.254
  Active virtual MAC address is 0000.0c07.ac14 (MAC In Use)
    Local virtual MAC address is 0000.0c07.ac14 (v1 default)
  Hello time 3 sec, hold time 10 sec
    Next hello sent in 2.176 secs
  Preemption enabled
  Active router is local
  Standby router is unknown
  Priority 150 (configured 150)
  Group name is "hsrp-Fa0/0.20-20" (default)
FastEthernet0/0.30 - Group 30
  State is Active
    2 state changes, last state change 02:13:07
  Virtual IP address is 10.3.30.254
  Active virtual MAC address is 0000.0c07.ac1e (MAC In Use)
    Local virtual MAC address is 0000.0c07.ac1e (v1 default)
  Hello time 3 sec, hold time 10 sec
    Next hello sent in 2.416 secs
  Preemption enabled
  Active router is local
  Standby router is unknown
  Priority 100 (default 100)
  Group name is "hsrp-Fa0/0.30-30" (default)
```

r2  
```bash
r2#show standby
FastEthernet0/0.10 - Group 10
  State is Active
    2 state changes, last state change 02:14:07
  Virtual IP address is 10.3.10.254
  Active virtual MAC address is 0000.0c07.ac0a (MAC In Use)
    Local virtual MAC address is 0000.0c07.ac0a (v1 default)
  Hello time 3 sec, hold time 10 sec
    Next hello sent in 2.864 secs
  Preemption disabled
  Active router is local
  Standby router is unknown
  Priority 10 (configured 10)
  Group name is "hsrp-Fa0/0.10-10" (default)
FastEthernet0/0.20 - Group 20
  State is Active
    2 state changes, last state change 02:14:07
  Virtual IP address is 10.3.20.254
  Active virtual MAC address is 0000.0c07.ac14 (MAC In Use)
    Local virtual MAC address is 0000.0c07.ac14 (v1 default)
  Hello time 3 sec, hold time 10 sec
    Next hello sent in 2.304 secs
  Preemption disabled
  Active router is local
  Standby router is unknown
  Priority 100 (default 100)
  Group name is "hsrp-Fa0/0.20-20" (default)
FastEthernet0/0.30 - Group 30
  State is Active
    2 state changes, last state change 02:14:06
  Virtual IP address is 10.3.30.254
  Active virtual MAC address is 0000.0c07.ac1e (MAC In Use)
    Local virtual MAC address is 0000.0c07.ac1e (v1 default)
  Hello time 3 sec, hold time 10 sec
    Next hello sent in 1.696 secs
  Preemption disabled
  Active router is local
  Standby router is unknown
  Priority 150 (configured 150)
  Group name is "hsrp-Fa0/0.30-30" (default)
```

Etat de STP, par VLAN  
Core  
sw1  
```bash
sw1#show spanning-tree summary
Switch is in pvst mode
Root bridge for: VLAN0001, VLAN0010, VLAN0020, VLAN0030
Extended system ID                      is enabled
Portfast Default                        is disabled
Portfast Edge BPDU Guard Default        is disabled
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
VLAN0001                     0         0        0          3          3
VLAN0010                     0         0        0          4          4
VLAN0020                     0         0        0          4          4
VLAN0030                     0         0        0          4          4
---------------------- -------- --------- -------- ---------- ----------
4 vlans                      0         0        0         15         15
```


Distribution  
```bash
sw3#show spanning-tree summary
Switch is in pvst mode
Root bridge for: VLAN0001
Extended system ID                      is enabled
Portfast Default                        is disabled
Portfast Edge BPDU Guard Default        is disabled
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
VLAN0001                     0         0        0          3          3
VLAN0010                     1         0        0          4          5
VLAN0020                     1         0        0          4          5
VLAN0030                     1         0        0          4          5
---------------------- -------- --------- -------- ---------- ----------
4 vlans                      3         0        0         15         18
```

Access  
```bash
sw5#show spanning-tree summary
Switch is in pvst mode
Root bridge for: none
Extended system ID                      is enabled
Portfast Default                        is disabled
Portfast Edge BPDU Guard Default        is disabled
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
VLAN0010                     1         0        0          2          3
VLAN0020                     1         0        0          2          3
VLAN0030                     1         0        0          1          2
---------------------- -------- --------- -------- ---------- ----------
3 vlans                      3         0        0          5          8
```


# 🌞 Couper le routeur prioritaire
Etant donné que mon ping depuis un vpcs ne fonctionne pas vers l'extérieur, je ping l'ip virtuelle. Si le R1 ou R2 coupent, l'autre prendra le relais. Ca revient au même que ping l'extérieur.  

Qué pasa ?  
Ping 10.3.30.254 depuis vpcs5  
J'ai coupé le R1  
4 requêtes sont perdues  
R2 broadcast sa mac = 10.3.30.254 via ARP  
vpcs5 arrivent à reping 10.3.30.254  


# 🌞 Couper un switch crucial dans la topo STP