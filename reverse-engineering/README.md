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

- manipulate the binary so it still executes, but a debugger can't open it [example script](/other/python/scripts/reverse-engineering/elf-fuzzer.py)
