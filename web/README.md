# Web HTTP/HTTPS

## Burp suite

- extensions:
  - [http request-smuggler](https://github.com/portswigger/http-request-smuggler)
  - [jwt editor](https://github.com/PortSwigger/jwt-editor)

## more tools

- [OWASP ZAP - zaproxy](https://www.zaproxy.org/download/)
- [fiddler](https://www.telerik.com/fiddler) - a web-debugging tool that monitors, inspects, edits, and logs all HTTP(S) traffic, and issue requests between your computer and the Internet, and fiddles with incoming and outgoing data. It is a high-performance, cross-platform proxy for any browser, system, or platform.

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

- [burp suite - jwt editor extension](https://github.com/PortSwigger/jwt-editor)

## [XSS - Cross-site scripting](./XSS.md)

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

## Login page

- try common username and password cominations
  - username:password
    - admin:admin
    - test:password

## Misc

- clone, mirror a web page

  - `wget -m some-site.com`
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

## [request smuggling](./request-smuggling.md)

