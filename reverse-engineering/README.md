# Reverse Engineering

## quick tools

- `strings`
- `objdump -x` Show all headers
- `objdump -d/D` Disassemble
- `strace`
- `ltrace`

## gdb [cheat sheet](./gdb.md)

- `gdb -q <program> [core dump]`

## fuzzing

- manipulate the binary so it still executes, but a debugger can't open it
  - [example script, random, inefficient and dumb way](/other/python/scripts/reverse-engineering/elf-fuzzer.py)
  - [Melkor ELF Fuzzer](https://github.com/IOActive/Melkor_ELF_Fuzzer)
  - [elf specs 1](https://refspecs.linuxfoundation.org/elf/elf.pdf)
  - [elf specs 2](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f00/docs/elf.pdf)
