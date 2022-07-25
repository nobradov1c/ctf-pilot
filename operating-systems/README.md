# Operating systems

## Linux privesc

- https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS

  - SUID

    - https://gtfobins.github.io/
    - find suid binaries: `find / -perm -u=s -type f 2>/dev/null`

  - change $PATH to control what gets executed
