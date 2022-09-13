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

  1. `masscan -p1-65535 10.10.10.123 --rate=1000 -e tun0 > ports`
     - (alternative) `nmap -T4 -p- 10.10.10.123`
  2. `ports=$(cat ports | awk -F " " '{print $4}' | awk -F "/" '{print $1}' | sort -n | tr '\n' ',' | sed 's/,$//')`
     - (for alternative) `ports=$(cat ports | grep open | awk -F "/" '{print $1}' | tr '\n' ',' | sed 's/,$//')`
  3. `nmap -Pn -sV -sC -p$ports 10.10.10.123`

- msfconsole
  - auxiliary/scanner/portscan/\*

## [web](../web/README.md)

## [smb](./smb.md)
