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

  - `find / -newermt "2022-03-22" ! -newermt "2022-03-24" -ls 2>/dev/null`

    - find files modified at some date range, look for interesting, out of place files, not found by default

  - `/usr/local/*`

    - user added files

  - confirm running cron jobs without privilege

    - `watch -n .5 "ps -ef | grep git-sync"`, git-sync is the suspicious name

  - cronjobs
    - git
      - make a hook to execute a command
        - `.git/hooks/pre-commit`
      - execute command on `git status`
        - [fsmonitor config](https://blog.sonarsource.com/securing-developer-tools-git-integrations/)
