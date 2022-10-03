# Web HTTP/HTTPS

## enumeration

- [gobuster](https://github.com/OJ/gobuster)
  - `gobuster dir -t 100 --url 10.10.10.123 --wordlist /usr/share/seclists/Discovery/Web-Content/big.txt > gobuster-big.txt`
  - `gobuster dir -t 100 --url 10.10.10.123 --wordlist /usr/share/seclists/Discovery/Web-Content/big.txt -x txt,zip,bak,rar,asm,asmx,asp,aspx,php,js > gobuster-big.txt`
- [dirbuster](https://aur.archlinux.org/packages/dirbuster) - GUI app

### servers usual naming conventions

1. NodeJS:

   - index.html

2. python

   - app/app.py

3. PHP
   - index.php

---

Automated:

- [nikto](https://github.com/sullo/nikto)
  - `nikto -h tesla.com`
- [nessus](https://www.tenable.com/products/nessus)

## Tricky

- `wget --mirror`
  - mirror a website, could solve some ctfs

## JavaScript, JS

### javascript deobfuscator

https://deobfuscate.io/

### JWT

https://jwt.io/

`john --wordlist=/usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt jwt.txt`

`john --show jwt.txt`

## [SQL Injection](./SQLi.md)

- https://portswigger.net/web-security/sql-injection/cheat-sheet
- https://sqlwiki.netspi.com/

## SSTI - server side template injection

- https://github.com/payloadbox/ssti-payloads
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md#exploit-the-ssti-by-calling-ospopenread

## Prototype Pollution

- https://www.youtube.com/watch?v=MzlZIJjqsVE
- https://github.com/satoki/ctf_writeups/tree/master/TJCTF_2022/fruit-store

## WASM, web assembly, WebAssembly

[The WebAssembly Binary Toolkit](https://github.com/WebAssembly/wabt)

Instructions

`sudo apt install wabt`

### to wat [WebAssembly text](https://developer.mozilla.org/en-US/docs/WebAssembly/Understanding_the_text_format)

`wasm2wat --generate-names script.wasm > script.wat`

#### to c

`wasm2c main.wasm -o wasm.c`

### to pseudo code

`wasm-decompile main.wasm -o wasm.dcmp`

### wasmtime

Standalone JIT-style runtime for WebAssembly, using Cranelift

https://github.com/bytecodealliance/wasmtime

https://wasmtime.dev/

for python:

https://github.com/bytecodealliance/wasmtime-py

## Misc

- clone a web page

  - `wget -r some-site.com`

- exact location, can't access site via IP

  - `curl -v 10.129.253.118`

    > ERROR

    1. see Location header in response
    2. or `<meta http-equiv="refresh" content="0;url=http://unika.htb/">`
    3. or something else...?

- The top 10 most common passwords list 2022:

  - 123456
  - 123456789
  - qwerty
  - password
  - 12345
  - qwerty123
  - 1q2w3e
  - 12345678
  - 111111
  - 1234567890
