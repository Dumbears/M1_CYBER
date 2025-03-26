```bash
Host bastion
  Hostname 10.3.30.100
  User administrateur
  IdentityFile "C:\Users\rgebel\.ssh\toto"
 
 Host r1
  ProxyJump bastion
  HostName 10.3.30.254
  User administrateur
  IdentityFile "C:\Users\rgebel\.ssh\toto"
  KexAlgorithms +diffie-hellman-group14-sha1
  PubkeyAcceptedAlgorithms +ssh-rsa
  HostkeyAlgorithms +ssh-rsa
  Ciphers +aes256-cbc
  MACs hmac-sha1,hmac-md5
  StrictHostKeyChecking no
```