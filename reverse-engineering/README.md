# Reverse Engineering

## quick tools

- `file`
- `strings`
- `xxd` hex view
- `objdump -x` Show all headers
- `objdump -d/D` Disassemble
- `strace`
- `ltrace`

## Disassemblers and debugers

- IDA, Ghidra, gdb, edb
- if they don't work try Cutter
- ILSpy, dnSpy, dotPeek

- tips:

  - edb and Cutter can show hexdumps next to disassembly, look for parameters to function calls

  ### multipurpose

  - https://ide.kaitai.io/ - [kaitai](http://kaitai.io/)
  - https://cerbero.io/ - [tutorials](https://cerbero.io/resources/)

  ### tools for elf files

  - https://github.com/horsicq/XELFViewer

  ### tools for PE (windows)

  - https://github.com/Washi1337/AsmResolver

  ### .NET [dotnet, mono]

  - [ILSpy](https://github.com/icsharpcode/ILSpy)
  - [dotPeek](https://www.jetbrains.com/decompiler/)
  - [dnSpy](https://github.com/dnSpy/dnSpy)
    - can debug and edit binaries

## Packing

- [PEiD](https://www.aldeid.com/wiki/PEiD)\
  - detects most common packers, cryptors and compilers for PE files
- [UPX](https://github.com/upx/upx)
  - `upx -d cake.exe`
    - sometimes before unpacking with UPX you must disable the ASLR: `setdllcharacteristics -d cake.exe`, unpacked program might not run without this (for debugging) like cake.exe for example (chall from HTB)

## gdb [cheat sheet](./gdb.md)

- `gdb -q <program> [core dump]`

## fuzzing

- manipulate the binary so it still executes, but a debugger can't open it
  - [example script, random, inefficient and dumb way](/other/python/scripts/reverse-engineering/elf-fuzzer.py)
  - [Melkor ELF Fuzzer](https://github.com/IOActive/Melkor_ELF_Fuzzer)
  - [elf specs 1](https://refspecs.linuxfoundation.org/elf/elf.pdf)
  - [elf specs 2](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f00/docs/elf.pdf)

## Assembly

- [intel x86 manual](https://ost2images.s3.amazonaws.com/Arch2001/CourseMaterials/325462-sdm-vol-1-2abcd-3abcd.pdf)

## Other

- [Python vulnerabilities](./python.md)
- [Virus total](https://www.virustotal.com/gui/home/upload)
- [Meta Defender OPSWAT](https://metadefender.opswat.com/)
