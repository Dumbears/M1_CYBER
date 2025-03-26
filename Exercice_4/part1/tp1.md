# 🌞 Créer un utilisateur et activer serveur SSH


```bash
ip domaine-name pomme.local
crypto key generate rsa general-keys modulus 2048
ip ssh version 2
username romain privilege 15 secret Pomme33!
ip ssh pubkey-chain
username romain
key-string 
AAAAB3NzaC1yc2EAAAADAQABAAABAQC/XjCOCawcWweKbo3QmJDCaUZcyBp2eLKgW8NEJShwrRFspR6//OGZCju7TfKDYMjpNJy1jpn2nE1mKszNjAgv6xqO0Zx4V/596+LJKEm91HCXX9Q9O8qNCx5yPzXUOdguKIknWrj3m4D9wNxC8eazmTZJKqFdy24APVI7L7rd7le8eqDNdyVTClZ9+W01mN0oJ18wsXZo+ZFcsxNNmzBkeML58ZjnBC1ItIgzIa3TvY1eEEIdi6MyD17hBqwpShlTbsj3tCMadQYHkFUzdn9aTNVgnd+5MvbhzVmbc/Rs5kXRT7LdNt1pP+nuR+Ps+yV2Ug+P0IyQ2vm0qPkRUFHV
```  

# 🌞 Prouvez que la connexion est fonctionnelle
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
