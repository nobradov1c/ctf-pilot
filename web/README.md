# Web Exploitation

## JavaScript, JS

### javascript deobfuscator

https://deobfuscate.io/

### JWT

https://jwt.io/

`john --wordlist=/usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt jwt.txt`

`john --show jwt.txt`

## SQL Injection

- https://portswigger.net/web-security/sql-injection/cheat-sheet
- https://sqlwiki.netspi.com/

### tools:
- BurpSuite Intruder
- [sqlmap](https://github.com/sqlmapproject/sqlmap)
- TODO: ffuz
- [more...](https://github.com/The-Art-of-Hacking/h4cker/blob/master/web_application_testing/sql-injection-tools.md)
### payloads:
- https://github.com/payloadbox/sql-injection-payload-list/blob/master/Intruder/exploit/Auth_Bypass.txt
- https://github.com/payloadbox/sql-injection-payload-list
- https://github.com/swisskyrepo/PayloadsAllTheThings

Tricks:
- `admin' or 1=1;--`
- `ad'||'min'/*` // concatenation in SQLite
- `SELECT username, password FROM users WHERE username='ad'||'min' AND password='a' is not 'b'`
- `SELECT username, password FROM users WHERE username='ad'||'min' except select' AND password=','' `
- `SELECT username, password FROM users WHERE username='ad'||'min' AND password=''glob'*'`
- 

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
