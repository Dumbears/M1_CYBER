
!
! Last configuration change at 12:10:11 UTC Tue Mar 4 2025
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname access2
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
!
!
!
!
!
ip arp inspection vlan 10,20,30
ip arp inspection filter DAI vlan  10,20,30
!
!
!
ip cef
no ipv6 cef
!
!
!
spanning-tree mode pvst
spanning-tree portfast edge bpduguard default
spanning-tree extend system-id
!
!
! 
!
!
!
!
!
!
!
!
!
!
!
!
interface Ethernet0/0
 no shutdown
 switchport trunk allowed vlan 10,20,30
 switchport trunk encapsulation dot1q
 switchport mode trunk
 ip arp inspection trust
!
interface Ethernet0/1
 no shutdown
 switchport access vlan 10
 switchport mode access
 spanning-tree bpduguard enable
!
interface Ethernet0/2
 no shutdown
 switchport access vlan 20
 switchport mode access
 spanning-tree bpduguard enable
!
interface Ethernet0/3
 no shutdown
 switchport access vlan 30
 switchport mode access
 spanning-tree bpduguard enable
!
ip forward-protocol nd
!
ip http server
!
ip ssh server algorithm encryption aes128-ctr aes192-ctr aes256-ctr
ip ssh client algorithm encryption aes128-ctr aes192-ctr aes256-ctr
!
!
!
arp access-list DAI
 permit ip host 10.2.10.1 mac host 0050.7966.6805 
 permit ip host 10.2.10.2 mac host 0050.7966.6807 
 permit ip host 10.2.10.254 mac host ca01.0c18.0000 
 permit ip host 10.2.20.1 mac host 0050.7966.6806 
 permit ip host 10.2.20.2 mac host 0050.7966.6808 
 permit ip host 10.2.20.254 mac host ca01.0c18.0000 
 permit ip host 10.2.30.1 mac host 0050.7966.6809 
 permit ip host 10.2.30.254 mac host ca01.0c18.0000 
 deny ip any mac any 
arp 10.2.10.1 0050.7966.6805 ARPA
arp 10.2.10.2 0050.7966.6807 ARPA
arp 10.2.10.254 ca01.0c18.0000 ARPA
arp 10.2.20.1 0050.7966.6806 ARPA
arp 10.2.20.2 0050.7966.6808 ARPA
arp 10.2.20.254 ca01.0c18.0000 ARPA
arp 10.2.30.1 0050.7966.6809 ARPA
arp 10.2.30.254 ca01.0c18.0000 ARPA
!
!
!
control-plane
!
!
line con 0
 logging synchronous
line aux 0
line vty 0 4
 login
!
!
!
end


