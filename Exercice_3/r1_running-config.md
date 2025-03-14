Building configuration...

Current configuration : 1435 bytes
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
 ip nat outside
 duplex full
!
interface FastEthernet0/0.10
 encapsulation dot1Q 10
 ip address 10.3.10.252 255.255.255.0
 ip helper-address 10.3.30.251
 standby 10 ip 10.3.10.254
 standby 10 priority 150
 standby 10 preempt
!
interface FastEthernet0/0.20
 encapsulation dot1Q 20
 ip address 10.3.20.252 255.255.255.0
 ip helper-address 10.3.30.251
 standby 20 ip 10.3.20.254
 standby 20 priority 150
 standby 20 preempt
!
interface FastEthernet0/0.30
 encapsulation dot1Q 30
 ip address 10.3.30.252 255.255.255.0
 standby 30 ip 10.3.30.254
 standby 30 preempt
!
interface FastEthernet1/0
 ip address 10.99.99.50 255.255.255.0
 ip nat inside
 duplex full
!
interface FastEthernet2/0
 no ip address
 shutdown
 duplex full
!
ip nat inside source list 1 interface FastEthernet0/0 overload
ip forward-protocol nd
!
!
no ip http server
no ip http secure-server
ip route 0.0.0.0 0.0.0.0 10.99.99.1
!
access-list 1 permit 10.3.10.0 0.0.0.255
access-list 1 permit 10.3.20.0 0.0.0.255
access-list 1 permit 10.3.30.0 0.0.0.255
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