
# 🌞 Config réseau  

La machine linux est branchée à un switch d'accès dans le VLAN30

Elle porte l'adresse [IP 10.3.30.100](ip_machine_linux.md)

Branchée sur le switch d'accès (sw7) port e0/3
```bash
interface Ethernet0/3
 no shutdown
 switchport access vlan 30
 switchport mode access
 ```  

# 🌞 Serveur SSH

Status du [serveur SSH + écoute port 22](sshd_status.md)  
Status du [firewall + SSH ouvert](firewall_status.md)  

# 🌞 Connexion SSH
Test de connexion  
```bash
ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -oPubkeyAcceptedAlgorithms=+ssh-rsa -oHostkeyAlgorithms=+ssh-rsa -oCiphers=+aes256-cbc -oMACs=hmac-sha1 -i "C:\Users\rgebel\OneDrive - Andqo\Bureau\Cours Master\Cybersécurtié\tp4\private_ssh" romain@10.3.10.100
```  

Logs sur r1  
```bash
r1>
*Mar 24 14:37:43.323: %SSH-5-SSH2_CLOSE: SSH2 Session from 10.3.10.15 (tty = 0) for user 'romain' using crypto cipher 'aes256-cbc', hmac 'hmac-sha1' closed
*Mar 24 14:37:51.343: %SSH-5-SSH2_SESSION: SSH2 Session request from 10.3.10.15 (tty = 0) using crypto cipher 'aes256-cbc', hmac 'hmac-sha1' Succeeded
*Mar 24 14:37:57.603: %SSH-5-SSH2_USERAUTH: User 'romain' authentication for SSH2 Session from 10.3.10.15 (tty = 0) using crypto cipher 'aes256-cbc', hmac 'hmac-sha1' Succeeded
```  

# 🌞 Fichier SSH config
```bash
Host bastion
  Hostname 10.3.30.100
  User administrateur
  IdentityFile "C:\Users\rgebel\OneDrive - pomme\Bureau\Cours Master\Cybersécurtié\tp4\private_ssh"
  IdentitiesOnly yes
```  

# 🌞 Proof !
```bash
PS C:\Users\rgebel> ssh bastion
Activate the web console with: systemctl enable --now cockpit.socket

Last login: Tue Mar 25 08:40:38 2025 from 10.3.30.15
[administrateur@node1 ~]$
```

# 🌞 Mettre à jour la clé publique déposées sur les routeurs

no username test

# 🌞 Se connecter aux routeurs avec un rebond sur le bastion

```bash
ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -oPubkeyAcceptedAlgorithms=+ssh-rsa -oHostkeyAlgorithms=+ssh-rsa -oCiphers=+aes256-cbc -oMACs=hmac-sha1 -J bastion administrateur@10.3.30.254
r1>
```  

# 🌞 Modifier votre fichier SSH config
Configuration du [.ssh modifiée](conf_connexion_ssh_maj.md) 