# GDB cheat sheet

## **Changing Disassembly Syntax**

- `set disassembly-flavor intel`
- `set disassembly-flavor att`

## **Running**

- `gdb -q <program> [core dump]` Start GDB (with optional core dump).

- `run, r [args]` Run the program to be debugged.

- `start [args]` Start the program to be debugged with tmp breakpoint at entry.

- `kill` Kill the running program.

## **Breakpoints**

- `info b` List all breakpoints.
- `break <where>` Set a new breakpoint.

  - `break main` // symbol name or a \* followed by an absolute memory addresss

- `hbreak <where>, hb` Hardware Break On Execute

- `delete <breakpoint number (#)>, d <#>` Remove a breakpoint.
- `clear` Delete all breakpoints.

  - `clear main` // symbol name or a \* followed by an absolute memory address

- `enable <breakpoint#>` Enable a disabled breakpoint.
- `disable <breakpoint#>` Disable a breakpoint.

## **Watchpoints - Data Access Breakpoints: Setting Break-on-Read vs. Break-on-Write**

- `watch <address>` Set a breakpoint to break when the address is written to.
- `rwatch <address>` Set a breakpoint to break when the address is read from.
- `awatch <address>` Set a breakpoint to break when any access, read or write, is performed on the specified address.

- Setting the access-size of watchpoints

      In order to specify a particular size of memory access to restrict the watchpoint to, you can use C-style type-casting + dereferencing to. So for instance

  - `watch *(char *) <address>`

    would set a watchpoint to break on access to the one byte at \<address>, and therefore wouldn't fire if address+2 was written to. Whereas

  - `watch *(long long *) <address>`

    would fire if any of the 8 bytes starting at \<address> were written to.

## **Examine assembly**

- `disassemble`, `disas`, `disas <address or symbol name>` Disassemble the current function or
  given location
- `disas /r` View raw bytes
- `x/10i <address>` Display some number of instructions
- `display/10i <$rip / $pc>` Every time the program stops, some number of instructions (10 in the example) are printed out starting at the instruction pointer / program counter.

      On x86 systems <instruction pointer / program counter> would be $rip

      On ARM systems <instruction pointer / program counter> would be $pc

## **Commands: x (examine), print, display**

- Format Specifiers /FMT

  /FMT is the combination of the / character, followed by a number n, a format specifier f, and a unit size specifier u

  The most common other values for f are:

  - 'x' for hexidecimal,
  - 'd' for signed decimal,
  - 'u' for unsigned decimal,
  - 'c' for ASCII characters,
  - 's' for a full (presumed-null-terminated) ASCII string
  - [full list](https://sourceware.org/gdb/onlinedocs/gdb/Output-Formats.html)

  The unit sizes for u are

  - b for bytes
  - h for half-words (2 bytes)
  - w for words (4 bytes)
  - g for giant-words (8 bytes)

  Note that GDB's notion of words (4 bytes) is at odds with Intel's notion of words (2 bytes)! This will be something you will just have to memorize and keep in mind.

  ### **Viewing Registers**

  - `info registers, info r` Print some set of registers which the GDB developers consider most commonly needed.
  - `info r rax rbx rsp`
  - `print, p`
  - `p/x $rax, p/u $rax` [print docs](https://sourceware.org/gdb/current/onlinedocs/gdb/Data.html#index-printing-data)

  ### **Modifying Registers**

  - `set $rax = 0xdeadbeeff00dface`
  - `set $ax = 0xcafef00d`

  ### Viewing Memory [examine x docs](https://sourceware.org/gdb/current/onlinedocs/gdb/Memory.html#index-examining-memory)

  - `x/8xb $rsp`
  - `x/4xh $rsp`
  - `x/2xw $rsp`
  - `x/1xg $rsp`
  - `x/s 0x555555556008` =>

    0x555555556008: "First %d elements of the Fibbonacci sequence: "

  - `x/3i $rip` =>

    0x5555555551a9 \<main>: endbr64

    0x5555555551ad \<main+4>: push %rbp

    0x5555555551ae \<main+5>: mov %rsp,%rbp

  ### **Modifying Memory**

  - `set {char}$rsp = 0xFF`

    => 0x7fffffffe038: 0x00007ffff7ded0b3

    => 0x7fffffffe038: 0x00007ffff7ded0ff

  - `set {short}$rsp = 0xFF`

    => 0x7fffffffe038: 0x00007ffff7de00ff

  - `set {short}$rsp = 0xFFFF`

    => 0x7fffffffe038: 0x00007ffff7deffff

  - `set {long long}$rsp = 0x1337bee7`

    => 0x7fffffffe038: 0x000000001337bee7

  _Immediates which are smaller than the size of the specified memory write are zero-extended, not sign-extend._

## Updating Stack View

- `display/8xg $rsp`

## Informational

- `backtrace, bt` (short form: bt) provides a call stack backtrace. [docs](https://sourceware.org/gdb/current/onlinedocs/gdb/Backtrace.html#Backtrace)

## **Stepping**

- `nexti, ni` Step Over, next instruction
- `stepi, si` Step Into
- `finish, fin` Steps out of the current function context
- `until <address>, u` Step until address; If for some reason the address is never reached (e.g. because control flow branches some other direction) the until instruction will also break upon exit from the current function.

## **Attaching to Running Userspace Processes**

- set permissions: `echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope` [more about permissions](https://askubuntu.com/questions/41629/after-upgrade-gdb-wont-attach-to-process)
- unset permissions: `echo 1 | sudo tee /proc/sys/kernel/yama/ptrace_scope`

- `ps aux | grep proces-name`
- from gdb: `attach <process ID>`

## **Saving a Persistent GDB Configuration**

- `gdb -x ~/gdbcfg`

example gdb cfg file (~/gdbcfg):

```sh
display/10i $rip
display/x $rbp
display/x $rsp
display/x $rax
display/x $rbx
display/x $rcx
display/x $rdx
display/x $rdi
display/x $rsi
display/x $r8
display/x $r9
display/x $r12
display/x $r13
display/x $r14
display/10gx $rsp
start
```

## **Plugins**

https://github.com/apogiatzis/gdb-peda-pwndbg-gef
