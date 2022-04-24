# Web Exploitation

## JavaScript, JS

### javascript deobfuscator
https://deobfuscate.io/

## wasm, web assembly, WebAssembly
[The WebAssembly Binary Toolkit](https://github.com/WebAssembly/wabt)

Instructions

`sudo apt install wabt`

### to wat [WebAssembly text](https://developer.mozilla.org/en-US/docs/WebAssembly/Understanding_the_text_format)

`wasm2wat --generate-names script.wasm > script.wat`

#### to c
`wasm2c main.wasm -o wasm.c`

### to pseudo code
`wasm-decompile main.wasm -o wasm.dcmp`

