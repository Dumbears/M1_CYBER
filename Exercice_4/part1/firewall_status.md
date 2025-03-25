```bash
[administrateur@node1 ~]$ systemctl status firewalld
● firewalld.service - firewalld - dynamic firewall daemon
     Loaded: loaded (/usr/lib/systemd/system/firewalld.service; enabled; preset: enabled)
     Active: active (running) since Tue 2025-03-25 04:10:52 EDT; 2h 52min ago
       Docs: man:firewalld(1)
   Main PID: 768 (firewalld)
      Tasks: 2 (limit: 2110)
     Memory: 624.0K
        CPU: 550ms
     CGroup: /system.slice/firewalld.service
             ├─768 /usr/bin/python3 -s /usr/sbin/firewalld --nofork --nopid

Mar 25 04:10:52 node1.tpl.my systemd[1]: Starting firewalld - dynamic firewall d...
Mar 25 04:10:52 node1.tpl.my systemd[1]: Started firewalld - dynamic firewall da...

[administrateur@node1 ~]$ firewall-cmd --list-services
cockpit dhcpv6-client ssh
[administrateur@node1 ~]$
```