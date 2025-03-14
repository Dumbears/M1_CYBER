```bash
!
! Last configuration change at 17:43:10 UTC Tue Mar 11 2025
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname sw7
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
!
!
!
ip cef
no ipv6 cef
!
!
!
spanning-tree mode pvst
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
!
interface Ethernet0/1
 no shutdown
 switchport trunk allowed vlan 10,20,30
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/2
 no shutdown
 switchport access vlan 30
 switchport mode access
!
interface Ethernet0/3
 no shutdown
 switchport access vlan 30
 switchport mode access
!
interface Vlan10
 no shutdown
 no ip address
!
interface Vlan20
 no shutdown
 no ip address
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
```