```bash
[administrateur@node1 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:01:01:01 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.100/24 brd 10.1.1.255 scope global dynamic noprefixroute eth0
       valid_lft 86390sec preferred_lft 86390sec
    inet6 fe80::215:5dff:fe01:101/64 scope link 
       valid_lft forever preferred_lft forever
