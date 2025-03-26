```bash
[administrateur@node1 ~]$ systemctl status sshd
● sshd.service - OpenSSH server daemon
   Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; preset: ena>
   Active: active (running) since Tue 2025-03-25 04:10:53 EDT; 2h 44min ago
     Docs: man:sshd(8)
           man:sshd_config(5)
 Main PID: 878 (sshd)
   Tasks: 1 (limit: 2110)
   Memory: 148.0K
   CPU: 8ms
   CGroup: /system.slice/sshd.service
           └─878 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"

Mar 25 04:10:53 node1.tpl.my systemd[1]: Starting OpenSSH server daemon...
Mar 25 04:10:53 node1.tpl.my sshd[878]: Server listening on 0.0.0.0 port 22.
Mar 25 04:10:53 node1.tpl.my sshd[878]: Server listening on :: port 22.
Mar 25 04:10:53 node1.tpl.my systemd[1]: Started OpenSSH server daemon.
```