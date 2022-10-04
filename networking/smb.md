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

- no password
  - `smbclient -N -L \\\\192.168.57.134\\`
- username

  - `smbclient -U '' -L \\\\192.168.57.134\\`
  - `smbclient -U '. ' -L \\\\192.168.57.134\\`

- `enum4linux -a 10.10.10.4`

with credentials

- [crackmapexec](https://github.com/Porchetta-Industries/CrackMapExec)
  - `cme smb 10.10.11.106 -u tony -p liltony`
    - if it outputs pwn, we are able to get a shell
  - `cme smb 10.10.11.106 -u tony -p liltony --shares`
    - shows permissions

## connect

- `smbclient \\\\192.168.57.134\\ADMIN$`

  - connecting to a share
    - try empty credentials (anonymous login)

## exploit

- find exploits online based on version and os
