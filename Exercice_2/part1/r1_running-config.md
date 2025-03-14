```bash
r1#show running-config
Building configuration...

Current configuration : 1241 bytes
!
! Last configuration change at 15:07:20 UTC Mon Mar 3 2025
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
!
hostname r1
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
ip cef
no ipv6 cef
!
!
multilink bundle-name authenticated
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
!
!
!
!
!
!
interface FastEthernet0/0
 no ip address
 duplex full
!
interface FastEthernet0/0.10
 encapsulation dot1Q 10
 ip address 10.2.10.254 255.255.255.0
 ip nat inside
!
interface FastEthernet0/0.20
 encapsulation dot1Q 20
 ip address 10.2.20.254 255.255.255.0
 ip nat inside
!
interface FastEthernet0/0.30
 encapsulation dot1Q 30
 ip address 10.2.30.254 255.255.255.0
 ip nat inside
!
interface FastEthernet1/0
 ip address 10.99.99.50 255.255.255.0
 ip nat outside
 duplex full
!
interface FastEthernet2/0
 no ip address
 shutdown
 duplex full
!
interface FastEthernet3/0
 no ip address
 shutdown
 duplex full
!
ip nat inside source list 1 interface FastEthernet1/0 overload
ip forward-protocol nd
!
!
no ip http server
no ip http secure-server
ip route 0.0.0.0 0.0.0.0 10.99.99.1
!
access-list 1 permit any
!
!
!
control-plane
!
!
line con 0
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 login
!
!
end
```