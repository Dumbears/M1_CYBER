```bash
Host bastion
  Hostname 10.3.30.100
  User administrateur
  IdentityFile "C:\Users\rgebel\OneDrive - Andqo\Bureau\Cours Master\Cybersécurtié\tp4\private_ssh"
  IdentitiesOnly yes 
 
 Host r1
  ProxyJump bastion
  HostName 10.3.30.254
  User administrateur
  IdentityFile "C:\Users\rgebel\OneDrive - Andqo\Bureau\Cours Master\Cybersécurtié\tp4\private_ssh"
  KexAlgorithms +diffie-hellman-group1-sha1
  PubkeyAcceptedAlgorithms +ssh-rsa
  HostkeyAlgorithms +ssh-rsa
  Ciphers +aes256-cbc
  MACs hmac-sha1,hmac-md5
```
