# Operating systems

## Linux privesc

- https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS

  - SUID

    - https://gtfobins.github.io/
    - find suid binaries: `find / -perm -u=s -type f 2>/dev/null`

  - change $PATH to control what gets executed

- common vectors:
  - `sudo -l`, see what is executable as sudo
  - `find / -perm -u=s 2>/dev/null`, find files with suid
    - https://gtfobins.github.io/
