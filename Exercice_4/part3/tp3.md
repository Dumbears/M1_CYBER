🌞 Activer le service SNMP
```bash
configure terminal
snmp-server community tp4 RO
exit
```



🌞 Vérifier l'état du service SNMP
```bash
r1#show snmp community
Community name: ILMI
Community Index: ILMI
Community SecurityName: ILMI
storage-type: read-only  active
Community name: tp4
Community Index: tp4
Community SecurityName: tp4
storage-type: nonvolatile        active 
```

🌞 Sur votre bastion, installer et contacter le routeur avec snmpwalk
```bash
sudo dnf install -y net-snmp-utils
```  


🌞 Trouvez une commande qui récupère la liste des interfaces réseau et des connexions actives


🦈 Capture SNMP snmp.pcap


🌞 Installer Netdata sur votre bastion

🌞 Visitez l'interface web de Netdata

🌞 Ajouter la conf SNMP