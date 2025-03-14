Building configuration...

Current configuration : 1125 bytes
!
! Last configuration change at 17:43:47 UTC Tue Mar 11 2025
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
!
hostname dhcp
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
ip dhcp pool VLAN10
 network 10.3.10.0 255.255.255.0
 default-router 10.3.10.1 
 dns-server 8.8.8.8 
!
ip dhcp pool VLAN20
 network 10.3.20.0 255.255.255.0
 default-router 10.3.20.1 
 dns-server 8.8.8.8 
!
ip dhcp pool VLAN30
 network 10.3.30.0 255.255.255.0
 default-router 10.3.30.251 
 dns-server 8.8.8.8 
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
 ip address 10.3.30.251 255.255.255.0
 duplex full
!
interface FastEthernet1/0
 no ip address
 shutdown
 duplex full
!
interface FastEthernet2/0
 no ip address
 shutdown
 duplex full
!
ip forward-protocol nd
!
!
no ip http server
no ip http secure-server
ip route 10.3.10.0 255.255.255.0 10.3.30.254
ip route 10.3.20.0 255.255.255.0 10.3.30.254
!
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