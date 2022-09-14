# SMB - server message block

port 139, 445

## enumeration

- msfconsole

  - `use auxiliary/scanner/smb/*`
  - `info`
  - `set RHOSTS 10.10.10.123`
  - ...
  - `run`

- `smbclient -L \\192.168.57.134`
- `smbclient -L \\\\192.168.57.134\\`

- `enum4linux -a 10.10.10.4`

## connect

- `smbclient \\\\192.168.57.134\\ADMIN$`

  - connecting to a share
    - try empty credentials (anonymous login)

## exploit

- find exploits online based on version and os
