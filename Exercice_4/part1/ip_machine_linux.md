```bash
[administrateur@node1 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:01:01:15 brd ff:ff:ff:ff:ff:ff
    inet 10.3.30.100/24 brd 10.3.30.255 scope global noprefixroute eth0
       valid_lft forever preferred_lft forever
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:01:01:18 brd ff:ff:ff:ff:ff:ff
    inet 172.17.220.255/20 brd 172.17.223.255 scope global dynamic noprefixroute eth1
       valid_lft 77201sec preferred_lft 77201sec
    inet6 fe80::bcf9:c85a:9aae:4543/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
[administrateur@node1 ~]$
```