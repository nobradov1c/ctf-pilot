# Networking

## IP

https://h.43z.one/ipconverter/

## [wifi](./wifi.md)

## network mapping

- [netdiscover](https://github.com/netdiscover-scanner/netdiscover), use arp to discover network addresses
  - `netdiscover -r 192.168.1.0/24`
- [nmap](https://github.com/nmap/nmap), scan open ports

  - `nmap -sV -sC -O -oN nmap.txt 10.10.10.123`
  - `nmap -T4 -A -sS -Pn -p- 10.10.10.123`

- [masscan](https://github.com/robertdavidgraham/masscan) Scan all ports very quickly

  1. `sudo masscan -p1-65535 $ip --rate=1000 -e tun0 > ports`
     - (alternative) `nmap -T4 -p- $ip > ports`
  2. `ports=$(cat ports | awk -F " " '{print $4}' | awk -F "/" '{print $1}' | sort -n | tr '\n' ',' | sed 's/,$//')`
     - (for alternative) `ports=$(cat ports | grep "/tcp\|/udp" | awk -F "/" '{print $1}' | tr '\n' ',' | sed 's/,$//')`
  3. `sudo nmap -Pn -sC -sV -O -p$ports -oN nmap.txt $ip`

- alternative:

  - `ports=$(nmap -p- --min-rate=1000 -T4 10.10.11.106 | grep ^[0-9] | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//)`
  - `nmap -p$ports -sC -sV 10.10.11.106`

- msfconsole
  - auxiliary/scanner/portscan/\*

## [web](../web/README.md)

## [smb](./smb.md)

## Bro logs (zeek logs)

- [Zeek, formerly Bro](https://zeek.org/) - network analysis framework
  - [zeek logs, bro logs](https://docs.zeek.org/en/master/logs/index.html)
